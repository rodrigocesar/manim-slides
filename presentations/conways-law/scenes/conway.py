from __future__ import annotations

from manim import *

from components import (
    APIBoundary,
    CommunicationEdge,
    PersonNode,
    SoftwareModule,
    TeamBoundary,
    check_mark,
)
from theme import DECISION, INK, LINE, MUTE, STATE, UNCERTAINTY, appear, txt

from .base import ConwaySlide


class NotMicroservices(ConwaySlide):
    def construct(self):
        self.setup_slide("Conway is not asking for microservices")

        left_title = txt("Organization A", size=18, color=MUTE).move_to(LEFT * 3.45 + UP * 2.2)
        right_title = txt("Organization B", size=18, color=MUTE).move_to(RIGHT * 3.45 + UP * 2.2)

        a_people = [
            PersonNode("A").move_to(LEFT * 4.25 + UP * 1.05),
            PersonNode("B").move_to(LEFT * 2.65 + UP * 1.05),
            PersonNode("C").move_to(LEFT * 4.25 + DOWN * 0.25),
            PersonNode("D").move_to(LEFT * 2.65 + DOWN * 0.25),
        ]
        a_team = TeamBoundary("one team", a_people, buff=0.36)
        a_edges = [
            CommunicationEdge(a_people[0], a_people[1]),
            CommunicationEdge(a_people[2], a_people[3]),
            CommunicationEdge(a_people[0], a_people[2]),
            CommunicationEdge(a_people[1], a_people[3]),
            CommunicationEdge(a_people[0], a_people[3]),
        ]
        a_soft = SoftwareModule("one modular application", width=3.6, height=0.7, accent=STATE)
        a_soft.move_to(LEFT * 3.45 + DOWN * 2.05)

        b_people = [
            PersonNode("A").move_to(RIGHT * 1.85 + UP * 0.85),
            PersonNode("B").move_to(RIGHT * 3.45 + UP * 0.85),
            PersonNode("C").move_to(RIGHT * 5.05 + UP * 0.85),
        ]
        b_teams = VGroup(
            TeamBoundary("Team A", [b_people[0]], buff=0.32, extra_top=0.32),
            TeamBoundary("Team B", [b_people[1]], buff=0.32, extra_top=0.32),
            TeamBoundary("Team C", [b_people[2]], buff=0.32, extra_top=0.32),
        )
        api_l = APIBoundary("contract", height=0.95).move_to(RIGHT * 2.65 + UP * 0.85)
        api_r = APIBoundary("contract", height=0.95).move_to(RIGHT * 4.25 + UP * 0.85)
        b_soft = VGroup(
            SoftwareModule("comp A", width=1.7, height=0.58, accent=STATE),
            SoftwareModule("comp B", width=1.7, height=0.58, accent=STATE),
            SoftwareModule("comp C", width=1.7, height=0.58, accent=STATE),
        ).arrange(RIGHT, buff=0.22)
        b_soft.move_to(RIGHT * 3.45 + DOWN * 2.05)

        self.play(FadeIn(left_title), FadeIn(a_team), *[FadeIn(p) for p in a_people], *[Create(e) for e in a_edges], appear(a_soft), run_time=0.7)
        self.next_slide()
        self.play(
            FadeIn(right_title),
            FadeIn(b_teams),
            *[FadeIn(p) for p in b_people],
            FadeIn(api_l),
            FadeIn(api_r),
            appear(b_soft),
            run_time=0.7,
        )
        self.next_slide()

        marks = VGroup(check_mark().next_to(a_soft, DOWN, buff=0.18), check_mark().next_to(b_soft, DOWN, buff=0.18))
        none = txt("There is no universally correct shape.", size=22, color=INK)
        none.move_to(DOWN * 3.2)
        self.play(FadeIn(marks), FadeIn(none), run_time=0.45)
        self.next_slide()

        danger = txt("The danger is when the two graphs disagree.", size=22, color=DECISION, weight="BOLD")
        danger.move_to(none.get_center())
        self.play(FadeOut(none), FadeIn(danger), run_time=0.4)
        self.next_slide()

        self.play(
            FadeOut(VGroup(left_title, right_title, a_team, b_teams, marks, danger, a_soft, b_soft, api_l, api_r)),
            FadeOut(VGroup(*a_people, *b_people, *a_edges)),
            run_time=0.45,
        )

        m_people = [
            PersonNode("A").move_to(LEFT * 2.4 + UP * 1.2),
            PersonNode("B").move_to(RIGHT * 2.4 + UP * 1.2),
        ]
        m_teams = VGroup(
            TeamBoundary("Team A", [m_people[0]], buff=0.55),
            TeamBoundary("Team B", [m_people[1]], buff=0.55),
        )
        shared = SoftwareModule("giant shared module", width=4.4, height=0.85, accent=UNCERTAINTY, title_color=UNCERTAINTY)
        db = SoftwareModule("shared database", width=3.2, height=0.62, accent=UNCERTAINTY)
        shared.move_to(DOWN * 0.15)
        db.next_to(shared, DOWN, buff=0.22)
        self.play(FadeIn(m_teams), *[FadeIn(p) for p in m_people], appear(shared), appear(db), run_time=0.6)

        change = txt("Team A change", size=16, color=DECISION).next_to(m_people[0], UP, buff=0.55)
        red = txt("pipeline breaks", size=16, color=UNCERTAINTY).next_to(m_people[1], UP, buff=0.55)
        hit = Arrow(shared.get_top() + LEFT * 1.1, m_people[1].get_bottom(), buff=0.08, color=UNCERTAINTY, stroke_width=3)
        schema = txt("shared schema", size=16, color=UNCERTAINTY).next_to(db, DOWN, buff=0.18)
        self.play(FadeIn(change), shared.animate.set_color(UNCERTAINTY), run_time=0.4)
        self.play(Create(hit), FadeIn(red), db.box.animate.set_stroke(UNCERTAINTY), FadeIn(schema), run_time=0.55)

        labels = VGroup(
            txt("coordination", size=16, color=MUTE),
            txt("ownership", size=16, color=MUTE),
            txt("deployment", size=16, color=MUTE),
            txt("semantic coupling", size=16, color=MUTE),
        ).arrange(RIGHT, buff=0.45)
        labels.move_to(DOWN * 3.2)
        self.play(FadeIn(labels), run_time=0.4)
        self.next_slide()
