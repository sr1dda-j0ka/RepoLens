import os
import re
def rerank_results(results, question):

    question_words = set(
        re.sub(r'[^a-zA-Z0-9\s]', ' ', question.lower()).split()
    )

    IMPORTANT_FOLDERS = {
        "src",
        "lib",
        "app",
        "apps",
        "backend",
        "server",
        "core",
        "internal",
        "services",
        "service",
        "modules",
        "domain",
        "business",
        "api",
        "pkg",
        "cmd",
    }

    PLATFORM_FOLDERS = {
        "android",
        "ios",
        "windows",
        "linux",
        "macos",
        "web",
    }

    reranked = []

    for r in results:

        score = 0
        metadata = r.metadata

        path = metadata.get("path", "").lower()
        folder = metadata.get("folder", "").lower()
        filename = metadata.get("file_name", "").lower()
        size = metadata.get("size", 0)

        path_parts = path.replace("\\", "/").split("/")

        if any(part in IMPORTANT_FOLDERS for part in path_parts):
            score += 5

        if any(part in PLATFORM_FOLDERS for part in path_parts):
            score -= 5

        if metadata.get("is_test", False) or "test" in path_parts or filename.startswith("test_"):
            score -= 8

        if metadata.get("is_example", False) or "docs_src" in path_parts:
            score -= 4


        if 500 < size < 60000:
            score += 1


        name_without_ext, _ = os.path.splitext(filename)
        filename_words = set(re.split(r'[^a-zA-Z0-9]', name_without_ext))

        overlap = len(
            question_words.intersection(filename_words)
        )
        score += overlap * 4


        important_names = [
            "service",
            "controller",
            "handler",
            "manager",
            "repository",
            "model",
            "router",
            "route",
            "view",
            "api",
            "store",
            "context",
            "provider",
        ]

        if any(name in filename for name in important_names):
            score += 3

        reranked.append((score, r))

    reranked.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        r
        for _, r in reranked[:6]
    ]