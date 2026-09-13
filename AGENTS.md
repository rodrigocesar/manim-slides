# Agent notes

This repo is a **multi-talk kit**. Do not invent one-off colors, fonts, or slide chrome. Import from `sci_comm`.

## When the user describes a talk

Follow `.cursor/skills/create-manim-talk/SKILL.md`. In short:

1. Choose a kebab-case slug (`bayes-rule`, `attention-heads`).
2. Write `talks/<slug>/brief.md` from their description (audience, scenes, voice, render commands).
3. Write `talks/<slug>/main.py` with one `SciSlide` subclass per section.
4. Reuse `COLORS`, `bullets`, `callout`, `colored_math`, `two_column`, `fade_in_each`.
5. Pause with `self.next_slide()`. Use `loop=True` only for a repeating figure.
6. Titles and labels: `make_text` or `SciSlide.heading` (they set `FONT`). Do not call `Text(...)` without `font=FONT` — the default font drops spaces.
7. Equations: `MathTex` / `colored_math`.
8. Put the exact `manim-slides render` and `present` commands in the brief.

## Scene split

Prefer several small scene classes over one giant `construct`. Re-rendering `Idea` should not rebuild `Title`. A typical talk:

- `Title`
- one class per idea or section
- `Equation` (or similar) when math is central
- `Outro` or `Summary`

Share `talk_title` (and author, if needed) on a thin talk-specific base class that subclasses `SciSlide`.

## Commands

Always run from the repository root, with the package installed (`uv sync`):

```bash
uv run manim-slides render talks/<slug>/main.py SceneA SceneB
uv run manim-slides present SceneA SceneB
```

Use `-ql` for a draft. Do not commit `media/` or `slides/`.

## What not to do

- Do not add a new theme unless the user asks. Default is the dark 3Blue1Brown palette in `src/sci_comm/theme.py`.
- Do not paste walls of paragraph text onto a slide.
- Do not call `self.wait()` as a stand-in for a presenter pause; that is `self.next_slide()`.
- Do not generate a real research talk unless the user gave a brief. The `talks/demo` deck is only a smoke test.
