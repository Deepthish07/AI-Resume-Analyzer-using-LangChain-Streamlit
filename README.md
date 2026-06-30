# AI Resume Analyzer using LangChain & Streamlit

An intelligent **Resume Analyzer** built with **LangChain, FAISS, Streamlit, and Ollama/Hugging Face** that enables users to upload PDF resumes and interact with them using natural language. The application leverages **Retrieval-Augmented Generation (RAG)** to answer questions based on the uploaded resume.

---

## ✨ Features

* 📄 Upload PDF resumes
* 🤖 AI-powered resume question answering
* 🔍 Semantic search using FAISS vector database
* 🧠 Context-aware responses with LangChain
* ⚡ Interactive Streamlit web interface
* 💻 Supports both Local (Ollama) and Online (Hugging Face) LLMs

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* Hugging Face Embeddings
* Ollama (Local LLM)
* PyPDF

---

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│── app.py
│── requirements.txt
│── README.md
│── assets/
└── uploads/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Deepthish07/AI-Resume-Analyzer-using-LangChain-Streamlit.git
cd AI-Resume-Analyzer-using-LangChain-Streamlit
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows (PowerShell)

```bash
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

## 💬 Sample Questions

Try asking questions such as:

* Summarize this resume.
* What are the candidate's technical skills?
* What projects are mentioned?
* What certifications does the candidate have?
* What is the candidate's educational background?
* Is this candidate suitable for a Data Scientist role?

---

## 🧠 How It Works

1. Upload a PDF resume.
2. Resume text is extracted.
3. The text is split into smaller chunks.
4. Embeddings are generated for each chunk.
5. FAISS stores the embeddings as a vector database.
6. LangChain retrieves the most relevant information.
7. The LLM generates an accurate answer based on the retrieved context.

---

## ☁️ Deployment Notes

### Using Hugging Face API

* Add your Hugging Face API Token in the application's sidebar before asking questions.

### Using Ollama (Local)

Install Ollama from:

https://ollama.com

Pull your preferred model:

```bash
ollama pull llama3
```

(Or any other supported model available on your system.)

If deploying on **Streamlit Community Cloud**, ensure that `requirements.txt` is included in the repository.

---

## 📚 Learning Objectives

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* LangChain
* Vector Databases (FAISS)
* Embeddings
* Document Question Answering
* Streamlit Application Development

---

## 👨‍💻 Author

**Deepthish D**

📧 Email: [deepthishraj@gmail.com](mailto:deepthishraj@gmail.com)

💼 LinkedIn: https://www.linkedin.com/in/deepthish-d-422181242

🐙 GitHub: https://github.com/Deepthish07


