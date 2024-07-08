from retrieval.document_store import DocumentStore
from retrieval.retriever import Retriever
from retrieval.rag_pipeline import RAGPipeline
from agents.language_agent import LanguageAgent
from agents.rag_agent import RAGAgent

class RAGWorkflow:
    def __init__(self):
        self.document_store = DocumentStore()
        self.retriever = Retriever(self.document_store)
        self.language_agent = LanguageAgent()
        self.rag_pipeline = RAGPipeline(self.retriever, self.language_agent)
        self.rag_agent = RAGAgent(self.rag_pipeline)

    async def process_query(self, query: str) -> str:
        return await self.rag_agent.process(query)

    def add_document(self, content: str, metadata: dict = None):
        from retrieval.document_store import Document
        document = Document(content, metadata)
        self.document_store.add_document(document)