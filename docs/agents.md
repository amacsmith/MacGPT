# Agentic Architecture

[<-](vector_store.md) [Home](index.md) [->](workflow.md)

---

Our AI interface uses a multi-agent system to handle various tasks. Each agent is specialized for a specific type of operation.

## **Agents**

### BaseAgent

- All agents inherit from the `BaseAgent` abstract base class, which defines the common interface.

### LanguageAgent

- Handles general language tasks using a pre-trained language model.

### AnalysisAgent

- Performs text analysis, including sentiment analysis and named entity recognition.

### CodeAgent

- Generates code snippets based on text prompts.

### TaskAgent

- Manages long-running or periodic tasks.

### EmbeddingAgent

- Creates vector embeddings for text inputs.

### ControllerAgent

- Orchestrates the interaction between different agents and manages the overall workflow.

---

[Workflows](workflow.md)
