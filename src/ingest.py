from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

PDF_PATH = "document.pdf"

CONNECTION = "postgresql+psycopg://postgres:postgres@localhost:5432/rag"

COLLECTION_NAME = "documents"


def ingest():
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(documents)

    print(f"Total de chunks: {len(chunks)}")

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    PGVector.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        connection=CONNECTION,
    )

    print("Ingestão concluída com sucesso!")


if __name__ == "__main__":
    ingest()
