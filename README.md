# evaluation-3-rag-with-backend

setup docker for qdrant DB


```
docker compose -f docker-compose.db.yml up -d
```

RAG
```
python indexing.py

python chat.py

```

Once docker is up, You can see qdrant GUI at http://localhost:6333/dashboard

FastAPI

```
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

fastapi dev main.py
```

run http://localhost:8000/docs for fastapi 

and ```/user-query``` with get method

