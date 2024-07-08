import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.dimension = 768  # Adjust based on your embedding size
        self.index = faiss.IndexFlatL2(self.dimension)
        self.texts = []

    def add(self, text, embedding):
        self.index.add(np.array([embedding]))
        self.texts.append(text)

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(np.array([query_embedding]), k)
        return [(self.texts[i], distances[0][j]) for j, i in enumerate(indices[0])]