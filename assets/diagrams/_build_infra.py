"""Infra / DevOps lecture diagrams."""
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


def diagram_edge(theme: Theme):
    img, d = canvas(920, 300, theme)
    d.text((PAD, PAD), "엣지: 요청이 앱에 닿기까지", fill=theme.ink, font=F_TITLE)
    steps = [
        ("Client", theme.fill),
        ("DNS", theme.fill),
        ("LB / Proxy", theme.soft),
        ("App", theme.highlight),
    ]
    x0, y0, bw, bh = PAD, 120, 160, 70
    for i, (label, fill) in enumerate(steps):
        x = x0 + i * (bw + 36)
        box(d, (x, y0, x + bw, y0 + bh), theme, fill=fill)
        center_text(d, x + bw / 2, y0 + bh / 2, label, F_BODY, theme.ink)
        if i < len(steps) - 1:
            d.line((x + bw + 4, y0 + bh / 2, x + bw + 32, y0 + bh / 2), fill=theme.ink, width=2)
            d.polygon(
                [(x + bw + 32, y0 + bh / 2), (x + bw + 20, y0 + bh / 2 - 6), (x + bw + 20, y0 + bh / 2 + 6)],
                fill=theme.ink,
            )
    d.text((PAD, 230), "이름 찾기 → 분배 → 앱 프로세스", fill=theme.accent, font=F_HINT)
    save("infra-edge.png", img, theme)


def diagram_docker(theme: Theme):
    img, d = canvas(900, 320, theme)
    d.text((PAD, PAD), "Docker: Image → Container", fill=theme.ink, font=F_TITLE)
    box(d, (PAD, 110, 360, 250), theme, fill=theme.soft)
    center_text(d, 208, 145, "Image", F_BODY, theme.ink)
    center_text(d, 208, 180, "불변 설계도", F_SMALL, theme.muted)
    center_text(d, 208, 210, "layers + config", F_SMALL, theme.muted)
    box(d, (480, 110, 840, 250), theme, fill=theme.highlight)
    center_text(d, 660, 145, "Container", F_BODY, theme.ink)
    center_text(d, 660, 180, "실행 중인 상자", F_SMALL, theme.muted)
    center_text(d, 660, 210, "process + mounts", F_SMALL, theme.muted)
    d.line((370, 180, 470, 180), fill=theme.ink, width=2)
    d.polygon([(470, 180), (458, 174), (458, 186)], fill=theme.ink)
    d.text((PAD, 275), "같은 이미지로 여러 컨테이너를 띄운다", fill=theme.accent, font=F_HINT)
    save("infra-docker.png", img, theme)


def diagram_k8s(theme: Theme):
    img, d = canvas(920, 340, theme)
    d.text((PAD, PAD), "Kubernetes: Deploy · Pod · Service", fill=theme.ink, font=F_TITLE)

    box(d, (PAD, 140, 220, 250), theme, fill=theme.fill)
    center_text(d, 138, 175, "Client", F_BODY, theme.ink)
    center_text(d, 138, 210, "traffic", F_SMALL, theme.muted)

    box(d, (300, 140, 540, 250), theme, fill=theme.highlight)
    center_text(d, 420, 175, "Service", F_BODY, theme.ink)
    center_text(d, 420, 210, "안정된 진입점", F_SMALL, theme.muted)

    box(d, (620, 100, 860, 280), theme, fill=theme.soft)
    center_text(d, 740, 130, "Deployment", F_BODY, theme.ink)
    center_text(d, 740, 165, "원하는 replica", F_SMALL, theme.muted)
    box(d, (670, 195, 810, 255), theme, fill=theme.fill)
    center_text(d, 740, 225, "Pods", F_BODY, theme.ink)

    # Client → Service → Pods
    d.line((220, 195, 290, 195), fill=theme.ink, width=2)
    d.polygon([(290, 195), (278, 189), (278, 201)], fill=theme.ink)
    d.line((540, 195, 610, 195), fill=theme.ink, width=2)
    d.polygon([(610, 195), (598, 189), (598, 201)], fill=theme.ink)
    d.text((PAD, 300), "Pod는 바뀌어도 Service 이름은 유지한다", fill=theme.accent, font=F_HINT)
    save("infra-k8s.png", img, theme)


def diagram_cicd(theme: Theme):
    img, d = canvas(920, 300, theme)
    d.text((PAD, PAD), "CI/CD: 검증 후 배포", fill=theme.ink, font=F_TITLE)
    steps = ["Commit", "Build", "Test", "Deploy"]
    x0, y0, bw, bh = PAD, 120, 160, 70
    for i, label in enumerate(steps):
        x = x0 + i * (bw + 36)
        fill = theme.highlight if label == "Test" else theme.fill
        box(d, (x, y0, x + bw, y0 + bh), theme, fill=fill)
        center_text(d, x + bw / 2, y0 + bh / 2, label, F_BODY, theme.ink)
        if i < len(steps) - 1:
            d.line((x + bw + 4, y0 + bh / 2, x + bw + 32, y0 + bh / 2), fill=theme.ink, width=2)
            d.polygon(
                [(x + bw + 32, y0 + bh / 2), (x + bw + 20, y0 + bh / 2 - 6), (x + bw + 20, y0 + bh / 2 + 6)],
                fill=theme.ink,
            )
    d.text((PAD, 230), "사람이 손으로 옮기지 않고 파이프라인이 옮긴다", fill=theme.accent, font=F_HINT)
    save("infra-cicd.png", img, theme)


def diagram_observe(theme: Theme):
    img, d = canvas(900, 300, theme)
    d.text((PAD, PAD), "관측: Logs · Metrics · Traces", fill=theme.ink, font=F_TITLE)
    cols = [
        (PAD, "Logs", "무슨 일이", theme.fill),
        (320, "Metrics", "얼마나", theme.soft),
        (580, "Traces", "어디를 지나", theme.highlight),
    ]
    for x, title, desc, fill in cols:
        box(d, (x, 110, x + 240, 230), theme, fill=fill)
        center_text(d, x + 120, 150, title, F_BODY, theme.ink)
        center_text(d, x + 120, 190, desc, F_SMALL, theme.muted)
    d.text((PAD, 255), "증상 → 범위 → 원인 순으로 좁힌다", fill=theme.accent, font=F_HINT)
    save("infra-observe.png", img, theme)


ALL = [diagram_edge, diagram_docker, diagram_k8s, diagram_cicd, diagram_observe]

if __name__ == "__main__":
    for theme in THEMES:
        for fn in ALL:
            fn(theme)
    print("done")
