from __future__ import annotations

from manim import *

from components import (
    AgentNode,
    CommunicationEdge,
    ContextDoc,
    PersonNode,
    SoftwareModule,
    graph_formula,
    motif_stack,
    play_pulses,
)
from theme import AGENT, DECISION, INK, LINE, MUTE, OK, STATE, UNCERTAINTY, appear, card, txt

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
        self.setup_slide("Then AI enters the organization")

        people = _quad()
        human = [
            CommunicationEdge(people[0], people[1]),
            CommunicationEdge(people[2], people[3]),
            CommunicationEdge(people[0], people[2]),
            CommunicationEdge(people[1], people[3]),
        ]
        self.play(LaggedStart(*[FadeIn(p, scale=0.9) for p in people], lag_ratio=0.08), run_time=0.5)
        self.play(*[Create(e) for e in human], run_time=0.4)
        play_pulses(self, human, color=STATE, run_time=0.5)
        self.next_slide()

        agents = [
            AgentNode().move_to(people[0].get_center() + UP * 0.85 + LEFT * 0.85),
            AgentNode().move_to(people[1].get_center() + UP * 0.85 + RIGHT * 0.85),
            AgentNode().move_to(people[2].get_center() + DOWN * 0.85 + LEFT * 0.85),
            AgentNode().move_to(people[3].get_center() + DOWN * 0.85 + RIGHT * 0.85),
        ]
        agent_edges = [CommunicationEdge(p, a, kind="agent", buff=0.42) for p, a in zip(people, agents)]
        self.play(LaggedStart(*[FadeIn(a, scale=0.8) for a in agents], lag_ratio=0.08), run_time=0.5)
        self.play(*[Create(e) for e in agent_edges], run_time=0.4)
        play_pulses(self, agent_edges, color=AGENT, run_time=0.4)
        play_pulses(self, agent_edges, color=AGENT, run_time=0.4)
        self.play(*[e.animate.set_opacity(0.28) for e in human], run_time=0.5)
        self.next_slide()

        modules = VGroup(
            SoftwareModule("module", width=1.7, height=0.5, size=14),
            SoftwareModule("PR", width=1.4, height=0.5, size=14, accent=DECISION, title_color=DECISION),
            SoftwareModule("tests", width=1.5, height=0.5, size=14, accent=OK),
            SoftwareModule("helper", width=1.6, height=0.5, size=14),
            SoftwareModule("PR", width=1.4, height=0.5, size=14, accent=DECISION, title_color=DECISION),
            SoftwareModule("wrapper", width=1.7, height=0.5, size=14),
        ).arrange_in_grid(rows=2, cols=3, buff=0.18)
        modules.move_to(RIGHT * 3.55 + UP * 0.15)
        self.play(LaggedStart(*[FadeIn(m, scale=0.85) for m in modules], lag_ratio=0.08), run_time=0.7)
        cheap = txt("Code became cheaper to produce.", size=22, color=OK)
        cheap.move_to(DOWN * 3.2)
        self.play(FadeIn(cheap), run_time=0.4)
        self.next_slide()

        ask = txt("Did shared understanding become cheaper too?", size=22, color=DECISION, weight="BOLD")
        ask.move_to(cheap.get_center())
        self.play(ReplacementTransform(cheap, ask), run_time=0.5)
        self.next_slide()


class NewConwayGraph(ConwaySlide):
    def construct(self):
        self.setup_slide("The new Conway graph")

        classical_h = txt("Human  ↔  Human", size=24, color=STATE)
        classical_a = txt("↓", size=28, color=DECISION)
        classical_s = txt("Software", size=24, color=INK)
        classical = VGroup(classical_h, classical_a, classical_s).arrange(DOWN, buff=0.22)
        tag = txt("Classical", size=18, color=MUTE)
        tag.next_to(classical, UP, buff=0.3)
        classical.move_to(UP * 0.2)
        self.play(FadeIn(tag), FadeIn(classical), run_time=0.5)
        self.next_slide()

        agentic = VGroup(
            txt("Human  ↔  Human", size=22, color=STATE),
            txt("↘         ↙", size=26, color=AGENT),
            txt("Agents", size=24, color=AGENT, weight="BOLD"),
            txt("↓", size=24, color=DECISION),
            txt("Shared context?", size=22, color=DECISION),
            txt("↓", size=24, color=DECISION),
            txt("Software", size=24, color=INK),
        ).arrange(DOWN, buff=0.12)
        agentic.move_to(UP * 0.15)
        new_tag = txt("Agentic development", size=18, color=AGENT)
        new_tag.next_to(agentic, UP, buff=0.22)
        self.play(FadeOut(classical), FadeOut(tag), FadeIn(new_tag), FadeIn(agentic), run_time=0.65)
        self.next_slide()

        self.play(FadeOut(agentic), FadeOut(new_tag), run_time=0.3)
        pairs = VGroup()
        defs = [
            ("A", "physical parking location"),
            ("B", "logical order group"),
            ("C", "optimizer entity"),
        ]
        xs = [-4.2, 0.0, 4.2]
        pair_edges = []
        def_labels = []
        for x, (who, meaning) in zip(xs, defs):
            person = PersonNode(who).move_to(UP * 1.55 + RIGHT * x)
            agent = AgentNode().move_to(DOWN * 0.05 + RIGHT * x)
            edge = CommunicationEdge(person, agent, kind="agent", buff=0.4)
            meaning_t = txt(meaning, size=15, color=MUTE).next_to(agent, DOWN, buff=0.28)
            pairs.add(person, agent)
            pair_edges.append(edge)
            def_labels.append(meaning_t)
        concept = SoftwareModule("Stopping Point", width=3.2, height=0.7, accent=DECISION, title_color=DECISION)
        concept.move_to(DOWN * 2.55)
        self.play(FadeIn(pairs), *[Create(e) for e in pair_edges], run_time=0.55)
        self.play(*[FadeIn(d) for d in def_labels], appear(concept), run_time=0.45)
        play_pulses(self, pair_edges, color=AGENT, run_time=0.45)
        self.play(*[d.animate.set_color(UNCERTAINTY).move_to(concept.get_top() + UP * 0.55) for d in def_labels], run_time=0.7)
        collide = txt("The synthetic feedback loop", size=20, color=UNCERTAINTY)
        collide.move_to(DOWN * 3.25)
        self.play(Indicate(concept, color=UNCERTAINTY), FadeIn(collide), run_time=0.5)
        self.next_slide()

        self.play(FadeOut(pairs), FadeOut(VGroup(*pair_edges)), FadeOut(VGroup(*def_labels)), FadeOut(concept), FadeOut(collide), run_time=0.35)

        loop_words = ["Assumption", "Prompt", "Generated code", "AI review", "Same assumption"]
        loop = VGroup(*[SoftwareModule(w, width=2.7, height=0.48, size=14) for w in loop_words]).arrange(DOWN, buff=0.12)
        loop.move_to(LEFT * 3.2 + UP * 0.1)
        loop_arrows = VGroup(
            *[
                Arrow(loop[i].get_bottom(), loop[i + 1].get_top(), buff=0.03, stroke_width=2, color=AGENT, max_tip_length_to_length_ratio=0.22)
                for i in range(4)
            ]
        )
        back = CurvedArrow(loop[-1].get_left(), loop[0].get_left(), angle=-TAU / 3.4, color=UNCERTAINTY, stroke_width=2)
        self.play(FadeIn(loop), Create(loop_arrows), Create(back), run_time=0.7)
        self.next_slide()

        human_loop = VGroup(
            SoftwareModule("Assumption", width=2.5, height=0.48, size=14),
            SoftwareModule("Teammate", width=2.5, height=0.48, size=14, accent=STATE),
        ).arrange(DOWN, buff=0.35)
        human_loop.move_to(RIGHT * 3.1 + UP * 0.7)
        wait = txt("Wait…", size=40, weight="BOLD", color=DECISION)
        wait.next_to(human_loop, DOWN, buff=0.45)
        self.play(appear(human_loop[0]), run_time=0.3)
        self.play(appear(human_loop[1]), run_time=0.3)
        self.play(FadeIn(wait, scale=0.8), loop.animate.set_opacity(0.28), loop_arrows.animate.set_opacity(0.25), back.animate.set_opacity(0.25), run_time=0.55)
        self.next_slide()

        self.play(FadeOut(VGroup(loop, loop_arrows, back, human_loop, wait)), run_time=0.3)
        stack = motif_stack()
        stack.move_to(UP * 0.35)
        key = txt("Software mirrors who shares context with whom.", size=22, color=DECISION, weight="BOLD")
        key.move_to(DOWN * 3.15)
        self.play(FadeIn(stack), run_time=0.6)
        self.play(FadeIn(key), run_time=0.4)
        self.next_slide()


class HugePR(ConwaySlide):
    def construct(self):
        self.setup_slide("The 15,000-line PR problem")

        a = PersonNode("A").move_to(LEFT * 5.0 + UP * 0.4)
        ai_a = AgentNode().next_to(a, UP, buff=0.45)
        edge_a = CommunicationEdge(a, ai_a, kind="agent", buff=0.36)
        self.play(FadeIn(a), FadeIn(ai_a), Create(edge_a), run_time=0.45)
        play_pulses(self, [edge_a], color=AGENT, run_time=0.4)

        pr = RoundedRectangle(
            width=2.3,
            height=0.7,
            corner_radius=0.12,
            stroke_color=LINE,
            stroke_width=2,
            fill_color="#172033",
            fill_opacity=1,
        )
        pr.move_to(LEFT * 1.7 + UP * 0.2)
        stats = VGroup(
            txt("+15,284", size=26, weight="BOLD", color=OK),
            txt("-3,912", size=20, color=UNCERTAINTY),
        ).arrange(DOWN, buff=0.08)
        self.play(GrowFromCenter(pr), run_time=0.35)
        self.play(pr.animate.stretch_to_fit_height(3.6).shift(DOWN * 0.15), run_time=0.7)
        stats.move_to(pr)
        self.play(FadeIn(stats), run_time=0.3)

        b = PersonNode("B").move_to(RIGHT * 2.6 + DOWN * 0.9)
        b.scale(0.78)
        self.play(pr.animate.shift(RIGHT * 2.6), stats.animate.shift(RIGHT * 2.6), FadeIn(b), run_time=0.7)
        self.next_slide()

        ai_b = AgentNode().next_to(b, UP, buff=0.4)
        self.play(FadeIn(ai_b), run_time=0.3)
        scan = Line(pr.get_top() + LEFT * 0.9, pr.get_top() + RIGHT * 0.9, color=AGENT, stroke_width=4)
        self.play(scan.animate.shift(DOWN * 3.2), run_time=0.7)
        lgtm = txt("Looks good to me  ✓", size=26, weight="BOLD", color=OK)
        lgtm.move_to(DOWN * 3.15)
        self.play(FadeOut(scan), FadeIn(lgtm), run_time=0.4)
        self.next_slide()

        missing = VGroup(
            txt("architectural reasoning", size=18, color=MUTE),
            txt("shared vocabulary", size=18, color=MUTE),
            txt("why the change exists", size=18, color=MUTE),
            txt("mental model transfer", size=18, color=MUTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        missing.move_to(LEFT * 3.6 + DOWN * 2.35)
        self.play(
            FadeOut(lgtm),
            FadeOut(ai_a),
            FadeOut(ai_b),
            FadeOut(edge_a),
            FadeIn(missing),
            run_time=0.55,
        )
        code = txt("Code crossed the boundary.", size=22, color=INK)
        understand = txt("Understanding didn't.", size=22, color=DECISION, weight="BOLD")
        lines = VGroup(code, understand).arrange(DOWN, buff=0.16)
        lines.move_to(RIGHT * 3.3 + DOWN * 2.55)
        empty = DashedLine(a.get_right(), b.get_left(), color=MUTE, stroke_width=2)
        self.play(Create(empty), FadeIn(code), run_time=0.45)
        self.play(FadeIn(understand), run_time=0.35)
        self.next_slide()
