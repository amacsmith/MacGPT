from typing import List, Dict
from uuid import uuid4

class Document:
    def __init__(self, content: str, metadata: Dict = None):
        self.id = str(uuid4())
        self.content = content
        self.metadata = metadata or {}

class DocumentStore:
    def __init__(self):
        self.documents = {}

    def add_document(self, document: Document):
        self.documents[document.id] = document

    def get_document(self, doc_id: str) -> Document:
        return self.documents.get(doc_id)

    def search(self, query: str) -> List[Document]:
        # Simple search implementation. In a real-world scenario, 
        # this would use more sophisticated search algorithms.
        return [doc for doc in self.documents.values() if query.lower() in doc.content.lower()]