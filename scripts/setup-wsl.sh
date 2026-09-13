#!/usr/bin/env bash
# Install Ubuntu/WSL system packages and the uv environment for this kit.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ "$(id -u)" -eq 0 ]]; then
  APT=(apt-get)
else
  APT=(sudo apt-get)
fi

echo "==> Installing Ubuntu packages for Manim (Cairo, Pango, FFmpeg, TeX)..."
"${APT[@]}" update
"${APT[@]}" install -y --no-install-recommends \
  build-essential \
  python3-dev \
  pkg-config \
  libcairo2-dev \
  libpango1.0-dev \
  ffmpeg \
  texlive \
  texlive-latex-extra \
  texlive-fonts-recommended \
  texlive-science \
  tipa \
  curl \
  ca-certificates

if ! command -v uv >/dev/null 2>&1; then
  echo "==> Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="${HOME}/.local/bin:${PATH}"
fi

echo "==> Syncing the Python environment..."
uv python install 3.12
uv sync

echo "==> Checking Manim..."
uv run manim checkhealth

echo
echo "Setup complete. From ${ROOT} you can render the demo with:"
echo "  uv run manim-slides render talks/demo/main.py Title Opening Idea Equation Outro"
echo "  uv run manim-slides present Title Opening Idea Equation Outro"
