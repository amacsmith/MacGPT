from .base_agent import BaseAgent
from retrieval.rag_pipeline import RAGPipeline

class RAGAgent(BaseAgent):
    def __init__(self, rag_pipeline: RAGPipeline):
        self.rag_pipeline = rag_pipeline

    async def process(self, content: str) -> str:
        return await self.rag_pipeline.process(content)