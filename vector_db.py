# vector_db.py
import os
from langchain_community.document_loaders import PyPDFLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Set your model and directory
EMBEDDING_MODEL = "text-embedding-004"
PERSIST_DIR = "./chroma_db"
DATA_DIR = "./data"

def create_local_retriever():
    """Loads local documents, splits them, creates embeddings, and initializes the ChromaDB retriever."""
    
    # Check if the persistence directory exists and is populated
    if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
        print("Using existing Chroma DB.")
        embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
        vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
        return vectorstore.as_retriever(search_kwargs={"k": 3})

    print("Building new Chroma DB from local documents...")
    documents = []
    
    # 1. Load Documents
    for filename in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, filename)
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())
        elif filename.endswith(".md"):
            loader = UnstructuredMarkdownLoader(file_path)
            documents.extend(loader.load())
    
    if not documents:
        raise FileNotFoundError(f"No documents found in the {DATA_DIR} directory. Please create local_doc_1.pdf and report_notes.md.")

    # 2. Split Documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200, 
        add_start_index=True
    )
    all_chunks = text_splitter.split_documents(documents)
    
    # 3. Create Embeddings & Store
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    vectorstore = Chroma.from_documents(
        documents=all_chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )
    # The .persist() call is deprecated in modern Chroma, but included for compatibility if needed.
    # vectorstore.persist() 
    print(f"Successfully indexed {len(all_chunks)} chunks.")

    # 4. Return Retriever
    return vectorstore.as_retriever(search_kwargs={"k": 3})