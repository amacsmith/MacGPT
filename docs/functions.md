# Functions

[<-](workflow.md) [Home](index.md) [->](api.md)

---

Custom functions extend the capabilities of the AI interface beyond the core agent functionalities.

## Available Functions

- `weather`: Get simulated weather information for a given location
- `calculator`: Evaluate mathematical expressions

## Usage

Functions can be called by specifying the function name in the request type:

```json
{
  "type": "weather",
  "content": "New York"
}
```

**To add a new custom function:**

1. Implement the function in `functions/custom_functions.py`
2. Add the function to the `available_functions` dictionary
3. The function will automatically be available for use in the agentic workflow

---

[API Reference](api.md)
