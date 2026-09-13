from __future__ import annotations

from manim import *

from theme import DECISION, INK, MUTE, txt

from .base import ConwaySlide


class WhoIsInTheConversation(ConwaySlide):
    def construct(self):
        self.setup_slide()

        first = txt("Your software mirrors your conversations.", size=28, color=INK)
        first.move_to(UP * 0.35)
        self.play(FadeIn(first), run_time=0.6)
        self.next_slide()

        second = txt("Now some of those conversations are with machines.", size=24, color=DECISION)
        second.next_to(first, DOWN, buff=0.4)
        self.play(FadeIn(second), run_time=0.55)
        self.next_slide()

        question = txt("WHO IS IN OUR CONVERSATION?", size=36, weight="BOLD", color=DECISION)
        missing = txt("And who is missing?", size=22, color=MUTE)
        closer = VGroup(question, missing).arrange(DOWN, buff=0.28)
        closer.move_to(UP * 0.55)
        self.play(FadeOut(first), FadeOut(second), FadeIn(closer), run_time=0.65)
        self.next_slide()

        q1 = txt("Which TPNG dependencies no longer have a conversation behind them?", size=18, color=INK)
        q2 = txt("Whose communication structure did the last thing we shipped inherit?", size=18, color=INK)
        q3 = txt("What independent loop can still tell our agents we are wrong?", size=18, color=INK)
        qs = VGroup(q1, q2, q3).arrange(DOWN, buff=0.28)
        qs.move_to(DOWN * 1.7)
        for q in qs:
            self.play(FadeIn(q, shift=UP * 0.08), run_time=0.4)
            self.next_slide()
