"""Shared visual system for Manim Slides talks in this repo."""

from __future__ import annotations

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    FadeIn,
    MarkupText,
    RoundedRectangle,
    Tex,
    VGroup,
)

BG = "#0E1520"
INK = "#F5F7FA"
MUTE = "#9AA4B2"
DECISION = "#FFCC00"
STATE = "#4C8DFF"
UNCERTAINTY = "#FF6B4A"
OK = "#3DDC97"
CARD = "#172033"
CARD_STROKE = "#2A3A52"
LINE = "#3A4A63"

FONT = "DejaVu Sans"

TITLE_SIZE = 40
BODY_SIZE = 26
SMALL_SIZE = 20
TINY_SIZE = 16

SAFE_TOP = 3.55
SAFE_BOTTOM = -3.65
CONTENT_TOP = 2.55


def txt(
    text: str,
    size: int = BODY_SIZE,
    color: str = INK,
    weight: str = "NORMAL",
    **kwargs,
) -> MarkupText:
    escaped = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    weight_name = "bold" if weight == "BOLD" else "normal"
    return MarkupText(
        f'<span weight="{weight_name}">{escaped}</span>',
        font=FONT,
        font_size=size,
        color=color,
        **kwargs,
    )


def slide_title(text: str) -> MarkupText:
    return txt(text, size=TITLE_SIZE, weight="BOLD").to_edge(UP, buff=0.38)


def footer(text: str) -> MarkupText:
    return txt(text, size=14, color=MUTE).to_edge(DOWN, buff=0.22)


def caption(text: str, color: str = MUTE, size: int = SMALL_SIZE) -> MarkupText:
    return txt(text, size=size, color=color)


def card(
    width: float,
    height: float,
    accent: str = CARD_STROKE,
    fill: str = CARD,
    stroke_width: float = 2.0,
) -> RoundedRectangle:
    return RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.16,
        fill_color=fill,
        fill_opacity=1.0,
        stroke_color=accent,
        stroke_width=stroke_width,
    )


def labeled_card(
    title: str,
    lines: list[str],
    width: float = 5.2,
    height: float = 3.6,
    accent: str = CARD_STROKE,
    title_color: str = INK,
) -> VGroup:
    box = card(width, height, accent=accent)
    title_m = txt(title, size=28, weight="BOLD", color=title_color)
    body = VGroup(*[txt(line, size=SMALL_SIZE, color=MUTE) for line in lines])
    body.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    title_m.next_to(box.get_top(), DOWN, buff=0.28)
    title_m.align_to(box, LEFT).shift(RIGHT * 0.32)
    body.next_to(title_m, DOWN, buff=0.32).align_to(title_m, LEFT)
    return VGroup(box, title_m, body)


def pill(label: str, accent: str = CARD_STROKE, width: float = 2.35, height: float = 0.82) -> VGroup:
    box = card(width, height, accent=accent)
    t = txt(label, size=18, color=INK)
    t.move_to(box)
    return VGroup(box, t)


def node_box(
    title: str,
    subtitle: str = "",
    width: float = 2.15,
    height: float = 1.15,
    accent: str = CARD_STROKE,
    title_color: str = INK,
) -> VGroup:
    box = card(width, height, accent=accent)
    title_m = txt(title, size=18, weight="BOLD", color=title_color)
    parts = [title_m]
    if subtitle:
        sub = txt(subtitle, size=13, color=MUTE)
        parts.append(sub)
    labels = VGroup(*parts).arrange(DOWN, buff=0.08)
    labels.move_to(box)
    return VGroup(box, labels)


def eq(tex: str, size: int = 42) -> Tex:
    return Tex(tex, color=INK, font_size=size)


def appear(mobject, run_time: float = 0.55):
    return FadeIn(mobject, shift=UP * 0.12, run_time=run_time)


def dim_to(mobject, opacity: float = 0.35):
    return mobject.animate.set_opacity(opacity)
