from __future__ import annotations

import numpy as np
from manim import Dot, Line, MoveAlongPath, VGroup, linear

from theme import AGENT, DECISION, MUTE, STATE


def _ends(src, dst, buff: float = 0.38):
    start = np.array(src.get_center())
    end = np.array(dst.get_center())
    vec = end - start
    norm = np.linalg.norm(vec)
    if norm < 1e-6:
        return start, end
    unit = vec / norm
    return start + unit * buff, end - unit * buff


class CommunicationEdge(VGroup):
    def __init__(self, src, dst, kind: str = "strong", buff: float = 0.38, **kwargs):
        super().__init__(**kwargs)
        start, end = _ends(src, dst, buff=buff)
        if kind == "weak":
            color, width, dash = MUTE, 2.0, True
        elif kind == "agent":
            color, width, dash = AGENT, 2.6, False
        elif kind == "contract":
            color, width, dash = DECISION, 3.2, False
        else:
            color, width, dash = STATE, 3.0, False
        self.guide = Line(start, end, color=color, stroke_width=width)
        if dash:
            self.guide.set_stroke(color, width=width, opacity=1)
            dashed = self.guide.copy()
            # Draw dashes onto a copy; keep the solid guide for pulses.
            n = max(8, int(np.linalg.norm(end - start) / 0.18))
            self.visual = dashed
            self._dash_visual(n)
        else:
            self.visual = self.guide
        self.path = self.guide
        self.kind = kind
        self.add(self.visual)
        self.set_z_index(0)

    def _dash_visual(self, n: int):
        # Replace visual with a dashed look without using DashedLine's empty parent.
        start = self.guide.get_start()
        end = self.guide.get_end()
        pieces = VGroup()
        for i in range(n):
            if i % 2 == 1:
                continue
            a = start + (end - start) * (i / n)
            b = start + (end - start) * min(1.0, (i + 1) / n)
            pieces.add(Line(a, b, color=MUTE, stroke_width=2))
        self.visual = pieces


def play_pulses(scene, edges, color=DECISION, run_time: float = 0.5):
    paths = [e.guide if hasattr(e, "guide") else e for e in edges]
    dots = []
    anims = []
    for path in paths:
        dot = Dot(radius=0.07, color=color)
        dot.move_to(path.get_start())
        dots.append(dot)
        anims.append(MoveAlongPath(dot, path, rate_func=linear))
    scene.add(*dots)
    scene.play(*anims, run_time=run_time)
    scene.remove(*dots)


def flow_dots(scene, sources, target, color=DECISION, run_time: float = 0.55):
    guides = []
    for src in sources:
        start, end = _ends(src, target, buff=0.4)
        guides.append(Line(start, end))
    dots = []
    anims = []
    for path in guides:
        dot = Dot(radius=0.08, color=color)
        dot.move_to(path.get_start())
        dots.append(dot)
        anims.append(MoveAlongPath(dot, path, rate_func=linear))
    scene.add(*dots)
    scene.play(*anims, run_time=run_time)
    scene.remove(*dots)
