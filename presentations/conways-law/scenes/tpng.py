from __future__ import annotations

from manim import *

from components import APIBoundary, CommunicationEdge, PersonNode, SoftwareModule, TeamBoundary, play_pulses
from theme import DECISION, INK, LINE, MUTE, STATE, UNCERTAINTY, appear, txt

from .base import ConwaySlide


class TPNGGraph(ConwaySlide):
    def construct(self):
        self.setup_slide("TPNG: our communication graph")

        dora_people = [
            PersonNode("DS").move_to(LEFT * 4.55 + UP * 0.55),
            PersonNode("SWE").move_to(LEFT * 3.15 + UP * 0.55),
        ]
        opt_people = [PersonNode("SWE").move_to(RIGHT * 0.05 + UP * 0.55)]
        sec_people = [PersonNode("PO").move_to(RIGHT * 4.15 + UP * 0.55), PersonNode("BA").move_to(RIGHT * 5.45 + UP * 0.55)]

        dora = TeamBoundary("DORA", dora_people, buff=0.7, extra_top=0.42)
        opt = TeamBoundary("Optimizer", opt_people, buff=0.85, extra_top=0.42)
        sec = TeamBoundary("Sectorization", sec_people, buff=0.55, extra_top=0.42)
        teams = VGroup(dora, opt, sec)

        spp = VGroup(
            SoftwareModule("Trajectory", width=2.15, height=0.48, size=14),
            SoftwareModule("Graph Builder", width=2.15, height=0.48, size=14, accent=STATE),
            SoftwareModule("Recommender", width=2.15, height=0.48, size=14, accent=STATE),
            SoftwareModule("VDP", width=2.15, height=0.48, size=14),
        ).arrange(DOWN, buff=0.12)
        spp.move_to(LEFT * 3.85 + DOWN * 1.55)

        opt_box = SoftwareModule("Optimizer", width=2.2, height=0.7, accent=DECISION, title_color=DECISION)
        opt_box.move_to(RIGHT * 0.05 + DOWN * 1.15)
        sec_box = SoftwareModule("sectors", width=2.2, height=0.7)
        sec_box.move_to(RIGHT * 4.8 + DOWN * 1.15)

        self.play(FadeIn(teams), *[FadeIn(p) for p in dora_people + opt_people + sec_people], run_time=0.55)
        self.play(LaggedStart(*[appear(m) for m in spp], lag_ratio=0.08), appear(opt_box), appear(sec_box), run_time=0.7)
        self.next_slide()

        api = APIBoundary("API", height=1.7)
        api.move_to(LEFT * 1.85 + DOWN * 1.2)
        link = CommunicationEdge(spp[2], opt_box, kind="contract", buff=0.55)
        self.play(FadeIn(api), Create(link), run_time=0.5)
        play_pulses(self, [link], color=DECISION, run_time=0.5)

        change = txt("a change crosses the boundary", size=18, color=DECISION)
        change.move_to(DOWN * 3.2)
        self.play(spp[2].box.animate.set_stroke(DECISION, width=3), FadeIn(change), run_time=0.45)
        self.next_slide()

        talk = txt("conversation", size=18, color=STATE).move_to(LEFT * 3.3 + UP * 2.15)
        iface = txt("interface", size=18, color=MUTE).move_to(ORIGIN + UP * 2.15)
        contract = txt("API contract", size=18, color=DECISION).move_to(RIGHT * 3.3 + UP * 2.15)
        a1 = Arrow(talk.get_right(), iface.get_left(), buff=0.12, color=MUTE, stroke_width=2, max_tip_length_to_length_ratio=0.18)
        a2 = Arrow(iface.get_right(), contract.get_left(), buff=0.12, color=DECISION, stroke_width=2, max_tip_length_to_length_ratio=0.18)
        punch = txt("Conversation becomes contract.", size=22, color=DECISION, weight="BOLD")
        punch.move_to(DOWN * 3.2)
        self.play(FadeIn(talk), run_time=0.3)
        self.play(Create(a1), FadeIn(iface), run_time=0.35)
        self.play(Create(a2), FadeIn(contract), ReplacementTransform(change, punch), run_time=0.45)
        self.next_slide()


class PlanningTask(ConwaySlide):
    def construct(self):
        self.setup_slide("Architecture inherits history")

        order = SoftwareModule("Order", width=2.6, height=0.62, accent=UNCERTAINTY, title_color=UNCERTAINTY)
        kids = VGroup(
            SoftwareModule("DeliveryOrder", width=2.5, height=0.48, size=14, accent=LINE),
            SoftwareModule("TransportOrder", width=2.5, height=0.48, size=14, accent=LINE),
            SoftwareModule("HomeCollection", width=2.5, height=0.48, size=14, accent=LINE),
        ).arrange(DOWN, buff=0.1)
        tree = VGroup(order, kids).arrange(DOWN, buff=0.22)
        tree.move_to(LEFT * 4.0 + UP * 0.35)
        self.play(appear(order), LaggedStart(*[appear(k) for k in kids], lag_ratio=0.1), run_time=0.65)
        self.next_slide()

        dora = SoftwareModule("DORA internals", width=3.3, height=1.15, accent=STATE)
        dora.move_to(RIGHT * 2.8 + UP * 0.9)
        self.play(tree.animate.scale(0.92).shift(RIGHT * 0.15), appear(dora), run_time=0.55)
        branches = VGroup(
            txt("if DeliveryOrder...", size=16, color=UNCERTAINTY),
            txt("elif TransportOrder...", size=16, color=UNCERTAINTY),
            txt("elif HomeCollection...", size=16, color=UNCERTAINTY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        branches.next_to(dora, DOWN, buff=0.35)
        arrows = VGroup(
            *[
                Line(kids[i].get_right(), branches[i].get_left(), color=UNCERTAINTY, stroke_width=2)
                for i in range(3)
            ]
        )
        self.play(Create(arrows), FadeIn(branches), run_time=0.6)

        concepts = VGroup(
            txt("orderType", size=16, color=MUTE),
            txt("actionType", size=16, color=MUTE),
            txt("productCategory", size=16, color=MUTE),
        ).arrange(RIGHT, buff=0.4)
        concepts.move_to(DOWN * 2.35)
        self.play(FadeIn(concepts, shift=DOWN * 0.1), run_time=0.4)
        tangled = txt("An integration model became an internal domain model.", size=20, color=DECISION)
        tangled.move_to(DOWN * 3.2)
        self.play(FadeIn(tangled), run_time=0.4)
        self.next_slide()

        external = SoftwareModule("External API", width=2.4, height=0.62, accent=LINE)
        adapter = SoftwareModule("Adapter", width=2.4, height=0.62, accent=DECISION, title_color=DECISION)
        task = SoftwareModule("PlanningTask", width=2.6, height=0.72, accent=STATE, title_color=STATE)
        owned = VGroup(external, adapter, task).arrange(DOWN, buff=0.35)
        owned.move_to(LEFT * 3.9 + UP * 0.15)
        down_arrows = VGroup(
            Arrow(external.get_bottom(), adapter.get_top(), buff=0.05, stroke_width=3, color=DECISION, max_tip_length_to_length_ratio=0.2),
            Arrow(adapter.get_bottom(), task.get_top(), buff=0.05, stroke_width=3, color=STATE, max_tip_length_to_length_ratio=0.2),
        )
        fields = VGroup(
            txt("task.housekey", size=16, color=INK),
            txt("task.action_type", size=16, color=INK),
            txt("task.target_time_windows", size=16, color=INK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        fields.move_to(RIGHT * 2.6 + UP * 0.2)

        owned_lab = txt("DORA-owned model", size=22, color=STATE, weight="BOLD")
        owned_lab.move_to(DOWN * 3.2)
        self.play(
            FadeOut(VGroup(tree, dora, arrows, branches, concepts)),
            FadeIn(owned),
            Create(down_arrows),
            run_time=0.7,
        )
        self.play(ReplacementTransform(tangled, owned_lab), FadeIn(fields), run_time=0.5)
        self.next_slide()

        punch = txt("Change the communication boundary  →  change the software boundary", size=18, color=DECISION)
        punch.move_to(DOWN * 3.2)
        inverse = txt("We can choose the boundary. Inverse Conway — on purpose.", size=16, color=MUTE)
        inverse.next_to(punch, UP, buff=0.18)
        self.play(ReplacementTransform(owned_lab, punch), FadeIn(inverse), run_time=0.45)
        self.next_slide()
