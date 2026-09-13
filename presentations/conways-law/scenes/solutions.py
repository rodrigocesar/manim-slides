from __future__ import annotations

from manim import *

from components import (
    AgentNode,
    CommunicationEdge,
    ContextDoc,
    PersonNode,
    SoftwareModule,
    WorldNode,
    graph_formula,
)
from theme import AGENT, DECISION, INK, LINE, MUTE, OK, STATE, UNCERTAINTY, appear, txt

from .base import ConwaySlide


class SharedContext(ConwaySlide):
    def construct(self):
        self.setup_slide("TPNG already has part of the answer")

        people = [
            PersonNode("A").move_to(LEFT * 4.6 + DOWN * 2.15),
            PersonNode("B").move_to(ORIGIN + DOWN * 2.15),
            PersonNode("C").move_to(RIGHT * 4.6 + DOWN * 2.15),
        ]
        agents = [
            AgentNode().move_to(LEFT * 4.6 + DOWN * 0.55),
            AgentNode().move_to(ORIGIN + DOWN * 0.55),
            AgentNode().move_to(RIGHT * 4.6 + DOWN * 0.55),
        ]
        private = [
            ContextDoc("private prompt").next_to(agents[0], UP, buff=0.28),
            ContextDoc("private prompt").next_to(agents[1], UP, buff=0.28),
            ContextDoc("private prompt").next_to(agents[2], UP, buff=0.28),
        ]
        edges = [CommunicationEdge(p, a, kind="agent", buff=0.38) for p, a in zip(people, agents)]
        self.play(*[FadeIn(p) for p in people], *[FadeIn(a) for a in agents], *[Create(e) for e in edges], run_time=0.55)
        self.play(*[FadeIn(d) for d in private], run_time=0.35)
        self.next_slide()

        repo = SoftwareModule("SHARED CONTEXT", width=4.6, height=0.85, accent=DECISION, title_color=DECISION)
        repo.move_to(UP * 2.05)
        docs = VGroup(
            ContextDoc("SKILL.md", accent=DECISION, width=1.7),
            ContextDoc("ADR", accent=STATE, width=1.3),
            ContextDoc("API spec", width=1.6),
            ContextDoc("Confluence", width=1.85),
            ContextDoc("Jira", width=1.3),
            ContextDoc("tests", width=1.35),
        ).arrange(RIGHT, buff=0.12)
        docs.next_to(repo, DOWN, buff=0.22)
        self.play(
            *[d.animate.move_to(docs[i].get_center()) for i, d in enumerate(private)],
            FadeIn(repo),
            FadeIn(docs),
            run_time=0.75,
        )
        self.play(*[FadeOut(d) for d in private], run_time=0.2)

        mcp = VGroup(
            txt("MCP", size=14, color=AGENT, weight="BOLD"),
            txt("Code   ·   Confluence   ·   Jira   ·   GitHub", size=16, color=MUTE),
        ).arrange(DOWN, buff=0.08)
        mcp.next_to(docs, DOWN, buff=0.2)
        spokes = VGroup(
            *[Line(repo.get_bottom(), ag.get_top(), color=DECISION, stroke_width=2) for ag in agents]
        )
        self.play(Create(spokes), FadeIn(mcp), run_time=0.5)

        human = [
            CommunicationEdge(people[0], people[1], kind="strong", buff=0.4),
            CommunicationEdge(people[1], people[2], kind="strong", buff=0.4),
        ]
        self.play(*[Create(e) for e in human], run_time=0.35)
        self.next_slide()

        skills = txt("tourpla-skills", size=16, color=DECISION)
        skills.next_to(repo, RIGHT, buff=0.3)
        note = txt("Shared AI context is not a replacement for team communication.", size=20, color=INK)
        note2 = txt("It is infrastructure for keeping agents inside the team's conversation.", size=18, color=DECISION)
        notes = VGroup(note, note2).arrange(DOWN, buff=0.12)
        notes.move_to(DOWN * 3.2)
        self.play(FadeIn(skills), FadeIn(notes), run_time=0.5)
        self.next_slide()


class DesignConversations(ConwaySlide):
    def construct(self):
        self.setup_slide("Design the conversations")

        formula = graph_formula()
        formula.move_to(UP * 2.15)
        self.play(FadeIn(formula), run_time=0.4)
        self.next_slide()

        people = VGroup(
            PersonNode("DS"),
            PersonNode("SWE"),
            PersonNode("PO"),
        ).arrange(RIGHT, buff=0.45)
        model = SoftwareModule("shared architecture", width=3.3, height=0.7, accent=DECISION, title_color=DECISION)
        together = VGroup(people, model).arrange(DOWN, buff=0.35)
        together.move_to(UP * 0.15)
        lab1 = txt("1  Shared model before generated code", size=20, color=DECISION)
        lab1.move_to(DOWN * 2.5)
        self.play(FadeIn(together), FadeIn(lab1), run_time=0.55)
        self.next_slide()

        left = SoftwareModule("DORA", width=2.2, height=0.75, accent=STATE)
        right = SoftwareModule("Optimizer", width=2.2, height=0.75, accent=STATE)
        api = SoftwareModule("contract + vocabulary", width=3.1, height=0.6, size=14, accent=DECISION, title_color=DECISION)
        pair = VGroup(left, right).arrange(RIGHT, buff=2.4)
        pair.move_to(UP * 0.35)
        api.move_to(UP * 0.35)
        lab2 = txt("2  Ownership + contracts + vocabulary", size=20, color=DECISION)
        lab2.move_to(DOWN * 2.5)
        self.play(FadeOut(together), ReplacementTransform(lab1, lab2), FadeIn(pair), FadeIn(api), run_time=0.55)
        self.next_slide()

        docs = VGroup(
            ContextDoc("SKILL.md", accent=DECISION, width=1.8),
            ContextDoc("AGENTS.md", width=1.9),
            ContextDoc("ADR", width=1.4),
            ContextDoc("API rules", width=1.7),
            ContextDoc("glossary", width=1.6),
        ).arrange(RIGHT, buff=0.15)
        git = SoftwareModule("git", width=1.6, height=0.7, accent=OK, title_color=OK)
        pack = VGroup(docs, git).arrange(DOWN, buff=0.4)
        pack.move_to(UP * 0.2)
        lab3 = txt("3  Private instructions → shared infrastructure", size=20, color=DECISION)
        lab3.move_to(DOWN * 2.5)
        self.play(FadeOut(pair), FadeOut(api), ReplacementTransform(lab2, lab3), FadeIn(pack), run_time=0.55)
        self.next_slide()

        soft = SoftwareModule("Software", width=2.4, height=0.7, accent=STATE)
        world = WorldNode("REAL WORLD")
        extras = VGroup(
            SoftwareModule("tests", width=1.5, height=0.48, size=14),
            SoftwareModule("metrics", width=1.6, height=0.48, size=14),
            SoftwareModule("operations", width=1.9, height=0.48, size=14),
        ).arrange(RIGHT, buff=0.2)
        loop = VGroup(soft, extras, world).arrange(DOWN, buff=0.4)
        loop.move_to(UP * 0.05)
        arrows = VGroup(
            Arrow(soft.get_bottom(), extras.get_top(), buff=0.06, stroke_width=2, color=MUTE, max_tip_length_to_length_ratio=0.2),
            Arrow(extras.get_bottom(), world.get_top(), buff=0.06, stroke_width=2, color=UNCERTAINTY, max_tip_length_to_length_ratio=0.2),
        )
        lab4 = txt("4  Reality must be able to disagree with the agent.", size=20, color=DECISION)
        lab4.move_to(DOWN * 3.2)
        self.play(FadeOut(pack), ReplacementTransform(lab3, lab4), FadeIn(loop), Create(arrows), run_time=0.6)
        self.next_slide()
