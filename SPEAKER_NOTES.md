# Speaker notes — 15 minutes

Use the right arrow (or click) at each `▸` beat. Total target: **14:00–14:30**, leaving a buffer.

---

## Title — 0:20

**Are we making better decisions?**

▸ After the title settles:

“This is a DORA and Sectorization conversation. I want to borrow Warren Powell’s sequential-decision framework from CASTLE Lab — not as a new algorithm, but as a way to talk about the last mile.”

---

## What does “good” mean? — 2:00

▸ Two plan cards appear.

“One difficulty we face is surprisingly basic. We build complex systems before we fully agree on what *good* means.”

“Here are two plans for the same day. PLADATO uses more tours, less driving, no overtime — and two late deliveries. TOURPLA uses fewer tours, more driving, some overtime — and no lates.”

▸ “fewer hours / fewer tours” captions.

“Each plan wins on something different. If we cannot say which of those outcomes we prefer, we cannot say which system is better.”

▸ **BETTER?**

“The real question is not whether the system produced a nicer output. It is whether it improved the decision that changed the operation.”

---

## Outputs are not decisions — 1:30

▸ DATA → MODEL → OUTPUT

“A common path: we gather data, we fit a model, we ship an output, then we look for a dashboard metric.”

▸ SITUATION → DECISION → OUTCOME

“Powell asks us to reverse that. Start from the situation, name the decision, then look at the outcome after reality arrives.”

▸ Three lines.

“A graph is not a decision. A VDP prediction is not a decision. A leadership dashboard is not a decision. They become valuable when they change what someone — or some policy — chooses.”

---

## Last mile is many decisions — 1:30

▸ The chain appears.

“National last-mile is not one giant state-to-decision problem. It is many coupled decisions at different timescales.”

▸ Sectorization: “Which area belongs together?”
▸ SPP: “Where can the vehicle stop?”
▸ VDP: “How long will visits take?” — *and notice: this may be an estimate used by other decisions, not a decision itself.*
▸ Optimizer: “How do we build the tour?”
▸ Execution: “What does the carrier do now?”
▸ Trajectories: “What actually happened?”

“Different owners. Different information. Different uncertainty. TPNG’s first question is: which of these are we actually trying to improve?”

---

## A delivery day in five pieces — 2:00

▸ \(S_t\) — “What we know now: orders, housekeys, vehicles, time windows, the stop graph.”
▸ \(x_t\) — “What we choose: stops, grouping, sequence, the plan we send.”
▸ \(W_{t+1}\) — “What arrives after we decide: traffic, parking, absence, weather, scans, carrier behavior.”
▸ \(S_{t+1}\) — “What the world becomes: remaining work, delay, completed deliveries.”
▸ Objective bar — “And separately: what *good* means. That is a business choice, not a solver default.”
▸ Equation — “The policy is the rule that maps the state we see to the decision we take: \(x_t = X^\pi(S_t)\). TOURPLA and PLADATO are two different policies on roughly the same state.”

---

## A plan can be optimal and fragile — 2:30

**This is the centerpiece. Slow down.**

▸ The deterministic formula.

“This is what we often optimize: estimated cost under the information and assumptions we have.”

▸ Network.

“A small delivery day. Depot, a handful of stops.”

▸ Green route, 6h 48m.

“The solver finds a clean optimum.”

▸ Traffic.
▸ Parking blocked.
▸ Service +7 minutes.

“Then the operational day arrives. None of this was in \(\hat C\).”

▸ Plan B becomes preferable. \(S_t \neq S_{t+1}\).

“The mathematically optimal plan can be operationally fragile.”

▸ “What is the optimal solution?”
▸ “What policy performs as reality unfolds?” plus the expectation.

“We do not only want the best plan for a deterministic model. We want a policy that repeatedly makes good decisions when demand, traffic, parking, execution and data quality are uncertain.”

---

## Stopping points are not one decision — 2:00

▸ Trajectories — “We observe what carriers actually did.”
▸ Graph Builder — “We learn feasible stopping alternatives. Data, not a recommendation.”
▸ Stop graph — “That becomes part of the information and action space for someone else.”
▸ Demand + Recommender — “SPP Recommender actually selects stopping points for today’s tasks. That *is* a decision.”
▸ Optimizer — “Sequencing is a later decision. SPP documentation already says it does not own that.”
▸ Role caption.

“Graph Builder improves knowledge. VDP improves our estimate of consequences. SPP makes a stopping-point decision. The optimizer makes a broader tour decision. Execution generates new evidence.”

“The interesting architectural question is not ‘should we merge SPP and the optimizer?’ It is: how much future decision quality do we lose by choosing stops without anticipating the sequence?”

---

## Only one plan is executed — 1:30

▸ Same \(S_t\).

“The Leadership Dashboard is where this becomes concrete. Same operational state.”

▸ Fork into TOURPLA and PLADATO.

“Two planning policies. We can compare the plans they produce.”

▸ \(Y_A\) observed, \(Y_B\) counterfactual.

“If TOURPLA is executed, PLADATO is not. So ‘TOURPLA was better’ is a counterfactual claim unless we design the comparison — same-input simulation, observational adjustment, or a controlled rollout.”

▸ Closing line.

“Do not attribute everything in the observed outcome to the planning algorithm. Traffic happened. The carrier may not have followed the plan.”

---

## Not every metric answers the same question — 1:15

Build from the bottom:

▸ Model / data diagnostics — “Is VDP accurate? Is the graph complete?”
▸ Plan characteristics — “How many tours? Is the plan feasible?”
▸ Operational outcomes — “What did the day actually cost in time?”
▸ Business outcomes — “Did we move cost, SLA, workforce, customer quality?”
▸ Punchline.

“A dashboard can go green because duration error improved while delivery hours did not. Leadership should see which layer they are looking at.”

---

## Products sit under decisions — 1:00

▸ Decision row, then products underneath.

“Do not start from the architecture. Start from the decisions, then hang SPP, VDP, Sectorization, the optimizer, trajectories and the dashboard underneath.”

▸ Dashboard pill.

“The dashboard measures arrows in this picture. It does not make the decision.”

---

## Five questions — 1:00

Read each as it appears.

1. What decision are we improving?
2. Who or what makes that decision?
3. What information is available at decision time?
4. What uncertainty appears after the decision?
5. What metric proves the operation improved?

▸ Final line.

“If we cannot answer these, we may still be building something technically impressive — but we may not yet know whether we are making better decisions.”

Stop. Let the room talk.

---

## Backup — four policy classes

Only if someone asks “so how should we decide?”

- **PFA** — a rule.
- **CFA** — an optimizer whose costs and constraints were engineered. SPP Recommender is probably here.
- **VFA** — value the leftover state.
- **DLA** — look ahead / simulate, then act.

Do not teach the taxonomy unless asked.
