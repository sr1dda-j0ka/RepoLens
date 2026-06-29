from fastapi import FastAPI
from pydantic import BaseModel
from services.github_loader import clone_repo
from services.file_loader import load_code_files
from services.embedder import create_vector_store
from services.gemini_service import ask_gemini
from services.repo_summary import generate_summary
from services.repo_summary import generate_folder_tree
from services.repo_summary import generate_repo_stats
from services.reranker import rerank_results
from services.progress_tracker import tracker
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

frontend_url=os.getenv("FRONTEND_URL")
backend_url=os.getenv("BACKEND_URL")

origins=[frontend_url,backend_url]

app = FastAPI()
vector_store=None

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RepoRequest(BaseModel):
    repo_url: str

@app.get("/")
def home():
    return {"message": "Server is running"}

@app.post("/repo-request")
def getRepo(data: RepoRequest):
    global vector_store

    tracker.reset()
    tracker.update(
        stage="Cloning Repository",
        progress=5
    )

    path=clone_repo(data.repo_url)

    tracker.update(
        stage="Scanning Source Files",
        progress=15
    )

    docs=load_code_files(path)

    tracker.update(
        files=len(docs),
        progress=20
    )
    tracker.update(
        stage="Generating Code Chunks",
        progress=30
    )

    vector_store=create_vector_store(docs)

    tracker.update(
        stage="Generating Repository Summary",
        progress=95
    )

    stats=generate_repo_stats(path)
    folder_tree =generate_folder_tree(path)
    context=f"""
    Folder Tree: {folder_tree}
    Statistics: {stats}
    """
    summary=generate_summary(context)
    tracker.update(
        stage="Completed",
        progress=100
    )
    
    return{
        "message": "Repo cloned successfully",
        "summary": summary,
        "total-files": len(docs),
        "folder_tree": folder_tree,
        "stats": stats
    }

@app.get("/test-search")
def test_search(query: str):

    results = vector_store.similarity_search(query, k=3)

    output = []

    for result in results:
        output.append({
            "content": result.page_content[:300],  # first 300 chars
            "metadata": result.metadata
        })

    return output


@app.get("/ask")
def ask_repo(question: str):

    if vector_store is None:
        return {"error": "Load a repo first"}
    
    results = vector_store.max_marginal_relevance_search(question, k=15,fetch_k=50)

    results=rerank_results(results,question)

    context_parts = []

    MAX_CHARS_PER_CHUNK = 4000
    MAX_TOTAL_CONTEXT = 16000

    current_length = 0

    for result in results:

        chunk = result.page_content[:MAX_CHARS_PER_CHUNK]

        formatted_chunk = (
            f"\nFILE: {result.metadata['path']}\n"
            f"\nFOLDER: {result.metadata['folder']}\n"
            f"\nLANGUAGE: {result.metadata['language']}\n"
            f"{chunk}\n"
        )

        if current_length + len(formatted_chunk) > MAX_TOTAL_CONTEXT:
            break

        context_parts.append(formatted_chunk)

        current_length += len(formatted_chunk)

    context = "\n".join(context_parts)

    try:
        answer=ask_gemini(context,question)
    except Exception as e:
        return{
            "error": str(e)
        }

    return {
    "question": question,
    "answer": answer,
    "sources": list(
        set(
            [result.metadata["path"] for result in results]
        )
    )
}

@app.get("/progress")
def get_progress():
    return tracker.to_dict() 