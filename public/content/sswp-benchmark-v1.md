# SSWP Benchmark v1.0 — Sovereign Software Witness Protocol

**111 repos. 55,190 dependencies. 555 gate checks. 1,837 npm audit vulnerabilities. Zero SSWP adversarial flags.**

## What This Is

SSWP was benchmarked against npm audit across 111 VERITAS ecosystem repositories spanning 55,190 production dependencies. npm audit uses CVE database lookups. SSWP uses adversarial probes for typosquatting, version anomalies, and integrity gaps. They measure different attack surfaces — and together provide complete npm supply-chain coverage.

## Quick Numbers

| Metric | Value |
|---|---|
| Repositories tested | 111 |
| Total dependencies | 55,190 |
| Gate checks executed | 555 (5 per repo) |
| npm audit vulnerabilities | 1,837 |
| SSWP adversarial flags | 0 |
| Seal hash | f1655910...a4585 |

## Top Results

| Repository | Dependencies | npm Vulns | SSWP Risk |
|---|---|---|---|
| gravity-omega-v2 | 571 | 17 | 0.0% |
| NemoClaw | 749 | 15 | 0.0% |
| aegis-rewrite | 417 | 14 | 0.0% |
| clone-response | 1,201 | 80 | 0.0% |
| veritas-vault | 407 | 6 | 0.0% |

## Why This Matters

- **npm audit:** CVE database — known vulnerabilities, catalogued
- **SSWP:** Adversarial probes — unknown attack vectors, real-time
- **Together:** Full npm supply-chain attack surface coverage

Every result cryptographically sealed with SHA-256. Tamper-evident. Verifiable. Immutable.

*Benchmark executed: 2026-04-30 08:15 UTC | SSWP v1.1.0*
