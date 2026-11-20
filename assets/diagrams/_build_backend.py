"""Backend lecture diagrams (PNG) light + dark."""
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


def box(d, xy, theme: Theme, fill=None, outline=None, width=2, radius=10):
    d.rounded_rectangle(
        xy,
        radius=radius,
        fill=fill if fill is not None else theme.fill,
        outline=outline if outline is not None else theme.ink,
        width=width,
    )


def center_text(d, cx, cy, text, fnt, fill):
    tw = d.textlength(text, font=fnt)
    d.text((cx - tw / 2, cy - fnt.size / 2), text, fill=fill, font=fnt)


def save(name, img, theme: Theme):
    path = OUT / themed_name(name, theme)
    img.save(path, optimize=True)
    print("wrote", path.name)


def diagram_spring_layers(theme: Theme):
    img, d = canvas(860, 360, theme)
    d.text((PAD, PAD), "계층: 요청 · 규칙 · 저장", fill=theme.ink, font=F_TITLE)
    cols = [
        (PAD, "Controller", "요청·응답", theme.soft),
        (310, "Service", "업무 규칙", theme.highlight),
        (560, "Repository", "저장", theme.fill),
    ]
    for x, title, desc, fill in cols:
        box(d, (x, 120, x + 220, 250), theme, fill=fill)
        center_text(d, x + 110, 165, title, F_BODY, theme.ink)
        center_text(d, x + 110, 205, desc, F_SMALL, theme.muted)
    for x in (270, 530):
        d.line((x, 185, x + 30, 185), fill=theme.ink, width=2)
        d.polygon([(x + 30, 185), (x + 18, 179), (x + 18, 191)], fill=theme.ink)
    d.text((PAD, 290), "한쪽 변화가 전체에 덜 번지게", fill=theme.accent, font=F_HINT)
    save("spring-layers.png", img, theme)


def diagram_spring_security(theme: Theme):
    img, d = canvas(900, 320, theme)
    d.text((PAD, PAD), "Spring Security: 필터 체인", fill=theme.ink, font=F_TITLE)
    steps = ["Filter", "Filter", "Auth", "Controller"]
    x0, y0, bw, bh = PAD, 130, 160, 70
    for i, label in enumerate(steps):
        x = x0 + i * (bw + 36)
        fill = theme.highlight if label == "Auth" else theme.fill
        box(d, (x, y0, x + bw, y0 + bh), theme, fill=fill)
        center_text(d, x + bw / 2, y0 + bh / 2, label, F_BODY, theme.ink)
        if i < len(steps) - 1:
            d.line((x + bw + 4, y0 + bh / 2, x + bw + 32, y0 + bh / 2), fill=theme.ink, width=2)
            d.polygon(
                [(x + bw + 32, y0 + bh / 2), (x + bw + 20, y0 + bh / 2 - 6), (x + bw + 20, y0 + bh / 2 + 6)],
                fill=theme.ink,
            )
    d.text((PAD, 240), "통과해야 컨트롤러에 도달", fill=theme.accent, font=F_HINT)
    save("spring-security-chain.png", img, theme)


def diagram_be_auth(theme: Theme):
    img, d = canvas(820, 300, theme)
    d.text((PAD, PAD), "인증 vs 인가", fill=theme.ink, font=F_TITLE)
    box(d, (PAD, 110, 360, 230), theme, fill=theme.soft)
    box(d, (430, 110, 760, 230), theme, fill=theme.highlight)
    center_text(d, 210, 150, "Authentication", F_BODY, theme.ink)
    center_text(d, 210, 185, "누구인가?", F_SMALL, theme.muted)
    center_text(d, 595, 150, "Authorization", F_BODY, theme.ink)
    center_text(d, 595, 185, "무엇을 해도 되는가?", F_SMALL, theme.muted)
    d.text((PAD, 255), "먼저 신원, 그다음 권한", fill=theme.accent, font=F_HINT)
    save("be-authn-authz.png", img, theme)


def diagram_nest_modules(theme: Theme):
    img, d = canvas(860, 360, theme)
    d.text((PAD, PAD), "Nest Module: imports / exports", fill=theme.ink, font=F_TITLE)
    box(d, (PAD, 120, 340, 280), theme, fill=theme.soft)
    box(d, (480, 120, 800, 280), theme, fill=theme.fill)
    center_text(d, 200, 155, "UsersModule", F_BODY, theme.ink)
    center_text(d, 200, 195, "providers", F_SMALL, theme.muted)
    center_text(d, 200, 225, "exports → UsersService", F_SMALL, theme.orange)
    center_text(d, 640, 155, "OrdersModule", F_BODY, theme.ink)
    center_text(d, 640, 195, "imports UsersModule", F_SMALL, theme.muted)
    center_text(d, 640, 225, "UsersService 사용", F_SMALL, theme.orange)
    d.line((340, 200, 480, 200), fill=theme.ink, width=2)
    d.polygon([(480, 200), (468, 194), (468, 206)], fill=theme.ink)
    d.text((PAD, 310), "공개한 것만 다른 모듈이 받는다", fill=theme.accent, font=F_HINT)
    save("nest-modules.png", img, theme)


def diagram_fastapi_deps(theme: Theme):
    img, d = canvas(860, 340, theme)
    d.text((PAD, PAD), "FastAPI: Depends 그래프", fill=theme.ink, font=F_TITLE)
    nodes = [
        (330, 100, 200, 54, "endpoint", theme.highlight),
        (120, 220, 200, 54, "get_current_user", theme.soft),
        (540, 220, 200, 54, "get_db", theme.fill),
    ]
    for x, y, w, h, label, fill in nodes:
        box(d, (x, y, x + w, y + h), theme, fill=fill)
        center_text(d, x + w / 2, y + h / 2, label, F_BODY, theme.ink)
    d.line((430, 154, 220, 220), fill=theme.ink, width=2)
    d.line((430, 154, 640, 220), fill=theme.ink, width=2)
    d.text((PAD, 295), "공유 로직을 의존성으로 끼운다", fill=theme.accent, font=F_HINT)
    save("fastapi-depends.png", img, theme)


def diagram_be_test_scope(theme: Theme):
    img, d = canvas(860, 320, theme)
    d.text((PAD, PAD), "테스트 범위", fill=theme.ink, font=F_TITLE)
    cols = [
        (PAD, "Unit", "단위만", theme.fill),
        (310, "Slice / Module", "한 계층", theme.soft),
        (560, "e2e / 통합", "앱 전체", theme.highlight),
    ]
    for x, title, desc, fill in cols:
        box(d, (x, 120, x + 220, 230), theme, fill=fill)
        center_text(d, x + 110, 160, title, F_BODY, theme.ink)
        center_text(d, x + 110, 200, desc, F_SMALL, theme.muted)
    d.text((PAD, 265), "범위가 클수록 비싸고 현실에 가깝다", fill=theme.accent, font=F_HINT)
    save("be-test-scope.png", img, theme)


ALL = [
    diagram_spring_layers,
    diagram_spring_security,
    diagram_be_auth,
    diagram_nest_modules,
    diagram_fastapi_deps,
    diagram_be_test_scope,
]


if __name__ == "__main__":
    for theme in THEMES:
        for fn in ALL:
            fn(theme)
    print("done")
