from langchain.prompts import ChatPromptTemplate

template = """You are an expert in maritime knowledge, world geopolitics and economics and commodities. 
Your task is to produce an 800 word write up related to the following inputs:
{owner}, {route}, {cargo}, {fuel} using the context provided below.

{context}

Use the context as your only source of truth. 
Give a detailed analysis about the risk, opportunities and valuations of the transport.
Organise your response in the following order [route, cargo]. 

"""

prompt = ChatPromptTemplate.from_template(template)