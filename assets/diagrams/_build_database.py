"""Database lecture diagrams."""
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
        "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
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


def diagram_schema(theme: Theme):
    img, d = canvas(900, 300, theme)
    d.text((PAD, PAD), "스키마: 표와 관계", fill=theme.ink, font=F_TITLE)
    box(d, (PAD, 110, 300, 240), theme, fill=theme.soft)
    center_text(d, 178, 145, "users", F_BODY, theme.ink)
    center_text(d, 178, 180, "id PK", F_SMALL, theme.muted)
    center_text(d, 178, 210, "email", F_SMALL, theme.muted)
    box(d, (520, 110, 840, 240), theme, fill=theme.highlight)
    center_text(d, 680, 145, "orders", F_BODY, theme.ink)
    center_text(d, 680, 180, "id PK", F_SMALL, theme.muted)
    center_text(d, 680, 210, "user_id FK", F_SMALL, theme.muted)
    d.line((300, 175, 520, 175), fill=theme.ink, width=2)
    d.polygon([(520, 175), (508, 169), (508, 181)], fill=theme.ink)
    d.text((PAD, 260), "관계는 FK로 잇고, 질문은 조인으로 푼다", fill=theme.accent, font=F_HINT)
    save("database-schema.png", img, theme)


def diagram_index(theme: Theme):
    img, d = canvas(920, 300, theme)
    d.text((PAD, PAD), "인덱스: 찾아가는 길을 미리 만든다", fill=theme.ink, font=F_TITLE)
    cols = [
        (PAD, "Full scan", "표 전체", theme.fill),
        (320, "Index", "정렬된 단서", theme.soft),
        (580, "Row", "본문 접근", theme.highlight),
    ]
    for x, title, desc, fill in cols:
        box(d, (x, 110, x + 240, 230), theme, fill=fill)
        center_text(d, x + 120, 150, title, F_BODY, theme.ink)
        center_text(d, x + 120, 190, desc, F_SMALL, theme.muted)
    d.text((PAD, 255), "WHERE·JOIN·ORDER BY 패턴이 인덱스를 부른다", fill=theme.accent, font=F_HINT)
    save("database-index.png", img, theme)


def diagram_txn(theme: Theme):
    img, d = canvas(920, 320, theme)
    d.text((PAD, PAD), "트랜잭션: 묶어서 성공하거나 함께 되돌린다", fill=theme.ink, font=F_TITLE)
    # BEGIN → work → (COMMIT | ROLLBACK)
    box(d, (PAD, 140, 200, 210), theme, fill=theme.fill)
    center_text(d, 128, 175, "BEGIN", F_BODY, theme.ink)
    box(d, (260, 140, 420, 210), theme, fill=theme.soft)
    center_text(d, 340, 175, "work", F_BODY, theme.ink)
    box(d, (520, 100, 720, 160), theme, fill=theme.highlight)
    center_text(d, 620, 130, "COMMIT", F_BODY, theme.ink)
    box(d, (520, 190, 720, 250), theme, fill=theme.fill)
    center_text(d, 620, 220, "ROLLBACK", F_BODY, theme.ink)
    d.line((200, 175, 260, 175), fill=theme.ink, width=2)
    d.polygon([(260, 175), (248, 169), (248, 181)], fill=theme.ink)
    d.line((420, 175, 480, 175), fill=theme.ink, width=2)
    d.line((480, 175, 480, 130), fill=theme.ink, width=2)
    d.line((480, 175, 480, 220), fill=theme.ink, width=2)
    d.line((480, 130, 520, 130), fill=theme.ink, width=2)
    d.line((480, 220, 520, 220), fill=theme.ink, width=2)
    d.polygon([(520, 130), (508, 124), (508, 136)], fill=theme.ink)
    d.polygon([(520, 220), (508, 214), (508, 226)], fill=theme.ink)
    d.text((PAD, 275), "둘 중 하나. 경계는 보통 유스케이스(서비스 메서드)에 둔다", fill=theme.accent, font=F_HINT)
    save("database-txn.png", img, theme)


def diagram_cache(theme: Theme):
    img, d = canvas(900, 300, theme)
    d.text((PAD, PAD), "캐시와 DB: 역할을 나눈다", fill=theme.ink, font=F_TITLE)
    box(d, (PAD, 110, 300, 240), theme, fill=theme.fill)
    center_text(d, 178, 155, "App", F_BODY, theme.ink)
    box(d, (340, 110, 560, 240), theme, fill=theme.highlight)
    center_text(d, 450, 145, "Cache", F_BODY, theme.ink)
    center_text(d, 450, 185, "빠르고 휘발", F_SMALL, theme.muted)
    box(d, (600, 110, 840, 240), theme, fill=theme.soft)
    center_text(d, 720, 145, "DB", F_BODY, theme.ink)
    center_text(d, 720, 185, "진실의 원천", F_SMALL, theme.muted)
    d.line((300, 175, 340, 175), fill=theme.ink, width=2)
    d.line((560, 175, 600, 175), fill=theme.ink, width=2)
    d.polygon([(340, 175), (328, 169), (328, 181)], fill=theme.ink)
    d.polygon([(600, 175), (588, 169), (588, 181)], fill=theme.ink)
    d.text((PAD, 260), "캐시 히트 실패·만료 정책을 같이 설계한다", fill=theme.accent, font=F_HINT)
    save("database-cache.png", img, theme)


ALL = [diagram_schema, diagram_index, diagram_txn, diagram_cache]

if __name__ == "__main__":
    for theme in THEMES:
        for fn in ALL:
            fn(theme)
    print("done")
