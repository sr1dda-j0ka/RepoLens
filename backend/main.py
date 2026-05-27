from fastapi import FastAPI
from pydantic import BaseModel
from services.github_loader import clone_repo
from services.file_loader import load_code_files
from services.embedder import create_vector_store

app = FastAPI()
vector_store=None

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