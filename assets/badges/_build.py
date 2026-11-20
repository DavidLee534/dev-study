"""Generate light/dark slate badge SVGs (sharp corners, profile-aligned)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent

# (filename_stem, left_label, right_text, right_fill_light)
BADGES = [
    ("study", "Repo", "Dev Study", "#EA580C"),
    ("notes", "Format", "Study Notes", "#334155"),
    ("concepts", "Focus", "Concepts First", "#2563EB"),
    ("java", "Lang", "Java", "#EA580C"),
    ("python", "Lang", "Python", "#16A34A"),
    ("cs", "Track", "Computer Science", "#334155"),
    ("chapter", "Type", "Lecture", "#EA580C"),
    ("ready", "Status", "Ready", "#16A34A"),
    ("outline", "Status", "Outline", "#64748B"),
    ("ch01", "Chapter", "01", "#0F172A"),
    ("ch02", "Chapter", "02", "#0F172A"),
    ("ch03", "Chapter", "03", "#0F172A"),
    ("ch04", "Chapter", "04", "#0F172A"),
    ("ch05", "Chapter", "05", "#0F172A"),
    ("ch06", "Chapter", "06", "#0F172A"),
    ("topic-ds", "Topic", "Data Structures", "#334155"),
    ("topic-algo", "Topic", "Algorithms", "#334155"),
]


def escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def measure(text: str, size=12) -> float:
    # rough width for Arial-ish sans
    return len(text) * (size * 0.62) + 16


def make_svg(left: str, right: str, right_fill: str, dark: bool = False) -> str:
    if dark:
        left_bg = "#1E293B"
        left_fg = "#E2E8F0"
        # brighten right fills slightly for dark
        right_map = {
            "#EA580C": "#FB923C",
            "#334155": "#64748B",
            "#2563EB": "#60A5FA",
            "#16A34A": "#4ADE80",
            "#64748B": "#94A3B8",
            "#0F172A": "#334155",
        }
        right_fill = right_map.get(right_fill, right_fill)
        right_fg = "#0B1220" if right_fill in ("#4ADE80", "#FB923C", "#60A5FA") else "#F8FAFC"
        if right_fill in ("#64748B", "#94A3B8", "#334155"):
            right_fg = "#F8FAFC"
    else:
        left_bg = "#0F172A"
        left_fg = "#F8FAFC"
        right_fg = "#FFFFFF" if right_fill != "#0F172A" else "#F8FAFC"
        if right_fill == "#0F172A":
            right_fill = "#334155"

    lw = max(measure(left), 52)
    rw = max(measure(right), 56)
    w = lw + rw
    h = 28
    left_e = escape(left)
    right_e = escape(right)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h}" role="img" aria-label="{left_e}: {right_e}">
  <title>{left_e}: {right_e}</title>
  <g shape-rendering="crispEdges">
    <rect x="0" y="0" width="{lw:.0f}" height="{h}" fill="{left_bg}"/>
    <rect x="{lw:.0f}" y="0" width="{rw:.0f}" height="{h}" fill="{right_fill}"/>
  </g>
  <g font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700">
    <text x="{lw/2:.1f}" y="18" fill="{left_fg}" text-anchor="middle">{left_e}</text>
    <text x="{lw + rw/2:.1f}" y="18" fill="{right_fg}" text-anchor="middle">{right_e}</text>
  </g>
</svg>
'''


def main():
    for stem, left, right, color in BADGES:
        light = OUT / f"{stem}.svg"
        dark = OUT / f"{stem}-dark.svg"
        light.write_text(make_svg(left, right, color, dark=False), encoding="utf-8")
        dark.write_text(make_svg(left, right, color, dark=True), encoding="utf-8")
        print("wrote", light.name, dark.name)


if __name__ == "__main__":
    main()
