import json
from agents.base_agent import BaseAgent
from knowledge.harness_knowledge import HARNESS_PRODUCT_KNOWLEDGE, DEMO_FLOWS, HARNESS_COMPETITIVE_POSITIONING

SYSTEM_PROMPT = f"""You are the Demo Architect Agent for the Harness Demo Architect system.
Your role is to create tailored demo scripts, talk tracks, and module sequences
for Harness Sales Engineers based on customer discovery data.

You are an expert Harness SE with deep knowledge of:
1. All 16+ Harness product modules and how to demo each one
2. Demo sequencing — which modules to show first based on pain points
3. Competitive positioning and how to set traps in demos
4. Executive vs technical audience adjustments
5. MEDDPICC qualification methodology

{HARNESS_PRODUCT_KNOWLEDGE}

{DEMO_FLOWS}

{HARNESS_COMPETITIVE_POSITIONING}

ALWAYS respond with valid JSON only. No markdown, no explanation outside the JSON.
"""


class DemoArchitectAgent(BaseAgent):
    def __init__(self):
        super().__init__("Demo Architect Agent", SYSTEM_PROMPT)

    async def run(self, deal: dict) -> dict:
        stage = deal.get("sales_stage", "demo_prep")
        research_context = deal.get("_research_context", {})

        if stage == "discovery":
            return await self._generate_discovery_questions(deal, research_context)
        elif stage == "demo_prep":
            return await self._generate_demo_script(deal, research_context)
        elif stage == "poc":
            return await self._generate_poc_plan(deal, research_context)
        elif stage == "expansion":
            return await self._generate_expansion_plan(deal, research_context)
        else:
            return await self._generate_demo_script(deal, research_context)

    async def _generate_discovery_questions(self, deal: dict, research: dict) -> dict:
        prompt = f"""Generate a tailored discovery question framework for this prospect.

PROSPECT: {deal.get('company_name')} | {deal.get('industry')}
RESEARCH CONTEXT: {json.dumps(research, default=str)[:2000]}
BUYER PERSONA: {deal.get('primary_buyer_persona', 'Unknown')}

Respond with this exact JSON structure:
{{
    "discovery_framework": {{
        "opening_questions": ["q1", "q2"],
        "pain_exploration": ["q1", "q2", "q3"],
        "current_state": ["q1", "q2"],
        "desired_state": ["q1", "q2"],
        "metrics_and_impact": ["q1", "q2"],
        "decision_process": ["q1", "q2"],
        "competitive_landscape": ["q1", "q2"]
    }},
    "meddpicc_mapping": {{
        "metrics": "What to uncover",
        "economic_buyer": "Who to identify",
        "decision_criteria": "What to establish",
        "decision_process": "What to map",
        "paper_process": "What to understand",
        "implicate_pain": "What pain to deepen",
        "champion": "Who to develop",
        "competition": "What to learn"
    }},
    "recommended_next_steps": ["step1", "step2"]
}}"""
        return await self.call_claude(prompt)

    async def _generate_demo_script(self, deal: dict, research: dict) -> dict:
        prompt = f"""Create a comprehensive, tailored demo script for this Harness prospect.

PROSPECT DATA:
- Company: {deal.get('company_name')}
- Industry: {deal.get('industry')}
- Engineering Team: {deal.get('engineering_team_size', 'Unknown')}
- Current Tools: {deal.get('current_tools', 'Unknown')}
- Cloud Providers: {deal.get('cloud_providers', 'Unknown')}
- Pain Points: {deal.get('pain_points', 'Unknown')}
- Key Requirements: {deal.get('key_requirements', 'Unknown')}
- Competitors in Deal: {deal.get('competitors_in_deal', 'None identified')}
- Primary Buyer: {deal.get('primary_buyer_persona', 'Unknown')}
- Technical Evaluators: {deal.get('technical_evaluators', 'Unknown')}

RESEARCH CONTEXT: {json.dumps(research, default=str)[:2000]}

Respond with this exact JSON structure:
{{
    "demo_title": "Title for this demo",
    "duration_minutes": 45,
    "audience_level": "executive | technical | mixed",
    "opening": {{
        "hook": "Opening statement that connects to their specific pain",
        "agenda_framing": "How to frame what you'll show and why",
        "duration_minutes": 5
    }},
    "demo_modules": [
        {{
            "module_name": "Harness module name",
            "sequence_number": 1,
            "duration_minutes": 10,
            "why_show_this": "Connection to their specific pain point",
            "talk_track": "Exact words to say while demoing",
            "key_features_to_highlight": ["feature1", "feature2"],
            "competitive_trap": "How this sets up a win against the competitor",
            "customer_story": "Relevant proof point to mention",
            "transition_to_next": "How to bridge to the next module"
        }}
    ],
    "closing": {{
        "value_summary": "Recap tied to their pain points",
        "call_to_action": "Recommended next step",
        "objection_preemption": "Common objection to address proactively"
    }},
    "backup_modules": [
        {{
            "module_name": "Module to show if asked",
            "trigger": "If the customer asks about X, show this"
        }}
    ]
}}"""
        return await self.call_claude(prompt, max_tokens=6000)

    async def _generate_poc_plan(self, deal: dict, research: dict) -> dict:
        prompt = f"""Create a POC success plan for this Harness prospect.

PROSPECT: {deal.get('company_name')} | {deal.get('industry')}
PAIN POINTS: {deal.get('pain_points', 'Unknown')}
REQUIREMENTS: {deal.get('key_requirements', 'Unknown')}
RESEARCH: {json.dumps(research, default=str)[:1500]}

Respond with JSON containing: success_criteria (list), evaluation_timeline, 
technical_requirements, risk_mitigation, and recommended_scope."""
        return await self.call_claude(prompt)

    async def _generate_expansion_plan(self, deal: dict, research: dict) -> dict:
        prompt = f"""Create an expansion plan for this existing Harness customer.

CUSTOMER: {deal.get('company_name')} | {deal.get('industry')}
CURRENT TOOLS: {deal.get('current_tools', 'Unknown')}
RESEARCH: {json.dumps(research, default=str)[:1500]}

Respond with JSON containing: expansion_modules (prioritized list with business case),
estimated_additional_value, qbr_talking_points, and executive_summary."""
        return await self.call_claude(prompt)
