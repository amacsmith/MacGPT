import subprocess

def execute_code(code: str, language: str) -> str:
    """Execute code and return the output."""
    if language == "python":
        try:
            result = subprocess.run(["python", "-c", code], capture_output=True, text=True, timeout=5)
            return result.stdout if result.returncode == 0 else result.stderr
        except subprocess.TimeoutExpired:
            return "Execution timed out"
    else:
        return f"Execution for {language} is not supported"