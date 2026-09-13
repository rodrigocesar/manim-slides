#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
# shellcheck disable=SC1091
source .venv/bin/activate

QUALITY="${1:--ql}"
shift || true

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
  BackupPolicies
)

if [[ $# -gt 0 ]]; then
  SCENES=("$@")
fi

# Everything after -- is forwarded to Manim. manim-slides itself only accepts --CE/--GL.
manim-slides render -- "$QUALITY" --disable_caching src/deck.py "${SCENES[@]}"
