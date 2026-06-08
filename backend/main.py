from fastapi import FastAPI
from pydantic import BaseModel
from services.github_loader import clone_repo
from services.file_loader import load_code_files
from services.embedder import create_vector_store
from services.gemini_service import ask_gemini
from fastapi.middleware.cors import CORSMiddleware

origins=["http://localhost:5173","http://127.0.0.1:5173"]

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
    path=clone_repo(data.repo_url)
    docs=load_code_files(path)
    vector_store=create_vector_store(docs)
    return{
        "message": "Repo cloned successfully",
        "total-files": len(docs)
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

    # Retrieve only top relevant chunks
    results = vector_store.max_marginal_relevance_search(question, k=3,fetch_k=10)

    context_parts = []

    MAX_CHARS_PER_CHUNK = 1200
    MAX_TOTAL_CONTEXT = 3500

    current_length = 0

    for result in results:

        chunk = result.page_content[:MAX_CHARS_PER_CHUNK]

        formatted_chunk = (
            f"\nFILE: {result.metadata['path']}\n"
            f"{chunk}\n"
        )

        # Stop if total context becomes too large
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
