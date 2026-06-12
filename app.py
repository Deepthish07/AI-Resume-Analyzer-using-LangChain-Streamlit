import streamlit as st
from pypdf import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint

from langchain_classic.chains import RetrievalQA
from langchain_community.llms import Ollama

st.title("Resume Analyzer Bot")

# LLM Configuration
st.sidebar.header("⚙️ LLM Configuration")
llm_option = st.sidebar.radio(
    "Choose LLM:",
    ["HuggingFace (Online)", "Ollama (Local)"],
    help="Choose an online or local LLM."
)

api_token = None
hf_model = None
ollama_model = None

if llm_option == "HuggingFace (Online)":
    hf_model = st.sidebar.selectbox(
        "HuggingFace model",
        [
            "mistralai/Mistral-7B-Instruct-v0.1",
            "meta-llama/Llama-2-7b-chat-hf",
            "tiiuae/falcon-7b-instruct",
        ],
        index=0,
        help="Select an online HuggingFace model repository."
    )
    api_token = st.sidebar.text_input(
        "HuggingFace API Token",
        type="password",
        help="Get it from https://huggingface.co/settings/tokens"
    )
    if not api_token:
        st.sidebar.warning("⚠️ Enter your HuggingFace API token to use online LLM")
else:
    ollama_model = st.sidebar.selectbox(
        "Ollama model",
        ["llama2-mini", "llama3"],
        index=0,
        help="Select the local Ollama model."
    )
    st.sidebar.info("Local Ollama must be installed and the model pulled in advance.")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    # Extract text
    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    if not text.strip():
        st.error("❌ No text could be extracted from this PDF.")
        st.stop()

    page_count = len(pdf.pages)
    st.info(f"📄 Resume loaded with {page_count} page{'s' if page_count != 1 else ''}.")

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.create_documents([text])

    # Embeddings
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    except ImportError as e:
        st.error(
            "❌ Missing dependency: sentence-transformers.\n"
            "Install it with `pip install sentence-transformers` or `pip install -r requirements.txt` and restart the app."
        )
        st.stop()

    # Vector Store
    try:
        db = FAISS.from_documents(
            docs,
            embeddings
        )
    except ImportError as e:
        st.error(
            "❌ Missing dependency: faiss.\n"
            "Install it with `pip install faiss-cpu` or `pip install faiss-gpu` if you have CUDA support, then restart the app."
        )
        st.stop()

    # Retriever
    retriever = db.as_retriever()

    # Initialize LLM
    try:
        if llm_option == "Ollama (Local)":
            llm = Ollama(model=ollama_model)
            # Test the connection
            llm.invoke("test")
        else:
            if not api_token:
                st.error("❌ Please enter your HuggingFace API token in the sidebar")
                st.stop()
            llm = HuggingFaceEndpoint(
                repo_id=hf_model,
                huggingfacehub_api_token=api_token,
                temperature=0.5
            )
    except Exception as e:
        st.error(f"❌ LLM initialization failed: {str(e)}")
        if "404" in str(e) or isinstance(e, FileNotFoundError):
            st.info(
                f"💡 If using Ollama, install it and pull the model:\n"
                f"   ollama pull {ollama_model}\n"
                "Or use the HuggingFace option instead."
            )
        st.stop()

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    st.success("✅ Resume Loaded")

    question = st.text_input(
        "Ask anything about the resume"
    )

    if question:
        try:
            with st.spinner("🔄 Analyzing..."):
                answer = qa.run(question)
            st.write("### Answer")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")