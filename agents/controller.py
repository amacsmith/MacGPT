from .base_agent import BaseAgent
from functions import weather, calculator, custom_function
from tools import web_search, file_operations

class ControllerAgent:
    def __init__(self):
        self.agents = {
            'language': LanguageAgent(),
            'analysis': AnalysisAgent(),
            'code': CodeAgent(),
            'task': TaskAgent(),
            'embedding': EmbeddingAgent()
        }
        self.functions = {
            'custom_function': custom_function.custom_function,
            'weather': weather.get_weather,
            'calculator': calculator.calculate
        }
        self.tools = {
            'web_search': web_search.web_search,
            'list_files': file_operations.list_files,
            'read_file': file_operations.read_file,
            'write_file': file_operations.write_file
        }

    async def process_request(self, request, vector_store):
        if request.type in self.agents:
            return await self.agents[request.type].process(request.content)
        elif request.type in self.functions:
            return self.functions[request.type](request.content)
        elif request.type in self.tools:
            return self.tools[request.type](request.content)
        else:
            return f"Unknown request type: {request.type}"