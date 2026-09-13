# Speaker notes — Conway's Law (~12 minutes)

Each `▸` is one click.

---

## Title — 0:20

▸ After the title settles.

“This is a conversation about why our last-mile systems look the way they do — and whether that is a technical choice or an organizational one.”

---

## What Conway wrote — 1:30

▸ The sentence.

“Melvin Conway wrote this in 1968, in *How do committees invent?* He was talking about any designed system, not only software.”

▸ The citation.

“The important word is not ‘organization chart.’ It is communication structure.”

▸ *communication structure*

“Who can talk cheaply, how often, and with what shared language. That is what gets copied into the design.”

---

## The org chart becomes the architecture — 1:30

▸ Left: how we are organized.

“Suppose TPNG is staffed as SPP, VDP, Optimizer.”

▸ Right: what we ship.

“Then Conway predicts we will ship a stop graph, a duration model, and a tour planner — with seams between them.”

▸ Same shape.

“That is not automatically wrong. It is a prediction. The question is whether we chose those seams on purpose.”

---

## It is about who can talk — 1:30

▸ Three teams.

“Boxes on a slide are not the law. Talk is the law.”

▸ Solid link A–B.

“If two teams talk every day, their parts will integrate.”

▸ Dashed links to C, then the line.

“If another team is reached only by tickets, the system will grow an interface, a delay, and a local optimum. The system will integrate where we converse, and split where we don't.”

---

## Team seams become system interfaces — 1:30

▸ Two standups → an API / queue / file / ticket.

▸ Unclear owner → a gap nobody optimizes.

▸ Local metric → a locally good, globally fragile plan.

“This is the same discomfort we had with TOURPLA versus PLADATO, and with SPP then sequencing. The interface is often a team handoff wearing a technical name.”

---

## Look at last mile through Conway — 2:00

▸ The decision / product row.

“Hang the products under the decisions, as in the better-decisions talk.”

▸ SPP and Optimizer seam.

“If stopping points and sequencing are owned by different teams, Conway predicts we will optimize them separately — even if the best stop depends on the sequence.”

▸ Is the seam a good decision boundary?

“That is the useful question. Not ‘should we merge the repos?’”

---

## The inverse Conway maneuver — 1:30

▸ System copies today's teams.

“Left alone, the architecture will keep photocopying the current org.”

▸ Desired decisions shape the teams.

“The inverse move: decide the conversation you need, then staff so that conversation is cheap.”

▸ Three captions.

“Do not start from the product list. Start from the last-mile decisions. Then ask whether our teams can even have that conversation.”

---

## Questions for TPNG — 2:00

Read each as it appears.

1. Where does our architecture copy our org chart?
2. Which seams are intentional decision boundaries?
3. Which seams are just how we happened to staff the work?
4. If we wanted one last-mile decision system, who would need to talk?
5. What would we reorganize so the conversation becomes cheap?

▸ Closing line.

“Organize for the decisions. The system will follow.”
