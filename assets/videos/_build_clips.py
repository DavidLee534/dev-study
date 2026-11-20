"""Short lecture GIFs in light + dark themes."""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from _theme import THEMES, Theme, themed_name  # noqa: E402

OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)

W, H = 800, 460
PAD = 56


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
F16 = font(16, True)
F14 = font(14)
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


def save_gif(name, frames, theme: Theme, duration=450, hold_ends_ms=1600):
    path = OUT / themed_name(name, theme)
    n = len(frames)
    if n == 1:
        durations = [hold_ends_ms]
    elif n == 2:
        durations = [hold_ends_ms, hold_ends_ms]
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


def clip_stack(theme: Theme):
    frames = []
    layers = []
    items = ["Skipper", "Kowalski", "Rico"]

    def draw_scene(title, stack_items, hint=""):
        img, d = new_frame(theme)
        d.text((PAD, PAD), title, fill=theme.ink, font=F18)
        base_x, base_y = 295, 330
        bw, bh = 170, 44
        for i, label in enumerate(reversed(stack_items)):
            y = base_y - (i + 1) * (bh + 8)
            fill = theme.orange if i == len(stack_items) - 1 else theme.fill
            rounded(d, (base_x, y, base_x + bw, y + bh), theme, fill=fill)
            tw = d.textlength(label, font=F14)
            color = theme.white if fill == theme.orange else theme.ink
            d.text((base_x + (bw - tw) / 2, y + 12), label, fill=color, font=F14)
        d.line((base_x - 10, base_y, base_x + bw + 10, base_y), fill=theme.line, width=3)
        if hint:
            d.text((PAD, H - PAD - 8), hint, fill=theme.accent, font=F13)
        return img

    frames.append(draw_scene("스택: LIFO", [], "비어 있음"))
    for item in items:
        layers.append(item)
        frames.append(draw_scene("스택: push", layers, f"push → {item}"))
        frames.append(draw_scene("스택: push", layers, f"push → {item}"))
    while layers:
        top = layers[-1]
        frames.append(draw_scene("스택: pop", layers, f"pop ← {top}"))
        layers.pop()
        frames.append(draw_scene("스택: pop", layers, f"{top} 제거됨"))
    frames.append(draw_scene("스택: LIFO", [], "다시 비움"))
    save_gif("stack-lifo.gif", frames, theme, duration=550)


def clip_queue(theme: Theme):
    frames = []
    q = []

    def draw_scene(title, items, hint=""):
        img, d = new_frame(theme)
        d.text((PAD, PAD), title, fill=theme.ink, font=F18)
        d.text((PAD + 20, 190), "out", fill=theme.orange, font=F16)
        d.text((W - PAD - 40, 190), "in", fill=theme.accent, font=F16)
        x0, y0, bw, bh = 150, 170, 140, 52
        for i, label in enumerate(items):
            x = x0 + i * (bw + 14)
            rounded(d, (x, y0, x + bw, y0 + bh), theme)
            tw = d.textlength(label, font=F13)
            d.text((x + (bw - tw) / 2, y0 + 16), label, fill=theme.ink, font=F13)
        if hint:
            d.text((PAD, 290), hint, fill=theme.accent, font=F14)
        d.text((PAD, H - PAD - 8), "FIFO: 앞에서 빼고 뒤에 넣는다", fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene("큐: FIFO", [], "대기열 비어 있음"))
    for item in ["Skipper", "Kowalski", "Private"]:
        q.append(item)
        frames.append(draw_scene("큐: enqueue", q, f"뒤에 추가 → {item}"))
        frames.append(draw_scene("큐: enqueue", q, f"뒤에 추가 → {item}"))
    while q:
        front = q[0]
        frames.append(draw_scene("큐: dequeue", q, f"앞에서 제거 ← {front}"))
        q.pop(0)
        frames.append(draw_scene("큐: dequeue", q, f"{front} 나감"))
    frames.append(draw_scene("큐: FIFO", [], "대기열 비움"))
    save_gif("queue-fifo.gif", frames, theme, duration=550)


def clip_array(theme: Theme):
    cells = ["Skipper", "Kowalski", "Private", "Rico"]
    frames = []

    def draw_scene(highlight=None, hint=""):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "배열: 인덱스로 바로 접근", fill=theme.ink, font=F18)
        x0, y0, cw, ch = PAD + 10, 150, 150, 64
        for i, label in enumerate(cells):
            x = x0 + i * (cw + 14)
            fill = theme.highlight if highlight == i else theme.fill
            rounded(d, (x, y0, x + cw, y0 + ch), theme, fill=fill)
            tw = d.textlength(label, font=F14)
            d.text((x + (cw - tw) / 2, y0 + 14), label, fill=theme.ink, font=F14)
            idx = f"[{i}]"
            iw = d.textlength(idx, font=F13)
            d.text((x + (cw - iw) / 2, y0 + ch + 14), idx, fill=theme.muted, font=F13)
        if hint:
            d.text((PAD, 300), hint, fill=theme.accent, font=F14)
        d.text((PAD, H - PAD - 8), "index만 알면 O(1)", fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(None, "모든 칸이 나란히 붙어 있다"))
    for i, name in enumerate(cells):
        frames.append(draw_scene(i, f"index {i} → {name}"))
        frames.append(draw_scene(i, f"index {i} → {name}"))
    frames.append(draw_scene(None, "중간 삽입은 뒤를 밀어야 해서 비용↑"))
    save_gif("array-index.gif", frames, theme, duration=600)


def clip_hash(theme: Theme):
    frames = []

    def draw_scene(step=0):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "해시: 키로 위치 찾기", fill=theme.ink, font=F18)
        key_fill = theme.highlight if step >= 1 else theme.fill
        rounded(d, (PAD + 10, 130, PAD + 130, 185), theme, fill=key_fill)
        d.text((PAD + 30, 148), '"Skipper"', fill=theme.ink, font=F14)
        if step >= 1:
            d.line((PAD + 140, 157, 250, 157), fill=theme.ink, width=2)
            d.polygon([(250, 157), (240, 151), (240, 163)], fill=theme.ink)
        hash_fill = theme.soft if step >= 2 else theme.fill
        rounded(d, (260, 130, 370, 185), theme, fill=hash_fill)
        d.text((285, 148), "hash()", fill=theme.ink, font=F16)
        if step >= 2:
            d.line((380, 157, 450, 157), fill=theme.ink, width=2)
            d.polygon([(450, 157), (440, 151), (440, 163)], fill=theme.ink)
        for i, val in enumerate(["…", "25", "…"]):
            y = 100 + i * 55
            rounded(d, (470, y, 520, y + 40), theme, fill=theme.fill, outline=theme.line, width=1)
            d.text((485, y + 10), str(i), fill=theme.muted, font=F13)
            bucket_fill = theme.highlight if step >= 3 and i == 1 else theme.fill
            rounded(d, (535, y, 670, y + 40), theme, fill=bucket_fill)
            d.text((575, y + 10), val, fill=theme.ink if val != "…" else theme.muted, font=F14)
        hints = [
            "키가 들어온다",
            "해시 함수로 번호를 만든다",
            "버킷 위치로 이동",
            "값 25를 O(1)에 가깝게 읽는다",
        ]
        d.text((PAD, H - PAD - 8), hints[min(step, 3)], fill=theme.accent, font=F14)
        return img

    for s in range(4):
        frames.append(draw_scene(s))
        frames.append(draw_scene(s))
    save_gif("hash-lookup.gif", frames, theme, duration=650)


def clip_binary_search(theme: Theme):
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 11
    frames = []
    blue = (96, 165, 250) if theme.name == "dark" else (37, 99, 235)

    def draw_scene(lo, hi, mid=None, found=False, hint=""):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "이분 탐색: 반씩 줄이기", fill=theme.ink, font=F18)
        x0, y0, cw, ch = PAD + 8, 150, 88, 56
        for i, v in enumerate(arr):
            x = x0 + i * (cw + 8)
            in_range = lo <= i <= hi
            if mid == i:
                fill = theme.highlight
            elif in_range:
                fill = theme.fill
            else:
                fill = theme.line
            outline = theme.orange if mid == i else (theme.line if not in_range else theme.ink)
            rounded(d, (x, y0, x + cw, y0 + ch), theme, fill=fill, outline=outline)
            tw = d.textlength(str(v), font=F16)
            color = theme.muted if not in_range else theme.ink
            d.text((x + (cw - tw) / 2, y0 + 16), str(v), fill=color, font=F16)
            if i == lo and lo <= hi:
                d.text((x + 28, y0 + ch + 12), "L", fill=theme.orange, font=F13)
            if i == hi and lo <= hi:
                d.text((x + 28, y0 + ch + 12), "R", fill=blue, font=F13)
        d.text((PAD, 280), f"target = {target}", fill=theme.accent, font=F14)
        if hint:
            d.text((PAD, 315), hint, fill=theme.accent, font=F14)
        d.text((PAD, H - PAD - 8), "정렬된 배열에서만 성립", fill=theme.muted, font=F13)
        return img

    lo, hi = 0, len(arr) - 1
    frames.append(draw_scene(lo, hi, hint="전체 구간에서 시작"))
    while lo <= hi:
        mid = (lo + hi) // 2
        frames.append(draw_scene(lo, hi, mid, hint=f"중간 index {mid} → {arr[mid]}"))
        if arr[mid] == target:
            frames.append(draw_scene(lo, hi, mid, found=True, hint=f"찾음: {target}"))
            break
        if arr[mid] < target:
            frames.append(draw_scene(lo, hi, mid, hint="중간보다 큼 → 오른쪽"))
            lo = mid + 1
        else:
            frames.append(draw_scene(lo, hi, mid, hint="중간보다 작음 → 왼쪽"))
            hi = mid - 1
        frames.append(draw_scene(lo, hi, hint="탐색 구간 축소"))
    save_gif("binary-search.gif", frames, theme, duration=700)


def clip_dfs_bfs(theme: Theme):
    frames = []
    nodes = {
        "S": (380, 110, "Skipper"),
        "K": (240, 210, "Kowalski"),
        "P": (520, 210, "Private"),
        "R": (180, 310, "Rico"),
    }
    edges = [("S", "K"), ("S", "P"), ("K", "R")]

    def draw_scene(title, order, current=None, hint=""):
        img, d = new_frame(theme)
        d.text((PAD, PAD), title, fill=theme.ink, font=F18)
        for a, b in edges:
            d.line((*nodes[a][:2], *nodes[b][:2]), fill=theme.line, width=2)
        for key, (cx, cy, label) in nodes.items():
            visited = key in order
            fill = (
                theme.orange
                if key == current
                else (theme.highlight if visited else theme.fill)
            )
            color = theme.white if key == current else theme.ink
            w = 130 if label == "Kowalski" else 110
            rounded(d, (cx - w / 2, cy - 22, cx + w / 2, cy + 22), theme, fill=fill)
            tw = d.textlength(label, font=F13)
            d.text((cx - tw / 2, cy - 8), label, fill=color, font=F13)
        path = " → ".join(order) if order else "(없음)"
        d.text((PAD, H - PAD - 28), f"방문 순서: {path}", fill=theme.accent, font=F13)
        if hint:
            d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    dfs = []
    frames.append(draw_scene("DFS: 깊게 먼저", dfs, hint="스택/재귀 감각"))
    for step in ["S", "K", "R", "P"]:
        dfs.append(step)
        frames.append(draw_scene("DFS: 깊게 먼저", dfs, current=step, hint=f"방문 {nodes[step][2]}"))
        frames.append(draw_scene("DFS: 깊게 먼저", dfs, hint=f"방문 {nodes[step][2]}"))
    bfs = []
    frames.append(draw_scene("BFS: 넓게 먼저", bfs, hint="큐 감각"))
    for step in ["S", "K", "P", "R"]:
        bfs.append(step)
        frames.append(draw_scene("BFS: 넓게 먼저", bfs, current=step, hint=f"방문 {nodes[step][2]}"))
        frames.append(draw_scene("BFS: 넓게 먼저", bfs, hint=f"방문 {nodes[step][2]}"))
    save_gif("dfs-bfs.gif", frames, theme, duration=650)


def clip_two_pointer(theme: Theme):
    arr = [1, 2, 3, 4, 5, 6]
    target = 9
    frames = []
    blue = (96, 165, 250) if theme.name == "dark" else (37, 99, 235)

    def draw_scene(L, R, hint="", ok=False):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "투 포인터: 양쪽에서 좁히기", fill=theme.ink, font=F18)
        x0, y0, cw, ch = PAD + 20, 150, 90, 56
        for i, v in enumerate(arr):
            x = x0 + i * (cw + 12)
            fill = theme.highlight if i in (L, R) else theme.fill
            rounded(d, (x, y0, x + cw, y0 + ch), theme, fill=fill)
            tw = d.textlength(str(v), font=F16)
            d.text((x + (cw - tw) / 2, y0 + 16), str(v), fill=theme.ink, font=F16)
            if i == L:
                d.text((x + 32, y0 + ch + 14), "L", fill=theme.orange, font=F14)
            if i == R:
                d.text((x + 32, y0 + ch + 14), "R", fill=blue, font=F14)
        s = arr[L] + arr[R]
        d.text((PAD, 280), f"합 = {arr[L]} + {arr[R]} = {s}  (목표 {target})", fill=theme.accent, font=F14)
        if hint:
            d.text((PAD, 315), hint, fill=theme.accent, font=F14)
        d.text((PAD, H - PAD - 8), "정렬된 배열에서 구간/합을 O(n)으로", fill=theme.muted, font=F13)
        return img

    L, R = 0, len(arr) - 1
    frames.append(draw_scene(L, R, "양 끝에서 시작"))
    while L < R:
        s = arr[L] + arr[R]
        frames.append(draw_scene(L, R, f"현재 합 {s}"))
        if s == target:
            frames.append(draw_scene(L, R, f"목표 달성: {arr[L]} + {arr[R]}", ok=True))
            break
        if s < target:
            frames.append(draw_scene(L, R, "합이 작음 → L 이동"))
            L += 1
        else:
            frames.append(draw_scene(L, R, "합이 큼 → R 이동"))
            R -= 1
        frames.append(draw_scene(L, R, "포인터 갱신"))
    save_gif("two-pointer.gif", frames, theme, duration=700)


CLIPS = [
    clip_array,
    clip_stack,
    clip_queue,
    clip_hash,
    clip_binary_search,
    clip_dfs_bfs,
    clip_two_pointer,
]


if __name__ == "__main__":
    for theme in THEMES:
        for fn in CLIPS:
            fn(theme)
    print("done")
