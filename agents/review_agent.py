from .base_agent import BaseAgent
from prompts.system_prompts import REVIEW_SYSTEM_PROMPT
from prompts.user_prompts import REVIEW_USER_PROMPT

class ReviewAgent(BaseAgent):
    def __init__(self):
        self.system_prompt = REVIEW_SYSTEM_PROMPT

    async def process(self, content: str) -> str:
        user_prompt = REVIEW_USER_PROMPT.format(content=content)
        full_prompt = f"{self.system_prompt}\n\n{user_prompt}"

        # Use a language model to generate a review here
        # This is a placeholder for the actual implementation
        generated_review = self.generator(full_prompt, max_length=100)[0]['generated_text']

        return generated_review