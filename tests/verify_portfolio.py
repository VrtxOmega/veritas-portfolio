#!/usr/bin/env python3
"""Verify the Trust Lab portfolio proof point without external dependencies.

Before this change, the portfolio advertised six shipped proof points and had
no VERITAS Agent Trust Lab card. After this change, it must advertise seven,
link the live lab, source, and release, retain the INCONCLUSIVE independence
boundary, and describe the fixed-price pilot without inflating adoption.
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
    "14 passing tests",
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

print("PASS: Trust Lab portfolio proof point and claim boundaries verified")
