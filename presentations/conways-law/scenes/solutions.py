from __future__ import annotations

from manim import *

from components import AgentNode, CommunicationEdge, ContextDoc, PersonNode, SoftwareModule
from theme import AGENT, DECISION, INK, MUTE, txt

from .base import ConwaySlide


class SharedContext(ConwaySlide):
    def construct(self):
        self.setup_slide("Design the shared context")

        people = [
            PersonNode("A").move_to(LEFT * 4.6 + DOWN * 2.05),
            PersonNode("B").move_to(ORIGIN + DOWN * 2.05),
            PersonNode("C").move_to(RIGHT * 4.6 + DOWN * 2.05),
        ]
        agents = [
            AgentNode().move_to(LEFT * 4.6 + DOWN * 0.45),
            AgentNode().move_to(ORIGIN + DOWN * 0.45),
            AgentNode().move_to(RIGHT * 4.6 + DOWN * 0.45),
        ]
        private = [
            ContextDoc("private prompt").next_to(agents[0], UP, buff=0.28),
            ContextDoc("private prompt").next_to(agents[1], UP, buff=0.28),
            ContextDoc("private prompt").next_to(agents[2], UP, buff=0.28),
        ]
        edges = [CommunicationEdge(p, a, kind="agent", buff=0.38) for p, a in zip(people, agents)]
        self.play(
            *[FadeIn(p) for p in people],
            *[FadeIn(a) for a in agents],
            *[Create(e) for e in edges],
            *[FadeIn(d) for d in private],
            run_time=0.55,
        )
        self.next_slide()

        repo = SoftwareModule("SHARED CONTEXT", width=4.6, height=0.8, accent=DECISION, title_color=DECISION)
        repo.move_to(UP * 2.1)
        docs = VGroup(
            ContextDoc("SKILL.md", accent=DECISION, width=1.7),
            ContextDoc("ADR", width=1.3),
            ContextDoc("API spec", width=1.6),
            ContextDoc("tests", width=1.35),
        ).arrange(RIGHT, buff=0.14)
        docs.next_to(repo, DOWN, buff=0.2)
        skills = txt("tourpla-skills", size=16, color=DECISION)
        skills.next_to(repo, RIGHT, buff=0.28)
        spokes = VGroup(*[Line(repo.get_bottom(), ag.get_top(), color=DECISION, stroke_width=2) for ag in agents])
        human = [
            CommunicationEdge(people[0], people[1], kind="strong", buff=0.4),
            CommunicationEdge(people[1], people[2], kind="strong", buff=0.4),
        ]
        actions = VGroup(
            txt("Model together", size=16, color=INK),
            txt("Version agent context", size=16, color=INK),
            txt("Let reality disagree", size=16, color=DECISION),
        ).arrange(RIGHT, buff=0.55)
        actions.move_to(DOWN * 3.25)
        self.play(
            *[d.animate.move_to(docs[min(i, len(docs) - 1)].get_center()) for i, d in enumerate(private)],
            FadeIn(repo),
            FadeIn(docs),
            FadeIn(skills),
            run_time=0.65,
        )
        self.play(*[FadeOut(d) for d in private], Create(spokes), *[Create(e) for e in human], FadeIn(actions), run_time=0.5)
        self.next_slide()
