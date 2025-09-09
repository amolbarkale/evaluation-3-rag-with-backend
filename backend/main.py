from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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
    #TODO: Add your code here to get the answer from the model
    return {"answer": "Hello World"}

@app.get("/health")
async def health():
    return {"status": "ok"}
