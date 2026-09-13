# manim-slides

Scientific communication kit: describe a talk, generate animated [Manim](https://www.manim.community/) slides, and present them with [Manim Slides](https://manim-slides.eertmans.be/).

This repository cannot be written onto your WSL disk from the cloud. Clone it into `~/projects` on Ubuntu:

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/rodrigocesar/manim-slides.git
cd manim-slides
./scripts/setup-wsl.sh
```

The setup script installs Cairo, Pango, FFmpeg, a science-oriented TeX Live set (not `texlive-full`), then syncs the `uv` environment.

## How a talk is added

1. Write a description in chat, or add `talks/<slug>/brief.md`.
2. An agent (see [AGENTS.md](AGENTS.md) and `.cursor/skills/create-manim-talk/`) turns that brief into `talks/<slug>/main.py` using the `sci_comm` theme and components.
3. Render and present from the repository root.

Reusable code lives in `src/sci_comm/`. Each talk is a folder under `talks/`. Long talks are split into several scene classes so one section can re-render without rebuilding the whole deck.

## Demo

```bash
uv run manim-slides render talks/demo/main.py Title Opening Idea Equation Outro
uv run manim-slides present Title Opening Idea Equation Outro
```

Low-quality preview:

```bash
uv run manim-slides render -ql talks/demo/main.py Title Opening Idea Equation Outro
```

`present` needs the Qt bindings from the `dev` group (`uv sync` installs them). That GUI is for your WSL desktop, not a headless cloud machine.

## Layout

```
src/sci_comm/          theme, SciSlide, bullets / callout / equations
talks/demo/            short kit smoke-test
scripts/setup-wsl.sh   Ubuntu / WSL bootstrap
AGENTS.md              description → scenes contract
```
