from __future__ import annotations

from manim import ManimColor
from manim_slides import Slide

from theme import BG, footer, slide_title

CITE = "Conway, M. E. (1968). How do committees invent? Datamation."


class ConwaySlide(Slide):
    skip_reversing = True

    def setup_slide(self, title: str | None = None, cite: bool = False):
        self.camera.background_color = ManimColor(BG)
        parts = []
        if title:
            parts.append(slide_title(title))
        if cite:
            parts.append(footer(CITE))
        if parts:
            self.add(*parts)
        return parts
