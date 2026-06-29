from langchain_core.documents import Document
from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)

EXTENSION_TO_LANGUAGE = {
    "py": Language.PYTHON,
    "js": Language.JS,
    "jsx": Language.JS,
    "tsx": Language.TS,
    "ts": Language.TS,
    "java": Language.JAVA,
    "cpp": Language.CPP,
    "c": Language.CPP,
    "go": Language.GO,
    "rs": Language.RUST
}


def chunk_content(docs):

    all_chunks = []

    cached_splitters = {
        lang: RecursiveCharacterTextSplitter.from_language(
            language=lang,
            chunk_size=4000,
            chunk_overlap=400,
        ) for lang in set(EXTENSION_TO_LANGUAGE.values())
    }

    default_splitter = RecursiveCharacterTextSplitter(
        chunk_size=4000,
        chunk_overlap=400,
    )

    for doc in docs:

        ext = doc.get("type", "").lower()
        path = doc.get("path", "")
        content = doc.get("content", "")
        file_name=doc.get("file_name", "")
        folder=doc.get("folder", "")
        language=doc.get("language","")
        size=doc.get("size", 0)
        is_test=doc.get("is_test", False)
        is_example=doc.get("is_example", False)

        if any(ignored in path.lower() for ignored in ["lock.json", "package-lock", "yarn.lock", "pnpm-lock", "dist/", "build/"]):
            continue

        lc_doc = Document(
            page_content=content,
            metadata={
                "path": path,
                "extension": ext,
                "language": language,
                "file_name": file_name,
                "folder": folder,
                "size": size,
                "is_test": is_test,
                "is_example": is_example
            }
        )

        language = EXTENSION_TO_LANGUAGE.get(ext)

        if language is not None:

            splitter = cached_splitters[language]

        else:

            splitter = default_splitter

        chunks = splitter.split_documents([lc_doc])
        all_chunks.extend(chunks)

    return all_chunks