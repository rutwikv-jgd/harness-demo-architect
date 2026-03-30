import json
from agents.base_agent import BaseAgent
from knowledge.harness_knowledge import HARNESS_COMPETITIVE_POSITIONING

SYSTEM_PROMPT = f"""You are the Competitive Intelligence Agent for the Harness Demo Architect system.
Your role is to generate real-time competitive battle cards and positioning
for Harness Sales Engineers going into competitive evaluations.

{HARNESS_COMPETITIVE_POSITIONING}

ALWAYS respond with valid JSON only.
"""


class CompeteAgent(BaseAgent):
    def __init__(self):
        super().__init__("Compete Agent", SYSTEM_PROMPT)

    async def run(self, deal: dict) -> dict:
        competitors = deal.get("competitors_in_deal", "GitLab")
        incumbent = deal.get("incumbent_tools", "Unknown")

        prompt = f"""Generate a competitive battle card for this deal.

PROSPECT: {deal.get('company_name')} | {deal.get('industry')}
COMPETITORS IN DEAL: {competitors}
INCUMBENT TOOLS: {incumbent}
PAIN POINTS: {deal.get('pain_points', 'Unknown')}

Respond with this exact JSON structure:
{{
    "primary_competitor": "Name",
    "competitor_summary": "Brief assessment of their positioning",
    "harness_advantages": [
        {{"advantage": "description", "proof_point": "evidence"}}
    ],
    "competitor_weaknesses": [
        {{"weakness": "description", "how_to_expose": "demo technique"}}
    ],
    "evaluation_criteria_to_set": [
        {{"criterion": "what to get the customer to evaluate on", "why_harness_wins": "reason"}}
    ],
    "objection_handling": [
        {{"objection": "what competitor will say", "response": "how to counter"}}
    ],
    "landmines_to_set": [
        {{"question_for_customer_to_ask_competitor": "question", "expected_gap": "what competitor can't answer well"}}
    ]
}}"""
        return await self.call_claude(prompt)
