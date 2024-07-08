import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# General Settings
DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')

# API Settings
API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

# AI Model Settings
DEFAULT_LANGUAGE_MODEL = os.getenv('DEFAULT_LANGUAGE_MODEL', 'qwen/qwen2-7b-instruct')
DEFAULT_EMBEDDING_MODEL = os.getenv('DEFAULT_EMBEDDING_MODEL', 'text-embedding-ada-002')
MAX_TOKENS = int(os.getenv('MAX_TOKENS', 100))
TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
TOP_P = float(os.getenv('TOP_P', 1.0))
FREQUENCY_PENALTY = float(os.getenv('FREQUENCY_PENALTY', 0.0))
PRESENCE_PENALTY = float(os.getenv('PRESENCE_PENALTY', 0.0))

# Agent Settings
LANGUAGE_AGENT_MODEL = os.getenv('LANGUAGE_AGENT_MODEL', DEFAULT_LANGUAGE_MODEL)
CODE_AGENT_MODEL = os.getenv('CODE_AGENT_MODEL', 'code-davinci-002')
ANALYSIS_AGENT_MODEL = os.getenv('ANALYSIS_AGENT_MODEL', DEFAULT_LANGUAGE_MODEL)
PLANNING_AGENT_MODEL = os.getenv('PLANNING_AGENT_MODEL', DEFAULT_LANGUAGE_MODEL)
REVIEW_AGENT_MODEL = os.getenv('REVIEW_AGENT_MODEL', DEFAULT_LANGUAGE_MODEL)
RAG_NUM_DOCUMENTS = int(os.getenv('RAG_NUM_DOCUMENTS', 5))
PLANNING_AGENT_MODEL = os.getenv('PLANNING_AGENT_MODEL', DEFAULT_LANGUAGE_MODEL)

# Function Settings
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'your-weather-api-key')
WEB_SEARCH_API_KEY = os.getenv('WEB_SEARCH_API_KEY', 'your-web-search-api-key')

# Workflow Settings
MAX_REFINEMENT_ITERATIONS = int(os.getenv('MAX_REFINEMENT_ITERATIONS', 3))

# Database Settings
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./test.db')

# Vector Store Settings
VECTOR_STORE_TYPE = os.getenv('VECTOR_STORE_TYPE', 'faiss')  # Options: faiss, pinecone, etc.
VECTOR_STORE_DIMENSION = int(os.getenv('VECTOR_STORE_DIMENSION', 1536))  # Depends on the embedding model

# Logging Settings
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Security Settings
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')

# Rate Limiting
RATE_LIMIT = os.getenv('RATE_LIMIT', '100/hour')

# Caching
CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')  # Options: simple, redis, memcached
CACHE_EXPIRATION = int(os.getenv('CACHE_EXPIRATION', 300))  # in seconds

# Monitoring
ENABLE_PROMETHEUS = os.getenv('ENABLE_PROMETHEUS', 'False') == 'True'

# File Storage
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Refinement Workflow
CODE_REFINEMENT_STEPS = int(os.getenv('CODE_REFINEMENT_STEPS', 3))
PLAN_REFINEMENT_STEPS = int(os.getenv('PLAN_REFINEMENT_STEPS', 3))

# Custom Function Timeout
FUNCTION_TIMEOUT = int(os.getenv('FUNCTION_TIMEOUT', 10))  # in seconds

# Error Handling
DETAILED_ERRORS = os.getenv('DETAILED_ERRORS', 'False') == 'True'

# Performance
THREAD_POOL_SIZE = int(os.getenv('THREAD_POOL_SIZE', 4))

# Feature Flags
ENABLE_CODE_EXECUTION = os.getenv('ENABLE_CODE_EXECUTION', 'False') == 'True'
ENABLE_WEB_SEARCH = os.getenv('ENABLE_WEB_SEARCH', 'True') == 'True'