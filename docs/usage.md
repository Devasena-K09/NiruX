# NiruX — Usage Notes

## Local
1. python -m venv env
2. source env/bin/activate   (or env\\Scripts\\activate on Windows)
3. pip install -r requirements.txt
4. python src/main.py

## Development ideas
- Add FastAPI server in src/api.py
- Integrate OpenAI or local models for core agent responses
- Add vector DB for retrieval (e.g., FAISS, Milvus, Pinecone)
