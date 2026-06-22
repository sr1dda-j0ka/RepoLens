def rerank_results(results, question):

    question_words = set(
        question.lower()
        .replace("_", " ")
        .replace("-", " ")
        .split()
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
            score += 4

        if any(part in PLATFORM_FOLDERS for part in path_parts):
            score -= 5

        if metadata.get("is_test", False):
            score -= 4

        if metadata.get("is_example", False):
            score -= 2


        if 500 < size < 50000:
            score += 1


        filename_words = set(
            filename
            .replace(".py", "")
            .replace(".js", "")
            .replace(".ts", "")
            .replace(".tsx", "")
            .replace(".jsx", "")
            .replace(".java", "")
            .replace(".cpp", "")
            .replace(".go", "")
            .replace(".rs", "")
            .replace("_", " ")
            .replace("-", " ")
            .split()
        )

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
            score += 2

        reranked.append(
            (
                score,
                r
            )
        )

    reranked.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        r
        for _, r in reranked[:6]
    ]