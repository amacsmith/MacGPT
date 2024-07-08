from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    async def process(self, content):
        pass