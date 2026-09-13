"""Conway's Law — a TPNG / DORA discussion."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "shared"))

from manim import *
from manim_slides import Slide

from theme import (
    BG,
    CARD_STROKE,
    DECISION,
    INK,
    LINE,
    MUTE,
    OK,
    STATE,
    UNCERTAINTY,
    appear,
    caption,
    card,
    footer,
    node_box,
    pill,
    slide_title,
    txt,
)

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


class Title(ConwaySlide):
    def construct(self):
        self.setup_slide(cite=True)
        title = txt("Conway's Law", size=52, weight="BOLD")
        subtitle = txt(
            "Our systems will look like how we talk to each other",
            size=22,
            color=MUTE,
        )
        rule = Line(LEFT * 2.2, RIGHT * 2.2, color=DECISION, stroke_width=3)
        tag = txt("A TPNG conversation about teams, products and seams", size=18, color=DECISION)
        group = VGroup(title, subtitle, rule, tag).arrange(DOWN, buff=0.32)
        group.move_to(ORIGIN).shift(UP * 0.15)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(subtitle), Create(rule), FadeIn(tag), run_time=0.7)
        self.next_slide()


class TheSentence(ConwaySlide):
    def construct(self):
        self.setup_slide("What Conway wrote", cite=True)
        quote = txt(
            "Any organization that designs a system\n"
            "will produce a design whose structure\n"
            "is a copy of the organization's\n"
            "communication structure.",
            size=28,
            color=INK,
            line_spacing=1.25,
        )
        quote.move_to(UP * 0.15)
        year = caption("Melvin E. Conway, 1968").next_to(quote, DOWN, buff=0.55)
        self.play(FadeIn(quote, shift=UP * 0.1), run_time=0.7)
        self.next_slide()
        self.play(FadeIn(year), run_time=0.4)
        self.next_slide()
        highlight = txt("communication structure", size=32, weight="BOLD", color=DECISION)
        highlight.next_to(year, DOWN, buff=0.5)
        self.play(FadeIn(highlight), run_time=0.5)
        self.next_slide()


class OrgMirrorsSystem(ConwaySlide):
    def construct(self):
        self.setup_slide("The org chart becomes the architecture")
        org_title = txt("How we are organized", size=18, color=MUTE)
        sys_title = txt("What we ship", size=18, color=MUTE)

        def tree(labels, accent):
            top = node_box(labels[0], width=2.3, height=0.85, accent=accent, title_color=INK)
            children = VGroup(
                *[node_box(name, width=2.1, height=0.75, accent=LINE) for name in labels[1:]]
            ).arrange(RIGHT, buff=0.22)
            col = VGroup(top, children).arrange(DOWN, buff=0.45)
            arrows = VGroup()
            for child in children:
                arrows.add(
                    Arrow(
                        top.get_bottom(),
                        child.get_top(),
                        buff=0.06,
                        stroke_width=2,
                        color=MUTE,
                        max_tip_length_to_length_ratio=0.2,
                    )
                )
            return VGroup(col, arrows)

        org = tree(["TPNG", "SPP team", "VDP team", "Optimizer"], STATE)
        system = tree(["Last mile", "Stop graph", "Durations", "Tours"], DECISION)
        org_title.next_to(org, UP, buff=0.25)
        sys_title.next_to(system, UP, buff=0.25)
        left = VGroup(org_title, org)
        right = VGroup(sys_title, system)
        pair = VGroup(left, right).arrange(RIGHT, buff=1.4)
        pair.move_to(DOWN * 0.15)
        self.play(appear(left), run_time=0.6)
        self.next_slide()
        self.play(appear(right), run_time=0.6)
        self.next_slide()
        same = txt("Same shape. That is not an accident.", size=24, color=DECISION)
        same.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(same), run_time=0.45)
        self.next_slide()


class CommunicationNotBoxes(ConwaySlide):
    def construct(self):
        self.setup_slide("It is about who can talk — not the boxes")
        a = node_box("Team A", width=2.2, height=0.95, accent=STATE)
        b = node_box("Team B", width=2.2, height=0.95, accent=STATE)
        c = node_box("Team C", width=2.2, height=0.95, accent=LINE)
        teams = VGroup(a, b, c).arrange(RIGHT, buff=2.0)
        teams.move_to(UP * 0.7)
        talk = DoubleArrow(a.get_right(), b.get_left(), buff=0.08, color=DECISION, stroke_width=4)
        talk_lab = txt("daily, cheap", size=16, color=DECISION).next_to(talk, UP, buff=0.12)
        weak_l = DashedLine(a.get_bottom(), c.get_top() + LEFT * 0.2, color=UNCERTAINTY, stroke_width=2)
        weak_r = DashedLine(b.get_bottom(), c.get_top() + RIGHT * 0.2, color=UNCERTAINTY, stroke_width=2)
        weak_lab = txt("tickets, quarterly, expensive", size=16, color=UNCERTAINTY)
        weak_lab.next_to(c, DOWN, buff=0.35)
        self.play(appear(a), appear(b), appear(c), run_time=0.6)
        self.next_slide()
        self.play(Create(talk), FadeIn(talk_lab), run_time=0.5)
        self.next_slide()
        self.play(Create(weak_l), Create(weak_r), FadeIn(weak_lab), run_time=0.6)
        punch = txt("The system will integrate where we converse, and split where we don't.", size=22, color=INK)
        punch.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(punch), run_time=0.5)
        self.next_slide()


class SeamsBecomeInterfaces(ConwaySlide):
    def construct(self):
        self.setup_slide("Team seams become system interfaces")
        rows = [
            ("Handoff in the org", "Interface in the product"),
            ("Two teams, two standups", "An API, a queue, a file, a ticket"),
            ("Unclear owner", "A gap nobody optimizes"),
            ("Local metric", "A locally good, globally fragile plan"),
        ]
        header_l = txt(rows[0][0], size=20, weight="BOLD", color=MUTE)
        header_r = txt(rows[0][1], size=20, weight="BOLD", color=MUTE)
        header = VGroup(header_l, header_r).arrange(RIGHT, buff=1.6)
        header.move_to(UP * 1.7)
        self.play(FadeIn(header), run_time=0.4)
        body = VGroup()
        for left, right in rows[1:]:
            l = pill(left, accent=STATE, width=5.4, height=0.7)
            r = pill(right, accent=DECISION, width=5.6, height=0.7)
            body.add(VGroup(l, r).arrange(RIGHT, buff=0.35))
        body.arrange(DOWN, buff=0.28)
        body.next_to(header, DOWN, buff=0.45)
        for row in body:
            self.play(appear(row), run_time=0.4)
            self.next_slide()


class DORAExample(ConwaySlide):
    def construct(self):
        self.setup_slide("Look at last mile through Conway")
        decisions = [
            ("Which area?", "Sectorization"),
            ("Stop where?", "SPP"),
            ("How long?", "VDP"),
            ("Which tour?", "Optimizer"),
            ("What happened?", "Dashboard"),
        ]
        cols = []
        for q, prod in decisions:
            qbox = node_box(q, width=2.15, height=0.95, accent=DECISION, title_color=DECISION)
            pbox = node_box(prod, width=2.15, height=0.8, accent=LINE)
            cols.append(VGroup(qbox, pbox).arrange(DOWN, buff=0.28))
        row = VGroup(*cols).arrange(RIGHT, buff=0.18)
        row.move_to(UP * 0.35)
        self.play(LaggedStart(*[appear(c) for c in cols], lag_ratio=0.08), run_time=0.9)
        self.next_slide()
        ask = VGroup(
            txt("If SPP and the Optimizer are different teams,", size=22, color=INK),
            txt("Conway predicts a seam between stops and sequence.", size=22, color=DECISION),
        ).arrange(DOWN, buff=0.16)
        ask.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(ask), run_time=0.5)
        self.next_slide()
        replace = txt(
            "The question is whether that seam is a good decision boundary.",
            size=24,
            color=DECISION,
        )
        replace.to_edge(DOWN, buff=0.45)
        self.play(FadeOut(ask), FadeIn(replace), run_time=0.55)
        self.next_slide()


class InverseConway(ConwaySlide):
    def construct(self):
        self.setup_slide("The inverse Conway maneuver")
        old = txt("System  ←  copies  ←  today's teams", size=26, color=MUTE)
        new = txt("Desired decisions  →  shape  →  the teams we need", size=26, color=DECISION, weight="BOLD")
        stack = VGroup(old, new).arrange(DOWN, buff=0.45)
        stack.move_to(UP * 0.55)
        self.play(FadeIn(old), run_time=0.5)
        self.next_slide()
        self.play(FadeIn(new), run_time=0.5)
        self.next_slide()
        points = VGroup(
            caption("Do not start from the current product list."),
            caption("Start from the decisions the last mile must make well."),
            caption("Then ask whether our teams can even have that conversation."),
        ).arrange(DOWN, buff=0.22)
        points.next_to(stack, DOWN, buff=0.55)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.08) for p in points], lag_ratio=0.15), run_time=0.8)
        self.next_slide()


class Questions(ConwaySlide):
    def construct(self):
        self.setup_slide("Questions for TPNG")
        questions = [
            "Where does our architecture copy our org chart?",
            "Which seams are intentional decision boundaries?",
            "Which seams are just how we happened to staff the work?",
            "If we wanted one last-mile decision system, who would need to talk?",
            "What would we reorganize so the conversation becomes cheap?",
        ]
        rows = VGroup()
        for i, q in enumerate(questions, start=1):
            num = txt(f"{i}", size=24, color=DECISION, weight="BOLD")
            num_box = card(0.5, 0.5, accent=DECISION)
            num.move_to(num_box)
            label = txt(q, size=22, color=INK)
            rows.add(VGroup(VGroup(num_box, num), label).arrange(RIGHT, buff=0.26))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        rows.move_to(UP * 0.05)
        for row in rows:
            self.play(appear(row), run_time=0.35)
            self.next_slide()
        close = txt("Organize for the decisions. The system will follow.", size=22, color=DECISION)
        close.to_edge(DOWN, buff=0.38)
        self.play(FadeIn(close), run_time=0.45)
        self.next_slide()
