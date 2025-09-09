import os
from dotenv import load_dotenv
from langchain_qdrant.qdrant import QdrantVectorStore
from langchain_openai import OpenAI, OpenAIEmbeddings

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

embedding_models = OpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_key=api_key
)

retriever = QdrantVectorStore.from_existing_collection(
    embedding=embedding_models,
    url="http://localhost:6333",
    collection_name="text_collection"
)

user_query = "What is Nodejs?"

chunks = retriever.similarity_search(query=user_query, k=3)

for chunk in chunks:
    print(chunk.page_content)

SYSTEM_PROMPT = "You are a helpful assistant who answers questions based on the context provided."

# Fetch answer from chunks using Openai LLM with system prompt

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
    max_retries=2,
    api_key=api_key,
)

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": user_query},
    {"role": "user", "content": "Context: " + " ".join([chunk.page_content for chunk in chunks])}
]

response = llm.invoke(messages)
# print("Answer: ", response)
