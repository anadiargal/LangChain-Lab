from langchain_google_genai import GoogleGenerativeAIEmbeddings
# Imports Google's embedding model into LangChain

from dotenv import load_dotenv
# Imports function to load variables from .env file

load_dotenv()
# Loads your API key and other environment variables from .env

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)
# Creates the Gemini embedding model

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
# These are the texts we want to convert into vectors

result = embedding.embed_documents(documents)
# Converts each document into an embedding vector (list of numbers)

print(result)
# Prints all the generated embedding vectors
#embed_documents() is a method/function that converts multiple pieces of text 
#into embedding vectors (lists of numbers).
#If you don't use embed_documents(), your text will not be converted 
#into embedding vectors.