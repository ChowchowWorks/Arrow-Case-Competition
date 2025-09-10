import os
from langchain_community.document_loaders import PyPDFDirectoryLoader, PyPDFLoader , WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def check_pdfs(filename):
    '''This function takes in as input a string
    if the string is a pathname to a pdf file it will return true
    else it will return false. Returns Boolean.'''

    if not filename.lower().endswith('.pdf'):
        print(f"---Error! {filename} is not a .pdf file!")
        return False
    else:
        return True

def load(file: str):
    '''This function takes in a pathname as input
    it only takes in PDF documents and will load them into a local variable
    returns documents stored in the local variable'''

    if os.path.isdir(file):
        print("---Received Folder! Loading the folder documents now...---")
        try:
            loader = PyPDFDirectoryLoader(file)
            documents = loader.load()
        except Exception as e:
            print("--- Error: Failed to load folder documents ---")
            print(f"Reason: {e}")
            return None
    elif os.path.isfile(file):
        print("---Received File! Loading the file documents now... ---")
        try:
            loader = PyPDFLoader(file)
            documents = loader.load()
        except Exception as e: 
            print("---Error: Failed to load document ---")
            print(f"Reason: {e}")
            return None
    else: 
        print("---Error: Nothing found in this location!---")
        return None
    
    return documents

def web_loader(link:str):
    '''This function takes in a weblink as input
    it will load the webpage into a local variable
    returns the webpage stored in the local variable'''
    
    try:
        loader = WebBaseLoader(link)
        document = loader.load()
        return document
    except Exception as e: 
        print(f"Error: Web Loader failed. \nReason: {e}")
        return None

def split(documents:list):
    '''This function takes a list of documents as input,
    it will split the document into chunks of 800 tokens and each chunk overlaps by 200 tokens
    it will return the chunks '''

    # check if empty list
    if not documents:
        raise Exception("--- Error: Empty List of Document. Check the previous step! ---")
    else:
        print("--- Splitting Documents Now ---")
        splitter = RecursiveCharacterTextSplitter(chunk_size = 800, chunk_overlap = 200)
        try:
            texts = splitter.split_documents(documents)
        except Exception as e:
            print("---Error: Failed to split document into chunks ---")
            print(f"Reason: {e}")
            return None
    return texts

def receive(input:str):
    # check input type:
    if check_pdfs(input): # carry out pdf loading
        documents = load(input)
    else:
        documents = web_loader(input)
    if documents == None:
        raise Exception("---Error: Document Loading failed---")
    # carry out splitting
    texts = split(documents)
    if texts == None:
        raise Exception("---Error: Document splitting failed---")
    return texts

