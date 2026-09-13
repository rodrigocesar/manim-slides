"""Conway's Law, extended for agentic development at TPNG."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TALK = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "shared"))
sys.path.insert(0, str(TALK))

from scenes import agents, closing, conway, opening, solutions, tpng


class WhyArchitecture(opening.WhyArchitecture):
    pass


class InvisibleArchitecture(opening.InvisibleArchitecture):
    pass


class NotMicroservices(conway.NotMicroservices):
    pass


class TPNGGraph(tpng.TPNGGraph):
    pass


class PlanningTask(tpng.PlanningTask):
    pass


class AIEnters(agents.AIEnters):
    pass


class NewConwayGraph(agents.NewConwayGraph):
    pass


class HugePR(agents.HugePR):
    pass


class SharedContext(solutions.SharedContext):
    pass


class DesignConversations(solutions.DesignConversations):
    pass


class WhoIsInTheConversation(closing.WhoIsInTheConversation):
    pass
