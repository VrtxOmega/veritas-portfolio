# VERITAS — Conference Submissions

## 1. DEF CON AI Village (2026)

**Talk Title:** *The Renderer Cannot Sign: Architectural Security Guarantees for Desktop Wallets*

**Format:** 25-minute talk + 5-min Q&A

**Abstract:**
Browser-extension wallets dominate crypto, but they share a fundamental security limitation: the extension runs in the same process as every website the user visits. This talk presents OmegaWallet's alternative — a desktop Ethereum wallet where the renderer process physically cannot sign transactions. We walk through the three-tier process model (Renderer → IPC → Main Process), the adversary test suite (141 scenarios across 11 campaigns), and the architectural guarantees that separate OmegaWallet from every browser wallet on the market.

**Key takeaways for attendees:**
- Why process isolation is a stronger security primitive than permission prompts
- How to build an adversarial test suite that validates architectural claims
- What "renderer-cannot-sign" actually means in an Electron context

**Evidence:** SECURITY_REPORT.md, SSWP attestation, open-source repo

---

**Talk Title:** *VERITAS: A 10-Gate Deterministic Verification Pipeline for AI Agents*

**Format:** 25-minute talk + 5-min Q&A

**Abstract:**
AI agents can hallucinate, drift from their task, or take unauthorized actions. VERITAS addresses this with a 10-gate deterministic pipeline — from intake validation through cryptographic sealing — that provides mathematical guardrails for AI agent behavior. This talk covers the gate architecture, the CLAEG state machine (what happens when a gate fails), and the SEAL chain (a SHA-256 hash chain providing immutable audit evidence). We'll demonstrate the pipeline live against a sovereign AI agent.

**Evidence:** omega-brain-mcp (Triple-A Glama rated), VERITAS-Omega-CODE spec v2.0, SSWP attestation

---

## 2. Black Hat USA (2026)

**Talk Title:** *Beyond Content Scripts: Desktop Wallet Security Through Process Architecture*

**Format:** 50-minute briefing

**Abstract:**
The dominant wallet security model — browser extensions with content-script isolation — has been exploited repeatedly. This talk makes the case that the security boundary itself is the problem: extensions and websites share a rendering engine, and that shared surface is inherently attackable. We present OmegaWallet's alternative architecture — an Electron desktop wallet where the renderer process has zero cryptographic capability — and walk through the 11-campaign adversarial test suite that validates it. We'll cover IPC schema enforcement, FreshAuth token architecture, two-phase signing with cryptographic prepareIds, and the specific attacks the architecture defends against (signing lies, IPC injection, renderer compromise, nonce races).

**Key evidence:** 141/141 adversarial tests passed, boundary scorecard (100% across 7 boundaries), severity distribution (zero S1-S5 events)

**Target audience:** Security engineers, wallet developers, crypto security researchers

---

## 3. RSA Conference (2027)

**Panel Proposal:** *Sovereign AI: The Infrastructure We Need Before Regulation Catches Up*

**Format:** Panel (3-4 speakers, 60 minutes)

**Position:** VERITAS as the case study for "what sovereign AI infrastructure looks like in practice"

**Panel description:**
The AI safety conversation has focused on model alignment, but the infrastructure question is equally critical: where does the AI run, who controls the compute, and who can verify the output? This panel brings together builders of sovereign AI infrastructure to discuss what "offline-first, verifiable AI" looks like in practice, why it matters for defense and enterprise deployment, and how deterministic verification (10-gate pipelines, cryptographic attestation, hash-chain audit trails) provides the trust layer that AI regulation will require.

**Why VERITAS on this panel:** The VERITAS Omega Universe is the most complete open-source implementation of a sovereign AI stack — governance, execution, inference, and applications — with cryptographic verifiability at every layer.

---

## Submission Status

| Conference | Submission | Status | Timeline |
|------------|-----------|--------|----------|
| DEF CON AI Village | 2 talks | Drafted | CFP typically opens May |
| Black Hat USA | 1 briefing | Drafted | CFP closed for 2026, target 2027 |
| RSA Conference | 1 panel | Drafted | CFP typically opens June for 2027 |
