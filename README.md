# Harness Demo Architect — AI-Powered SE Copilot

A multi-agent AI system that helps Harness Sales Engineers prepare tailored demos, competitive battle cards, and customer deliverables for enterprise deals.

## Architecture

- **Orchestrator Agent** — Routes inputs by sales stage, manages agent execution
- **Research Agent** — Prospect enrichment, industry pain mapping
- **Demo Architect Agent** — Demo scripts, talk tracks, module sequencing
- **Compete Agent** — Real-time competitive battle cards
- **Content Agent** — Slide decks, leave-behind documents, follow-up emails

## Tech Stack

- **Frontend**: React + Vite + Tailwind CSS (deployed on Vercel)
- **Backend**: Python FastAPI (deployed on Railway)
- **AI Engine**: Claude API (Anthropic)
- **Knowledge Base**: Harness product knowledge embedded in agent system prompts

## Quick Start

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your Anthropic API key
python main.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Sales Stages Supported

1. **Pre-Discovery** — Prospect research brief and pain point hypotheses
2. **Discovery** — Tailored discovery questions with MEDDPICC mapping
3. **Demo Prep** — Full demo script, talk track, competitive traps, slide deck
4. **POC** — Success criteria and technical evaluation plan
5. **Expansion** — Module expansion roadmap and business case

## Built by Rutwik Vashi
Demonstrating AI-powered solutions for Sales Engineering at Harness.
