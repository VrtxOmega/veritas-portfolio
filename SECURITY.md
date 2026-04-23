# Security Policy

## Scope

`veritas-portfolio` is a static site with no server-side code, no authentication, no user data collection, and no external API integration at runtime. The attack surface is limited to:

- The static files served by GitHub Pages.
- The GitHub Actions workflow that builds and deploys the site.
- Third-party resources loaded by `index.html` (fonts, etc.).

## Reporting a Vulnerability

If you discover a security issue in this repository (including the Actions workflow, a supply-chain issue in the single build dependency, or a compromised third-party resource loaded by the site), please report it privately:

- Open a [GitHub Security Advisory](https://github.com/VrtxOmega/veritas-portfolio/security/advisories/new) on this repository.
- Do not open a public issue for security vulnerabilities.

Expected response time: within 7 days for acknowledgment.

## Out of Scope

- Social engineering attacks against VrtxOmega.
- Vulnerabilities in GitHub itself or GitHub Pages infrastructure.
- Issues in linked ecosystem repos (report those to the respective repo's security contact).

## Ecosystem Security Contacts

For security issues in other VERITAS Universae components, refer to the `SECURITY.md` in each respective repository.
