from llm import chat
from prompts import prompt
from indexing import embed, get_vector_store

def retrieve(inputs:dict):
    '''This function takes as input the requirements of a charterer
    It formats the inputs into a query to facilitate retrieval 
    Retrieval only selects documents with distance <= 0.4 for relevance
    returns document as context'''
    
    query = f"I want information about the following: {inputs}"
    vectorstore = get_vector_store()
    try:
        context = vectorstore.similarity_search_with_score(query, k = 10)
        filtered = [(doc, score) for doc, score in context if score <= 0.4]
        final = [doc.page_content for doc, score in filtered]
        return context
    except Exception as e:
        print(f"Error: Retriever failed to retrieve documents. \nReason: {e}")
        return None
        
def generate(inputs:dict):
    return