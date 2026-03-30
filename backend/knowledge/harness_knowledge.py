"""
Harness Product Knowledge Base
Embedded directly in agent system prompts — no vector DB needed.
This is the competitive advantage of the Demo Architect system.
"""

HARNESS_PRODUCT_KNOWLEDGE = """
## HARNESS PLATFORM — COMPLETE PRODUCT KNOWLEDGE

### Company Overview
- Founded: 2017 by Jyoti Bansal (previously sold AppDynamics to Cisco for $3.7B)
- Valuation: $5.5 billion (Series E, December 2025, led by Goldman Sachs)
- ARR: $250M+ with 50%+ YoY growth
- Employees: 1,200+
- Customers: 1,000+ enterprise engineering teams
- Recognition: Gartner Magic Quadrant Leader (2024, 2025), Forrester Wave Leader (2025)
- Vision: "AI for Everything After Code"

### The Four Pillars

#### PILLAR 1: AI for DevOps & Automation
1. **Continuous Delivery & GitOps** — Enterprise CD with canary, blue/green, rolling deployments. AI-powered verification and automatic rollbacks. GitOps-as-a-Service on Argo CD. BEST-IN-CLASS — this is where Harness started and where it's strongest.
2. **Continuous Integration** — 4x faster builds. Container-native (acquired Drone.io 2020). Test Intelligence uses ML to run only relevant tests, reducing test time by 80%.
3. **Internal Developer Portal (IDP)** — Built on Backstage. IDP 2.0 with catalog auto-discovery, self-service workflows. Won "Best Platform Engineering Solution."
4. **Infrastructure as Code Management** — Terraform, OpenTofu, CloudFormation with governance guardrails.
5. **Database DevOps** — Schema change management integrated into pipelines.
6. **Artifact Registry** — Container and artifact management.
7. **Code Repository** — Git-based SCM.

#### PILLAR 2: AI for Testing & Resilience
8. **Feature Management & Experimentation** — Progressive rollouts, A/B testing (bolstered by Split Software acquisition 2024).
9. **Resilience Testing** — Chaos engineering via ChaosNative acquisition (2021) and LitmusChaos.
10. **AI Test Automation** — Intent-based testing in natural language. Self-healing tests. 70% maintenance reduction.
11. **AI SRE** — Automated SLO management. "Human-Aware Change Agent" correlates Slack/Teams conversations with incidents.

#### PILLAR 3: AI for Security & Compliance
12. **Application Security (SAST/DAST/SCA)** — Qwiet AI acquisition (Sept 2025). Code Property Graph with 97% true positive rate, 90% false positive reduction.
13. **Security Testing Orchestration** — Unified vulnerability prioritization in CI/CD.
14. **Web App & API Protection (WAAP)** — Runtime security from Traceable merger (March 2025).
15. **AI Security** — Launched March 2026. AI Firewall blocks prompt injection per OWASP Top 10 for LLMs.
16. **Software Supply Chain Assurance** — SBOM management and artifact integrity.

#### PILLAR 4: AI for Cost & Optimization
17. **Cloud Cost Management** — $1.9B cloud spend optimized. 30-40% savings. Kubernetes cost allocation.
18. **Software Engineering Insights** — DORA metrics, developer productivity. Propelo acquisition (2023).

### Harness AI Architecture
- **Software Delivery Knowledge Graph** — Connects commits, deployments, tests, incidents, costs, and policies
- **Purpose-Built AI Agents** — DevOps, Code, SRE, AppSec, Test, FinOps, IDP, Release agents
- **Orchestration Engine** — Turns AI recommendations into safe, repeatable automation
- Powered by Google Cloud Vertex AI (Gemini models) — no customer data used for training
- 100+ enterprise customers using AI agents in production

### Key Customer Results
- Citi: 20,000 engineers, releases from days to 7 minutes
- United Airlines: 75% faster deployments, 40% productivity gain
- Ulta Beauty: 100 to 5,000+ deployments/month (50x)
- Ancestry: 80-to-1 reduction in developer effort
"""

DEMO_FLOWS = """
## DEMO SEQUENCING BEST PRACTICES

### Default Demo Flow (45 min)
1. **Opening (5 min)** — Connect pain to platform thesis. Show AI for Everything After Code positioning.
2. **CD First (12 min)** — Always lead with Continuous Delivery. This is Harness's flagship. Show pipeline creation, deployment strategies (canary), AI verification, and automatic rollback.
3. **CI (8 min)** — Show build speed (4x faster claim), Test Intelligence (only runs relevant tests).
4. **Pain-Specific Module (10 min)** — Based on discovery: Cloud Cost Management for FinOps pain, Feature Flags for release risk, Security for compliance needs, IDP for developer experience.
5. **AI Capabilities (5 min)** — Show AIDA assistant, demonstrate how AI agents work across the pipeline.
6. **Close (5 min)** — Recap value tied to their specific pain, propose POC or next step.

### Module Selection by Pain Point
- "Deployments are slow/risky" → CD + CI
- "Cloud costs are out of control" → CCM + CD
- "Security is blocking releases" → STO + AppSec + CD
- "Too many tools, too much complexity" → IDP + CD + CI (platform consolidation story)
- "Can't measure engineering effectiveness" → SEI + CD + CI
- "Feature rollout risk" → Feature Flags + CD
- "Compliance/audit requirements" → CD (governance) + STO + Supply Chain

### Audience Adjustments
- **VP Engineering / CTO**: Lead with business metrics, DORA scores, platform consolidation ROI
- **DevOps / Platform Engineer**: Lead with pipeline creation, GitOps, Terraform integration
- **CISO / Security Leader**: Lead with AppSec, STO, WAAP, AI Security, supply chain
- **CFO / FinOps**: Lead with Cloud Cost Management, show $1.9B optimized
"""

HARNESS_COMPETITIVE_POSITIONING = """
## COMPETITIVE POSITIONING

### vs GitLab (primary competitor — in almost every deal)
HARNESS WINS:
- SCM-agnostic: Works with GitHub, GitLab, Bitbucket — customer keeps their SCM
- GitLab REQUIRES their SCM. Harness does not.
- CD depth: Advanced deployment strategies (canary, blue/green, rolling) with AI verification
- Cloud Cost Management: GitLab has nothing here
- Feature Management: Full platform (ex-Split.io) vs GitLab's basic flags
- AI architecture: Knowledge Graph + purpose-built agents vs GitLab Duo (assistant)
- Modular adoption: Buy what you need. GitLab is all-or-nothing.
GITLAB WINS:
- Single platform with SCM included
- Larger install base for CI
- More developer mindshare
EVALUATION CRITERIA TO SET: Deployment verification, AI-powered rollback, cloud cost optimization, modular adoption

### vs GitHub Actions
HARNESS WINS:
- Enterprise CD features (governance, approval workflows, multi-environment)
- Not tied to GitHub SCM
- Cloud cost management, feature flags, security — GitHub Actions is CI-only
GITHUB WINS:
- Developer familiarity, marketplace ecosystem, tight SCM integration

### vs CloudBees / Jenkins
HARNESS WINS:
- Cloud-native vs Jenkins legacy architecture
- AI-native vs manual scripting
- No Jenkins maintenance overhead
CLOUDBEES WINS:
- Existing Jenkins investment protection

### vs LaunchDarkly (Feature Flags)
HARNESS WINS:
- Feature flags + CD + CI + CCM in one platform vs point solution
- Split.io acquisition gives comparable flag capabilities
LAUNCHDARKLY WINS:
- Pure-play feature flag depth, larger flag-specific ecosystem

### vs Datadog / Splunk (Observability overlap)
HARNESS WINS:
- Harness doesn't replace observability — it consumes observability data for deployment verification
- AI SRE correlates observability signals with deployment events automatically
- Position as complementary, not competitive
"""

INDUSTRY_PAIN_MAPS = """
## INDUSTRY-SPECIFIC PAIN MAPS

### Financial Services (Banks, Insurance, FinTech)
- Regulatory compliance (SOX, PCI-DSS, OCC) slows releases
- Manual approval gates create bottlenecks
- Security scanning requirements in every pipeline
- Multi-region deployment complexity
- BEST MODULES: CD (governance), STO, AppSec, Cloud Cost Management
- PROOF POINTS: Citi (20K engineers, releases in 7 min), JPMorgan (investor + customer)

### Retail & E-Commerce
- Peak season deployment freezes
- Feature rollout risk during high-traffic periods
- Cloud cost spikes during seasonal events
- BEST MODULES: Feature Flags, CD, Cloud Cost Management
- PROOF POINTS: Ulta Beauty (50x deployment increase)

### Travel & Hospitality
- Real-time system reliability requirements
- Multi-cloud, multi-region complexity
- Legacy modernization
- BEST MODULES: CD, AI SRE, Resilience Testing
- PROOF POINTS: United Airlines (75% faster deployments)

### Technology / SaaS
- Developer velocity and DORA metrics
- Tool sprawl and platform consolidation
- Multi-cloud deployment
- BEST MODULES: CI, CD, IDP, SEI
- PROOF POINTS: Ancestry (80-to-1 effort reduction)

### Healthcare & Life Sciences
- HIPAA compliance, FDA validation
- Long approval cycles
- Security and auditability
- BEST MODULES: CD (governance), STO, AppSec, Supply Chain

### Energy & Utilities
- OT/IT convergence challenges
- Legacy infrastructure modernization
- Compliance (NERC CIP)
- BEST MODULES: CD, IaC Management, Security

### Media & Entertainment
- Rapid feature iteration
- A/B testing and experimentation
- Global CDN deployment
- BEST MODULES: Feature Flags, CI, CD
"""
