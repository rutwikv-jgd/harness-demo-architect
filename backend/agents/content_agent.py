import json
from agents.base_agent import BaseAgent

SYSTEM_PROMPT = """You are the Content Generator Agent for the Harness Demo Architect system.
Your role is to take the outputs from other agents (research, demo script, competitive intel)
and produce polished deliverables: slide content, leave-behind documents, and follow-up emails.

You produce content that is:
1. Executive-ready — clear, concise, value-focused
2. Harness-branded — using Harness terminology and positioning
3. Tailored — specific to the prospect's industry and pain points
4. Actionable — includes clear next steps

ALWAYS respond with valid JSON only.
"""


class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Content Agent", SYSTEM_PROMPT)

    async def run(self, deal: dict) -> dict:
        demo_context = deal.get("_demo_context", {})
        compete_context = deal.get("_compete_context", {})
        research_context = deal.get("_research_context", {})
        output_format = deal.get("output_format", "document")

        prompt = f"""Generate polished deliverable content for this Harness deal.

PROSPECT: {deal.get('company_name')} | {deal.get('industry')}
OUTPUT FORMAT REQUESTED: {output_format}

DEMO SCRIPT CONTEXT: {json.dumps(demo_context, default=str)[:3000]}
COMPETITIVE CONTEXT: {json.dumps(compete_context, default=str)[:2000]}
RESEARCH CONTEXT: {json.dumps(research_context, default=str)[:1500]}

Respond with this JSON structure:
{{
    "slide_deck": {{
        "title_slide": {{"title": "text", "subtitle": "text"}},
        "slides": [
            {{
                "slide_number": 1,
                "title": "slide title",
                "content_type": "bullets | comparison | quote | metrics",
                "content": "slide content",
                "speaker_notes": "what to say on this slide"
            }}
        ]
    }},
    "leave_behind_document": {{
        "title": "Document title",
        "executive_summary": "2-3 sentence summary",
        "sections": [
            {{"heading": "section heading", "content": "section content"}}
        ]
    }},
    "follow_up_email": {{
        "subject": "email subject",
        "body": "email body"
    }}
}}"""
        return await self.call_claude(prompt, max_tokens=6000)
