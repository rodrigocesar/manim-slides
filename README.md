# manim-slides

A folder of Manim Slides talks. Shared look-and-feel lives in [`shared/`](shared/). Each talk lives under [`presentations/`](presentations/).

| Talk | Folder | Idea |
|---|---|---|
| Are we making better decisions? | [`presentations/tpng-better-decisions`](presentations/tpng-better-decisions) | Powell's sequential-decision frame for DORA, Sectorization and last-mile planning |
| Conway's Law | [`presentations/conways-law`](presentations/conways-law) | Systems copy communication structure — including private developer–agent conversations |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

System packages expected: FFmpeg, Cairo, Pango, TeX Live.

## Commands

Every script takes the **talk folder name** first.

```bash
./scripts/render.sh tpng-better-decisions          # draft, all scenes
./scripts/render.sh tpng-better-decisions -qh      # 1080p
./scripts/render.sh conways-law -ql Title TheSentence

./scripts/export_html.sh tpng-better-decisions
./scripts/export_html.sh conways-law

./scripts/present.sh tpng-better-decisions
./scripts/present.sh conways-law
```

`present.sh` serves that talk's `dist/` at **http://127.0.0.1:8000/**. Keep the talk's `SPEAKER_NOTES.md` open; press `S` in the browser for RevealJS speaker view. Override the port with `PORT=8080 ./scripts/present.sh conways-law`.

Do not open `index.html` as `file://` if you want the speaker-view popup.

## Add a talk

1. Create `presentations/<name>/`.
2. Add `deck.py` (import theme from `shared/` the same way the existing talks do).
3. Add `talk.json` with `title` and `scenes`.
4. Add `SPEAKER_NOTES.md`.
5. Render, export, present with the scripts above.

## Citation

Powell, W. B. (2022). *Reinforcement Learning and Stochastic Optimization*. Wiley. https://warrenpowell.org/

Conway, M. E. (1968). How do committees invent? *Datamation*, 14(4), 28–31.
