"""Base Manim Slides scene with kit chrome and the dark theme applied."""

from __future__ import annotations

from manim import LEFT, RIGHT, UP, Line, Text, VGroup
from manim_slides import Slide

from sci_comm.theme import COLORS, DEFAULT_AUTHOR, SIZES, SPACING


class SciSlide(Slide):
    """Manim Slides scene with the dark theme, footer, and optional section label.

    Set ``talk_title`` on the class (or override per scene). Call ``add_chrome``
    at the start of ``construct`` so the footer stays on screen across pauses.
    """

    talk_title: str = ""
    author: str = DEFAULT_AUTHOR
    show_chrome: bool = True

    def setup(self) -> None:
        super().setup()
        self.camera.background_color = COLORS.bg

    def add_chrome(
        self,
        section: str | None = None,
        index: int | None = None,
        total: int | None = None,
    ) -> VGroup:
        """Pin a top accent bar, optional section label, and footer to the frame."""
        chrome = VGroup()
        if not self.show_chrome:
            return chrome

        bar = Line(
            LEFT * 7.1,
            RIGHT * 7.1,
            color=COLORS.blue,
            stroke_width=2.0,
        ).to_edge(UP, buff=SPACING.chrome_top)
        chrome.add(bar)

        if section:
            label = Text(section, font_size=SIZES.small, color=COLORS.blue)
            label.to_edge(UP, buff=SPACING.chrome_top + 0.12).to_edge(
                LEFT, buff=SPACING.margin
            )
            chrome.add(label)

        bits: list[str] = []
        if self.author:
            bits.append(self.author)
        if self.talk_title:
            bits.append(self.talk_title)
        if index is not None and total is not None:
            bits.append(f"{index} / {total}")
        if bits:
            footer = Text("  ·  ".join(bits), font_size=SIZES.footer, color=COLORS.muted)
            footer.to_edge(DOWN, buff=SPACING.chrome_bottom)
            chrome.add(footer)

        self.add(chrome)
        return chrome

    def heading(self, text: str, size: int | None = None) -> Text:
        heading = Text(text, font_size=size or SIZES.title, color=COLORS.fg)
        return heading
