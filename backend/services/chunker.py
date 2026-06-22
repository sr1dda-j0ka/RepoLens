from langchain_core.documents import Document
from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)

EXTENSION_TO_LANGUAGE = {
    "py": Language.PYTHON,
    "js": Language.JS,
    "ts": Language.TS,
    "java": Language.JAVA,
    "cpp": Language.CPP,
    "c": Language.CPP,
    "go": Language.GO,
    "rs": Language.RUST
}


def chunk_content(docs):

    all_chunks = []

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

            splitter = RecursiveCharacterTextSplitter.from_language(
                language=language,
                chunk_size=1200,
                chunk_overlap=200,
            )

        else:

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1200,
                chunk_overlap=200,
            )

        chunks = splitter.split_documents([lc_doc])

        all_chunks.extend(chunks)

    return all_chunks