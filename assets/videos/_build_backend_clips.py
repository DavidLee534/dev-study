"""Backend lecture GIFs light + dark."""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from _theme import THEMES, Theme, themed_name  # noqa: E402

OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)

W, H = 860, 420
PAD = 48


def font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\malgunbd.ttf" if bold else r"C:\Windows\Fonts\malgun.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


F18 = font(18, True)
F14 = font(14, True)
F13 = font(13)


def new_frame(theme: Theme):
    img = Image.new("RGB", (W, H), theme.bg)
    return img, ImageDraw.Draw(img)


def rounded(draw, xy, theme: Theme, fill=None, outline=None, width=2, radius=10):
    draw.rounded_rectangle(
        xy,
        radius=radius,
        fill=fill if fill is not None else theme.fill,
        outline=outline if outline is not None else theme.ink,
        width=width,
    )


def save_gif(name, frames, theme: Theme, duration=500, hold_ends_ms=1400):
    path = OUT / themed_name(name, theme)
    n = len(frames)
    if n <= 2:
        durations = [hold_ends_ms] * n
    else:
        durations = [duration] * n
        durations[0] = hold_ends_ms
        durations[-1] = hold_ends_ms
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=True,
    )
    print("wrote", path.name, f"({n} frames)")


def pipeline_clip(theme: Theme, name: str, title: str, steps: list[str]):
    frames = []
    bw, bh = 150, 64
    gap = 28
    total_w = len(steps) * bw + (len(steps) - 1) * gap
    x0 = (W - total_w) // 2
    y0 = 160

    for active in range(len(steps) + 1):
        img, d = new_frame(theme)
        d.text((PAD, PAD), title, fill=theme.ink, font=F18)
        for i, label in enumerate(steps):
            x = x0 + i * (bw + gap)
            fill = theme.orange if i < active else theme.fill
            color = theme.white if fill == theme.orange else theme.ink
            rounded(d, (x, y0, x + bw, y0 + bh), theme, fill=fill)
            tw = d.textlength(label, font=F14)
            d.text((x + (bw - tw) / 2, y0 + 22), label, fill=color, font=F14)
            if i < len(steps) - 1:
                d.line((x + bw + 4, y0 + bh / 2, x + bw + gap - 4, y0 + bh / 2), fill=theme.line, width=2)
        hint = "요청이 단계를 통과한다" if active == len(steps) else f"→ {steps[active]}" if active < len(steps) else ""
        if active == 0:
            hint = "요청 도착"
        d.text((PAD, H - PAD - 10), hint, fill=theme.accent, font=F13)
        frames.append(img)
        frames.append(img.copy())
    save_gif(name, frames, theme, duration=450)


def clip_spring_request(theme: Theme):
    pipeline_clip(
        theme,
        "spring-request.gif",
        "Spring: 요청 흐름",
        ["Filter", "Servlet", "Interceptor", "Controller"],
    )


def clip_nest_request(theme: Theme):
    pipeline_clip(
        theme,
        "nest-request.gif",
        "Nest: 요청 흐름",
        ["Middleware", "Guard", "Interceptor", "Pipe", "Controller"],
    )


def clip_fastapi_request(theme: Theme):
    pipeline_clip(
        theme,
        "fastapi-request.gif",
        "FastAPI: 요청 흐름",
        ["Middleware", "Depends", "Route", "Response"],
    )


def clip_be_di(theme: Theme):
    frames = []
    parts = [
        ("Controller", "비어 있음"),
        ("+ Service", "규칙 주입"),
        ("+ Repository", "저장 주입"),
        ("조립 완료", "생성자로 연결"),
    ]
    boxes = ["Controller", "Service", "Repository"]
    for step, (title, hint) in enumerate(parts):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "DI: 생성자 주입", fill=theme.ink, font=F18)
        for i, label in enumerate(boxes):
            x = PAD + i * 240
            filled = step > i or (step == 3)
            fill = theme.highlight if filled else theme.fill
            rounded(d, (x, 150, x + 200, 230), theme, fill=fill)
            tw = d.textlength(label, font=F14)
            d.text((x + (200 - tw) / 2, 180), label, fill=theme.ink, font=F14)
            if i < 2:
                d.line((x + 200 + 8, 190, x + 240 - 8, 190), fill=theme.ink if step > i else theme.line, width=2)
        d.text((PAD, H - PAD - 10), f"{title} — {hint}", fill=theme.accent, font=F13)
        frames.append(img)
        frames.append(img.copy())
    save_gif("be-di.gif", frames, theme)


def clip_be_persist(theme: Theme):
    frames = []
    states = [
        ("메모리만 변경", "영속성 컨텍스트", False),
        ("flush", "SQL 전송 준비", True),
        ("commit", "DB에 확정", True),
    ]
    for title, hint, db_on in states:
        img, d = new_frame(theme)
        d.text((PAD, PAD), "영속성: flush / commit", fill=theme.ink, font=F18)
        rounded(d, (PAD, 140, 360, 260), theme, fill=theme.soft)
        tw = d.textlength("Entity", font=F14)
        d.text((PAD + (312 - tw) / 2, 180), "Entity", fill=theme.ink, font=F14)
        rounded(d, (480, 140, 800, 260), theme, fill=theme.highlight if db_on else theme.fill)
        tw = d.textlength("Database", font=F14)
        d.text((480 + (320 - tw) / 2, 180), "Database", fill=theme.ink, font=F14)
        d.line((360, 200, 480, 200), fill=theme.orange if db_on else theme.line, width=3)
        d.text((PAD, H - PAD - 10), f"{title} — {hint}", fill=theme.accent, font=F13)
        frames.append(img)
        frames.append(img.copy())
    save_gif("be-persist.gif", frames, theme)


def clip_be_session_jwt(theme: Theme):
    frames = []
    for mode in ("Session", "JWT"):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "상태 유지: Session vs JWT", fill=theme.ink, font=F18)
        left_fill = theme.orange if mode == "Session" else theme.fill
        right_fill = theme.orange if mode == "JWT" else theme.fill
        left_color = theme.white if mode == "Session" else theme.ink
        right_color = theme.white if mode == "JWT" else theme.ink
        rounded(d, (PAD, 130, 380, 280), theme, fill=left_fill)
        rounded(d, (460, 130, 800, 280), theme, fill=right_fill)
        d.text((PAD + 90, 175), "Session", fill=left_color, font=F18)
        d.text((PAD + 60, 220), "서버가 상태 보관", fill=left_color, font=F13)
        d.text((460 + 120, 175), "JWT", fill=right_color, font=F18)
        d.text((460 + 70, 220), "토큰에 주장 담김", fill=right_color, font=F13)
        hint = "쿠키·세션 ID로 서버 조회" if mode == "Session" else "요청마다 토큰 검증"
        d.text((PAD, H - PAD - 10), hint, fill=theme.accent, font=F13)
        frames.append(img)
        frames.append(img.copy())
    save_gif("be-session-jwt.gif", frames, theme)


CLIPS = [
    clip_spring_request,
    clip_nest_request,
    clip_fastapi_request,
    clip_be_di,
    clip_be_persist,
    clip_be_session_jwt,
]


if __name__ == "__main__":
    for theme in THEMES:
        for fn in CLIPS:
            fn(theme)
    print("done")
