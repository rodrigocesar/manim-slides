#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck disable=SC1091
source "${ROOT}/scripts/_talk.sh"
# shellcheck disable=SC1091
source "${ROOT}/.venv/bin/activate"

TALK_DIR="$(resolve_talk "${1:-}")"
shift
QUALITY="${1:--ql}"
if [[ "${QUALITY}" == -q* ]]; then
  shift || true
fi

mapfile -t SCENES < <(talk_scenes "${TALK_DIR}")
if [[ $# -gt 0 ]]; then
  SCENES=("$@")
fi

export PYTHONPATH="${ROOT}/shared${PYTHONPATH:+:${PYTHONPATH}}"
cd "${TALK_DIR}"
manim-slides render -- "${QUALITY}" --disable_caching -c "${ROOT}/manim.cfg" deck.py "${SCENES[@]}"
