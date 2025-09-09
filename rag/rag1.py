import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant.qdrant import QdrantVectorStore

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

file_path = Path(__file__).parent / "nodejs.pdf"

pdf_loader = PyPDFLoader(file_path=file_path)

docs = pdf_loader.load()

text_spliters = RecursiveCharacterTextSplitter(
     chunk_size=1000,
    chunk_overlap=200,
)

text_spliters.split_documents(text_spliters)

embedding_models = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=api_key
)

vector_store = QdrantVectorStore.from_documents(
    documents=docs,
    embedding=embedding_models,
    url="http://localhost:6333",
    collection_name="text_collection"
)
print("Ingestion DONE")