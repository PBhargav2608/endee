import json
import requests
from sentence_transformers import SentenceTransformer

INDEX_NAME = "rootsofchange"
INSERT_URL = f"http://127.0.0.1:8080/api/v1/index/{INDEX_NAME}/vector/insert"

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

with open("agriculture_data.json", "r") as f:
    data = json.load(f)

print("Storing vectors with metadata...")

for item in data:

    text_data = item["question"] + " " + item["answer"]
    embedding = model.encode(text_data).tolist()

    payload = {
        "id": item["id"],
        "vector": embedding,

        # ✅ CORRECT FIELD FOR ENDEE
        "text": {
            "question": item["question"],
            "answer": item["answer"],
            "soil": item.get("soil", ""),
            "category": item.get("category", "")
        }
    }

    response = requests.post(
        INSERT_URL,
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    print("Uploaded:", item["id"], "| Status:", response.status_code)

print("Done storing.")