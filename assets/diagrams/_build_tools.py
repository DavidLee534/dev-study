"""Tools / collaboration lecture diagrams."""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from _theme import THEMES, Theme, themed_name  # noqa: E402

OUT = Path(__file__).resolve().parent
PAD = 56


def font(size, bold=False):
    paths = [
        r"C:\Windows\Fonts\malgunbd.ttf" if bold else r"C:\Windows\Fonts\malgun.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for p in paths:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


F_TITLE = font(22, True)
F_BODY = font(16, True)
F_SMALL = font(14)
F_HINT = font(15)


def canvas(w, h, theme: Theme):
    img = Image.new("RGB", (w, h), theme.bg)
    return img, ImageDraw.Draw(img)


def box(d, xy, theme: Theme, fill=None, width=2, radius=10):
    d.rounded_rectangle(
        xy,
        radius=radius,
        fill=fill if fill is not None else theme.fill,
        outline=theme.ink,
        width=width,
    )


def center_text(d, cx, cy, text, fnt, fill):
    tw = d.textlength(text, font=fnt)
    d.text((cx - tw / 2, cy - fnt.size / 2), text, fill=fill, font=fnt)


def save(name, img, theme: Theme):
    path = OUT / themed_name(name, theme)
    img.save(path, optimize=True)
    print("wrote", path.name)


def diagram_git_areas(theme: Theme):
    img, d = canvas(900, 300, theme)
    d.text((PAD, PAD), "Git: 작업 · 스테이징 · 기록", fill=theme.ink, font=F_TITLE)
    cols = [
        (PAD, "Working", "고친 파일", theme.fill),
        (320, "Staging", "올릴 묶음", theme.soft),
        (580, "Commit", "스냅샷", theme.highlight),
    ]
    for x, title, desc, fill in cols:
        box(d, (x, 120, x + 240, 230), theme, fill=fill)
        center_text(d, x + 120, 155, title, F_BODY, theme.ink)
        center_text(d, x + 120, 195, desc, F_SMALL, theme.muted)
    for x in (290, 550):
        d.line((x, 175, x + 30, 175), fill=theme.ink, width=2)
        d.polygon([(x + 30, 175), (x + 18, 169), (x + 18, 181)], fill=theme.ink)
    d.text((PAD, 255), "add → commit", fill=theme.accent, font=F_HINT)
    save("tools-git-areas.png", img, theme)


def diagram_pr_flow(theme: Theme):
    img, d = canvas(900, 300, theme)
    d.text((PAD, PAD), "PR: 갈래 → 검토 → 합치기", fill=theme.ink, font=F_TITLE)
    steps = ["Branch", "PR", "Review", "Merge"]
    x0, y0, bw, bh = PAD, 120, 160, 70
    for i, label in enumerate(steps):
        x = x0 + i * (bw + 36)
        fill = theme.highlight if label == "Review" else theme.fill
        box(d, (x, y0, x + bw, y0 + bh), theme, fill=fill)
        center_text(d, x + bw / 2, y0 + bh / 2, label, F_BODY, theme.ink)
        if i < len(steps) - 1:
            d.line((x + bw + 4, y0 + bh / 2, x + bw + 32, y0 + bh / 2), fill=theme.ink, width=2)
            d.polygon(
                [(x + bw + 32, y0 + bh / 2), (x + bw + 20, y0 + bh / 2 - 6), (x + bw + 20, y0 + bh / 2 + 6)],
                fill=theme.ink,
            )
    d.text((PAD, 230), "혼자 합치지 않고 창구를 연다", fill=theme.accent, font=F_HINT)
    save("tools-pr-flow.png", img, theme)


def diagram_review(theme: Theme):
    img, d = canvas(820, 300, theme)
    d.text((PAD, PAD), "리뷰: 제안과 질문", fill=theme.ink, font=F_TITLE)
    box(d, (PAD, 110, 360, 230), theme, fill=theme.soft)
    box(d, (430, 110, 760, 230), theme, fill=theme.highlight)
    center_text(d, 210, 150, "Author", F_BODY, theme.ink)
    center_text(d, 210, 185, "설명·의도", F_SMALL, theme.muted)
    center_text(d, 595, 150, "Reviewer", F_BODY, theme.ink)
    center_text(d, 595, 185, "질문·제안", F_SMALL, theme.muted)
    d.text((PAD, 255), "비난이 아니라 다음 커밋을 돕는다", fill=theme.accent, font=F_HINT)
    save("tools-review.png", img, theme)


ALL = [diagram_git_areas, diagram_pr_flow, diagram_review]

if __name__ == "__main__":
    for theme in THEMES:
        for fn in ALL:
            fn(theme)
    print("done")
