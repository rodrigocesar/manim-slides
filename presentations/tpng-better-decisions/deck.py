"""Are we making better decisions? — DORA / Sectorization talk."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "shared"))

from manim import *
from manim_slides import Slide

from theme import (
    BG,
    CARD,
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
    labeled_card,
    node_box,
    pill,
    slide_title,
    txt,
)


class DoraSlide(Slide):
    skip_reversing = True

    def setup_slide(self, title: str | None = None, cite: bool = False):
        self.camera.background_color = ManimColor(BG)
        parts = []
        if title:
            parts.append(slide_title(title))
        if cite:
            parts.append(footer("Powell (2022) · CASTLE Lab · sequential decision analytics"))
        if parts:
            self.add(*parts)
        return parts


class Title(DoraSlide):
    def construct(self):
        self.setup_slide(cite=True)
        title = txt("Are we making better decisions?", size=48, weight="BOLD")
        subtitle = txt(
            "A decision-centric view of DORA, Sectorization and last-mile planning",
            size=22,
            color=MUTE,
        )
        rule = Line(LEFT * 2.2, RIGHT * 2.2, color=DECISION, stroke_width=3)
        tag = txt("Powell's sequential decision framework  ·  CASTLE Lab", size=18, color=DECISION)
        group = VGroup(title, subtitle, rule, tag).arrange(DOWN, buff=0.32)
        group.move_to(ORIGIN).shift(UP * 0.15)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(subtitle), Create(rule), FadeIn(tag), run_time=0.7)
        self.next_slide()


class WhatDoesGoodMean(DoraSlide):
    def construct(self):
        self.setup_slide("What does “good” mean?")
        left = labeled_card(
            "PLADATO",
            ["10 tours", "16 h driving", "15 h walking", "0 h overtime", "2 late deliveries"],
            width=4.6,
            height=3.7,
            accent=LINE,
        )
        right = labeled_card(
            "TOURPLA",
            ["9 tours", "18 h driving", "12 h walking", "3 h overtime", "0 late deliveries"],
            width=4.6,
            height=3.7,
            accent=LINE,
        )
        cards = VGroup(left, right).arrange(RIGHT, buff=0.7)
        cards.move_to(DOWN * 0.15)
        self.play(appear(left), appear(right), run_time=0.7)
        self.next_slide()

        wins = VGroup(
            txt("fewer hours on the road", size=16, color=OK).next_to(left, DOWN, buff=0.22),
            txt("fewer tours, no lates", size=16, color=OK).next_to(right, DOWN, buff=0.22),
        )
        self.play(FadeIn(wins, shift=DOWN * 0.1), run_time=0.5)
        self.next_slide()

        question = txt("BETTER?", size=64, weight="BOLD", color=DECISION)
        question.move_to(ORIGIN)
        veil = card(13.2, 6.4, accent=BG, fill=BG).set_opacity(0.72)
        self.play(FadeIn(veil), FadeIn(question, scale=0.85), run_time=0.7)
        self.next_slide()


class OutputsAreNotDecisions(DoraSlide):
    def construct(self):
        self.setup_slide("Outputs are not decisions")

        def chain(labels: list[str], accents: list[str]) -> VGroup:
            boxes = [node_box(lab, width=2.6, height=1.05, accent=acc, title_color=INK) for lab, acc in zip(labels, accents)]
            group = VGroup(*boxes).arrange(RIGHT, buff=1.15)
            arrows = VGroup()
            for a, b in zip(boxes, boxes[1:]):
                arrows.add(
                    Arrow(
                        a.get_right() + RIGHT * 0.06,
                        b.get_left() + LEFT * 0.06,
                        buff=0.04,
                        stroke_width=3,
                        color=MUTE,
                        max_tip_length_to_length_ratio=0.18,
                    )
                )
            return VGroup(group, arrows)

        old = chain(
            ["DATA", "MODEL", "OUTPUT"],
            [LINE, LINE, LINE],
        )
        old.move_to(UP * 0.55)
        old_cap = caption("A common path: produce an artifact, then look for a metric.").next_to(old, DOWN, buff=0.45)
        self.play(appear(old), FadeIn(old_cap), run_time=0.7)
        self.next_slide()

        new = chain(
            ["SITUATION", "DECISION", "OUTCOME"],
            [STATE, DECISION, OK],
        )
        new.move_to(UP * 0.55)
        new_cap = caption("Value appears only when something in the operation changes.").next_to(new, DOWN, buff=0.45)
        self.play(FadeOut(old), FadeOut(old_cap), FadeIn(new), FadeIn(new_cap), run_time=0.8)
        self.next_slide()

        extras = VGroup(
            caption("A graph is not a decision.", color=INK, size=22),
            caption("A prediction is not a decision.", color=INK, size=22),
            caption("A dashboard is not a decision.", color=INK, size=22),
        ).arrange(DOWN, buff=0.18)
        extras.next_to(new_cap, DOWN, buff=0.4)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.08) for m in extras], lag_ratio=0.2), run_time=0.9)
        self.next_slide()


class CoupledDecisions(DoraSlide):
    def construct(self):
        self.setup_slide("Last mile is many decisions")
        specs = [
            ("Sectorization", "weeks"),
            ("SPP", "hours"),
            ("VDP", "hours"),
            ("Optimizer", "hours"),
            ("Execution", "minutes"),
            ("Trajectories", "after"),
        ]
        nodes = [node_box(name, when, width=2.05, height=1.2) for name, when in specs]
        row = VGroup(*nodes).arrange(RIGHT, buff=0.22)
        row.move_to(UP * 0.35)
        arrows = VGroup()
        for a, b in zip(nodes, nodes[1:]):
            arrows.add(
                Arrow(
                    a.get_right(),
                    b.get_left(),
                    buff=0.04,
                    stroke_width=2.5,
                    color=LINE,
                    max_tip_length_to_length_ratio=0.28,
                )
            )
        note = caption("Different owners. Different information. Different uncertainty.").next_to(row, DOWN, buff=0.7)
        self.play(LaggedStart(*[appear(n) for n in nodes], lag_ratio=0.08), FadeIn(arrows), run_time=1.0)
        self.play(FadeIn(note), run_time=0.4)
        self.next_slide()

        roles = [
            "Which area belongs together?",
            "Where can the vehicle stop?",
            "How long will visits take?",
            "How do we build the tour?",
            "What does the carrier do now?",
            "What actually happened?",
        ]
        prompt = txt(roles[0], size=26, color=DECISION)
        prompt.next_to(note, DOWN, buff=0.45)
        for i, role in enumerate(roles):
            anims = []
            for j, node in enumerate(nodes):
                target = DECISION if j == i else CARD_STROKE
                width = 3.5 if j == i else 2.0
                anims.append(node[0].animate.set_stroke(target, width=width))
            nxt = txt(role, size=26, color=DECISION).move_to(prompt)
            self.play(*anims, Transform(prompt, nxt), run_time=0.45)
            self.next_slide()


class PowellFive(DoraSlide):
    def construct(self):
        self.setup_slide("A delivery day in five pieces", cite=True)
        items = [
            (r"S_t", "State", ["orders · housekeys", "vehicles · time windows", "stop graph"], STATE),
            (r"x_t", "Decision", ["stops · grouping", "sequence · sector", "the plan we send"], DECISION),
            (r"W_{t+1}", "Uncertainty", ["traffic · parking", "absence · weather", "scans · behavior"], UNCERTAINTY),
            (r"S_{t+1}", "New state", ["remaining work", "delay", "completed deliveries"], OK),
        ]
        boxes = []
        for sym, name, body_lines, accent in items:
            box = card(3.05, 2.55, accent=accent)
            s = MathTex(sym, color=accent, font_size=40)
            n = txt(name, size=20, weight="BOLD", color=INK)
            b = VGroup(*[txt(line, size=14, color=MUTE) for line in body_lines]).arrange(DOWN, buff=0.06)
            inner = VGroup(s, n, b).arrange(DOWN, buff=0.14)
            inner.move_to(box)
            boxes.append(VGroup(box, inner))
        row = VGroup(*boxes).arrange(RIGHT, buff=0.22)
        row.move_to(UP * 0.25)

        arrows = VGroup()
        for a, b in zip(boxes, boxes[1:]):
            arrows.add(
                Arrow(
                    a.get_right(),
                    b.get_left(),
                    buff=0.02,
                    stroke_width=2.5,
                    color=MUTE,
                    max_tip_length_to_length_ratio=0.35,
                )
            )

        self.play(appear(boxes[0]), run_time=0.5)
        self.next_slide()
        self.play(Create(arrows[0]), appear(boxes[1]), run_time=0.5)
        self.next_slide()
        self.play(Create(arrows[1]), appear(boxes[2]), run_time=0.5)
        self.next_slide()
        self.play(Create(arrows[2]), appear(boxes[3]), run_time=0.5)
        self.next_slide()

        obj = VGroup(
            card(12.8, 0.85, accent=DECISION),
            txt("Objective  —  what “good” means:  cost · time · SLA · workload · customer quality", size=20, color=INK),
        )
        obj[1].move_to(obj[0])
        obj.next_to(row, DOWN, buff=0.38)
        self.play(appear(obj), run_time=0.5)
        self.next_slide()

        formula = MathTex(
            r"S_t \;\rightarrow\; x_t \;\rightarrow\; W_{t+1} \;\rightarrow\; S_{t+1}",
            color=INK,
            font_size=40,
        )
        policy = MathTex(r"x_t = X^{\pi}(S_t)", color=DECISION, font_size=38)
        maths = VGroup(formula, policy).arrange(DOWN, buff=0.35)
        maths.move_to(ORIGIN + DOWN * 0.1)
        self.play(FadeOut(VGroup(row, arrows, obj)), run_time=0.45)
        self.play(FadeIn(formula), run_time=0.5)
        self.play(FadeIn(policy), run_time=0.4)
        self.next_slide()


class OptimalVsRobust(DoraSlide):
    def construct(self):
        self.setup_slide("A plan can be optimal and fragile")
        det = MathTex(r"x^{\star} = \arg\min_{x}\,\hat{C}(x, S_t)", color=INK, font_size=40)
        det.to_edge(UP, buff=1.15)
        hint = caption("Best decision according to the model we have now.").next_to(det, DOWN, buff=0.2)
        self.play(Write(det), FadeIn(hint), run_time=0.8)
        self.next_slide()

        positions = {
            "Depot": LEFT * 4.4 + DOWN * 0.15,
            "A": LEFT * 1.7 + UP * 1.15,
            "B": RIGHT * 0.7 + UP * 1.25,
            "C": RIGHT * 3.6 + UP * 0.35,
            "D": LEFT * 1.5 + DOWN * 1.45,
            "E": RIGHT * 1.5 + DOWN * 1.35,
        }
        dots = {}
        labels = VGroup()
        for name, pos in positions.items():
            color = DECISION if name == "Depot" else INK
            d = Dot(pos, radius=0.11, color=color)
            lab = txt(name, size=16, color=MUTE).next_to(d, DOWN if name != "A" else UP, buff=0.12)
            dots[name] = d
            labels.add(lab)
        edges = VGroup(
            Line(positions["Depot"], positions["A"], color=LINE, stroke_width=2),
            Line(positions["Depot"], positions["D"], color=LINE, stroke_width=2),
            Line(positions["A"], positions["B"], color=LINE, stroke_width=2),
            Line(positions["B"], positions["C"], color=LINE, stroke_width=2),
            Line(positions["C"], positions["E"], color=LINE, stroke_width=2),
            Line(positions["D"], positions["E"], color=LINE, stroke_width=2),
            Line(positions["A"], positions["E"], color=LINE, stroke_width=2),
        )
        shift = DOWN * 0.45
        for name in positions:
            positions[name] = positions[name] + shift
        net = VGroup(edges, VGroup(*dots.values()), labels)
        net.shift(shift)
        self.play(FadeOut(hint), FadeIn(net), run_time=0.7)
        self.next_slide()

        route_a = ["Depot", "A", "B", "C", "E", "D"]
        path_a = VGroup(
            *[
                Line(positions[u], positions[v], color=OK, stroke_width=6)
                for u, v in zip(route_a, route_a[1:])
            ]
        )
        badge = pill("OPTIMAL  ·  6h 48m", accent=OK, width=3.4, height=0.55)
        badge.next_to(det, DOWN, buff=0.18)
        self.play(LaggedStart(*[Create(seg) for seg in path_a], lag_ratio=0.12), FadeIn(badge), run_time=1.1)
        self.next_slide()

        events = [
            ("Traffic on A → B", positions["A"], UNCERTAINTY),
            ("Parking at C blocked", positions["C"], UNCERTAINTY),
            ("Service +7 min", positions["E"], DECISION),
        ]
        chips = VGroup(*[pill(label, accent=color, width=3.4, height=0.46) for label, _, color in events])
        chips.arrange(RIGHT, buff=0.22)
        chips.to_edge(DOWN, buff=0.38)
        for chip, (_, pos, color) in zip(chips, events):
            self.play(
                FadeIn(chip, shift=UP * 0.1),
                Flash(Dot(pos, radius=0.01), color=color, flash_radius=0.45),
                run_time=0.55,
            )
            self.next_slide()

        path_b = VGroup(
            *[
                Line(positions[u], positions[v], color=DECISION, stroke_width=6)
                for u, v in zip(["Depot", "D", "E", "C", "B", "A"], ["D", "E", "C", "B", "A"])
            ]
        )
        new_badge = pill("NOW PREFERABLE  ·  Plan B", accent=DECISION, width=3.9, height=0.55)
        new_badge.move_to(badge)
        ineq = MathTex(r"S_t \neq S_{t+1}", color=UNCERTAINTY, font_size=36)
        ineq.next_to(new_badge, DOWN, buff=0.15)
        self.play(
            path_a.animate.set_stroke(opacity=0.25, width=3),
            Create(path_b),
            ReplacementTransform(badge, new_badge),
            FadeIn(ineq),
            run_time=0.9,
        )
        self.next_slide()

        self.play(*[FadeOut(m) for m in [net, path_a, path_b, chips, new_badge, ineq, det]], run_time=0.45)
        old_q = txt("What is the optimal solution?", size=32, color=MUTE)
        new_q = txt("What policy performs as reality unfolds?", size=34, color=DECISION, weight="BOLD")
        qs = VGroup(old_q, new_q).arrange(DOWN, buff=0.4)
        pol = MathTex(
            r"\min_{\pi}\ \mathbb{E}\big[C(S_t, X^{\pi}(S_t), W_{t+1})\big]",
            color=INK,
            font_size=38,
        )
        pol.next_to(qs, DOWN, buff=0.55)
        self.play(FadeIn(old_q), run_time=0.4)
        self.next_slide()
        self.play(FadeIn(new_q), Write(pol), run_time=0.8)
        self.next_slide()


class SPPPipeline(DoraSlide):
    def construct(self):
        self.setup_slide("Stopping points are not one decision")

        def _dots(n=12, seed=3):
            rng_x = [ -0.9, -0.4, 0.2, 0.7, -0.6, 0.1, 0.8, -0.2, 0.45, -0.75, 0.3, 0.0 ]
            rng_y = [ 0.35, -0.2, 0.4, 0.05, 0.15, -0.35, 0.3, 0.25, -0.15, -0.3, 0.0, 0.2 ]
            g = VGroup(*[Dot([rng_x[i], rng_y[i], 0], radius=0.05, color=STATE) for i in range(n)])
            return g

        traj_box = card(2.7, 1.7, accent=STATE)
        traj_dots = _dots().scale(0.85).move_to(traj_box)
        traj_lab = txt("TRAJECTORIES", size=14, color=MUTE).next_to(traj_box, DOWN, buff=0.12)
        traj = VGroup(traj_box, traj_dots, traj_lab)

        stops = VGroup(*[Dot(ORIGIN, radius=0.09, color=DECISION) for _ in range(4)])
        stops.arrange_in_grid(2, 2, buff=0.35)
        gb_box = card(2.7, 1.7, accent=LINE)
        stops.move_to(gb_box)
        gb_lab = txt("GRAPH BUILDER", size=14, color=MUTE).next_to(gb_box, DOWN, buff=0.12)
        graph_builder = VGroup(gb_box, stops, gb_lab)

        houses = VGroup(*[Square(0.18, color=MUTE, fill_opacity=0.2) for _ in range(6)]).arrange_in_grid(2, 3, buff=0.18)
        stop_nodes = VGroup(*[Dot(ORIGIN, radius=0.08, color=DECISION) for _ in range(3)]).arrange(RIGHT, buff=0.35)
        bip = VGroup(houses, stop_nodes).arrange(DOWN, buff=0.28)
        links = VGroup(
            Line(houses[0].get_bottom(), stop_nodes[0].get_top(), color=LINE, stroke_width=1.5),
            Line(houses[1].get_bottom(), stop_nodes[0].get_top(), color=LINE, stroke_width=1.5),
            Line(houses[2].get_bottom(), stop_nodes[1].get_top(), color=LINE, stroke_width=1.5),
            Line(houses[3].get_bottom(), stop_nodes[1].get_top(), color=LINE, stroke_width=1.5),
            Line(houses[4].get_bottom(), stop_nodes[2].get_top(), color=LINE, stroke_width=1.5),
            Line(houses[5].get_bottom(), stop_nodes[2].get_top(), color=LINE, stroke_width=1.5),
        )
        gbox = card(2.7, 1.7, accent=LINE)
        bip_all = VGroup(houses, stop_nodes, links)
        bip_all.move_to(gbox)
        glab = txt("STOP GRAPH", size=14, color=MUTE).next_to(gbox, DOWN, buff=0.12)
        graph = VGroup(gbox, bip_all, glab)

        stage1 = VGroup(traj, graph_builder, graph).arrange(RIGHT, buff=0.35)
        stage1.move_to(UP * 1.15)
        self.play(appear(traj), run_time=0.5)
        self.next_slide()
        self.play(appear(graph_builder), run_time=0.5)
        self.next_slide()
        self.play(appear(graph), run_time=0.5)
        self.next_slide()

        demand = VGroup(*[Square(0.22, color=INK, fill_opacity=0.15) for _ in range(4)]).arrange(RIGHT, buff=0.18)
        dbox = card(2.7, 1.45, accent=LINE)
        demand.move_to(dbox)
        dlab = txt("TODAY'S DEMAND", size=14, color=MUTE).next_to(dbox, DOWN, buff=0.1)
        demand_g = VGroup(dbox, demand, dlab)

        rec_box = card(2.7, 1.45, accent=DECISION)
        rec_stops = VGroup(*[Dot(ORIGIN, radius=0.1, color=DECISION) for _ in range(2)]).arrange(RIGHT, buff=0.55)
        rec_stops.move_to(rec_box)
        rec_lab = txt("SPP RECOMMENDER", size=14, color=DECISION).next_to(rec_box, DOWN, buff=0.1)
        rec = VGroup(rec_box, rec_stops, rec_lab)

        opt_box = card(2.7, 1.45, accent=OK)
        p1 = Dot(LEFT * 0.55, radius=0.1, color=OK)
        p2 = Dot(ORIGIN, radius=0.1, color=OK)
        p3 = Dot(RIGHT * 0.55, radius=0.1, color=OK)
        opt_path = VGroup(Line(p1.get_center(), p2.get_center(), color=OK, stroke_width=3), Line(p2.get_center(), p3.get_center(), color=OK, stroke_width=3), p1, p2, p3)
        opt_path.move_to(opt_box)
        opt_lab = txt("OPTIMIZER", size=14, color=OK).next_to(opt_box, DOWN, buff=0.1)
        opt = VGroup(opt_box, opt_path, opt_lab)

        stage2 = VGroup(demand_g, rec, opt).arrange(RIGHT, buff=0.35)
        stage2.move_to(DOWN * 1.05)
        self.play(appear(demand_g), appear(rec), run_time=0.6)
        self.next_slide()
        self.play(appear(opt), run_time=0.5)
        self.next_slide()

        roles = txt(
            "Graph Builder: knowledge     VDP: estimates     SPP: a decision     Optimizer: another decision",
            size=18,
            color=INK,
        )
        roles.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(roles), run_time=0.5)
        self.next_slide()


class Counterfactual(DoraSlide):
    def construct(self):
        self.setup_slide("Only one plan is executed")
        state = node_box("Same operational state", "S_t   ·   orders, workforce, geography, commitments", width=7.2, height=1.15, accent=STATE)
        state.to_edge(UP, buff=1.15)
        self.play(appear(state), run_time=0.5)
        self.next_slide()

        tourpla = labeled_card("TOURPLA", ["Plan A", "9 tours", "predicted 6.8% fewer hours"], width=4.5, height=2.15, accent=DECISION, title_color=DECISION)
        pladato = labeled_card("PLADATO", ["Plan B", "10 tours", "legacy planning policy"], width=4.5, height=2.15, accent=LINE)
        policies = VGroup(tourpla, pladato).arrange(RIGHT, buff=0.7)
        policies.next_to(state, DOWN, buff=0.45)
        fork_l = Arrow(state.get_bottom() + LEFT * 1.6, tourpla.get_top(), buff=0.08, color=MUTE, stroke_width=2.5, max_tip_length_to_length_ratio=0.12)
        fork_r = Arrow(state.get_bottom() + RIGHT * 1.6, pladato.get_top(), buff=0.08, color=MUTE, stroke_width=2.5, max_tip_length_to_length_ratio=0.12)
        self.play(Create(fork_l), Create(fork_r), appear(tourpla), appear(pladato), run_time=0.7)
        self.next_slide()

        obs = pill("EXECUTED   ·   Y_A observed", accent=OK, width=4.5, height=0.55)
        cf = pill("NOT EXECUTED   ·   Y_B  ?", accent=UNCERTAINTY, width=4.6, height=0.55)
        obs.next_to(tourpla, DOWN, buff=0.28)
        cf.next_to(pladato, DOWN, buff=0.28)
        self.play(appear(obs), run_time=0.45)
        self.play(FadeIn(cf, run_time=0.45))
        self.next_slide()

        ask = txt("“TOURPLA is better” is a counterfactual claim.", size=24, color=DECISION)
        ask.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(ask), run_time=0.5)
        self.next_slide()


class MetricLayers(DoraSlide):
    def construct(self):
        self.setup_slide("Not every metric answers the same question")
        layers = [
            ("Business outcomes", "cost · reliability · SLA · workforce · customer", DECISION),
            ("Operational outcomes", "driving · walking · service · overtime · failures", OK),
            ("Plan characteristics", "tours · stops · balance · feasibility · planned hours", STATE),
            ("Model / data diagnostics", "VDP error · graph support · GPS coverage · completeness", MUTE),
        ]
        blocks = []
        for title, body, accent in layers:
            box = card(11.6, 0.95, accent=accent)
            t = txt(title, size=22, weight="BOLD", color=INK)
            b = txt(body, size=16, color=MUTE)
            lab = VGroup(t, b).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            lab.next_to(box.get_left(), RIGHT, buff=0.32)
            blocks.append(VGroup(box, lab))
        stack = VGroup(*blocks).arrange(DOWN, buff=0.16)
        stack.move_to(DOWN * 0.15)
        for block in reversed(blocks):
            self.play(appear(block), run_time=0.4)
            self.next_slide()
        punch = txt("Prediction accuracy is not operational impact.", size=24, color=DECISION)
        punch.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(punch), run_time=0.45)
        self.next_slide()


class DecisionMap(DoraSlide):
    def construct(self):
        self.setup_slide("Products sit under decisions")
        decisions = [
            ("Which area?", "Sectorization"),
            ("Stop where?", "SPP"),
            ("How long?", "VDP"),
            ("Which tour?", "Optimizer"),
            ("What now?", "Carrier"),
            ("What learned?", "Trajectories"),
        ]
        cols = []
        for q, prod in decisions:
            qbox = node_box(q, width=2.05, height=1.05, accent=DECISION, title_color=DECISION)
            pbox = node_box(prod, width=2.05, height=0.85, accent=LINE)
            arrow = Arrow(qbox.get_bottom(), pbox.get_top(), buff=0.08, color=MUTE, stroke_width=2, max_tip_length_to_length_ratio=0.3)
            cols.append(VGroup(qbox, arrow, pbox).arrange(DOWN, buff=0.12))
        row = VGroup(*cols).arrange(RIGHT, buff=0.18)
        row.move_to(UP * 0.15)
        dash = pill("Leadership Dashboard measures arrows — it does not make the decision", accent=LINE, width=11.2, height=0.55)
        dash.next_to(row, DOWN, buff=0.55)
        self.play(LaggedStart(*[appear(c) for c in cols], lag_ratio=0.08), run_time=1.0)
        self.next_slide()
        self.play(appear(dash), run_time=0.5)
        self.next_slide()


class FiveQuestions(DoraSlide):
    def construct(self):
        self.setup_slide("Five questions for every initiative")
        questions = [
            "What decision are we improving?",
            "Who or what makes that decision?",
            "What information is available at decision time?",
            "What uncertainty appears after the decision?",
            "What metric proves the operation improved?",
        ]
        rows = VGroup()
        for i, q in enumerate(questions, start=1):
            num = txt(f"{i}", size=26, color=DECISION, weight="BOLD")
            num_box = card(0.55, 0.55, accent=DECISION)
            num.move_to(num_box)
            label = txt(q, size=24, color=INK)
            row = VGroup(VGroup(num_box, num), label).arrange(RIGHT, buff=0.28)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        rows.move_to(UP * 0.05)
        for row in rows:
            self.play(appear(row), run_time=0.4)
            self.next_slide()

        close = txt(
            "Technically impressive is not the same as making better decisions.",
            size=22,
            color=DECISION,
        )
        close.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(close), run_time=0.5)
        self.next_slide()


class BackupPolicies(DoraSlide):
    def construct(self):
        self.setup_slide("Backup  ·  four ways to make a decision")
        items = [
            ("PFA", "Use a rule", "If workload > X, split the tour."),
            ("CFA", "Optimize a designed cost", "Distance + θ walking + stop penalty."),
            ("VFA", "Value the leftover state", "A slightly worse stop can leave a better tour."),
            ("DLA", "Look ahead", "Simulate the next 90 minutes, then act."),
        ]
        cards = []
        for name, idea, example in items:
            box = card(5.8, 1.45, accent=LINE)
            n = txt(name, size=22, color=DECISION, weight="BOLD")
            i = txt(idea, size=20, color=INK)
            e = txt(example, size=16, color=MUTE)
            inner = VGroup(n, i, e).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            inner.next_to(box.get_left(), RIGHT, buff=0.28)
            cards.append(VGroup(box, inner))
        grid = VGroup(*cards).arrange_in_grid(2, 2, buff=0.28)
        grid.move_to(DOWN * 0.1)
        self.play(LaggedStart(*[appear(c) for c in cards], lag_ratio=0.12), run_time=0.9)
        note = caption("Useful later. Not required for today's discussion.").to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note), run_time=0.4)
        self.next_slide()
