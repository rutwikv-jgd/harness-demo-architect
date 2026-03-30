import asyncio
import time
from typing import Any
from agents.research_agent import ResearchAgent
from agents.demo_architect_agent import DemoArchitectAgent
from agents.compete_agent import CompeteAgent
from agents.content_agent import ContentAgent


class Orchestrator:
    """
    Routes deal input to the right agents based on sales stage.
    Manages agent execution order and merges outputs.
    """

    def __init__(self):
        self.research = ResearchAgent()
        self.demo_architect = DemoArchitectAgent()
        self.compete = CompeteAgent()
        self.content = ContentAgent()

    async def run(self, deal: dict) -> dict:
        stage = deal.get("sales_stage", "demo_prep")
        agent_trace = []
        result = {"stage": stage, "agent_trace": agent_trace}

        # ---- Stage routing logic ----
        if stage == "pre_discovery":
            # Only research agent needed
            research = await self._run_agent("research", self.research, deal, agent_trace)
            result["research_brief"] = research

        elif stage == "discovery":
            # Research + Demo Architect (for discovery questions)
            research = await self._run_agent("research", self.research, deal, agent_trace)
            deal["_research_context"] = research
            demo = await self._run_agent("demo_architect", self.demo_architect, deal, agent_trace)
            result["research_brief"] = research
            result["demo_script"] = demo

        elif stage == "demo_prep":
            # All four agents — the full pipeline
            research = await self._run_agent("research", self.research, deal, agent_trace)
            deal["_research_context"] = research

            # Run demo architect and compete agent in parallel
            demo_task = self._run_agent("demo_architect", self.demo_architect, deal, agent_trace)
            compete_task = self._run_agent("compete", self.compete, deal, agent_trace)
            demo, compete = await asyncio.gather(demo_task, compete_task)

            deal["_demo_context"] = demo
            deal["_compete_context"] = compete
            content = await self._run_agent("content", self.content, deal, agent_trace)

            result["research_brief"] = research
            result["demo_script"] = demo
            result["competitive_intel"] = compete
            result["content_output"] = content

        elif stage == "poc":
            research = await self._run_agent("research", self.research, deal, agent_trace)
            deal["_research_context"] = research
            demo = await self._run_agent("demo_architect", self.demo_architect, deal, agent_trace)
            result["research_brief"] = research
            result["demo_script"] = demo

        elif stage == "expansion":
            research = await self._run_agent("research", self.research, deal, agent_trace)
            deal["_research_context"] = research
            demo = await self._run_agent("demo_architect", self.demo_architect, deal, agent_trace)
            result["research_brief"] = research
            result["demo_script"] = demo

        return result

    async def _run_agent(self, name: str, agent: Any, deal: dict, trace: list) -> dict:
        start = time.time()
        try:
            output = await agent.run(deal)
            elapsed = round(time.time() - start, 2)
            trace.append({
                "agent": name,
                "status": "success",
                "duration_seconds": elapsed
            })
            return output
        except Exception as e:
            elapsed = round(time.time() - start, 2)
            trace.append({
                "agent": name,
                "status": "error",
                "error": str(e),
                "duration_seconds": elapsed
            })
            return {"error": str(e)}
