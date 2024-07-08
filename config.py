# config.py
import os

MODEL_CACHE_DIR = os.path.join(os.path.dirname(__file__), 'model_cache')
os.makedirs(MODEL_CACHE_DIR, exist_ok=True)

MODEL_CONFIG = {
    'language': {
        'name': 'distilgpt2',
        'type': 'text-generation'
    },
    'analysis': {
        'name': 'distilbert-base-uncased-finetuned-sst-2-english',
        'type': 'sentiment-analysis'
    },
    # Add configurations for other models
}