from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.scraper import scrape_wiki_page
from app.chunker import chunk_text
from app.faiss_store import store_chunks_in_faiss, retrieve_relevant_chunks
from app.llm_api import query_llm

app = FastAPI()

class Question(BaseModel):
    question: str

text = scrape_wiki_page("https://en.wikipedia.org/wiki/Luke_Skywalker", "luke_walker_wiki_text.txt")
chunks = chunk_text(text)
index, vectorizer = store_chunks_in_faiss(chunks)

@app.post("/ask")
def ask_question(question: Question):
    query = question.question
    try:
        relevant_chunks = retrieve_relevant_chunks(query, vectorizer, index, chunks)
        prompt = "\n".join(relevant_chunks)+ "\n\n"+ query
        print(prompt)
        answer = query_llm(prompt)
        return {"question": query, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
