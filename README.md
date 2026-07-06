# 🤖 Industrial Knowledge Brain

> AI-powered Industrial Document Assistant using **RAG (Retrieval-Augmented Generation)**, **Gemini AI**, **ChromaDB**, **FastAPI**, and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)

---

# 📖 Overview

Industrial Knowledge Brain is an AI-powered assistant that helps engineers, technicians, operators, and students interact with industrial documents through natural language.

Instead of manually searching through hundreds of pages of manuals, SOPs, maintenance guides, or safety documents, users can simply ask questions and receive accurate, context-aware answers.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve the most relevant document chunks before generating responses with **Google Gemini AI**.

---

# 🚀 Features

### 📄 PDF Upload
- Upload industrial manuals
- Upload SOPs
- Upload maintenance guides
- Automatic document indexing

### 🔍 AI Question Answering
- Ask questions in natural language
- Context-aware responses
- RAG-powered retrieval
- Gemini AI generated answers

### 📚 Source References
- Displays retrieved document chunks
- Evidence for every answer
- Explainable AI responses

### ⚡ Quick AI Actions
- Summarize Document
- Safety Analysis
- Maintenance Checklist
- Procedure Explanation

### 📁 Document Management
- View uploaded documents
- Search documents
- Delete documents
- Automatic vector cleanup

### 📊 Dashboard
- Total Documents
- Indexed Chunks
- AI Model
- Vector Database
- Backend Status

---

# 🏗️ System Architecture

```
                Streamlit Frontend
                        │
                        ▼
                  FastAPI Backend
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   PDF Parser      Gemini API      ChromaDB
   (PyPDF)        (LLM Response)  (Embeddings)
        │
        ▼
   AI-Powered Answers
```

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI
- Uvicorn

## AI
- Google Gemini 2.5 Flash

## Vector Database
- ChromaDB

## Embedding Model
- Gemini Embeddings

## PDF Processing
- PyPDF

## Language
- Python

---

# 📂 Project Structure

```
Industrial-Knowledge-Brain
│
├── backend
│   ├── api
│   ├── services
│   ├── core
│   ├── models
│   └── uploads
│
├── frontend
│   ├── components
│   ├── styles
│   ├── api.py
│   └── app.py
│
├── chroma_db
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/sneha140305/Industrial-Knowledge-Brain.git

cd Industrial-Knowledge-Brain
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Backend

```bash
cd backend

uvicorn app.main:app --reload
```

Backend:

```
http://localhost:8000
```

---

## Start Frontend

```bash
cd frontend

streamlit run app.py
```

Frontend:

```
http://localhost:8501
```

---

# 💡 How It Works

1. Upload PDF documents.
2. Extract text from the document.
3. Split text into chunks.
4. Generate embeddings.
5. Store embeddings in ChromaDB.
6. User asks a question.
7. Retrieve relevant chunks.
8. Send context + question to Gemini.
9. Generate accurate answer.
10. Display answer with source evidence.

---

# 🎯 Example Questions

- Summarize this document.
- What is this document about?
- Explain the maintenance procedure.
- List all safety precautions.
- What PPE is required?
- Which equipment is discussed?
- Generate a maintenance checklist.

---

# 📸 Screenshots

### Dashboard

![alt text](<Screenshot 2026-07-06 164559.png>)
---

### AI Assistant
![alt text](<Screenshot 2026-07-06 230438.png>)

### Upload Documents
![alt text](<Screenshot 2026-07-06 164957.png>)

### Chat with Sources
![alt text](<Screenshot 2026-07-06 231521.png>)

# 🔮 Future Improvements

- Multi-document chat
- OCR support for scanned PDFs
- User authentication
- Role-based access
- Voice interaction
- Multi-language support
- Cloud deployment
- Citation highlighting

---

# 👨‍💻 Team

**Team Name:** *(Add Your Team Name)*

### Members

- Sneha Choudhary
- Stuti Jain

---

# ⭐ Why This Project?

Industrial professionals spend significant time searching through lengthy manuals and SOPs.

Industrial Knowledge Brain simplifies this process by combining **RAG**, **Vector Search**, and **Generative AI** to provide instant, explainable, and context-aware answers directly from uploaded industrial documents.

---

# 📄 License

This project is developed for educational and hackathon purposes.