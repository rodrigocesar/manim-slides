from __future__ import annotations

from manim import DOWN, LEFT, PI, RIGHT, UP, Circle, RegularPolygon, RoundedRectangle, Square, VGroup

from theme import (
    AGENT,
    AGENT_FILL,
    CARD,
    CARD_STROKE,
    DECISION,
    INK,
    LINE,
    MUTE,
    STATE,
    UNCERTAINTY,
    card,
    txt,
)


class PersonNode(VGroup):
    def __init__(self, label: str, radius: float = 0.34, accent: str = STATE, **kwargs):
        super().__init__(**kwargs)
        self.ring = Circle(
            radius=radius,
            stroke_color=accent,
            stroke_width=2.5,
            fill_color=CARD,
            fill_opacity=1.0,
        )
        self.caption = txt(label, size=15, weight="BOLD", color=INK)
        self.caption.move_to(self.ring)
        self.add(self.ring, self.caption)
        self.set_z_index(2)


class AgentNode(VGroup):
    def __init__(self, label: str = "AI", size: float = 0.52, **kwargs):
        super().__init__(**kwargs)
        body = Square(
            side_length=size,
            stroke_color=AGENT,
            stroke_width=2.5,
            fill_color=AGENT_FILL,
            fill_opacity=1.0,
        ).rotate(PI / 4)
        lab = txt(label, size=12, weight="BOLD", color=AGENT)
        lab.move_to(body)
        self.body = body
        self.add(body, lab)
        self.set_z_index(2)


class SoftwareModule(VGroup):
    def __init__(
        self,
        title: str,
        width: float | None = None,
        height: float = 0.72,
        accent: str = LINE,
        title_color: str = INK,
        size: int = 16,
        **kwargs,
    ):
        super().__init__(**kwargs)
        if width is None:
            width = max(1.7, 0.125 * len(title) + 1.05)
        self.box = card(width, height, accent=accent)
        self.label = txt(title, size=size, weight="BOLD", color=title_color)
        self.label.move_to(self.box)
        self.add(self.box, self.label)
        self.set_z_index(1)


class TeamBoundary(VGroup):
    def __init__(
        self,
        name: str,
        members: VGroup | list,
        buff: float = 0.42,
        extra_top: float = 0.38,
        accent: str = STATE,
        **kwargs,
    ):
        super().__init__(**kwargs)
        cluster = VGroup(*members)
        self.box = RoundedRectangle(
            width=cluster.width + 2 * buff,
            height=cluster.height + 2 * buff + extra_top,
            corner_radius=0.2,
            stroke_color=accent,
            stroke_width=2,
            fill_color=accent,
            fill_opacity=0.08,
        )
        self.box.move_to(cluster.get_center() + UP * (extra_top / 2))
        self.caption = txt(name, size=16, weight="BOLD", color=accent)
        self.caption.next_to(self.box.get_top(), DOWN, buff=0.1)
        self.add(self.box, self.caption)
        self.set_z_index(0)


class APIBoundary(VGroup):
    def __init__(self, label: str = "API", height: float = 1.45, **kwargs):
        super().__init__(**kwargs)
        self.box = RoundedRectangle(
            width=0.42,
            height=height,
            corner_radius=0.08,
            stroke_color=DECISION,
            stroke_width=2,
            fill_color=DECISION,
            fill_opacity=0.18,
        )
        self.caption = txt(label, size=12, weight="BOLD", color=DECISION)
        self.caption.rotate(PI / 2)
        self.caption.move_to(self.box)
        self.add(self.box, self.caption)
        self.set_z_index(1)


class ContextDoc(VGroup):
    def __init__(self, name: str, accent: str = CARD_STROKE, width: float = 2.15, **kwargs):
        super().__init__(**kwargs)
        self.box = RoundedRectangle(
            width=width,
            height=0.48,
            corner_radius=0.08,
            stroke_color=accent,
            stroke_width=1.6,
            fill_color=CARD,
            fill_opacity=1.0,
        )
        tab = RoundedRectangle(
            width=0.28,
            height=0.14,
            corner_radius=0.04,
            stroke_width=0,
            fill_color=accent,
            fill_opacity=0.85,
        )
        tab.next_to(self.box, UP, buff=0).align_to(self.box, LEFT).shift(RIGHT * 0.12 + DOWN * 0.02)
        self.caption = txt(name, size=13, color=INK)
        self.caption.move_to(self.box)
        self.add(tab, self.box, self.caption)


class WorldNode(VGroup):
    def __init__(self, label: str = "REAL WORLD", **kwargs):
        super().__init__(**kwargs)
        body = RegularPolygon(
            n=6,
            radius=0.72,
            stroke_color=UNCERTAINTY,
            stroke_width=2.5,
            fill_color=CARD,
            fill_opacity=1.0,
        )
        lab = txt(label, size=12, weight="BOLD", color=UNCERTAINTY)
        lab.move_to(body)
        self.add(body, lab)


def people_square(labels: tuple[str, ...] = ("A", "B", "C", "D"), origin=None, spread: float = 1.15):
    if origin is None:
        origin = LEFT * 3.2 + DOWN * 0.15
    offsets = [UP + LEFT, UP + RIGHT, DOWN + LEFT, DOWN + RIGHT]
    people = []
    for lab, off in zip(labels, offsets):
        node = PersonNode(lab)
        node.move_to(origin + off * spread)
        people.append(node)
    return people
