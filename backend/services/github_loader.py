from git import Repo
import os

def clone_repo(repo_url: str):
    repo_name = repo_url.split("/")[-1]
    path = os.path.join("repos", repo_name)

    if not os.path.exists("repos"):
        os.makedirs("repos")

    if not os.path.exists(path):
        Repo.clone_from(repo_url, path)

    return path