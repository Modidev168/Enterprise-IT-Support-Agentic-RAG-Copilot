from app.services.ingestion import load_file , chunk_documents
from pathlib import Path
from app.rag.vectorstore import add_documents , get_embeddings

docs = load_file(Path("data/sample_kb/company_it_handbook.md"))
chunks = chunk_documents(docs)
embeddings = get_embeddings()

# vector = embeddings.embed_query("What is Agentic RAG?")

# print("Embedding dimension:", len(vector))
add_documents(chunks)