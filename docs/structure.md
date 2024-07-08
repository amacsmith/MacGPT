# Project Structure

[<-](installation.md) [Home](index.md) [->](configuration.md)

---

```plaintext
ai_interface/
│
├── agents/
│ ├──__init__.py
│ ├── base_agent.py
│ ├── language_agent.py
│ ├── analysis_agent.py
│ ├── code_agent.py
│ ├── task_agent.py
│ └── embedding_agent.py
│
├── prompts/
│ ├── __init__.py
│ ├── system_prompts.py
│ └── user_prompts.py
│
├── functions/
│ ├── __init__.py
│ ├── weather.py
│ └── calculator.py
│
├── tools/
│ ├── __init__.py
│ ├── web_search.py
│ └── file_operations.py
│
├── models/
│ ├── __init__.py
│ ├── database.py
│ └── vector_store.py
│
├── workflows/
│ ├── __init__.py
│ └── agentic_workflow.py
│
├── config/
│ ├── **init**.py
│ ├── settings.py
│ └── constants.py
│
├── main.py
└── requirements.txt
```

---

[Configuration](configuration.md)
