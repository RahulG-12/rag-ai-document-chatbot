# 📚 RAG-Based AI Chat System using FastAPI and Qdrant

A scalable Retrieval-Augmented Generation (RAG) system designed to answer user queries based on document knowledge using vector search and LLM reasoning.  
The system uses asynchronous background processing with Redis Queue (RQ) for improved performance and scalability.

This project demonstrates modern AI backend architecture combining semantic search, vector databases, and large language models to deliver context-aware responses.

---

## 🚀 Features

- Document ingestion and semantic search
- Vector database integration using Qdrant
- Asynchronous task processing with Redis Queue (RQ)
- Context-aware response generation using Large Language Models (LLMs)
- FastAPI backend with REST APIs
- Modular and scalable architecture
- Production-ready backend design

---

## 🧠 Architecture

User Query → FastAPI → Vector Search (Qdrant) → Context Retrieval → LLM → Response

Background workers process heavy tasks asynchronously to improve performance and scalability.

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Redis (RQ)
- Qdrant Vector Database
- OpenAI API
- LangChain
- Docker
- REST APIs

---
## 📂 Project Structure


rag-system/
│── main.py
│── server.py
│── queues/
│── requirements.txt
│── docker-compose.yml
│── README.md


---

## 🎥 Demo

Due to infrastructure setup (Redis, Qdrant, and API usage), the project is demonstrated via recorded execution.

🔗 Demo Link: https://drive.google.com/drive/folders/1uPLtrFIX7AR6og8tQcSchVyqWZoesowy?usp=sharing

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO
cd YOUR_REPO
pip install -r requirements.txt
python main.py

## 📂 Project Structure
