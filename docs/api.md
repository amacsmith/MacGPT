# API Reference

[<-](functions.md) [Home](index.md)

---

## Endpoints

### POST /process

Process a request using the AI interface.

#### Request Body

```json
{
  "type": "string",
  "content": "string"
}
```

- **Type:** The type of request (e.g., "language", "analysis", "code", "task", "embedding")
- **Content:** The content to process

#### Response body

```json
{
  "response": "string"
}
```

## SOLID principles

- Single Responsibility: Each agent and class has a single, well-defined responsibility.
- Open/Closed: The system is open for extension (e.g., adding new agents) but closed for modification.
- Liskov Substitution: All agents inherit from BaseAgent and can be used interchangeably.
- Interface Segregation: The BaseAgent interface is minimal, allowing for specific implementations.
- Dependency Inversion: High-level modules (like ControllerAgent) depend on abstractions (BaseAgent) rather than concrete implementations.

## Complete the setup

1. Update `requirements.txt` to include all necessary packages.
2. Implement any missing utility functions or classes.
3. Create unit tests for each agent and the overall workflow.
4. Set up proper error handling and logging throughout the application.

This structure provides a solid foundation for a local, multi-agent AI interface with advanced features, following SOLID principles and with comprehensive documentation.

---

[Home](index.md)
