# Resume Analyzer Bot

A Streamlit app that loads a PDF resume, creates embeddings, and answers questions using either a local Ollama model or an online HuggingFace endpoint.

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run locally

```powershell
streamlit run app.py
```

## Notes for deployment

- For online LLM use, supply a HuggingFace API token in the sidebar.
- For local Ollama use, install Ollama and pull the selected model first:

```powershell
ollama pull llama2-mini
```

- If deploying to Streamlit Cloud, make sure `requirements.txt` is included in the repo.
