from .agentic_workflow import AgenticWorkflow

class RefinementWorkflow:
    def __init__(self):
        self.workflow = AgenticWorkflow()

    async def refine_code(self, initial_code: str, iterations: int = 3):
        code = initial_code
        for _ in range(iterations):
            review = await self.workflow.execute("review", code)
            code = await self.workflow.execute("code", f"Refine this code based on the review: {review}\n\n{code}")
        return code

    async def refine_plan(self, initial_plan: str, iterations: int = 3):
        plan = initial_plan
        for _ in range(iterations):
            review = await self.workflow.execute("review", plan)
            plan = await self.workflow.execute("planning", f"Refine this plan based on the review: {review}\n\n{plan}")
        return plan