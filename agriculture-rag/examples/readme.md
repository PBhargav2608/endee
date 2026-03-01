# Agriculture AI Assistant using Endee Vector Database

## Project Overview

This project demonstrates an AI-powered Agriculture Assistant using Endee as the vector database.

It supports:

• Semantic Search  
• Retrieval Augmented Generation (RAG)  
• AI-powered question answering  

The system helps users get intelligent answers to agriculture-related questions.

---

## Problem Statement

Farmers and agriculture students need fast access to accurate agricultural knowledge.

Traditional keyword search is inefficient.

This project uses vector search and AI to provide intelligent answers.

---

## System Architecture

User Question
     ↓
Embedding Model (Sentence Transformers)
     ↓
Endee Vector Database
     ↓
Retrieve similar vectors
     ↓
LLM (Ollama / Gemini)
     ↓
Final Answer

---

## Technologies Used

• Endee Vector Database  
• Python  
• Sentence Transformers  
• Vector Search  
• Retrieval Augmented Generation (RAG)  
• LLM Integration  

---

## How Endee is Used

Endee stores vector embeddings of agriculture knowledge.

When user asks question:

• Question converted to embedding  
• Endee searches similar vectors  
• Top matches returned  
• Used for generating AI answer  

---

## Setup Instructions

### Step 1 Install dependencies

### Step 2 Start Endee server

### Step 3 Store vectors

### Step 4 Run semantic search

### Step 5 Run RAG system

---

## Features Demonstrated

✔ Semantic Search  
✔ Vector Database Integration  
✔ RAG Workflow  
✔ AI Question Answering  
