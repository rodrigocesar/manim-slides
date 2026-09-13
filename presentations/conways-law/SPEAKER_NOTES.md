# Speaker notes — Conway's Law at TPNG (~10–12 minutes)

Each `▸` is one click. Skip the beats marked **(shorten)** to land near 7 minutes.

Optional opening, before click one:

> We spend a lot of time designing software architecture. Boxes, APIs, services, data models. But there is another architecture that may be more important — and we almost never draw it.

Alternative:

> What if the architecture diagram of TPNG is not really designed in Confluence or code? What if we are designing it every time we decide who needs to talk to whom?

---

## 1. Why does architecture end up like this? — 1:00

**Purpose:** Create recognition before naming Conway.

**Core sentence:** The architecture we draw and the architecture we get are different — and we usually only tell the technical story of that gap.

**Talking points:**
- Start with a clean pipeline. This is the slide we put in Confluence.
- Nobody sat down and designed the tangle. Requirements changed, legacy accumulated, deadlines happened.
- Do not blame developers. The question is: what other force is shaping the system?

**Animation cues:**
- ▸ Clean chain: “This is the architecture we draw.”
- ▸ Dependencies appear: “This is the architecture we get.”
- ▸ *Why?* — hold. Then: “There is another force besides requirements and time.”

**Transition:** “To see it, we have to draw the organization — not the org chart, the communication graph.”

---

## 2. The invisible architecture — 1:15

**Purpose:** Let the audience watch software copy communication, then name Conway.

**Core sentence:** Cheap communication produces shared systems; expensive communication produces seams.

**Talking points:**
- Four people, everyone talks. Code flows into one shared component. That feels natural.
- Grow the org. Within-team talk stays cheap. Cross-team talk gets thinner and slower.
- Watch the software split at the same moment. Do not say “therefore microservices.”
- Only now: Melvin Conway, 1968. He was writing about any designed system.
- Compress to the motif we will reuse: **COMMUNICATION GRAPH → SOFTWARE GRAPH**.

**Animation cues:**
- ▸ Pulses, then code into one system.
- ▸ Split people and modules together. **(shorten:** let this play, do not linger)
- ▸ 1968 quote.
- ▸ The equation.

**Transition:** “Before we apply this to TPNG, one misunderstanding.”

---

## 3. Conway is not asking for microservices — 1:00

**Purpose:** Kill the usual misreading.

**Core sentence:** There is no universally correct shape. The danger is when the two graphs disagree.

**Talking points:**
- Organization A: one highly connected team → one modular application. Fine.
- Organization B: three teams, explicit contracts → three owned components. Also fine.
- Conway is not an argument for microservices. It is an argument for compatibility.
- Mismatch: two teams, one giant shared module and a shared database. Then Team A’s change lands in Team B’s pipeline. That is coordination, ownership, deployment, and semantic coupling — not a morality tale about monoliths.

**Animation cues:**
- ▸ Organization A.
- ▸ Organization B.
- ▸ Both get a check mark. “No universally correct shape.”
- ▸ “The danger is when the two graphs disagree.”
- ▸ Mismatch and friction. **(shorten:** one sentence over this beat)

**Transition:** “So what communication graph are we encoding into TPNG?”

---

## 4. TPNG: our communication graph — 1:00

**Purpose:** Make the room recognize itself.

**Core sentence:** The moment communication becomes expensive across a boundary, we tend to formalize it.

**Talking points:**
- DORA, Optimizer, Sectorization — plus the people who actually have to talk.
- Inside DORA, SPP already separates responsibilities: Graph Builder builds the stop graph from history; the Recommender uses that graph. That is a handoff, not a claim that Conway caused the split.
- When a change has to leave DORA for the Optimizer, we do not keep chatting forever. We write an API.
- Conversation becomes contract. That is neither good nor bad. It is what expensive communication looks like when we are being professional.

**Animation cues:**
- ▸ Teams and simplified internals.
- ▸ API lights up; a change crosses.
- ▸ conversation → interface → API contract.

**Transition:** “Here is a more precise TPNG example — not a full implementation story.”

---

## 5. Architecture inherits history — 1:15

**Purpose:** PlanningTask / adapter as ownership of a boundary.

**Core sentence:** Changing the communication boundary changes the software boundary.

**Talking points:**
- External Order arrived with Delivery / Transport / HomeCollection already baked in.
- Those distinctions travelled through DORA as `if/elif` and as `orderType`, `actionType`, `productCategory`.
- An integration model became an internal domain model. That is Conway in one refactor.
- The correction is organizational as well as technical: External API → Adapter → PlanningTask. External concepts stop at the adapter. DORA owns the rest.
- We are deciding which ideas belong to the contract between systems and which ideas DORA should own.
- Inverse Conway, in one line: we can choose the boundary instead of only inheriting it. Do not dwell on the term.

**Animation cues:**
- ▸ Order tree.
- ▸ Branches and leaking concepts.
- ▸ Adapter + PlanningTask; downstream collapses.
- ▸ The boundary sentence. **(shorten:** skip the Inverse Conway aside)

**Transition:** “That was the human communication graph. Then AI entered it.”

---

## 6. Then AI enters the organization — 1:00

**Purpose:** Pivot. AI does not repeal Conway. It changes the graph.

**Core sentence:** Code got cheaper. Shared understanding did not automatically get cheaper.

**Talking points:**
- Same four people. Normal pulses.
- An agent beside each person. Developer–agent edges get very busy.
- Some human–human edges fade. Not all. Substitution at the margin — Copilot, agents, private chats.
- Software side looks great at first: more modules, more PRs, more tests, more helpers.
- Hold the question. Do not answer it yet.

**Animation cues:**
- ▸ Human graph.
- ▸ Agents, busy edges, fading human talk.
- ▸ Code becomes cheap.
- ▸ “Did shared understanding become cheaper too?” — pause.

**Transition:** “Here is the updated picture.”

---

## 7. The new Conway graph — 1:30

**Purpose:** The intellectual contribution of the talk.

**Core sentence:** Software mirrors not only who talks to whom, but who shares context with whom.

**Talking points:**
- Classical: humans talk; software follows.
- Agentic: humans still talk, but both of them also talk to agents. Shared context is a question mark.
- Private configuration: A↔Agent A, B↔Agent B, C↔Agent C. Strong verticals, weak horizontals.
- Same phrase — Stopping Point — three interpretations: parking location, logical order group, optimizer entity. They collide in one object.
- Synthetic loop: assumption → prompt → generated code → AI review → same assumption. Fast, fluent, and closed.
- Human collaboration is inefficient in a useful way. Another person contains a different model. Their “Wait…” is information.
- Extended formula: human graph + agent graph + shared context graph → software graph.

**Animation cues:**
- ▸ Classical stack.
- ▸ Agentic stack.
- ▸ Private pairs and colliding definitions.
- ▸ Synthetic loop.
- ▸ “Wait…” interrupts.
- ▸ Extended formula + key sentence. **(shorten:** jump from private pairs to the formula)

**Transition:** “If that still feels abstract, here is the same failure in a pull request.”

---

## 8. The 15,000-line PR problem — 0:45

**Purpose:** Make the failure mode visceral. Slightly funny, then serious.

**Core sentence:** Code can cross a boundary while understanding does not.

**Talking points:**
- Developer A and Agent A grow a PR that is taller than Developer B.
- B hands it to Agent B. “Looks good to me.” Let the laugh happen.
- Then drop the joke. What disappeared: architectural reasoning, shared vocabulary, why the change exists, mental model transfer.
- Do not say AI review is bad. The failure is when machine review substitutes for an independent feedback loop.

**Animation cues:**
- ▸ PR grows and moves to B.
- ▸ Scan, then LGTM.
- ▸ Missing understanding; empty human edge.

**Transition:** “TPNG is not starting from zero here.”

---

## 9. TPNG already has part of the answer — 1:00

**Purpose:** Isolated agents → shared, versioned context. Constructive, not a tools pitch.

**Core sentence:** Shared AI context is infrastructure for keeping agents inside the team’s conversation.

**Talking points:**
- Today many of us have a private prompt, a private chat, a private `AGENTS.md`.
- Pull those artifacts into a shared place: skills, ADRs, API specs, Confluence, Jira, tests, domain vocabulary.
- MCP to code, Confluence, Jira, GitHub is how agents reach that place — the Copilot / skills direction we already have.
- Keep the human–human edges visible. Shared context does not replace talking.
- `tourpla-skills` and `SKILL.md` in version control: private prompt → reviewed artifact → team context.

**Animation cues:**
- ▸ Isolated pairs and private files.
- ▸ Files converge; MCP spokes; human edges stay.
- ▸ `tourpla-skills` and the two sentences.

**Transition:** “So what do we actually design, if we take this seriously?”

---

## 10. Design the conversations — 1:15

**Purpose:** Four mechanisms, not ten best practices.

**Core sentence:** If software copies the communication graph, we should design that graph on purpose.

**Talking points:**
1. Model together. Shared architecture before generated code.
2. Make boundaries explicit. Ownership, contracts, vocabulary.
3. Version-control agent context. Private instructions become shared infrastructure.
4. Preserve independent feedback. Tests, production, metrics, operations, other teams. Reality must be able to disagree with the agent.

**Animation cues:**
- ▸ The motif returns.
- ▸ Mechanism 1. **(shorten:** say 2–4 over the remaining clicks without pausing)
- ▸ Mechanism 2.
- ▸ Mechanism 3.
- ▸ Mechanism 4.

**Transition:** Close. Do not add a thank-you.

---

## 11. Who is in our conversation? — 0:45

**Purpose:** Leave a question, not a slogan.

**Core sentence:** Conway still holds. Some of the conversations that shape the system are now with machines, and some of them nobody else can see.

**Talking points:**
- “Your software mirrors your conversations.” Hold.
- “Now some of those conversations are with machines.” Hold.
- Replace both: **WHO IS IN OUR CONVERSATION?** And who is missing?
- Three reflections, one at a time. Stop after the third.

Optional spoken close:

> Conway’s Law says our systems inherit our communication structure. Agentic development doesn’t remove that constraint. It gives us a second communication network — one that can be faster, more private, and much harder to see. So if we want better architecture, maybe the question isn’t only what should we build. It is: what conversations must exist for that architecture to survive?

**Animation cues:**
- ▸ First line.
- ▸ Second line.
- ▸ The question.
- ▸ Q1, Q2, Q3.

**End there.**
