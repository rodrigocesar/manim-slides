"""Reusable slide building blocks. Prefer these over one-off colors and layout."""

from __future__ import annotations

from collections.abc import Iterable, Sequence

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    FadeIn,
    LaggedStart,
    Mobject,
    MathTex,
    Scene,
    SurroundingRectangle,
    Text,
    VGroup,
)

from sci_comm.theme import COLORS, SIZES, SPACING


def make_text(
    text: str,
    size: int | None = None,
    color: str | None = None,
    **kwargs,
) -> Text:
    return Text(
        text,
        font_size=size or SIZES.body,
        color=color or COLORS.fg,
        **kwargs,
    )


def bullets(
    items: Sequence[str],
    font_size: int | None = None,
    color: str | None = None,
    mark_color: str | None = None,
) -> VGroup:
    """Left-aligned bullet rows. Reveal with ``fade_in_each``."""
    size = font_size or SIZES.body
    rows = VGroup()
    for item in items:
        mark = Text("•", font_size=size, color=mark_color or COLORS.yellow)
        body = Text(item, font_size=size, color=color or COLORS.fg)
        row = VGroup(mark, body).arrange(RIGHT, buff=0.22, aligned_edge=UP)
        rows.add(row)
    rows.arrange(DOWN, buff=SPACING.bullet, aligned_edge=LEFT)
    return rows


def callout(
    title: str,
    body: str,
    accent: str | None = None,
) -> VGroup:
    """Titled note in a rounded stroke, for a warning, takeaway, or definition."""
    accent = accent or COLORS.gold
    title_m = Text(title, font_size=SIZES.small + 4, color=accent)
    body_m = Text(body, font_size=SIZES.small + 2, color=COLORS.fg)
    content = VGroup(title_m, body_m).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    box = SurroundingRectangle(
        content,
        color=accent,
        buff=0.28,
        corner_radius=0.12,
        stroke_width=2.0,
    )
    box.set_fill(COLORS.bg, opacity=0.0)
    return VGroup(box, content)


def two_column(left: Mobject, right: Mobject, buff: float = 1.0) -> VGroup:
    return VGroup(left, right).arrange(RIGHT, buff=buff, aligned_edge=UP)


def colored_math(
    *parts: str,
    colors: Sequence[str | None] | None = None,
    font_size: int = 56,
) -> MathTex:
    """``MathTex`` split into parts so each piece can take a kit color."""
    equation = MathTex(*parts, font_size=font_size)
    equation.set_color(COLORS.fg)
    if colors:
        for index, color in enumerate(colors):
            if color is not None and index < len(equation):
                equation[index].set_color(color)
    return equation


def fade_in_each(
    scene: Scene,
    group: VGroup | Iterable[Mobject],
    lag: float = 0.12,
    shift=DOWN * 0.15,
) -> None:
    """Play ``FadeIn`` for each submobject, pausing if ``lag`` is used via wait."""
    mobjects = list(group)
    scene.play(
        LaggedStart(*[FadeIn(mob, shift=shift) for mob in mobjects], lag_ratio=lag)
    )


# Re-export directions so talk scripts can stay on sci_comm helpers when needed.
__all__ = [
    "LEFT",
    "RIGHT",
    "UP",
    "DOWN",
    "bullets",
    "callout",
    "colored_math",
    "fade_in_each",
    "make_text",
    "two_column",
]
