import os
from dotenv import load_dotenv

load_dotenv("/Users/chowchow/Documents/GitHub/Arrow-Case-Competition/RAG/api.env")

HF_TOKEN = os.getenv("HF_API_TOKEN")

print(HF_TOKEN)