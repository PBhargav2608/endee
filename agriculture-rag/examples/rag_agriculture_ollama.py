import requests
import msgpack
import ollama
from sentence_transformers import SentenceTransformer

# =====================
# CONFIG
# =====================

ENDEE_URL = "http://127.0.0.1:8080"
INDEX_NAME = "rootsofchange"

# =====================
# LOAD EMBEDDING MODEL
# =====================

print("Loading embedding model...")
embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# =====================
# USER QUESTION
# =====================

question = input("\nAsk agriculture question: ")

# =====================
# GENERATE EMBEDDING
# =====================

print("Generating embedding...")

embedding = embed_model.encode(question).tolist()

# =====================
# SEARCH ENDEE
# =====================

search_url = f"{ENDEE_URL}/api/v1/index/{INDEX_NAME}/search"

payload = {
    "vector": embedding,
    "k": 3,
    "ef": 128,
    "include_vectors": False
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/x-msgpack"
}

response = requests.post(search_url, json=payload, headers=headers)

if response.status_code != 200:
    print("Endee search failed")
    exit()

results = msgpack.unpackb(response.content, raw=False)

# =====================
# EXTRACT CONTEXT
# =====================

context = ""

print("\nRetrieved context:\n")

for r in results:
    score = r[0]
    vec_id = r[1]

    print(f"ID: {vec_id} | Score: {score}")

    context += vec_id + "\n"

# =====================
# SEND TO OLLAMA
# =====================

prompt = f"""
You are an agriculture expert assistant.

Use the following knowledge:

{context}

Answer this question:

{question}

Give accurate agriculture advice.
"""

print("\nGenerating AI answer using Ollama...\n")

response = ollama.chat(
    model="phi3",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("AI Answer:\n")
print(response['message']['content'])