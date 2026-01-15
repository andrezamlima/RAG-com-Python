# Desafio MBA – Engenharia de Software com IA (Full Cycle)

Implementação de um sistema RAG (Retrieval-Augmented Generation) com busca semântica em PDFs, utilizando PostgreSQL + pgvector, Docker e Google Generative AI

## Visão geral

O sistema permite:

- Ingestão de um documento PDF
- Geração de embeddings
- Busca semântica no banco vetorial
- Respostas baseadas exclusivamente no conteúdo do documento

Não há uso de conhecimento externo nem interpretações fora do contexto.

## Stack utilizada

- Python
- LangChain
- Google Generative AI
    - Embeddings: models/embedding-001
    - LLM: gemini-2.5-flash-lite
- PostgreSQL 17 + pgvector
- Docker & Docker Compose

## Estrutura do projeto
```
.
├── docker-compose.yml
├── requirements.txt
├── document.pdf
└── src/
    ├── ingest.py   # Ingestão e vetorização do PDF
    ├── search.py   # Busca semântica no pgvector
    └── chat.py     # Interface de chat (CLI)
```

## Como Executar

### Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.8 ou superior
- Chave de API do Google Generative AI

### Configurar ambiente

#### Criar o arquivo .env na raiz
GOOGLE_API_KEY=sua_chave_aqui

#### Instalar dependências
pip install -r requirements.txt

#### Subir o banco
docker compose up -d


### Ingestão do documento

Coloque o PDF na raiz do projeto com o nome document.pdf e execute:
```bash
python src/ingest.py
```
Os embeddings serão armazenados no PostgreSQL com pgvector.
> **Nota**: O caminho do PDF é configurável no arquivo `src/ingest.py` na variável `PDF_PATH`

### Conversar com o documento
```bash
python src/chat.py
```

**Saída esperada**:
```
Faça sua pergunta: Qual o faturamento da empresa?
Resposta: Não tenho informações necessárias para responder sua pergunta.
```

As respostas seguem estritamente o contexto recuperado do banco.

## Observações

- O banco vetorial é persistido no PostgreSQL
- O prompt impede respostas fora do contexto
- Caso a informação não exista no documento, o sistema responde de forma explícita

## Licença

Projeto desenvolvido como parte do Desafio do MBA em Engenharia de Software com IA – Full Cycle.
