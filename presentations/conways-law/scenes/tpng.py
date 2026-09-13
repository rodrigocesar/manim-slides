from __future__ import annotations

from manim import *

from components import APIBoundary, CommunicationEdge, SoftwareModule, TeamBoundary, PersonNode, play_pulses
from theme import DECISION, LINE, MUTE, STATE, appear, txt

from .base import ConwaySlide


class TPNGGraph(ConwaySlide):
    def construct(self):
        self.setup_slide("TPNG: our communication graph")

        dora_people = [
            PersonNode("DS").move_to(LEFT * 4.55 + UP * 0.55),
            PersonNode("SWE").move_to(LEFT * 3.15 + UP * 0.55),
        ]
        opt_people = [PersonNode("SWE").move_to(RIGHT * 0.05 + UP * 0.55)]
        sec_people = [
            PersonNode("PO").move_to(RIGHT * 4.15 + UP * 0.55),
            PersonNode("BA").move_to(RIGHT * 5.45 + UP * 0.55),
        ]
        teams = VGroup(
            TeamBoundary("DORA", dora_people, buff=0.7, extra_top=0.42),
            TeamBoundary("Optimizer", opt_people, buff=0.85, extra_top=0.42),
            TeamBoundary("Sectorization", sec_people, buff=0.55, extra_top=0.42),
        )
        spp = VGroup(
            SoftwareModule("Graph Builder", width=2.2, height=0.5, size=14, accent=STATE),
            SoftwareModule("Recommender", width=2.2, height=0.5, size=14, accent=STATE),
            SoftwareModule("VDP", width=2.2, height=0.5, size=14),
        ).arrange(DOWN, buff=0.12)
        spp.move_to(LEFT * 3.85 + DOWN * 1.45)
        opt_box = SoftwareModule("Optimizer", width=2.2, height=0.7, accent=DECISION, title_color=DECISION)
        opt_box.move_to(RIGHT * 0.05 + DOWN * 1.15)
        sec_box = SoftwareModule("sectors", width=2.2, height=0.7)
        sec_box.move_to(RIGHT * 4.8 + DOWN * 1.15)
        api = APIBoundary("API", height=1.5)
        api.move_to(LEFT * 1.85 + DOWN * 1.15)
        link = CommunicationEdge(spp[1], opt_box, kind="contract", buff=0.5)

        self.play(
            FadeIn(teams),
            *[FadeIn(p) for p in dora_people + opt_people + sec_people],
            LaggedStart(*[appear(m) for m in (*spp, opt_box, sec_box)], lag_ratio=0.06),
            FadeIn(api),
            Create(link),
            run_time=0.85,
        )
        play_pulses(self, [link], color=DECISION, run_time=0.4)
        self.next_slide()

        punch = txt("Conversation becomes contract.", size=22, color=DECISION, weight="BOLD")
        punch.move_to(DOWN * 2.55)
        owned = VGroup(
            SoftwareModule("External API", width=2.2, height=0.48, size=14, accent=LINE),
            SoftwareModule("Adapter", width=2.2, height=0.48, size=14, accent=DECISION, title_color=DECISION),
            SoftwareModule("PlanningTask", width=2.4, height=0.48, size=14, accent=STATE),
        ).arrange(RIGHT, buff=0.45)
        owned.move_to(DOWN * 3.3)
        self.play(FadeIn(punch), FadeIn(owned), run_time=0.5)
        self.next_slide()
