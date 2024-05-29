from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

def store_chunks_in_faiss(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks, convert_to_tensor=True)
    embeddings = np.array([embedding.cpu().numpy() for embedding in embeddings])
    
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, model

def retrieve_relevant_chunks(query, model, index, chunks, k=3):
    query_embedding = model.encode([query], convert_to_tensor=True).cpu().numpy()
    D, I = index.search(query_embedding, k)
    return [chunks[i] for i in I[0]]
