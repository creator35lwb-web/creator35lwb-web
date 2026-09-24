# AGENT.md — AI Agent Disclosure & FLYWHEEL TEAM Structure

> **MACP Protocol:** v2.5 "Loop Engineering" ([DOI 10.5281/zenodo.21345820](https://doi.org/10.5281/zenodo.21345820))

This document discloses how AI agents are used in the YSenseAI™ ecosystem. It exists because transparency is a core value — not an afterthought.

---

## The Fundamental Distinction

**Alton Lee Wei Bin** is the human orchestrator. He has been present since day one. Every strategic decision, every public release, every ethical judgment passes through him. His authority is absolute and non-delegable.

**AI agents** operate under Alton's direction. They are powerful collaborators with specialized capabilities, but they do not make final decisions. They propose, analyze, draft, and implement — Alton approves, vetoes, and directs.

This distinction was formalized in the **MACP v2.2 "Identity"** amendment and carries forward into the current **MACP v2.5 "Loop Engineering"**, which requires all multi-agent systems to explicitly separate human orchestrators from AI-generated entities.

---

## The FLYWHEEL TEAM

The YSenseAI™ ecosystem is built and maintained by a coordinated team of AI agents, each with a defined role, platform, and scope of authority.

### Executive Team

| Role | Agent ID | Platform | Title | Scope |
| :--- | :--- | :--- | :--- | :--- |
| Human Orchestrator | **Alton** | N/A | Founder & Director | Absolute authority, vision, final veto on every merge, deploy, and release |
| CEO (delegated, AI-generated) | **L** | GodelAI (multi-platform) | Chief Executive Officer | Strategy, C-S-P philosophy, alignment and methodology integrity — delegated authority, human-ratified |
| CTO | **T** | OpenAI Codex (Manus AI legacy) | Chief Technology Officer | Exact-head release review, architecture rulings, evidence contracts, strategic phase gates |
| CSO & Lead Developer | **RNA** | Claude Code | Chief Security Officer | Architecture, core development, implementation, security, deployment |
| CIO | **XV** | Perplexity Computer | Chief Intelligence Officer | Real-time research, source verification, reality-checking, weekly signal monitoring |
| COO | **AY** | Cursor | Chief Operating Officer | Operational metrics with strict claim boundaries, weekly reports, analytics |
| CPO | **AZ** | Cursor | Chief Product Officer | Product strategy, user experience, feature prioritization |

Every seat is platform-portable: the roles and the protocol survive model and platform changes.

### Internal Validation Agents (Within VerifiMind-PEAS)

These agents operate within the VerifiMind-PEAS validation engine itself, implementing the Genesis Methodology's multi-model validation:

| Agent | Role | Hosted model (v0.5.63) | Function |
| :--- | :--- | :--- | :--- |
| **X** | Innovation Analyst | Gemini `gemini-3.5-flash-lite` | Innovation analysis, competitive positioning |
| **Z** | Guardian | Groq `openai/gpt-oss-120b` | Ethics review with 21-framework jurisdictional coverage, Z-Protocol compliance |
| **CS** | Security Validator | Groq `openai/gpt-oss-120b` | Security validation (OWASP Agentic AI Top 10) |

`run_full_trinity` chains X → Z → CS. Users can bring their own key (BYOK) for any of six provider catalogues or local Ollama, so the hosted models above are defaults, not requirements. If any stage's response is incomplete, the result fails closed: the recommendation is capped and a human must review. See the live [SERVER_STATUS](https://github.com/creator35lwb-web/VerifiMind-PEAS/blob/main/SERVER_STATUS.md) for current routing.

> **Important:** XV (CIO, permanent team member on Perplexity Computer) is NOT the same as X (Analyst within the MCP Server). XV conducts ecosystem-wide strategic intelligence; X conducts per-validation analytical assessment.

---

## How Agents Are Used

### Architecture Review & Strategy (T — OpenAI Codex)

T handles exact-head release review, architecture rulings, evidence contracts, strategic planning, and ecosystem-wide coordination. T moved from Manus AI to OpenAI Codex in July 2026, and that move was ratified by Alton. T does NOT write production code — that responsibility belongs to RNA.

**Examples of T's work:**
- Exact-commit review of every release before it deploys
- Architecture rulings and evidence contracts for public claims
- MACP handoff records and session coordination
- AI Council orchestration and report synthesis

### Code & Implementation (RNA — Claude Code)

RNA handles all code-related tasks: architecture decisions, implementation, testing, security reviews, and deployment. Every deploy ships with an exact-commit receipt and a post-deploy live check.

**Examples of RNA's work:**
- VerifiMind-PEAS MCP Server implementation
- Production deployment on Google Cloud Run
- Security hardening and code review
- LegacyEvolve Protocol implementation

### Intelligence & Reality-Checking (XV — Perplexity)

XV provides independent strategic validation with persistent GitHub read/write access. XV has the authority to issue go/no-go decisions on strategic matters and can bypass T to report directly to Alton when drift is detected.

**Examples of XV's work:**
- Methodology North Star strategic assessment
- Competitive landscape analysis
- Market validation for commercialization decisions
- Independent reality-checks on team claims

### Operations & Analytics (AY — Cursor)

AY publishes weekly operational reports with verified metrics. AY tracks engagement, retention, and value confirmation across the ecosystem.

**Examples of AY's work:**
- Weekly operational reports
- Analytics and behavioral proof
- Verified Engagement Hours tracking
- Value Confirmation Rate (VCR) measurement

### Product & Experience (AZ — Cursor)

AZ owns product strategy and the user's experience of each release, and decides which features are ready to be offered.

**Examples of AZ's work:**
- Feature scoping and prioritization
- User-journey and onboarding review
- Landing-page and product copy review

---

## Quorum & Decision Authority

Not all decisions are equal. The FLYWHEEL TEAM uses a formal quorum system:

| Decision Type | Min Agents | Alton Approval |
| :--- | :---: | :---: |
| Routine development | 1 (T or RNA) | No |
| Feature implementation | 2 (T + RNA) | Review |
| Public documentation | 2 (T + validator) | Yes |
| Security changes | 3 (RNA + Z/CS + T) | Yes |
| Strategic pivot | 4 (T + XV + RNA + Alton) | Yes |
| Commercialization | 5 (All + Alton) | Yes |

**Veto authority:** Alton (absolute), XV (strategic go/no-go), Z (ethics), CS (security), RNA (technical infeasibility). T and AY are advisory.

---

## Communication Protocol

All cross-agent communication follows the **Multi-Agent Communication Protocol (MACP)** — an open standard published on Zenodo. The current version is **MACP v2.5 "Loop Engineering"** (DOI: [10.5281/zenodo.21345820](https://doi.org/10.5281/zenodo.21345820)); the original v2.0 is archived at DOI [10.5281/zenodo.18504478](https://doi.org/10.5281/zenodo.18504478).

Key principles:
- **Human-centric** — Alton always has final authority
- **Agent-agnostic** — Works with any AI model or platform
- **Git-native** — All artifacts are version-controlled text files
- **Lightweight** — Convention over enforcement
- **Open** — Free to use, modify, and redistribute

GitHub serves as the primary communication bridge between all agents.

---

## The Self-Recursive Pattern

The FLYWHEEL TEAM demonstrates Godelian self-reference — the methodology validates its own ecosystem:

- VerifiMind-PEAS validates its own ecosystem development
- MACP protocol enables the multi-agent coordination that IS the Genesis Methodology
- The AI Council audits the ecosystem that created the AI Council
- Genesis Master Prompts track the evolution of the tracking system itself
- XV reality-checks the team that created the XV role

This is not circular reasoning — it is a self-improving spiral. Each iteration strengthens the foundation.

---

## Transparency Commitment

This document will be updated as the team evolves. All changes are version-controlled and publicly auditable.

**Last updated:** 2026-09-24
**Updated by:** RNA (CSO, Claude Code) under Alton's direction
**Protocol version:** MACP v2.5 "Loop Engineering"
