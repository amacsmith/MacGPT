# Configuration Guide

[<-](structure.md) [Home](index.md) [->](prompts.md)

---

The AI Interface uses a centralized configuration system defined in `config/settings.py`. This file loads settings from environment variables, allowing for easy configuration changes without modifying the code.

## Key Configuration Options

- `DEBUG`: Enable/disable debug mode
- `DEFAULT_LANGUAGE_MODEL`: The default language model to use
- `MAX_TOKENS`: Maximum number of tokens for model outputs
- `TEMPERATURE`: Controls randomness in model outputs
- `VECTOR_STORE_TYPE`: Type of vector store to use (e.g., 'faiss', 'pinecone')
- `DATABASE_URL`: URL for the database connection
- `ENABLE_CODE_EXECUTION`: Whether to allow code execution (use with caution)
- `ENABLE_WEB_SEARCH`: Whether to enable web search functionality

For a full list of configuration options, refer to `config/settings.py`.

## Setting Configuration Values

1. Create a `.env` file in the root directory of the project.
2. **Add your configuration values to this file:**

   ```shell
   DEBUG=True
   DEFAULT_LANGUAGE_MODEL=gpt-3.5-turbo
   MAX_TOKENS=100
   ```

3. These values will be automatically loaded when the application starts.

Alternatively, you can set these as environment variables in your system.

## Best Practices

- Keep sensitive information (like API keys) in the `.env` file and do not commit it to version control.
- Use different configuration values for development and production environments.
- Regularly review and update your configuration, especially security-related settings.

---

[Prompts](prompts.md)
