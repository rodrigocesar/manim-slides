#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
# shellcheck disable=SC1091
source .venv/bin/activate

mkdir -p dist

SCENES=(
  Title
  WhatDoesGoodMean
  OutputsAreNotDecisions
  CoupledDecisions
  PowellFive
  OptimalVsRobust
  SPPPipeline
  Counterfactual
  MetricLayers
  DecisionMap
  FiveQuestions
)

# --offline downloads RevealJS for air-gapped sharing; omit it if the CDN is blocked.
manim-slides convert --to html "${SCENES[@]}" dist/index.html \
  -c slide_number=true \
  -c reveal_theme=black \
  -c title="Are we making better decisions?"
