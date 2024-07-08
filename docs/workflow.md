# Agentic Workflow

[<-](vector_store.md) [Home](index.md) [->](functions.md)

---

The agentic workflow manages the execution of requests across multiple agents and custom functions.

## Features

- Routing requests to appropriate agents or functions
- Handling follow-up requests
- Integration with the vector store for embedding-based operations

## Workflow Execution

1. Check if the request requires a custom function
2. If not, process the request with the appropriate agent
3. Handle any follow-up actions if required
4. Return the final response

---

[Functions](functions.md)
