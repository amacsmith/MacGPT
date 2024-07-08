from .base_agent import BaseAgent
from transformers import pipeline
from prompts.system_prompts import ANALYSIS_AGENT_PROMPT
from prompts.user_prompts import SENTIMENT_ANALYSIS_PROMPT, ENTITY_RECOGNITION_PROMPT

class AnalysisAgent(BaseAgent):
    def __init__(self):
        self.sentiment_analyzer = pipeline('sentiment-analysis')
        self.ner = pipeline('ner')
        self.system_prompt = ANALYSIS_AGENT_PROMPT

    async def process(self, content):
        sentiment_prompt = SENTIMENT_ANALYSIS_PROMPT.format(text=content)
        ner_prompt = ENTITY_RECOGNITION_PROMPT.format(text=content)
        
        sentiment = self.sentiment_analyzer(sentiment_prompt)[0]
        entities = self.ner(ner_prompt)
        
        return {
            "sentiment": sentiment,
            "entities": entities
        }