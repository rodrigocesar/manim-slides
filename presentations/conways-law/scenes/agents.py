from __future__ import annotations

from manim import *

from components import AgentNode, CommunicationEdge, PersonNode, SoftwareModule, motif_stack, play_pulses
from theme import AGENT, DECISION, INK, MUTE, OK, STATE, UNCERTAINTY, appear, txt

from .base import ConwaySlide


def _quad():
    return [
        PersonNode("A").move_to(LEFT * 4.35 + UP * 1.15),
        PersonNode("B").move_to(LEFT * 1.85 + UP * 1.15),
        PersonNode("C").move_to(LEFT * 4.35 + DOWN * 0.85),
        PersonNode("D").move_to(LEFT * 1.85 + DOWN * 0.85),
    ]


class AIEnters(ConwaySlide):
    def construct(self):
        self.setup_slide("Then AI enters")

        people = _quad()
        human = [
            CommunicationEdge(people[0], people[1]),
            CommunicationEdge(people[2], people[3]),
            CommunicationEdge(people[0], people[2]),
            CommunicationEdge(people[1], people[3]),
        ]
        self.play(LaggedStart(*[FadeIn(p, scale=0.9) for p in people], lag_ratio=0.08), run_time=0.4)
        self.play(*[Create(e) for e in human], run_time=0.3)
        play_pulses(self, human, color=STATE, run_time=0.4)
        self.next_slide()

        agents = [
            AgentNode().move_to(people[0].get_center() + UP * 0.85 + LEFT * 0.85),
            AgentNode().move_to(people[1].get_center() + UP * 0.85 + RIGHT * 0.85),
            AgentNode().move_to(people[2].get_center() + DOWN * 0.85 + LEFT * 0.85),
            AgentNode().move_to(people[3].get_center() + DOWN * 0.85 + RIGHT * 0.85),
        ]
        agent_edges = [CommunicationEdge(p, a, kind="agent", buff=0.42) for p, a in zip(people, agents)]
        modules = VGroup(
            SoftwareModule("PR", width=1.4, height=0.5, size=14, accent=DECISION, title_color=DECISION),
            SoftwareModule("tests", width=1.5, height=0.5, size=14, accent=OK),
            SoftwareModule("helper", width=1.6, height=0.5, size=14),
            SoftwareModule("PR", width=1.4, height=0.5, size=14, accent=DECISION, title_color=DECISION),
        ).arrange_in_grid(rows=2, cols=2, buff=0.18)
        modules.move_to(RIGHT * 3.7 + UP * 0.15)
        cheap = txt("Code got cheaper.", size=22, color=OK)
        ask = txt("Did shared understanding?", size=22, color=DECISION, weight="BOLD")
        lines = VGroup(cheap, ask).arrange(DOWN, buff=0.12)
        lines.move_to(DOWN * 3.2)

        self.play(LaggedStart(*[FadeIn(a, scale=0.8) for a in agents], lag_ratio=0.06), run_time=0.4)
        self.play(*[Create(e) for e in agent_edges], run_time=0.3)
        play_pulses(self, agent_edges, color=AGENT, run_time=0.35)
        self.play(
            *[e.animate.set_opacity(0.28) for e in human],
            LaggedStart(*[FadeIn(m, scale=0.85) for m in modules], lag_ratio=0.06),
            FadeIn(lines),
            run_time=0.7,
        )
        self.next_slide()


class NewConwayGraph(ConwaySlide):
    def construct(self):
        self.setup_slide("Software mirrors who shares context")

        agentic = VGroup(
            txt("Human  ↔  Human", size=22, color=STATE),
            txt("↘         ↙", size=26, color=AGENT),
            txt("Agents", size=24, color=AGENT, weight="BOLD"),
            txt("↓", size=24, color=DECISION),
            txt("Shared context?", size=22, color=DECISION),
            txt("↓", size=24, color=DECISION),
            txt("Software", size=24, color=INK),
        ).arrange(DOWN, buff=0.1)
        agentic.move_to(UP * 0.2)
        self.play(FadeIn(agentic), run_time=0.5)
        self.next_slide()

        self.play(FadeOut(agentic), run_time=0.25)
        defs = [
            ("A", "parking location"),
            ("B", "order group"),
            ("C", "optimizer entity"),
        ]
        xs = [-4.2, 0.0, 4.2]
        pairs = VGroup()
        pair_edges = []
        def_labels = []
        for x, (who, meaning) in zip(xs, defs):
            person = PersonNode(who).move_to(UP * 1.55 + RIGHT * x)
            agent = AgentNode().move_to(DOWN * 0.15 + RIGHT * x)
            edge = CommunicationEdge(person, agent, kind="agent", buff=0.4)
            meaning_t = txt(meaning, size=16, color=MUTE).next_to(agent, DOWN, buff=0.28)
            pairs.add(person, agent)
            pair_edges.append(edge)
            def_labels.append(meaning_t)
        concept = SoftwareModule("Stopping Point", width=3.2, height=0.7, accent=DECISION, title_color=DECISION)
        concept.move_to(DOWN * 2.35)
        wait = txt("Wait…", size=36, weight="BOLD", color=DECISION)
        wait.move_to(DOWN * 3.25)
        self.play(FadeIn(pairs), *[Create(e) for e in pair_edges], run_time=0.45)
        self.play(*[FadeIn(d) for d in def_labels], appear(concept), run_time=0.35)
        self.play(*[d.animate.set_color(UNCERTAINTY).move_to(concept.get_top() + UP * 0.5) for d in def_labels], run_time=0.55)
        self.play(Indicate(concept, color=UNCERTAINTY), FadeIn(wait), run_time=0.45)
        self.next_slide()

        self.play(
            FadeOut(pairs),
            FadeOut(VGroup(*pair_edges)),
            FadeOut(VGroup(*def_labels)),
            FadeOut(concept),
            FadeOut(wait),
            run_time=0.25,
        )
        stack = motif_stack()
        stack.move_to(UP * 0.35)
        key = txt("Software mirrors who shares context with whom.", size=22, color=DECISION, weight="BOLD")
        key.move_to(DOWN * 3.15)
        self.play(FadeIn(stack), FadeIn(key), run_time=0.55)
        self.next_slide()
