from __future__ import annotations

from manim import DOWN, RIGHT, VGroup

from theme import DECISION, INK, MUTE, STATE, txt


def graph_formula(left: str = "COMMUNICATION GRAPH", right: str = "SOFTWARE GRAPH") -> VGroup:
    a = txt(left, size=22, weight="BOLD", color=STATE)
    arrow = txt("→", size=34, color=DECISION)
    b = txt(right, size=22, weight="BOLD", color=DECISION)
    return VGroup(a, arrow, b).arrange(RIGHT, buff=0.22)


def motif_stack() -> VGroup:
    lines = [
        txt("HUMAN GRAPH", size=26, weight="BOLD", color=STATE),
        txt("+", size=22, color=MUTE),
        txt("AGENT GRAPH", size=26, weight="BOLD", color="#C4B5FD"),
        txt("+", size=22, color=MUTE),
        txt("SHARED CONTEXT GRAPH", size=26, weight="BOLD", color=DECISION),
        txt("↓", size=30, color=DECISION),
        txt("SOFTWARE GRAPH", size=26, weight="BOLD", color=INK),
    ]
    return VGroup(*lines).arrange(DOWN, buff=0.16)


def check_mark() -> VGroup:
    return txt("✓", size=36, weight="BOLD", color="#3DDC97")
