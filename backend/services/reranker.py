def rerank_results(results, question):

    question = question.lower()

    reranked = []

    for r in results:

        score = 0

        metadata = r.metadata

        folder = metadata.get("folder", "")
        path = metadata.get("path", "").lower()
        filename = metadata.get("file_name", "").lower()
        size = metadata.get("size", 0)

        if folder.startswith("src"):
            score += 4

        if metadata.get("is_test", False):
            score -= 4

        if metadata.get("is_example", False):
            score -= 2

        if 500 < size < 50000:
            score += 1

        if "architecture" in question:

            if "app" in filename:
                score += 3

            if "blueprint" in path:
                score += 2

            if "ctx" in filename:
                score += 2

            if "config" in filename:
                score += 2

        if "route" in question or "routing" in question:

            if "app" in filename:
                score += 3

            if "blueprint" in path:
                score += 3

            if "scaffold" in filename:
                score += 2

        if "context" in question:

            if "ctx" in filename:
                score += 5

        if "config" in question:

            if "config" in filename:
                score += 5

        if "blueprint" in question:

            if "blueprint" in path:
                score += 5

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