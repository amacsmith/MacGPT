# Tools

[<-](prompts.md) [Home](index.md) [->](rag.md)

---

Tools provide additional utilities that can be used by the AI interface to perform various tasks.

## Available Tools

- **web_search:** Perform a simulated web search
- **list_files:** List files in a directory
- **read_file:** Read the contents of a file
- **write_file:** Write content to a file

## Usage

Tools can be called by specifying the tool name in the request type:

```json
{
  "type": "web_search",
  "content": "AI advancements"
}
```

---

[RAG](rag.md)
