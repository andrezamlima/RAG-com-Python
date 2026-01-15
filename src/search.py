from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

CONNECTION = "postgresql+psycopg://postgres:postgres@localhost:5432/rag"
COLLECTION_NAME = "documents"


def buscar_contexto(pergunta: str, k: int = 10) -> str | None:
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    vectorstore = PGVector(
        embeddings=embeddings,
        connection=CONNECTION,
        collection_name=COLLECTION_NAME,
    )

    resultados = vectorstore.similarity_search_with_score(
        pergunta,
        k=k
    )

    if not resultados:
        return None

    textos = []
    for documento, score in resultados:
        textos.append(documento.page_content)

    return "\n\n---\n\n".join(textos)
