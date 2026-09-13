# Are we making better decisions?

A 15-minute [Manim Slides](https://manim-slides.eertmans.be/) talk for DORA, Sectorization and TPNG. It uses Warren Powell’s sequential-decision skeleton to ask whether last-mile products improve the *decisions* Swiss Post actually makes.

Shareable artifact: `dist/index.html` (RevealJS). Speaker script: [`SPEAKER_NOTES.md`](SPEAKER_NOTES.md).

## Setup

System packages already expected on this machine: FFmpeg, Cairo, Pango, TeX Live.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Render

Draft (fast, 480p):

```bash
./scripts/render.sh -ql
```

Final (1080p):

```bash
./scripts/render.sh -qh
```

Render a subset:

```bash
./scripts/render.sh -ql Title PowellFive OptimalVsRobust
```

## Present and share

Export the HTML deck (after a render):

```bash
./scripts/export_html.sh
```

`dist/index.html` plus `dist/index_assets/` is the shareable package. Open the HTML in a browser and use arrow keys or click to advance.

RevealJS is loaded from a CDN, so the machine viewing the deck needs internet. If you want a fully offline folder, re-run convert with `--offline` on a network that can reach `cdn.jsdelivr.net`.

To present from the Manim Slides player instead:

```bash
source .venv/bin/activate
manim-slides Title WhatDoesGoodMean OutputsAreNotDecisions CoupledDecisions \
  PowellFive OptimalVsRobust SPPPipeline Counterfactual MetricLayers \
  DecisionMap FiveQuestions
```

`BackupPolicies` is omitted from the HTML export on purpose. Render it and add it to the present command only if you want the four policy classes in Q&A.

## Scene list

| Scene | Idea |
|---|---|
| `Title` | Are we making better decisions? |
| `WhatDoesGoodMean` | PLADATO vs TOURPLA: conflicting wins |
| `OutputsAreNotDecisions` | Artifacts vs decisions |
| `CoupledDecisions` | Many last-mile decisions, many timescales |
| `PowellFive` | \(S_t \to x_t \to W_{t+1} \to S_{t+1}\) |
| `OptimalVsRobust` | Deterministic optimum vs a policy under uncertainty |
| `SPPPipeline` | Graph Builder ≠ Recommender ≠ Optimizer |
| `Counterfactual` | Only one plan is executed |
| `MetricLayers` | Diagnostics ≠ impact |
| `DecisionMap` | Products sit under decisions |
| `FiveQuestions` | The ask for every initiative |
| `BackupPolicies` | PFA / CFA / VFA / DLA (skip in the talk) |

## Citation

Powell, W. B. (2022). *Reinforcement Learning and Stochastic Optimization: A Unified Framework for Sequential Decisions*. Wiley. CASTLE Lab, Princeton. https://warrenpowell.org/
