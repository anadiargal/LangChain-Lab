from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

# Create embedding model
embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=300
)

# Our documents
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# User's query
query = "tell me about bumrah"

# Convert documents into vectors
doc_embeddings = embedding.embed_documents(documents)

# Convert query into a vector
query_embedding = embedding.embed_query(query)

# Calculate similarity between query and every document
scores = cosine_similarity(
    [query_embedding],
    doc_embeddings
)[0]

# Find document with highest similarity score
index, score = sorted(
    list(enumerate(scores)),
    key=lambda x: x[1]
)[-1]

# Display result
print(query)
print(documents[index])
print("similarity score is:", score)

"""
                DOCUMENTS
                     │
                     ▼
          OpenAI Embedding Model
                     │
                     ▼
              Document Vectors
                     │
                     │
                     │
USER QUERY ────────► Embedding Model
                     │
                     ▼
                Query Vector
                     │
                     ▼
             Cosine Similarity
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Virat        Dhoni       ... Bumrah
      0.30         0.25            0.89
                                    ▲
                                    │
                              Highest score
                                    │
                                    ▼
                             Return Bumrah 

                             
                             
  this code converts the documents and user's question into
  vectors, compares their meanings using cosine similarity, and 
  returns the document whose meaning is closest to the question.

"""