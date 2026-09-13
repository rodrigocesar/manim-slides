"""Dark 3Blue1Brown-style palette and typography defaults."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    bg: str = "#0E0E10"
    fg: str = "#ECE7E1"
    muted: str = "#8A8580"
    yellow: str = "#FFFF00"
    gold: str = "#F0AC5F"
    blue: str = "#58C4DD"
    teal: str = "#5CD0B3"
    green: str = "#83C167"
    red: str = "#FC6255"
    orange: str = "#E07A3D"
    purple: str = "#9A72AC"
    gray: str = "#888888"


@dataclass(frozen=True)
class Sizes:
    display: int = 56
    title: int = 42
    body: int = 28
    small: int = 20
    footer: int = 16


@dataclass(frozen=True)
class Spacing:
    margin: float = 0.48
    chrome_top: float = 0.30
    chrome_bottom: float = 0.22
    stack: float = 0.32
    bullet: float = 0.28


COLORS = Colors()
SIZES = Sizes()
SPACING = Spacing()

DEFAULT_AUTHOR = "Rodrigo Cesar"
