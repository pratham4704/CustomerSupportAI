import os

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

VECTOR_PATH = "vectorstore"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def build_vectorstore():

    loader = PyPDFDirectoryLoader("knowledge_base")

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    db = FAISS.from_documents(
        chunks,
        embedding_model
    )

    db.save_local(VECTOR_PATH)

    print("Vector Store Created Successfully")


def load_vectorstore():

    if not os.path.exists(VECTOR_PATH):

        build_vectorstore()

    db = FAISS.load_local(
        VECTOR_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return db


def retrieve(query):

    db = load_vectorstore()

    docs = db.similarity_search(
        query,
        k=3
    )

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    return context