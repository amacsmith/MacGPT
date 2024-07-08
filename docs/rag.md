# Retrieval-Augmented Generation (RAG)

[<-](prompts.md) [Home](index.md) [->](vector_store.md)

---

Our AI interface now includes Retrieval-Augmented Generation (RAG) capabilities, allowing the system to leverage a knowledge base to provide more informed and contextually relevant responses.

## Components

1. **Document Store**: Stores and manages documents in the knowledge base.
2. **Retriever**: Retrieves relevant documents based on a given query.
3. **RAG Pipeline**: Combines retrieval and generation to produce responses.
4. **RAG Agent**: Interfaces with the RAG Pipeline to process queries.

## Usage

### Adding Documents

**To add documents to the knowledge base:**

    ```python
    POST /add_document
    {
        "content": "Document content goes here",
        "metadata": {"optional": "metadata"}
    }
    ```

### Querying with RAG

**To use the RAG system for querying:**

    ```python
    POST /process
    {
        "type": "rag",
        "content": "Your question here"
    }
    ```

## How It Works

1. When a query is received, the system retrieves relevant documents from the knowledge base.

2. These documents are used to augment the context provided to the language model.

3. The language model then generates a response based on both the query and the retrieved context.

---

[Vector Store](vector_store.md)
