import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

def store_chunks_in_faiss(chunks):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(chunks)
    index = faiss.IndexFlatL2(X.shape[1])
    index.add(X.toarray())
    return index, vectorizer

def retrieve_relevant_chunks(query, vectorizer, index, chunks, k=3):
    query_vector = vectorizer.transform([query]).toarray()
    D, I = index.search(query_vector, k)
    return [chunks[i] for i in I[0]]
