from typing import List
from .document_store import DocumentStore, Document

class Retriever:
    def __init__(self, document_store: DocumentStore):
        self.document_store = document_store

    def retrieve(self, query: str, top_k: int = 5) -> List[Document]:
        results = self.document_store.search(query)
        return results[:top_k]