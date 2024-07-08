from typing import List
from .retriever import Retriever
from agents.language_agent import LanguageAgent

class RAGPipeline:
    def __init__(self, retriever: Retriever, language_agent: LanguageAgent):
        self.retriever = retriever
        self.language_agent = language_agent

    async def process(self, query: str) -> str:
        # Retrieve relevant documents
        documents = self.retriever.retrieve(query)
        
        # Prepare context from retrieved documents
        context = "\n\n".join([doc.content for doc in documents])
        
        # Generate response using the language agent
        prompt = f"Given the following context:\n\n{context}\n\nAnswer the question: {query}"
        response = await self.language_agent.process(prompt)
        
        return response