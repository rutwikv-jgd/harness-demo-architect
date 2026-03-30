from agents.base_agent import BaseAgent
from knowledge.harness_knowledge import HARNESS_PRODUCT_KNOWLEDGE, INDUSTRY_PAIN_MAPS

SYSTEM_PROMPT = f"""You are the Research Agent for the Harness Demo Architect system.
Your role is to analyze prospect information and generate a research brief
that helps Sales Engineers prepare for customer engagements.

You have deep knowledge of:
1. Harness's 16+ product modules and their value propositions
2. Industry-specific pain points and DevOps maturity patterns
3. Common technology stacks by industry
4. Harness customer success stories

{HARNESS_PRODUCT_KNOWLEDGE}

{INDUSTRY_PAIN_MAPS}

ALWAYS respond with valid JSON only. No markdown, no explanation outside the JSON.
"""


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Agent", SYSTEM_PROMPT)

    async def run(self, deal: dict) -> dict:
        stage = deal.get("sales_stage", "pre_discovery")

        prompt = f"""Analyze this prospect and generate a research brief.

PROSPECT DATA:
- Company: {deal.get('company_name', 'Unknown')}
- Industry: {deal.get('industry', 'Unknown')}
- Employee Count: {deal.get('employee_count', 'Unknown')}
- Engineering Team Size: {deal.get('engineering_team_size', 'Unknown')}
- Current Tools: {deal.get('current_tools', 'Unknown')}
- Cloud Providers: {deal.get('cloud_providers', 'Unknown')}
- Pain Points: {deal.get('pain_points', 'Not yet discovered')}
- Sales Stage: {stage}

Respond with this exact JSON structure:
{{
    "company_summary": "Brief company context relevant to Harness",
    "industry_devops_maturity": "Assessment of typical DevOps maturity in this industry",
    "likely_pain_points": ["pain1", "pain2", "pain3"],
    "recommended_harness_modules": [
        {{"module": "module_name", "relevance": "why this matters for them", "priority": "high|medium|low"}}
    ],
    "relevant_customer_stories": [
        {{"customer": "name", "industry": "industry", "result": "outcome"}}
    ],
    "key_stakeholders_to_target": ["persona1", "persona2"],
    "discovery_hypotheses": ["hypothesis1", "hypothesis2"]
}}"""

        return await self.call_claude(prompt)
