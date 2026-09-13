# Demo: Scientific Communication with Manim

This talk is the kit smoke test. It is not a research presentation.

## Audience

Someone cloning this repo for the first time, checking that theme, components, render, and present all work.

## Scenes

1. **Title** — Name the kit. Subtitle: animated slides with Manim.
2. **Opening** — Why motion helps scientific talks: one idea at a time, the figure does the explaining, pauses are first-class.
3. **Idea** — Show a single animated figure (circle → square) so the pause (`next_slide`) is obvious.
4. **Equation** — Typeset Euler's identity and color the pieces. Proves LaTeX is wired up.
5. **Outro** — How to add the next talk: write a brief, then ask the agent to generate scenes.

## Voice

Dark 3Blue1Brown look. Short labels. No walls of text.

## Commands

From the repository root:

```bash
uv run manim-slides render talks/demo/main.py Title Opening Idea Equation Outro
uv run manim-slides present Title Opening Idea Equation Outro
```

Low-quality preview:

```bash
uv run manim-slides render -ql talks/demo/main.py Title Opening Idea Equation Outro
```
