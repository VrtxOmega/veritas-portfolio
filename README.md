# VERITAS Ω — Engineering the Sovereign Stack

> Public evidence index for the VERITAS Universe: a deterministic, local-first, zero-trust software ecosystem built and operated by VrtxOmega.

**Live Portfolio:** https://vrtxomega.github.io/veritas-portfolio/

---

## Ecosystem Canon

VERITAS Universe is a collection of independently deployable components that share one invariant: no capability is claimed without a corresponding implementation that can be audited, run, and broken. Every component operates under an explicit trust boundary; nothing is implicitly trusted by position or label. The portfolio site is the public-facing index — its job is to surface proof, not pitch. Local-first posture means each component runs fully offline by default; network access is opt-in and scoped. The sovereign stack is not a product — it is a set of constraints that produce predictable, auditable behavior at each integration point.

---

## What It Is

- A static GitHub Pages site (`index.html` + Vite build) that acts as a navigable index of the VERITAS Universe components.
- A public-facing surface demonstrating the engineering record: architecture decisions, threat models, and operational constraints of each ecosystem component.
- Built with Vite (no framework dependency). Deployed automatically on push to `master` via GitHub Actions.

## What It Is Not

- A financial portfolio manager or investment platform.
- A SaaS product with accounts, real-time data feeds, or a sign-up flow.
- A marketing site with unchecked claims — every statement in this repo's docs must be traceable to an actual implementation.

---

## Proof Surface

The following repos are the strongest signal in the ecosystem. Each link points to a real implementation with verifiable constraints.

| Repo | What This Proves |
|---|---|
| [omega-brain-mcp](https://github.com/VrtxOmega/omega-brain-mcp) | A production-grade MCP server with explicit stdio/SSE interfaces, Docker deployment, automated tests, and a documented threat model — not a proof of concept. |
| [veritas-vault](https://github.com/VrtxOmega/veritas-vault) | Local-first SQLite (WAL + FTS5) knowledge store with a clear module map and offline-only posture; demonstrates a real persistence architecture. |
| [Aegis](https://github.com/VrtxOmega/Aegis) | Explicit trust boundaries, in-scope/out-of-scope threat model, local-only binding — demonstrates security posture defined by constraint rather than by assertion. |
| [Ollama-Omega](https://github.com/VrtxOmega/Ollama-Omega) | Six strict-schema MCP tools, SSRF mitigation, safe JSON handling, and a multi-client quickstart — demonstrates safe-by-default LLM integration. |
| [OmegaWallet](https://github.com/VrtxOmega/OmegaWallet) | Renderer-Cannot-Sign Electron wallet; cryptographic operations are confined to the main process with a validated IPC bridge — demonstrates a hard process-isolation invariant. |
| [sovereign-arcade](https://github.com/VrtxOmega/sovereign-arcade) | Self-hosted game runtime demonstrating offline-first, no-external-dependency deployment. |

---

## Running Locally

Requires Node.js ≥ 18 and npm.

```bash
# Install dependencies
npm install

# Start development server (hot reload)
npm run dev

# Build for production
npm run build

# Preview the production build locally
npm run preview
```

The dev server runs on `http://localhost:5173` by default (Vite default port).

---

## Deployment

This site is deployed to **GitHub Pages** automatically on every push to `master` via `.github/workflows/deploy.yml`. The workflow:

1. Checks out code and sets up Node.js 22.
2. Runs `npm ci` (clean install from lockfile).
3. Runs `npm run build` (Vite outputs to `./dist`).
4. Uploads `./dist` as a Pages artifact and deploys it.

No manual deployment step is required. The live URL is published in the repo's About sidebar.

**Live URL:** https://vrtxomega.github.io/veritas-portfolio/

---

## Design and Engineering Principles

- **Local-first posture**: the site is fully static; no runtime server, no external API calls required to render.
- **Explicit constraints over implicit trust**: every component linked from this index documents what it does not do as clearly as what it does.
- **Minimal dependency surface**: Vite is the only devDependency. No framework, no build-time secrets, no external CDN required for the build itself.
- **Deterministic builds**: `npm ci` from a committed lockfile ensures reproducible output.

---

## Roadmap

Items are listed only when there is an open implementation path, not as aspirational marketing.

- [ ] Add per-component architecture summary cards to the site (linked directly to source README sections).
- [ ] Surface build/CI status badges for each ecosystem repo on the index page.
- [ ] Add structured data (`JSON-LD`) to the index page for better discoverability.
- [ ] Document the inter-component trust graph (which components call which, over what interface).

---

## License

MIT — see [LICENSE](./LICENSE) for the full text.

Copyright © 2026 VrtxOmega.
