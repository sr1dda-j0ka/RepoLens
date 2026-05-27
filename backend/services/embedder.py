from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_store(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    split_docs = []

    for doc in docs:
        chunks = text_splitter.split_text(doc["content"])

        for chunk in chunks:
            split_docs.append({
                "text": chunk,
                "metadata": {
                    "path": doc["path"],
                    "type": doc["type"]
                }
            })

    texts = [doc["text"] for doc in split_docs]
    metadatas = [doc["metadata"] for doc in split_docs]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(
        texts,
        embeddings,
        metadatas=metadatas
    )

    return vector_store