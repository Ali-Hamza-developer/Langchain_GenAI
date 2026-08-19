# Embedding Models

This folder contains examples of **Embedding Models** and how embeddings can be used to compare the meaning of text.

## What is an Embedding?

An embedding converts text into a list of numbers called a **vector**.

For example:

```text
"LangChain is a framework"
          ↓
Embedding Model
          ↓
[0.12, -0.45, 0.78, 0.23, ...]
```

The vector represents the semantic meaning of the text.

Texts with similar meanings generally produce vectors that are closer together.

## Why are Embeddings Used?

Embeddings are commonly used for:

- Semantic search
- Document search
- Recommendation systems
- Retrieval-Augmented Generation (RAG)
- Document similarity
- Question answering
- Clustering

## Files in this Folder

### `1_embedding_openai_query.py`

Demonstrates creating an embedding for a query using an OpenAI embedding model.

### `2_embedding_openai_docs.py`

Demonstrates creating embeddings for documents using an OpenAI embedding model.

### `3_embedding_hf_local.py`

Demonstrates generating embeddings using a Hugging Face model locally.

### `4_document_similarity.py`

Demonstrates comparing documents based on their embedding vectors.

## Basic Example

A typical embedding workflow looks like:

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector = embeddings.embed_query(
    "What is LangChain?"
)

print(vector)
```

The result is a vector containing many numerical values.

## Query Embedding vs Document Embedding

There are commonly two types of embedding operations.

### Query Embedding

Used when a user searches for something:

```python
embeddings.embed_query("What is LangChain?")
```

### Document Embedding

Used when converting documents into vectors:

```python
embeddings.embed_documents([
    "LangChain is a framework for building applications with LLMs.",
    "Embeddings represent text as numerical vectors."
])
```

## Document Similarity

Suppose we have:

```text
Document A:
"LangChain is used to build LLM applications."

Document B:
"LangChain helps developers create applications using language models."

Document C:
"Python is a programming language."
```

After converting them into embeddings, we can calculate their similarity.

Conceptually:

```text
Document A ─────┐
                ├── Similarity Calculation
Document B ─────┘
       ↑
   High similarity

Document C
   ↓
Lower similarity
```

A common similarity measure is **cosine similarity**.

## Embeddings in RAG

Embeddings are an important part of Retrieval-Augmented Generation (RAG).

A typical RAG pipeline is:

```text
Documents
    ↓
Document Embeddings
    ↓
Vector Database
    ↓
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Relevant Documents
    ↓
Chat Model / LLM
    ↓
Answer
```

## Environment Variables

If you are using an API-based embedding model, store the API key in `.env`.

Example:

```text
OPENAI_API_KEY=your_api_key
```

Never hard-code API keys directly into Python files.

## Learning Goals

After completing this folder, you should understand:

- What embeddings are
- How text is converted into vectors
- Query embeddings
- Document embeddings
- Semantic similarity
- Cosine similarity
- The role of embeddings in RAG
- The difference between embedding models and Chat Models
