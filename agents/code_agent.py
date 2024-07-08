from .base_agent import BaseAgent
from prompts.system_prompts import CODE_SYSTEM_PROMPT
from prompts.user_prompts import CODE_USER_PROMPT

class CodeAgent(BaseAgent):
    def __init__(self):
        self.system_prompt = CODE_SYSTEM_PROMPT

    async def process(self, content: str) -> str:
        user_prompt = CODE_USER_PROMPT.format(task=content)
        full_prompt = f"{self.system_prompt}\n\n{user_prompt}"
        
        # Use a language model to generate code here
        # This is a placeholder for the actual implementation
        generated_code = "print('Hello, World!')"
        
        return generated_code