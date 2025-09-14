import os
from dotenv import load_dotenv

HF_TOKEN = os.getenv("HF_API_TOKEN")
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(PROJECT_ROOT, "Documents")
CHROMA_DB_DIR = os.path.join(PROJECT_ROOT, "RAG/chroma_db")