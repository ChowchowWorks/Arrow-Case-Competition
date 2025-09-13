import os
from dotenv import load_dotenv

load_dotenv("/Users/chowchow/Documents/GitHub/Arrow-Case-Competition/RAG/api.env")

HF_TOKEN = os.getenv("HF_API_TOKEN")
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(PROJECT_ROOT, "Documents")