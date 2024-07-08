from .base_agent import BaseAgent
from sentence_transformers import SentenceTransformer

class EmbeddingAgent(BaseAgent):
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    async def process(self, content):
        return self.model.encode(content)