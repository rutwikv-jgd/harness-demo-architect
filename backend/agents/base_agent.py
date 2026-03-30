import os
import json
from anthropic import AsyncAnthropic


class BaseAgent:
    """Base class for all specialized agents. Handles Claude API calls."""

    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = "claude-sonnet-4-20250514"

    async def call_claude(self, user_message: str, max_tokens: int = 4096) -> dict:
        """Makes a Claude API call and parses JSON response"""
        response = await self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}]
        )

        text = response.content[0].text

        # Try to parse as JSON
        try:
            # Strip markdown code fences if present
            cleaned = text.strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            if cleaned.startswith("```"):
                cleaned = cleaned[3:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            return json.loads(cleaned.strip())
        except json.JSONDecodeError:
            return {"raw_response": text}

    async def run(self, deal: dict) -> dict:
        """Override in subclasses"""
        raise NotImplementedError
