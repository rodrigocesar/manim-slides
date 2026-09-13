# Conway's Law — and the conversations nobody else can see

A ~10–12 minute Manim Slides talk for TPNG. Classical Conway, then the 2026 extension: software mirrors **who shares context with whom**, including private developer–agent conversations.

```text
COMMUNICATION GRAPH  →  SOFTWARE GRAPH
HUMAN + AGENT + SHARED CONTEXT  →  SOFTWARE
```

## Commands

From the repo root, with `.venv` available (the scripts activate it):

```bash
./scripts/render.sh conways-law            # draft 480p, all scenes
./scripts/render.sh conways-law -qh        # 1080p60
./scripts/render.sh conways-law -ql WhyArchitecture InvisibleArchitecture

./scripts/export_html.sh conways-law
PORT=8001 ./scripts/present.sh conways-law
```

`present.sh` serves `dist/` at **http://127.0.0.1:8001/** (or 8000 if that port is free). Keep [`SPEAKER_NOTES.md`](SPEAKER_NOTES.md) open. Press `S` in the browser for Reveal speaker view. Do not open `index.html` as `file://` if you need the speaker popup.

Installed tools this README was checked against: Manim Community `0.21`, `manim-slides` `5.6`. Quality flags go **after** `--` (the render script already does this).

## Layout

```text
presentations/conways-law/
├── deck.py                 # scene registry for manim-slides
├── talk.json
├── components/             # people, agents, modules, edges
├── scenes/                 # one act per module
├── SPEAKER_NOTES.md
├── NARRATIVE.md            # arc, timings, claims to verify
└── dist/                   # exported HTML
```

## Seven-minute cut

Keep slides 1–2, 4, 6–7, 11. Compress 3, 5, 8–10 using the **(shorten)** beats in the speaker notes. Do not drop the colliding “Stopping Point” or the final question.
