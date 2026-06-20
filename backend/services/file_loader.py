import os

EXCLUDE_DIRS = {".git", "node_modules", "dist", "build", "__pycache__"}

GET_LANGUAGE = {
    "py": "Python",
    "js": "Javascript",
    "ts": "Typescript",
    "java": "Java",
    "cpp": "CPP",
    "c": "C",
    "go": "Go",
    "rs": "Rust"
}

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
                        relative_path = os.path.relpath(full_path,repo_path)
                        docs.append({
                            "path": os.path.relpath(full_path, repo_path),
                            "content": content,
                            "type": file.split(".")[-1],
                            "file_name": os.path.basename(relative_path),
                            "folder": os.path.dirname(relative_path),
                            "language": GET_LANGUAGE.get(file.split(".")[-1]),
                            "size": len(content),
                            "is_test" : (
                                "test" in relative_path.lower()
                                or "tests" in relative_path.lower()
                            ),
                            "is_example": (
                                "example" in relative_path.lower()
                                or "examples" in relative_path.lower()
                            )

                        })
                except Exception as e:
                    print(f"Error reading {full_path}: {e}")

    return docs