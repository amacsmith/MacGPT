import os

def list_files(directory: str) -> list:
    """List files in a given directory."""
    try:
        return os.listdir(directory)
    except Exception as e:
        return f"Error: {str(e)}"

def read_file(file_path: str) -> str:
    """Read contents of a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error: {str(e)}"

def write_file(file_path: str, content: str) -> str:
    """Write content to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error: {str(e)}"