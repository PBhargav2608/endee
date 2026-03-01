import requests
import msgpack
from sentence_transformers import SentenceTransformer

INDEX_NAME = "rootsofchange"

SEARCH_URL = f"http://127.0.0.1:8080/api/v1/index/{INDEX_NAME}/search"

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

query = input("\nEnter your agriculture question: ")

print("Generating embedding...")
embedding = model.encode(query).tolist()

payload = {
    "vector": embedding,
    "k": 5,
    "ef": 128
}

print("\nSearching in Endee...")

response = requests.post(
    SEARCH_URL,
    json=payload,
    headers={"Content-Type": "application/json"}
)

print("\nStatus:", response.status_code)

results = msgpack.unpackb(response.content, raw=False)

print("\nTop Matches:\n")

best_id = None
best_score = -1

for result in results:

    score = result[0]
    vector_id = result[1]

    print("Vector ID:", vector_id)
    print("Similarity Score:", score)
    print("----------------------------------")

    if score > best_score:
        best_score = score
        best_id = vector_id


print("\n==============================")
print("BEST MATCH")
print("==============================")

print("Vector ID:", best_id)
print("Similarity Score:", best_score)