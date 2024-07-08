import math

def calculate(expression: str) -> float:
    """Evaluate a mathematical expression."""
    try:
        # Use a restricted set of Python's math functions
        allowed_names = {
            k: v for k, v in math.__dict__.items()
            if not k.startswith('__')
        }
        return eval(expression, {"__builtins__": {}}, allowed_names)
    except Exception as e:
        return f"Error: {str(e)}"