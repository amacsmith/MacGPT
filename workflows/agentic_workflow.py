from agents.language_agent import LanguageAgent
from agents.analysis_agent import AnalysisAgent
from agents.code_agent import CodeAgent
from agents.planning_agent import PlanningAgent
from agents.review_agent import ReviewAgent
from functions import available_functions

class AgenticWorkflow:
    def __init__(self):
        self.agents = {
            "language": LanguageAgent(),
            "analysis": AnalysisAgent(),
            "code": CodeAgent(),
            "planning": PlanningAgent(),
            "review": ReviewAgent()
        }
        self.functions = available_functions

    async def execute(self, request_type: str, content: str):
        if request_type in self.agents:
            return await self.agents[request_type].process(content)
        elif request_type in self.functions:
            return self.functions[request_type](content)
        else:
            return f"Unknown request type: {request_type}"