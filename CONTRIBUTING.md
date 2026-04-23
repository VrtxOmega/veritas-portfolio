# Contributing to veritas-portfolio

## Scope

This repository is a documentation and static site index. Contributions are welcome in two categories:

1. **Documentation corrections** — factual errors, broken links, or outdated information in `README.md`, `CONTRIBUTING.md`, or `SECURITY.md`.
2. **Site content updates** — changes to `index.html` or `src/` that add or correct information surfaced in the portfolio index.

Code refactors, dependency upgrades, and redesigns are out of scope unless there is a tracked issue.

## VERITAS Universae Standard

All contributions must follow the spec + proof principle:

- Do not add a claim without a corresponding verifiable implementation.
- Do not link to a repo or resource that does not exist or is private without noting it explicitly.
- Keep the "What It Is Not" section accurate. If you add a capability, check whether it invalidates an existing "not" statement.

## Process

1. Fork the repository and create a branch from `master`.
2. Make your changes. Keep commits focused: one logical change per commit.
3. Open a pull request with a clear description of what changed and why.
4. PRs that touch documentation only do not require a build passing, but must not break the Vite build (`npm run build`).

## Code of Conduct

Treat contributors with respect. Disagreements about technical decisions are resolved by evidence, not by volume.
