from fastapi import FastAPI
from pydantic import BaseModel
from workflows.agentic_workflow import AgenticWorkflow
from workflows.refinement_workflow import RefinementWorkflow
from workflows.rag_workflow import RAGWorkflow

app = FastAPI()

agentic_workflow = AgenticWorkflow()
refinement_workflow = RefinementWorkflow()
rag_workflow = RAGWorkflow()

class Request(BaseModel):
    type: str
    content: str

class DocumentRequest(BaseModel):
    content: str
    metadata: dict = None

@app.post("/process")
async def process_request(request: Request):
    if request.type == "rag":
        response = await rag_workflow.process_query(request.content)
    else:
        response = await agentic_workflow.execute(request.type, request.content)
    return {"response": response}

@app.post("/refine_code")
async def refine_code(request: Request):
    refined_code = await refinement_workflow.refine_code(request.content)
    return {"refined_code": refined_code}

@app.post("/refine_plan")
async def refine_plan(request: Request):
    refined_plan = await refinement_workflow.refine_plan(request.content)
    return {"refined_plan": refined_plan}

@app.post("/add_document")
async def add_document(request: DocumentRequest):
    rag_workflow.add_document(request.content, request.metadata)
    return {"status": "Document added successfully"}

@app.post("/generate_plan")
async def generate_plan(request: Request):
    plan = await agentic_workflow.planning_agent.process(request.content)
    return {"plan": plan}