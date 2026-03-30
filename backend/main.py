import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional
import json

load_dotenv()

from agents.orchestrator import Orchestrator

app = FastAPI(title="Harness Demo Architect", version="1.0.0")

cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = Orchestrator()


class DealInput(BaseModel):
    # Company info
    company_name: str
    industry: str
    employee_count: Optional[str] = None
    engineering_team_size: Optional[str] = None

    # Sales context
    sales_stage: str  # pre_discovery | discovery | demo_prep | poc | expansion
    deal_size_estimate: Optional[str] = None
    timeline: Optional[str] = None

    # Technical context
    current_tools: Optional[str] = None
    cloud_providers: Optional[str] = None
    tech_stack: Optional[str] = None
    deployment_frequency: Optional[str] = None

    # Pain points & requirements
    pain_points: Optional[str] = None
    key_requirements: Optional[str] = None
    compliance_needs: Optional[str] = None

    # Competitive context
    competitors_in_deal: Optional[str] = None
    incumbent_tools: Optional[str] = None

    # Stakeholders
    primary_buyer_persona: Optional[str] = None
    technical_evaluators: Optional[str] = None
    champion: Optional[str] = None

    # Output preferences
    output_format: Optional[str] = "document"  # document | slides | both


class AgentResponse(BaseModel):
    stage: str
    research_brief: Optional[dict] = None
    demo_script: Optional[dict] = None
    competitive_intel: Optional[dict] = None
    content_output: Optional[dict] = None
    agent_trace: list = []  # Shows which agents ran and what they produced


@app.get("/health")
async def health():
    return {"status": "healthy", "version": "1.0.0"}


@app.post("/api/generate")
async def generate(deal: DealInput):
    """Main endpoint — orchestrates all agents based on sales stage"""
    result = await orchestrator.run(deal.model_dump())
    return result


@app.get("/api/stages")
async def get_stages():
    """Returns available sales stages and their descriptions"""
    return {
        "stages": [
            {
                "id": "pre_discovery",
                "name": "Pre-Discovery",
                "description": "Before first customer meeting. Generates prospect research brief and initial hypotheses.",
                "required_fields": ["company_name", "industry"],
                "outputs": ["Prospect brief", "Pain point hypotheses", "Recommended modules"]
            },
            {
                "id": "discovery",
                "name": "Discovery",
                "description": "First 1-2 calls. Generates discovery questions and post-call qualification summary.",
                "required_fields": ["company_name", "industry", "primary_buyer_persona"],
                "outputs": ["Discovery question framework", "MEDDPICC mapping", "Technical qualification"]
            },
            {
                "id": "demo_prep",
                "name": "Demo Prep",
                "description": "Core use case. Generates full demo script, talk track, and slide deck.",
                "required_fields": ["company_name", "industry", "pain_points", "current_tools"],
                "outputs": ["Demo script", "Talk track", "Competitive traps", "Slide deck"]
            },
            {
                "id": "poc",
                "name": "POC / Technical Evaluation",
                "description": "Customer wants proof of concept. Generates success criteria and evaluation plan.",
                "required_fields": ["company_name", "industry", "pain_points", "key_requirements"],
                "outputs": ["POC success criteria", "Evaluation plan", "Risk mitigation"]
            },
            {
                "id": "expansion",
                "name": "Technical Close & Expansion",
                "description": "Post-win expansion. Suggests additional modules and generates business case.",
                "required_fields": ["company_name", "industry", "current_tools"],
                "outputs": ["Expansion roadmap", "Business case", "QBR content"]
            }
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
