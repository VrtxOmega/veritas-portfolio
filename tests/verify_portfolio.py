#!/usr/bin/env python3
"""Verify the Trust Lab portfolio proof point without external dependencies.

The portfolio must advertise seven shipped proof points; link the live lab,
source, release, and public verifier challenge; report the canonical 9/50
Protocol v2 campaign state; retain the
INCONCLUSIVE efficacy and adoption boundary; and describe the fixed-price pilot
without inflating the scoped outside actions.
"""

from html.parser import HTMLParser
from pathlib import Path


class PortfolioParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag == "a":
            attributes = dict(attrs)
            if attributes.get("href"):
                self.hrefs.append(attributes["href"])


root = Path(__file__).resolve().parents[1]
html = (root / "index.html").read_text(encoding="utf-8")
parser = PortfolioParser()
parser.feed(html)
parser.close()

required_text = (
    "7 shipped proof points",
    "VERITAS Omega Agent Trust Lab",
    "56 passing tests",
    "9/50 scoped outside actions",
    "nine distinct validators",
    "41 remaining",
    "zero independent verifier runs",
    "$0 settled revenue",
    "20 direct external PR merges",
    "One review is an unfavorable root-cause rejection, not acceptance",
    "do not establish broad adoption, product efficacy, endorsement, certification, or payment",
    "$750",
    "INCONCLUSIVE",
)
required_links = (
    "https://vrtxomega.github.io/veritas-agent-trust-lab/",
    "https://github.com/VrtxOmega/veritas-agent-trust-lab",
    "https://github.com/VrtxOmega/veritas-agent-trust-lab/releases/tag/v0.1.0",
    "https://github.com/VrtxOmega/veritas-agent-trust-lab/issues/60",
)

for text in required_text:
    assert text in html, f"missing required portfolio text: {text}"

for link in required_links:
    assert link in parser.hrefs, f"missing required portfolio link: {link}"

assert "6 shipped proof points" not in html, "stale proof-point count remains"
assert "14 passing tests" not in html, "stale Trust Lab test count remains"
assert "43 passing tests" not in html, "stale Trust Lab test count remains"
assert "6/50 scoped independent actions" not in html, "stale campaign state remains"
assert "7/50 scoped independent actions" not in html, "stale campaign state remains"
assert "15 merged external contributions" not in html, "stale merge count remains"

print("PASS: Trust Lab portfolio proof point and claim boundaries verified")
