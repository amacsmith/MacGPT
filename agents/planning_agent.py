from .base_agent import BaseAgent
from prompts.system_prompts import PLANNING_SYSTEM_PROMPT
from prompts.user_prompts import PLANNING_USER_PROMPT
from config.settings import PLANNING_AGENT_MODEL, MAX_TOKENS, TEMPERATURE
from transformers import pipeline

class PlanningAgent(BaseAgent):
    def __init__(self):
        self.system_prompt = PLANNING_SYSTEM_PROMPT
        self.generator = pipeline('text-generation', model=PLANNING_AGENT_MODEL)

    async def process(self, content: str) -> str:
        user_prompt = PLANNING_USER_PROMPT.format(task=content)
        full_prompt = f"{self.system_prompt}\n\n{user_prompt}"
        
        response = self.generator(full_prompt, 
                                  max_length=MAX_TOKENS, 
                                  temperature=TEMPERATURE,
                                  num_return_sequences=1)
        
        plan = response[0]['generated_text']
        return self.format_plan(plan)

    def format_plan(self, raw_plan: str) -> str:
        # Remove the original prompt from the generated text
        plan_start = raw_plan.find("Here's a structured plan:")
        if plan_start != -1:
            formatted_plan = raw_plan[plan_start:]
        else:
            formatted_plan = raw_plan

        # Split the plan into steps
        steps = formatted_plan.split("\n")
        
        # Remove empty steps and add numbering
        numbered_steps = [f"{i+1}. {step.strip()}" for i, step in enumerate(steps) if step.strip()]
        
        return "\n".join(numbered_steps)

    async def refine_plan(self, original_plan: str, feedback: str) -> str:
        refinement_prompt = f"""
        Original Plan:
        {original_plan}

        Feedback:
        {feedback}

        Please refine the plan based on the given feedback. Provide a revised, structured plan.
        """
        
        response = self.generator(refinement_prompt, 
                                  max_length=MAX_TOKENS, 
                                  temperature=TEMPERATURE,
                                  num_return_sequences=1)
        
        refined_plan = response[0]['generated_text']
        return self.format_plan(refined_plan)