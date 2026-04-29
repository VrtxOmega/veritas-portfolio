## I built a desktop Ethereum wallet where the renderer process CANNOT sign — here's the security architecture

I've been working on a desktop Ethereum wallet called OmegaWallet, and the core security property is something I haven't seen in other wallets: **the renderer process physically cannot sign transactions.**

Here's the architecture:

**The Problem With Browser Wallets**

Every browser-extension wallet (MetaMask, Phantom, Rabby) runs in the same process as the websites you visit. They use content-script isolation, but at the end of the day, both the dapp and the wallet share the browser's rendering engine. A compromised renderer — whether through a malicious site, a supply-chain attack on a dependency, or a browser zero-day — can potentially:
- Intercept or modify transaction data before signing
- Exfiltrate approval prompts
- Inject malicious calldata

The user sees "you're signing X" but the signer receives "sign Y."

**OmegaWallet's Architecture**

OmegaWallet runs as a desktop Electron app with three process tiers:

1. **Renderer Process** — Runs the React UI. Has zero access to keys, signing functions, or crypto primitives. It can only render what the main process tells it to. It communicates with the main process exclusively through schema-validated IPC channels.

2. **Main Process** — The only process with cryptographic capability. Holds keys encrypted with AES-256-GCM. Validates every IPC message against a strict schema before acting. The renderer can say "user wants to sign transaction T" but the main process independently validates T before signing — the renderer cannot inject or modify fields.

3. **Cerberus Backend** — Optional multi-signature coordination service running in a separate context. Never shares memory with the UI.

**Adversarial Validation**

I wrote an adversarial test suite that simulates attacks against this architecture:
- **Signing Liar** — 10 scenarios attempting to make the renderer lie about what's being signed (10/10 blocked)
- **IPC Breaker** — 10 scenarios attempting to inject malformed messages into the IPC channel (10/10 blocked)
- **Renderer Compromise** — 12 scenarios simulating a fully compromised renderer process (12/12 blocked — the main process still won't sign unauthorized payloads)
- **Nonce Race** — 8 scenarios attempting transaction replay attacks (8/8 blocked)
- **Filesystem Corruption** — 8 scenarios corrupting stored state (8/8 detected, no signing on corrupted state)

**141 tests total. 141 passed.**

**Why This Matters**

Most wallet "security" is UI-level — confirmation dialogs, warnings, user prompts. OmegaWallet's security is architectural. The code that draws the confirm button and the code that signs the transaction do not share memory, do not share a process, and can only communicate through a channel the main process controls absolutely.

If you compromise the renderer completely — replace every line of UI code — you still cannot sign a transaction the user didn't authorize.

**What's Next**

- Hardware wallet integration (Ledger/Trezor as additional signing anchors)
- Formal external audit
- Signed desktop binaries for Windows/macOS/Linux

**Links:**
- GitHub: https://github.com/VrtxOmega/OmegaWallet
- Full security validation: https://github.com/VrtxOmega/OmegaWallet/blob/main/SECURITY_VALIDATION.md
- SSWP cryptographic attestation: https://github.com/VrtxOmega/OmegaWallet

Open source (MIT). Happy to answer questions.
