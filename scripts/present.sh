#!/usr/bin/env bash
# Serve a talk's HTML deck so RevealJS speaker view works (press S).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck disable=SC1091
source "${ROOT}/scripts/_talk.sh"

TALK_DIR="$(resolve_talk "${1:-}")"
PORT="${PORT:-8000}"
BIND="${BIND:-0.0.0.0}"
URL="http://127.0.0.1:${PORT}/"
DIST="${TALK_DIR}/dist"
NOTES="${TALK_DIR}/SPEAKER_NOTES.md"

if [[ ! -f "${DIST}/index.html" ]]; then
  echo "No exported deck at ${DIST}/index.html" >&2
  echo "Run: ./scripts/export_html.sh ${1}" >&2
  exit 1
fi

echo "Talk:          ${1}"
echo "Deck:          ${URL}"
echo "Speaker notes: ${NOTES}"
echo
echo "1. Keep SPEAKER_NOTES.md open on this machine (editor or second monitor)."
echo "2. Open ${URL} in a browser (audience / main screen)."
echo "3. Press S in that browser for RevealJS speaker view (timer + next slide)."
echo "4. Arrow keys or click advance. Space plays/pauses the current clip."
echo
echo "Serving ${DIST}  —  Ctrl+C to stop."
cd "${DIST}"
python3 -m http.server "${PORT}" --bind "${BIND}"
