import os
import torch

import time
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from services.chunker import chunk_content
from services.progress_tracker import tracker

print("Loading embedding model into memory...")
embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cuda'} if os.environ.get("USE_GPU") == "true" else {'device': 'cpu'},
    )

def create_vector_store(docs):
    print("CUDA Available:", torch.cuda.is_available())
    print("USE_GPU:", os.environ.get("USE_GPU"))
    start=time.perf_counter()
    chunks = chunk_content(docs)

    tracker.update(
        chunks=len(chunks)
    )

    print(f"Files: {len(docs)}")
    print(f"Chunks: {len(chunks)}")
    print(f"Chunking took {time.perf_counter()-start:.2f}s")
    if not chunks:
        return None

    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]

    
    start = time.perf_counter()

    tracker.update(
        stage="Generating Embeddings",
        progress=40,
        total_chunks=len(chunks)
    )
    
    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas
    )
    print(f"Embedding+FAISS took {time.perf_counter()-start:.2f}s")
    return vector_store