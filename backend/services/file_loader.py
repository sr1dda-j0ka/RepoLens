import os

EXCLUDE_DIRS = {".git", "node_modules", "dist", "build", "__pycache__","coverage",".next","out","public/assets"}
EXCLUDE_FILES={"package-lock.json", "yarn.lock", "pnpm-lock.yaml", "pnpm-workspace.yaml"}

GET_LANGUAGE = {
    "py": "Python",
    "js": "JavaScript",
    "jsx": "JavaScript",
    "ts": "TypeScript",
    "tsx": "TypeScript",
    "java": "Java",
    "cpp": "CPP",
    "c": "C",
    "cs": "CSharp",
    "go": "Go",
    "rs": "Rust",
    "dart": "Dart",
    "php": "PHP",
    "rb": "Ruby",
    "swift": "Swift",
    "kt": "Kotlin",
    "scala": "Scala",
}

MAX_FILE_SIZE=500*1024

def load_code_files(repo_path):
    docs = []

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            if file in EXCLUDE_FILES:
                continue

            if ".min." in file:
                continue

            if file.endswith((".py", ".js", ".jsx", ".ts", ".tsx", ".cpp", ".java", ".html", ".css",".cs",".dart",".go",".rs",".php",".rb",".swift",".kt",".scala")):
                full_path = os.path.join(root, file)

                try:
                    if os.path.getsize(full_path) > MAX_FILE_SIZE:
                        print(f"Skipping excessively large file: {full_path}")
                        continue
                    
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