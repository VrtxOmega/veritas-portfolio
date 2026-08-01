#!/usr/bin/env python3
"""Verify the Trust Lab portfolio proof point without external dependencies.

The portfolio must advertise seven shipped proof points; link the live lab,
source, and release; report the canonical 7/50 campaign state; retain the
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
    "51 passing tests",
    "7/50 scoped independent actions",
    "seven distinct validators",
    "43 remaining",
    "$0 verified payment",
    "One review is an unfavorable root-cause rejection, not acceptance",
    "do not establish broad adoption, product efficacy, endorsement, certification, or payment",
    "$750",
    "INCONCLUSIVE",
)
required_links = (
    "https://vrtxomega.github.io/veritas-agent-trust-lab/",
    "https://github.com/VrtxOmega/veritas-agent-trust-lab",
    "https://github.com/VrtxOmega/veritas-agent-trust-lab/releases/tag/v0.1.0",
)

for text in required_text:
    assert text in html, f"missing required portfolio text: {text}"

for link in required_links:
    assert link in parser.hrefs, f"missing required portfolio link: {link}"

assert "6 shipped proof points" not in html, "stale proof-point count remains"
assert "14 passing tests" not in html, "stale Trust Lab test count remains"
assert "43 passing tests" not in html, "stale Trust Lab test count remains"
assert "6/50 scoped independent actions" not in html, "stale campaign state remains"

print("PASS: Trust Lab portfolio proof point and claim boundaries verified")
