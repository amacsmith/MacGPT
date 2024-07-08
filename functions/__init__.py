from .weather import get_weather
from .calculator import calculate
from .code_execution import execute_code
from .web_search import web_search

available_functions = {
    "get_weather": get_weather,
    "calculate": calculate,
    "execute_code": execute_code,
    "web_search": web_search
}