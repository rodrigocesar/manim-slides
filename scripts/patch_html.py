#!/usr/bin/env python3
"""Harden the generated RevealJS deck and check that every video exists."""

from __future__ import annotations

import re
import sys
from pathlib import Path

UNSAFE = """        () => {
          var currentVideos = Reveal.getCurrentSlide().slideBackgroundContentElement.getElementsByTagName("video");
          if (currentVideos.length > 0) {
            if (currentVideos[0].paused == true) currentVideos[0].play();
            else currentVideos[0].pause();
          } else {
            Reveal.next();
          }
        }"""

SAFE = """        () => {
          var slide = Reveal.getCurrentSlide();
          var background = slide && slide.slideBackgroundContentElement;
          var currentVideos = background ? background.getElementsByTagName("video") : [];
          if (currentVideos.length > 0) {
            if (currentVideos[0].paused == true) currentVideos[0].play();
            else currentVideos[0].pause();
          } else {
            Reveal.next();
          }
        }"""


def main() -> int:
    html_path = Path(sys.argv[1] if len(sys.argv) > 1 else "dist/index.html")
    html = html_path.read_text(encoding="utf-8")

    if "slide && slide.slideBackgroundContentElement" not in html:
        if UNSAFE not in html:
            print(f"error: expected spacebar handler not found in {html_path}", file=sys.stderr)
            return 1
        html = html.replace(UNSAFE, SAFE)
        html_path.write_text(html, encoding="utf-8")
        print(f"patched spacebar handler in {html_path}")
    else:
        print(f"spacebar handler already safe in {html_path}")

    refs = re.findall(r'(?:src|data-background-video)="([^"]+\.mp4)"', html)
    missing = [ref for ref in refs if not (html_path.parent / ref).is_file()]
    if missing:
        print("error: HTML references videos that are not on disk:", file=sys.stderr)
        for ref in missing:
            print(f"  {ref}", file=sys.stderr)
        return 1
    print(f"ok: {len(refs)} video references exist next to {html_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
