from __future__ import annotations

from manim import *

from components import (
    CommunicationEdge,
    PersonNode,
    SoftwareModule,
    TeamBoundary,
    flow_dots,
    graph_formula,
    play_pulses,
)
from theme import DECISION, INK, LINE, MUTE, STATE, UNCERTAINTY, appear, txt

from .base import ConwaySlide


class WhyArchitecture(ConwaySlide):
    def construct(self):
        self.setup_slide("Why does architecture end up like this?")

        cap = txt("The architecture we draw", size=22, color=MUTE)
        cap.move_to(UP * 2.2)

        names = ["Input", "Planning", "Optimization", "Execution"]
        boxes = [SoftwareModule(name, width=3.0, height=0.68) for name in names]
        stack = VGroup(*boxes).arrange(DOWN, buff=0.32)
        stack.move_to(DOWN * 0.2)
        arrows = VGroup()
        for a, b in zip(boxes, boxes[1:]):
            arrows.add(
                Arrow(
                    a.get_bottom(),
                    b.get_top(),
                    buff=0.05,
                    stroke_width=3,
                    color=MUTE,
                    max_tip_length_to_length_ratio=0.18,
                )
            )
        clean = VGroup(stack, arrows)

        self.play(FadeIn(cap), LaggedStart(*[appear(b) for b in boxes], lag_ratio=0.1), run_time=0.75)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.08), run_time=0.45)
        self.next_slide()

        util = SoftwareModule("shared util", width=2.15, height=0.52, accent=UNCERTAINTY)
        db = SoftwareModule("shared DB", width=2.15, height=0.52, accent=UNCERTAINTY)
        dup = SoftwareModule("duplicated logic", width=2.35, height=0.52, accent=UNCERTAINTY)
        compat = SoftwareModule("compat layer", width=2.15, height=0.52, accent=LINE)
        extra_api = SoftwareModule("another API", width=2.15, height=0.52, accent=DECISION)
        util.move_to(LEFT * 4.15 + UP * 0.85)
        db.move_to(RIGHT * 4.15 + DOWN * 0.15)
        dup.move_to(RIGHT * 4.15 + UP * 1.35)
        compat.move_to(LEFT * 4.15 + DOWN * 1.35)
        extra_api.move_to(RIGHT * 4.15 + DOWN * 1.55)

        extras = VGroup(util, db, dup, compat, extra_api)
        mess = VGroup(
            Line(boxes[0].get_left(), util.get_right(), color=UNCERTAINTY, stroke_width=2),
            Line(boxes[1].get_right(), dup.get_left(), color=UNCERTAINTY, stroke_width=2),
            Line(boxes[2].get_right(), db.get_left(), color=UNCERTAINTY, stroke_width=2),
            Line(boxes[3].get_left(), compat.get_right(), color=LINE, stroke_width=2),
            Line(util.get_bottom(), compat.get_top(), color=MUTE, stroke_width=1.5),
            Line(dup.get_bottom(), db.get_top(), color=MUTE, stroke_width=1.5),
            Line(boxes[0].get_right(), extra_api.get_top() + UP * 0.05, color=DECISION, stroke_width=1.8),
            Line(boxes[2].get_bottom() + RIGHT * 0.8, extra_api.get_left(), color=DECISION, stroke_width=1.8),
        )

        got = txt("The architecture we get", size=22, color=UNCERTAINTY)
        got.move_to(cap.get_center())
        self.play(
            ReplacementTransform(cap, got),
            LaggedStart(*[FadeIn(m, scale=0.9) for m in extras], lag_ratio=0.08),
            LaggedStart(*[Create(line) for line in mess], lag_ratio=0.06),
            run_time=1.1,
        )
        self.next_slide()

        why = txt("Why?", size=76, weight="BOLD", color=DECISION)
        why.move_to(LEFT * 3.1 + DOWN * 0.15)
        tangle = VGroup(clean, extras, mess)
        self.play(tangle.animate.scale(0.78).to_edge(RIGHT, buff=0.35), FadeIn(why, scale=0.85), run_time=0.8)
        self.next_slide()


class InvisibleArchitecture(ConwaySlide):
    def construct(self):
        self.setup_slide("The invisible architecture", cite=True)

        people = [
            PersonNode("A").move_to(LEFT * 4.4 + UP * 1.05),
            PersonNode("B").move_to(LEFT * 2.15 + UP * 1.05),
            PersonNode("C").move_to(LEFT * 4.4 + DOWN * 0.85),
            PersonNode("D").move_to(LEFT * 2.15 + DOWN * 0.85),
        ]
        pairs = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]
        edges = [CommunicationEdge(people[i], people[j]) for i, j in pairs]
        software = SoftwareModule("shared system", width=3.0, height=1.05, accent=DECISION, title_color=DECISION)
        software.move_to(RIGHT * 3.35 + UP * 0.1)
        cap = txt("Cheap communication → shared system", size=20, color=MUTE)
        cap.move_to(DOWN * 3.15)

        self.play(LaggedStart(*[FadeIn(p, scale=0.9) for p in people], lag_ratio=0.08), run_time=0.55)
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.05), run_time=0.5)
        play_pulses(self, edges, color=STATE, run_time=0.55)
        self.play(appear(software), FadeIn(cap), run_time=0.45)
        flow_dots(self, people, software, color=DECISION, run_time=0.6)
        self.next_slide()

        extra = [
            PersonNode("E").move_to(RIGHT * 0.15 + UP * 1.05),
            PersonNode("F").move_to(RIGHT * 0.15 + DOWN * 0.85),
        ]
        self.play(LaggedStart(*[FadeIn(p, scale=0.9) for p in extra], lag_ratio=0.1), run_time=0.4)

        moves = [
            people[0].animate.move_to(LEFT * 5.15 + UP * 1.15),
            people[1].animate.move_to(LEFT * 5.15 + DOWN * 0.75),
            people[2].animate.move_to(LEFT * 1.85 + UP * 1.15),
            people[3].animate.move_to(LEFT * 1.85 + DOWN * 0.75),
            extra[0].animate.move_to(RIGHT * 1.45 + UP * 1.15),
            extra[1].animate.move_to(RIGHT * 1.45 + DOWN * 0.75),
        ]
        self.play(*moves, FadeOut(VGroup(*edges)), FadeOut(software), FadeOut(cap), run_time=0.75)

        teams = VGroup(
            TeamBoundary("Team A", [people[0], people[1]], buff=0.38),
            TeamBoundary("Team B", [people[2], people[3]], buff=0.38),
            TeamBoundary("Team C", extra, buff=0.38),
        )
        weak = [
            CommunicationEdge(people[0], people[1]),
            CommunicationEdge(people[2], people[3]),
            CommunicationEdge(extra[0], extra[1]),
            CommunicationEdge(people[0], people[2], kind="weak"),
            CommunicationEdge(people[3], extra[0], kind="weak"),
            CommunicationEdge(people[1], extra[1], kind="weak"),
        ]
        mods = VGroup(
            SoftwareModule("module A", width=2.15, height=0.62, accent=STATE),
            SoftwareModule("module B", width=2.15, height=0.62, accent=STATE),
            SoftwareModule("module C", width=2.15, height=0.62, accent=STATE),
        ).arrange(RIGHT, buff=0.35)
        mods.move_to(DOWN * 2.55)
        self.play(
            FadeIn(teams),
            LaggedStart(*[Create(e) for e in weak], lag_ratio=0.04),
            FadeIn(mods, shift=DOWN * 0.1),
            run_time=0.8,
        )
        play_pulses(self, weak[:3], color=STATE, run_time=0.45)
        play_pulses(self, weak[3:], color=MUTE, run_time=0.7)
        self.next_slide()

        year = txt("1968  —  Melvin Conway", size=22, color=DECISION, weight="BOLD")
        quote = txt(
            "Organizations design systems that reflect\ntheir communication structures.",
            size=20,
            color=INK,
            line_spacing=1.15,
        )
        year.move_to(RIGHT * 3.85 + UP * 1.55)
        quote.next_to(year, DOWN, buff=0.28)
        self.play(FadeIn(year), FadeIn(quote), run_time=0.55)
        self.next_slide()

        formula = graph_formula()
        formula.move_to(DOWN * 3.2)
        self.play(FadeOut(mods), FadeIn(formula), run_time=0.55)
        self.next_slide()
