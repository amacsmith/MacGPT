# Installation Guide

[<-](index.md) [Home](index.md) [->](structure.md)

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

## Steps

1.  **Clone the repository (if you haven't already):**

    ```shell
    git clone https://github.com/amacsmith/mac-ai-interface
    ```

2.  **Create a virtual environment:**

    ```shell
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    - **On Windows:**

      ```shell
      venv\Scripts\activate
      ```

    - **On macOS and Linux:**

      ```shell
      source venv/bin/activate
      ```

4.  **Install the package and its dependencies:**

    ```shell
    pip install -e
    ```

5.  **Create a `.env` file in the root directory and add your configuration:**

    ```shell
    DEBUG=True
    SECRET_KEY=your-secret-key
    DEFAULT_LANGUAGE_MODEL=some-model
    Add other configuration variables as needed
    ```

6.  **Run the application:**

    ```shell
    uvicorn main:app --reload
    ```

The application should now be running at <http://127.0.0.1:8000>.

## Configuration

Refer to `config/settings.py` for all available configuration options. You can set these in your `.env` file or as environment variables.

## Updating

**To update the application, pull the latest changes and reinstall:**

```shell
git pull
pip install -e .
```

## Troubleshooting

If you encounter any issues during installation, please check the following:

1. Ensure you're using Python 3.8 or higher: `python --version`
2. Make sure your virtual environment is activated
3. Check that all required dependencies are installed: `pip list`
4. Verify that your `.env` file is correctly configured

If problems persist, please open an issue on the GitHub repository.

---

[Structure](structure.md)
