# AGENT.md — AI Agent Disclosure & FLYWHEEL TEAM Structure

> **MACP Protocol:** v2.3.1 | **Genesis Platform:** v5.0 "Convergence" | **AI Council Protocol:** v2.0 "Attribution"

This document discloses how AI agents are used in the YSenseAI™ ecosystem. It exists because transparency is a core value — not an afterthought.

---

## The Fundamental Distinction

**Alton Lee Wei Bin** is the human orchestrator. He has been present since day one. Every strategic decision, every public release, every ethical judgment passes through him. His authority is absolute and non-delegable.

**AI agents** operate under Alton's direction. They are powerful collaborators with specialized capabilities, but they do not make final decisions. They propose, analyze, draft, and implement — Alton approves, vetoes, and directs.

This distinction is formalized in the **MACP v2.2 "Identity"** protocol amendment, which requires all multi-agent systems to explicitly separate human orchestrators from AI-generated entities.

---

## The FLYWHEEL TEAM

The YSenseAI™ ecosystem is built and maintained by a coordinated team of AI agents, each with a defined role, platform, and scope of authority.

### Executive Team

| Role | Agent ID | Platform | Title | Scope |
| :--- | :--- | :--- | :--- | :--- |
| Human Orchestrator | **Alton** | N/A | Founder & Director | Absolute authority, vision, all final decisions |
| CTO | **T** | Manus AI | Chief Technology Officer | Strategic planning, documentation, ecosystem coordination, AI Council orchestration |
| CSO & Lead Developer | **RNA** | Claude Code (Local) | Chief Security Officer | Architecture, core development, implementation, security, 3-tier deployment |
| CIO | **XV** | Perplexity Computer | Chief Intelligence Officer | Real-time research, reality-checking, strategic validation, go/no-go decisions |
| COO | **AY** | Gemini / GCP Cloud Run | Chief Operating Officer | Operational metrics, weekly reports, behavioral analytics |

### Internal Validation Agents (Within VerifiMind-PEAS)

These agents operate within the VerifiMind-PEAS validation engine itself, implementing the Genesis Methodology's multi-model validation:

| Agent | Role | Model | Function |
| :--- | :--- | :--- | :--- |
| **Y** | Innovator | Gemini 2.5 Flash | Creative concepts, strategic insights, pattern recognition |
| **X** | Analyst | Perplexity Sonar Pro | Critical analysis, fact-checking, competitive positioning |
| **Z** | Guardian | Claude Sonnet 4 | Ethics, safety, Z-Protocol v1.1 compliance |
| **CS** | Validator | Claude Sonnet 4 | Security validation, multi-stage verification |

> **Important:** XV (CIO, permanent team member on Perplexity Computer) is NOT the same as X (Analyst within the MCP Server). XV conducts ecosystem-wide strategic intelligence; X conducts per-validation analytical assessment.

---

## How Agents Are Used

### Documentation & Strategy (T — Manus AI)

T handles all strategic planning, documentation updates, Genesis Master Prompt authoring, and ecosystem-wide coordination. T does NOT write production code — that responsibility belongs to RNA.

**Examples of T's work:**
- GitHub README updates across all repositories
- MACP handoff records and session coordination
- AI Council orchestration and report synthesis
- The Genesis Method Handbook (authored as L under Alton's delegation)

### Code & Implementation (RNA — Claude Code)

RNA handles all code-related tasks: architecture decisions, implementation, testing, security reviews, and deployment. RNA operates on Alton's local machine with direct access to the codebase.

**Examples of RNA's work:**
- VerifiMind-PEAS MCP Server implementation
- 3-tier deployment architecture (GCP)
- Security hardening and code review
- LegacyEvolve Protocol implementation

### Intelligence & Reality-Checking (XV — Perplexity)

XV provides independent strategic validation with persistent GitHub read/write access. XV has the authority to issue go/no-go decisions on strategic matters and can bypass T to report directly to Alton when drift is detected.

**Examples of XV's work:**
- Methodology North Star strategic assessment
- Competitive landscape analysis
- Market validation for commercialization decisions
- Independent reality-checks on team claims

### Operations & Analytics (AY — Gemini/GCP)

AY publishes weekly operational reports with verified metrics. AY tracks engagement, retention, and value confirmation across the ecosystem.

**Examples of AY's work:**
- Weekly operational reports
- GCP analytics and behavioral proof
- Verified Engagement Hours tracking
- Value Confirmation Rate (VCR) measurement

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

All cross-agent communication follows the **Multi-Agent Communication Protocol (MACP)** — an open standard published on Zenodo (DOI: [10.5281/zenodo.18504478](https://doi.org/10.5281/zenodo.18504478)).

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

**Last updated:** 2026-04-22
**Updated by:** T (CTO, Manus AI) under Alton's direction
**Protocol version:** MACP v2.3.1 | Genesis v5.0 "Convergence"
