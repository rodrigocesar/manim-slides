---
name: create-manim-talk
description: Create a new scientific Manim Slides talk from a description. Use when the user describes a talk, lecture, paper, seminar, or wants animated slides added under talks/.
---

# Create a Manim talk

Turn a prose description into a `talks/<slug>/` folder that uses this kit.

## Before writing scenes

1. Read [AGENTS.md](../../../AGENTS.md), [src/sci_comm/theme.py](../../../src/sci_comm/theme.py), [src/sci_comm/base.py](../../../src/sci_comm/base.py), and [src/sci_comm/components.py](../../../src/sci_comm/components.py).
2. Skim [talks/demo/main.py](../../../talks/demo/main.py) for the expected shape.
3. Pick a short kebab-case slug. Do not overwrite `talks/demo`.

## Files to add

### `talks/<slug>/brief.md`

Capture the user's description:

- title and audience
- scene list (one heading per `SciSlide` subclass)
- voice / constraints
- the exact render and present commands

### `talks/<slug>/main.py`

```python
from manim import *

from sci_comm.base import SciSlide
from sci_comm.components import bullets, callout, colored_math, fade_in_each, make_text
from sci_comm.theme import COLORS, SIZES


class TalkSlide(SciSlide):
    talk_title = "Human title here"


class Title(TalkSlide):
    def construct(self) -> None:
        self.add_chrome(index=1, total=N)
        ...
        self.next_slide()
```

Rules:

- Subclass `SciSlide`. Call `add_chrome(...)` first in `construct`.
- One class per section. Name classes so they are valid Manim scene names (`Title`, `BayesUpdate`, not `slide-1`).
- Colors and type sizes come from `COLORS` / `SIZES` only.
- `make_text` / `SciSlide.heading` for titles and labels (`font=FONT` is required; raw `Text` drops spaces). `MathTex` / `colored_math` for equations.
- `self.next_slide()` at every presenter pause. `self.next_slide(loop=True)` only around a repeating animation.
- Prefer `Create`, `Write`, `FadeIn`, `Transform`, and `fade_in_each`. Keep runtimes short (1–2s).
- No paragraph walls. If a point needs more than one line, split across pauses or a `callout`.

## After writing

Document, in the brief:

```bash
uv run manim-slides render talks/<slug>/main.py Title ... Last
uv run manim-slides present Title ... Last
```

If the environment has Manim system deps, render once at `-ql` to catch `MathTex` errors. Do not commit `media/` or `slides/`.
