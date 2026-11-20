"""Shared light/dark tokens for lecture diagrams and GIFs."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    name: str  # "" for light (default filenames), "dark" for *-dark.*
    bg: tuple
    ink: tuple
    muted: tuple
    fill: tuple
    line: tuple
    accent: tuple
    orange: tuple
    soft: tuple
    white: tuple  # text on orange / contrast
    highlight: tuple


LIGHT = Theme(
    name="",
    bg=(255, 255, 255),
    ink=(15, 23, 42),
    muted=(100, 116, 139),
    fill=(248, 250, 252),
    line=(203, 213, 225),
    accent=(51, 65, 85),
    orange=(234, 88, 12),
    soft=(238, 242, 255),
    white=(255, 255, 255),
    highlight=(254, 215, 170),
)

DARK = Theme(
    name="dark",
    bg=(11, 18, 32),
    ink=(226, 232, 240),
    muted=(148, 163, 184),
    fill=(30, 41, 59),
    line=(51, 65, 85),
    accent=(203, 213, 225),
    orange=(251, 146, 60),
    soft=(30, 41, 59),
    white=(15, 23, 42),
    highlight=(124, 45, 18),
)

THEMES = (LIGHT, DARK)


def themed_name(base: str, theme: Theme) -> str:
    """array-index.gif + dark -> array-index-dark.gif"""
    if not theme.name:
        return base
    if "." not in base:
        return f"{base}-{theme.name}"
    stem, ext = base.rsplit(".", 1)
    return f"{stem}-{theme.name}.{ext}"
