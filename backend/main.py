from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..rag import chat

app = FastAPI(title="RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user-query")
async def answer(query: str):
    answer = await chat.fetch_query(query)
    print('answer:', answer)
    #TODO: Add your code here to get the answer from the model
    return {"answer": answer}

@app.get("/health")
async def health():
    return {"status": "ok"}
