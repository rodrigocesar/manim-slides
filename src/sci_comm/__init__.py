"""Reusable theme and components for scientific Manim Slides talks."""

from sci_comm.base import SciSlide
from sci_comm.components import (
    bullets,
    callout,
    colored_math,
    fade_in_each,
    make_text,
    two_column,
)
from sci_comm.theme import COLORS, FONT, SIZES, SPACING

__all__ = [
    "COLORS",
    "FONT",
    "SIZES",
    "SPACING",
    "SciSlide",
    "bullets",
    "callout",
    "colored_math",
    "fade_in_each",
    "make_text",
    "two_column",
]
