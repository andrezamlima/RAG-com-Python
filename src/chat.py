from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from search import buscar_contexto

load_dotenv()

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def chat():
    pergunta = input("Faça sua pergunta: ")

    contexto = buscar_contexto(pergunta)

    if not contexto:
        print("Não tenho informações necessárias para responder sua pergunta.")
        return

    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    mensagem = prompt.invoke({
        "contexto": contexto,
        "pergunta": pergunta
    })

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite"
    )

    resposta = llm.invoke(mensagem).content
    print("Resposta:", resposta)

if __name__ == "__main__":
    chat()
