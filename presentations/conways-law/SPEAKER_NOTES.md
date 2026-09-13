# Speaker notes — Conway's Law at TPNG (~7 minutes)

Each `▸` is one click. Optional opening:

> We spend a lot of time drawing software architecture. There is another architecture we almost never draw: who talks to whom — including who talks to an agent.

---

## 1. Why does architecture end up like this? — 0:50

**Purpose:** Recognition before Conway.

**Core sentence:** The architecture we draw and the one we get are different, and the usual technical story is incomplete.

**Talking points:**
- This is the Confluence diagram.
- Nobody designed the tangle. Requirements, legacy, deadlines — and another force.
- Do not blame developers.

**Cues:** ▸ Clean chain. ▸ Tangle + *Why?*

**Transition:** “To see that force, draw the communication graph.”

---

## 2. The invisible architecture — 1:00

**Purpose:** Watch software copy talk, then name Conway.

**Core sentence:** Cheap communication produces shared systems; expensive communication produces seams.

**Talking points:**
- Four people, everyone talks, one shared component. Natural.
- Grow the org. Within-team talk stays cheap. Cross-team talk thins. Software splits with it.
- Conway, 1968. Not an argument for microservices. There is no universally correct shape. The danger is when the two graphs disagree.

**Cues:** ▸ Shared system. ▸ Split + equation.

**Transition:** “What graph are we encoding into TPNG?”

---

## 3. TPNG: our communication graph — 1:00

**Purpose:** The room recognizes itself.

**Core sentence:** When talk across a boundary gets expensive, we formalize it — and we can also choose that boundary.

**Talking points:**
- DORA, Optimizer, Sectorization. SPP already splits Graph Builder and Recommender. That is a handoff, not a claim Conway caused it.
- A change leaving DORA for the Optimizer becomes an API. Conversation becomes contract.
- PlanningTask is the same idea inward: external Order stops at an adapter. DORA owns the rest. Change the communication boundary, change the software boundary.

**Cues:** ▸ Teams and API. ▸ Contract + Adapter → PlanningTask.

**Transition:** “That was the human graph. Then AI entered it.”

---

## 4. Then AI enters — 1:00

**Purpose:** AI does not repeal Conway. It changes the graph.

**Core sentence:** Code got cheaper. Shared understanding did not automatically.

**Talking points:**
- Same people. Then an agent beside each of them.
- Developer–agent edges get busy. Some human edges fade. Substitution at the margin — not the death of collaboration.
- Hold the question.

**Cues:** ▸ Humans. ▸ Agents, cheaper code, the question.

**Transition:** “Here is the updated picture.”

---

## 5. Software mirrors who shares context — 1:20

**Purpose:** The thesis.

**Core sentence:** Software mirrors who shares context with whom — including conversations nobody else can see.

**Talking points:**
- Humans still talk. Both also talk to agents. Shared context is a question mark.
- Same phrase, Stopping Point: parking location, order group, optimizer entity. They collide.
- “Wait…” is useful inefficiency. Another person contains a different model.
- Human graph + agent graph + shared context graph → software graph.

**Cues:** ▸ Agentic stack. ▸ Collision + Wait. ▸ Formula.

**Transition:** “TPNG already has part of the answer.”

---

## 6. Design the shared context — 1:00

**Purpose:** Isolated agents → versioned team context. Three actions, not ten practices.

**Core sentence:** Shared AI context keeps agents inside the team’s conversation. It does not replace talking.

**Talking points:**
- Private prompts become `SKILL.md`, ADRs, API specs, tests — `tourpla-skills`.
- Keep the human–human edges.
- Model together before generated code. Version agent context. Let production, tests, and other teams disagree with the agent.

**Cues:** ▸ Private pairs. ▸ Shared repo + three actions.

**Transition:** Close.

---

## 7. Who is in our conversation? — 0:40

**Purpose:** Leave a question.

**Core sentence:** Conway still holds. Some of the conversations that shape the system are now with machines.

**Talking points:**
- Hold the two lines.
- **WHO IS IN OUR CONVERSATION?** And who is missing?
- Two reflections. Stop.

Optional close:

> Agentic development does not remove Conway’s constraint. It adds a second communication network — faster, more private, harder to see. If we want better architecture, the question is not only what to build. It is what conversations must exist for that architecture to survive.

**Cues:** ▸ Two sentences. ▸ Question + two reflections.

**End there.**
