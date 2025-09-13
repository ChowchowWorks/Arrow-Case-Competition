import os
from loader import receive
from config import HF_TOKEN, DOCS_DIR, PROJECT_ROOT
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

os.environ['USER_AGENT'] = "ARROW_RAG"

def embed(documents, persist_directory = 'chroma_db'):
    '''This function takes as input a file_path as 'documents
    It calls the receive function to chunk the document at the file_path location
    Function will check if there is an existing vector store pre-tuned as chroma_db
    It will then embed the chunks into the vectorstore'''
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 
    texts = receive(documents)
    if not os.path.exists(persist_directory) or not os.listdir(persist_directory):
        print("No Existing Vectorstore. Creating a new one...")
        try:
            vectorstore = Chroma.from_documents(documents=texts, embedding=embedding_model, persist_directory=persist_directory)
        except Exception as e:
            print(f"Error: Failed to create vectorstore. \nReason: {e}")
            return False
    else: 
        print("Existing Vectorstore found. Loading and Updating...")
        try: 
            vectorstore = Chroma(persist_directory= persist_directory, embedding_function=embedding_model)
            vectorstore.add_documents(documents=texts)
        except Exception as e:
            print(f"Error: Failed to add documents. \nReason: {e}")
            return False
    return True

def get_vector_store(persist_dir= 'chroma_db'):
    if not os.path.exists(persist_dir) or not os.listdir(persist_dir):
        print("No Vectorstore found at this location!")
        return None
    embedding_model = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")
    print("Found a Vectorstore")
    try:
        vectorstore = Chroma(persist_directory= persist_dir, embedding_function=embedding_model)
        return vectorstore
    except Exception as e:
        print(f"Error: Vectorstore present but failed to retrieve it. \nReason: {e}")


def normalize_path(path: str) -> str:
    """Convert absolute path to relative path inside Documents/."""
    return os.path.relpath(path, DOCS_DIR)