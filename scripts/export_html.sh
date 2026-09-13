#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck disable=SC1091
source "${ROOT}/scripts/_talk.sh"
# shellcheck disable=SC1091
source "${ROOT}/.venv/bin/activate"

TALK_DIR="$(resolve_talk "${1:-}")"
TITLE="$(talk_title "${TALK_DIR}")"
mapfile -t SCENES < <(talk_scenes "${TALK_DIR}")

mkdir -p "${TALK_DIR}/dist"
export PYTHONPATH="${ROOT}/shared${PYTHONPATH:+:${PYTHONPATH}}"
cd "${TALK_DIR}"

manim-slides convert --to html --folder slides "${SCENES[@]}" dist/index.html \
  -c slide_number=true \
  -c reveal_theme=black \
  -c title="${TITLE}"

python "${ROOT}/scripts/patch_html.py" dist/index.html
