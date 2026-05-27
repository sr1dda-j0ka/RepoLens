import os

EXCLUDE_DIRS = {".git", "node_modules", "dist", "build", "__pycache__"}

def load_code_files(repo_path):
    docs = []

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            if file.endswith((".py", ".js", ".cpp", ".java", ".ts", ".html", ".css")):
                full_path = os.path.join(root, file)

                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()

                        docs.append({
                            "path": os.path.relpath(full_path, repo_path),
                            "content": content,
                            "type": file.split(".")[-1]
                        })
                except Exception as e:
                    print(f"Error reading {full_path}: {e}")

    return docs