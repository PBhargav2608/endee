# 🌾 Roots of Change — Agriculture AI Assistant using Endee Vector Database

## 📌 Project Overview

Roots of Change is an AI-powered Agriculture Assistant built using the Endee vector database. It helps farmers, researchers, and agricultural stakeholders get intelligent answers, recommendations, and insights based on semantic search and Retrieval-Augmented Generation (RAG).

This system combines:

* Semantic Search
* Retrieval-Augmented Generation (RAG)
* Vector Database (Endee)
* Local Large Language Model (Ollama)
* Recommendation logic

The assistant understands natural language queries and provides accurate agriculture advice using vector similarity and AI reasoning.

---

## 🎯 Problem Statement

Farmers and agriculture professionals often struggle to find precise, contextual, and reliable information quickly.

Traditional keyword search systems:

* Do not understand meaning
* Return irrelevant results
* Cannot provide intelligent recommendations

This project solves this problem using vector search and AI.

---

## 🚀 Features

### 1. Semantic Search

Finds relevant agriculture knowledge using meaning, not keywords.

Example:

```
Query: What grows in black soil?
Result: Cotton grows best in black soil.
```

---

### 2. Retrieval Augmented Generation (RAG)

Combines:

* Endee vector search
* Ollama local LLM

to generate intelligent answers.

Flow:

```
User Question
↓
Embedding generation
↓
Endee vector search
↓
Retrieve relevant knowledge
↓
Ollama generates final answer
```

---

### 3. Agriculture Recommendation System

Provides recommendations such as:

* Suitable crops
* Soil-based suggestions
* Farming advice

based on vector similarity.

---

### 4. Agentic AI Workflow

The system behaves like an intelligent agent:

* Understands query
* Searches vector DB
* Retrieves knowledge
* Generates intelligent response

---

## 🧠 How Endee Vector Database is Used

Endee is used for:

* Storing agriculture knowledge as vectors
* Fast similarity search
* Retrieving relevant information for RAG

Vector example stored in Endee:

```
{
"id": "agri_1",
"vector": [384 dimensional embedding],
"meta": {
"question": "What grows in black soil?",
"answer": "Cotton grows best in black soil"
}
}
```

Search example:

```
POST /api/v1/index/rootsofchange/search
```

Endee returns most similar vectors instantly.

---

## 🏗 System Architecture

```
User Question
      ↓
SentenceTransformer Embedding Model
      ↓
Endee Vector Database
      ↓
Top Similar Results Retrieved
      ↓
Ollama Local LLM
      ↓
Final AI Generated Answer
```

---

## 🧰 Technologies Used

| Component       | Technology                             |
| --------------- | -------------------------------------- |
| Vector Database | Endee                                  |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| LLM             | Ollama (phi3 / mistral)                |
| Backend         | Python                                 |
| API             | REST                                   |
| Container       | Docker                                 |
| Version Control | GitHub                                 |

---

## 📂 Project Structure

```
endee/
│
├── agriculture-rag/
│   ├── examples/
│   │   ├── store_vectors.py
│   │   ├── search_vectors.py
│   │   └── rag_agriculture_ollama.py
│   │
│   └── agriculture_data.json
│
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

## ⚙ Installation and Setup

### Step 1: Clone repository

```
git clone https://github.com/PBhargav2608/endee
cd endee
```

---

### Step 2: Start Endee server

```
docker compose up -d
```

Endee runs at:

```
http://127.0.0.1:8080
```

---

### Step 3: Create Python virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### Step 4: Install dependencies

```
pip install sentence-transformers requests msgpack ollama
```

---

### Step 5: Install Ollama

Download from:

https://ollama.com/download

Pull model:

```
ollama pull phi3
```

---

### Step 6: Store vectors

```
python store_vectors.py
```

---

### Step 7: Run semantic search

```
python search_vectors.py
```

---

### Step 8: Run RAG AI assistant

```
python rag_agriculture_ollama.py
```

Example:

```
Ask agriculture question: What grows in black soil?
```

Output:

```
Cotton grows best in black soil because it retains moisture well.
```

---

## 📊 Example Output

```
Query: rice

Semantic Search Result:
agri_0 score: 0.56

RAG Answer:
Rice grows best in clayey soil with good water retention.
```

---

## 📈 Performance Benefits

* Fast search using Endee vector indexing
* Accurate semantic understanding
* Intelligent answers using RAG
* Fully local AI using Ollama
* No external API dependency

---

## 🧪 Use Cases

* Farmer assistance
* Agriculture recommendation systems
* Smart agriculture platforms
* AI chatbots
* Knowledge retrieval systems

---

## 🔮 Future Improvements

* Add crop disease detection
* Add recommendation filtering
* Build web interface
* Deploy on cloud

---



## ⭐ Mandatory Endee Repository Usage

This project is built using forked Endee repository as required:

Official repo:
https://github.com/endee-io/endee

Forked repo used for development.

---

## 📜 License

This project follows Endee repository license.
