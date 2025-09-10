import os
from dotenv import load_dotenv

load_dotenv("api.env")

HF_TOKEN = os.getenv("HF_API_TOKEN")