from .base_agent import BaseAgent
from transformers import pipeline
from prompts.system_prompts import LANGUAGE_AGENT_PROMPT
from prompts.user_prompts import LANGUAGE_GENERATION_PROMPT

class LanguageAgent(BaseAgent):
    def __init__(self):
        self.generator = pipeline('text-generation', model='distilgpt2')
        self.system_prompt = LANGUAGE_AGENT_PROMPT

    async def process(self, content):
        prompt = LANGUAGE_GENERATION_PROMPT.format(topic=content)
        full_prompt = f"{self.system_prompt}\n\n{prompt}"
        return self.generator(full_prompt, max_length=100)[0]['generated_text']