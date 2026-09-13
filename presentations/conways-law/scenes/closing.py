from __future__ import annotations

from manim import *

from theme import DECISION, INK, MUTE, txt

from .base import ConwaySlide


class WhoIsInTheConversation(ConwaySlide):
    def construct(self):
        self.setup_slide()

        first = txt("Your software mirrors your conversations.", size=28, color=INK)
        second = txt("Now some of those conversations are with machines.", size=22, color=DECISION)
        pair = VGroup(first, second).arrange(DOWN, buff=0.32)
        pair.move_to(UP * 0.4)
        self.play(FadeIn(first), run_time=0.45)
        self.play(FadeIn(second), run_time=0.4)
        self.next_slide()

        question = txt("WHO IS IN OUR CONVERSATION?", size=34, weight="BOLD", color=DECISION)
        missing = txt("And who is missing?", size=22, color=MUTE)
        closer = VGroup(question, missing).arrange(DOWN, buff=0.24)
        closer.move_to(UP * 1.15)
        q1 = txt("Which TPNG dependencies no longer have a conversation behind them?", size=18, color=INK)
        q2 = txt("What loop can still tell our agents we are wrong?", size=18, color=INK)
        qs = VGroup(q1, q2).arrange(DOWN, buff=0.22)
        qs.move_to(DOWN * 1.35)
        self.play(FadeOut(pair), FadeIn(closer), FadeIn(qs), run_time=0.6)
        self.next_slide()
