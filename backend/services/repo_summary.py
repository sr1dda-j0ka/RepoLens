import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_summary(context):

    prompt = f"""
You are a senior software engineer analyzing a software repository.

Use ONLY the provided repository context.

Return your response in the following format:

Purpose:
(5-6 concise sentences)

Architecture:
(Explain the high-level design in 7-8 sentences.)

Key Modules:

module 1
module 2
module 3

Technologies:

technology 1
technology 2
technology 3

Do not mention uncertainty.
Do not copy the README verbatim.
Do not hallucinate.
Keep the total response under 200 words.

Context:
{context}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
            config={
                "temperature" : 0.1,
                "max_output_tokens" : 500
            }
        )
        return response.text
    
    except Exception as e:
        return f"Gemini Error: {str(e)}"

IGNORE_DIRS = {
    ".git",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode",
    ".next",
    "coverage",
    "target",
    "bin",
    "obj"

}

def generate_folder_tree(root):
    tree = []

    for current, dirs, files in os.walk(root):

        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        level = current.replace(root, "").count(os.sep)

        if level > 2:
            continue

        indent = "    " * level

        tree.append(f"{indent}{os.path.basename(current)}/")

        # Show first 5 files
        for file in files[:5]:
            tree.append(f"{indent}    {file}")

    return "\n".join(tree)

LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
    ".rb": "Ruby",
    ".html": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".json": "JSON",
    ".md": "Markdown"
}


def generate_repo_stats(root_path):

    total_files = 0
    total_folders = 0
    total_functions = 0
    total_classes = 0

    language_lines = {}

    for current_root, dirs, files in os.walk(root_path):

        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        total_folders += len(dirs)

        for file in files:

            path = os.path.join(current_root, file)

            total_files += 1

            extension = os.path.splitext(file)[1]

            language = LANGUAGE_MAP.get(extension)

            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:

                    lines = f.readlines()

                    if language:
                        language_lines[language] = (
                            language_lines.get(language, 0)
                            + len(lines)
                        )

                    for line in lines:

                        stripped = line.strip()

                        if stripped.startswith("def "):
                            total_functions += 1

                        elif stripped.startswith("class "):
                            total_classes += 1

                        elif (
                            "(" in stripped
                            and ")" in stripped
                            and "{"
                            in stripped
                        ):
                            total_functions += 1

            except:
                pass

    total_language_lines = sum(language_lines.values())

    language_percentages = {}

    if total_language_lines:

        for language, count in language_lines.items():

            language_percentages[language] = round(
                count * 100 / total_language_lines,
                1
            )

    return {
        "files": total_files,
        "folders": total_folders,
        "functions": total_functions,
        "classes": total_classes,
        "languages": language_percentages
    }