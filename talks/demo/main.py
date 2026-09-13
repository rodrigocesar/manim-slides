"""Short demo talk that exercises the kit. See brief.md for the source description."""

from manim import *

from sci_comm.base import SciSlide
from sci_comm.components import (
    bullets,
    callout,
    colored_math,
    fade_in_each,
    make_text,
    two_column,
)
from sci_comm.theme import COLORS, SIZES


class DemoSlide(SciSlide):
    talk_title = "Scientific Communication with Manim"


class Title(DemoSlide):
    def construct(self) -> None:
        self.add_chrome(index=1, total=5)
        kicker = make_text("A reusable kit", size=SIZES.small, color=COLORS.blue)
        line1 = make_text("Scientific", size=SIZES.display, color=COLORS.fg)
        line2 = make_text("Communication", size=SIZES.display, color=COLORS.yellow)
        subtitle = make_text(
            "Animated slides with Manim and Manim Slides",
            size=SIZES.body,
            color=COLORS.muted,
        )
        stack = VGroup(kicker, line1, line2, subtitle).arrange(DOWN, buff=0.28)
        stack.move_to(ORIGIN)

        self.play(FadeIn(kicker, shift=UP * 0.2))
        self.play(Write(line1), Write(line2))
        self.next_slide()
        self.play(FadeIn(subtitle, shift=DOWN * 0.2))


class Opening(DemoSlide):
    def construct(self) -> None:
        self.add_chrome(section="Why motion", index=2, total=5)
        heading = self.heading("Ideas should move")
        heading.to_edge(UP, buff=0.85)
        points = bullets(
            [
                "One claim on screen at a time",
                "The figure does the explaining",
                "Pauses are first-class, not an afterthought",
            ]
        )
        points.next_to(heading, DOWN, buff=0.55)

        self.play(FadeIn(heading, shift=DOWN * 0.15))
        self.next_slide()
        for row in points:
            self.play(FadeIn(row, shift=RIGHT * 0.2))
            self.next_slide()


class Idea(DemoSlide):
    def construct(self) -> None:
        self.add_chrome(section="One idea", index=3, total=5)
        heading = self.heading("Build, then pause")
        heading.to_edge(UP, buff=0.85)

        circle = Circle(radius=1.4, color=COLORS.blue, stroke_width=6)
        note = callout(
            "next_slide()",
            "The audience waits here. Then the shape becomes a square.",
            accent=COLORS.teal,
        )
        layout = two_column(circle, note, buff=1.2)
        layout.next_to(heading, DOWN, buff=0.7)
        square = Square(side_length=2.6, color=COLORS.yellow, stroke_width=6)
        square.move_to(circle)

        self.play(FadeIn(heading))
        self.play(Create(circle))
        self.next_slide()
        self.play(FadeIn(note, shift=RIGHT * 0.2))
        self.next_slide()
        self.play(Transform(circle, square))


class Equation(DemoSlide):
    def construct(self) -> None:
        self.add_chrome(section="Typesetting", index=4, total=5)
        heading = self.heading("Equations stay readable")
        heading.to_edge(UP, buff=0.85)
        identity = colored_math(
            r"e^{i\pi}",
            r"+",
            r"1",
            r"=",
            r"0",
            colors=(COLORS.yellow, COLORS.muted, COLORS.blue, COLORS.muted, COLORS.teal),
            font_size=84,
        )
        identity.next_to(heading, DOWN, buff=0.9)
        caption = make_text(
            "MathTex, colored by part — not a screenshot of a PDF",
            size=SIZES.small,
            color=COLORS.muted,
        )
        caption.next_to(identity, DOWN, buff=0.7)

        self.play(FadeIn(heading))
        self.play(Write(identity))
        self.next_slide()
        self.play(FadeIn(caption))


class Outro(DemoSlide):
    def construct(self) -> None:
        self.add_chrome(index=5, total=5)
        heading = self.heading("Your next talk")
        heading.to_edge(UP, buff=0.85)
        steps = bullets(
            [
                "Drop a description in chat, or write talks/<slug>/brief.md",
                "The agent adds scenes that reuse sci_comm",
                "Render and present from the repo root",
            ]
        )
        steps.next_to(heading, DOWN, buff=0.55)

        self.play(FadeIn(heading, shift=DOWN * 0.15))
        self.next_slide()
        fade_in_each(self, steps, lag=0.25)
        self.next_slide()
        closer = make_text(
            "Scientific communication, one slide at a time",
            size=SIZES.body,
            color=COLORS.yellow,
        )
        closer.to_edge(DOWN, buff=0.85)
        self.play(FadeIn(closer))
