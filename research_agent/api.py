from fastapi import FastAPI
from pydantic import BaseModel
from .agent import app as research_agent_app

api = FastAPI(title="Autonomous Research Agent API", version="1.0.0")

class ResearchRequest(BaseModel):
    topic: str

@api.post("/research")
async def research_endpoint(request: ResearchRequest):
    inputs = {"topic": request.topic}
    final_state = await research_agent_app.ainvoke(inputs, {"recursion_limit": 15})
    return {"report": final_state.get("report", "No report generated.")}

@api.get("/")
def read_root():
    return {"message": "Research Agent API is running."}