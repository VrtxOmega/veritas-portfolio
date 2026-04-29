## Show HN: Sovereign Arcade — 8 offline games with a gold-and-obsidian design system

Hey HN — I built an 8-game arcade that runs entirely in the browser with no ads, no accounts, and no internet requirement after the initial load. It's part of a larger sovereign AI infrastructure project, but the arcade stands on its own.

**Games included:**
- Sovereign Vector — Asteroids-style with VERITAS gold particle effects
- Kinetic Shield — Pong with dynamic ricochet physics
- Sovereign Breakout — Brick breaker with glassmorphism panels
- Sovereign Orbit — Orbital gravity simulator
- Sovereign Invaders — Space invaders with obsidian backgrounds
- Sovereign Stack — Tetris with gold scoring
- Sovereign Snake — Classic snake, crisp rendering
- Void Sweep — Minesweeper variant

**What's different:**
The design system is consistent across all 8 games — deep obsidian black (#000000), VERITAS gold (#D4AF37), and glassmorphism panel effects. Each game is a single HTML file with embedded CSS and JS. No frameworks, no dependencies, no build step. You can literally save any game as a standalone .html file and it works.

**Why I built this:**
I wanted to prove that you could build a polished, cohesive gaming experience without a game engine, without WebGL, and without any external assets. Everything is rendered with CSS — gradients, shadows, transforms. The entire arcade is ~8,400 lines of code across the games.

**Live:** https://vrtxomega.github.io/sovereign-arcade/
**Source:** https://github.com/VrtxOmega/sovereign-arcade

Happy to answer questions about the design system, the game physics, or the CSS rendering tricks. Everything is MIT licensed — fork away.
