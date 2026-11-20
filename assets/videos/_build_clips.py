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


def clip_net_dns(theme: Theme):
    frames = []

    def draw_scene(step=0, hint=""):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "DNS: 이름 → IP", fill=theme.ink, font=F18)

        name_fill = theme.highlight if step == 0 else theme.soft
        rounded(d, (PAD, 140, 240, 220), theme, fill=name_fill)
        tw = d.textlength("example.com", font=F14)
        d.text((PAD + (180 - tw) / 2 + 10, 162), "example.com", fill=theme.ink, font=F14)
        d.text((PAD + 50, 188), "이름", fill=theme.muted, font=F13)

        if step >= 1:
            d.line((250, 180, 320, 180), fill=theme.ink, width=2)
            d.polygon([(320, 180), (308, 174), (308, 186)], fill=theme.ink)
            d.text((255, 148), "DNS", fill=theme.orange, font=F13)

        dns_fill = theme.highlight if step == 1 else (theme.soft if step >= 1 else theme.fill)
        rounded(d, (330, 140, 480, 220), theme, fill=dns_fill)
        d.text((360, 168), "조회", fill=theme.ink, font=F16)

        if step >= 2:
            d.line((490, 180, 560, 180), fill=theme.ink, width=2)
            d.polygon([(560, 180), (548, 174), (548, 186)], fill=theme.ink)

        ip_fill = theme.highlight if step >= 2 else theme.fill
        rounded(d, (570, 140, 760, 220), theme, fill=ip_fill)
        ip = "93.184.216.34" if step >= 2 else "?.?.?.?"
        tw = d.textlength(ip, font=F14)
        d.text((570 + (190 - tw) / 2, 162), ip, fill=theme.ink, font=F14)
        d.text((625, 188), "IP", fill=theme.muted, font=F13)

        if step >= 3:
            d.text((PAD, 270), "이어서 :443 포트로 연결", fill=theme.accent, font=F14)
            rounded(d, (PAD, 310, 220, 360), theme, fill=theme.highlight)
            d.text((PAD + 55, 326), ":443", fill=theme.ink, font=F16)

        d.text((PAD, H - PAD - 8), hint or "도메인 이름을 주소로 바꾼다", fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(0, "브라우저가 이름을 든다"))
    frames.append(draw_scene(0, "브라우저가 이름을 든다"))
    frames.append(draw_scene(1, "DNS에 물어본다"))
    frames.append(draw_scene(1, "DNS에 물어본다"))
    frames.append(draw_scene(2, "IP를 받는다"))
    frames.append(draw_scene(2, "IP를 받는다"))
    frames.append(draw_scene(3, "IP + 포트로 서비스에 도착"))
    frames.append(draw_scene(3, "IP + 포트로 서비스에 도착"))
    save_gif("net-dns.gif", frames, theme, duration=600)


def clip_net_http(theme: Theme):
    frames = []

    def draw_scene(step=0, hint=""):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "HTTP: 요청 → 응답", fill=theme.ink, font=F18)

        rounded(d, (PAD, 140, 230, 250), theme, fill=theme.soft)
        d.text((PAD + 55, 175), "Client", fill=theme.ink, font=F16)
        d.text((PAD + 35, 205), "Browser", fill=theme.muted, font=F13)

        rounded(d, (570, 140, 760, 250), theme, fill=theme.soft)
        d.text((610, 175), "Server", fill=theme.ink, font=F16)
        d.text((610, 205), "API", fill=theme.muted, font=F13)

        if step >= 1:
            y = 165
            d.line((240, y, 550, y), fill=theme.orange, width=3)
            d.polygon([(550, y), (538, y - 6), (538, y + 6)], fill=theme.orange)
            d.text((300, 132), "GET /users", fill=theme.orange, font=F14)

        if step >= 2:
            y = 220
            d.line((550, y, 240, y), fill=theme.accent, width=3)
            d.polygon([(240, y), (252, y - 6), (252, y + 6)], fill=theme.accent)
            d.text((300, 235), "200 JSON", fill=theme.accent, font=F14)

        if step >= 3:
            d.text((PAD, 300), "HTTPS = 같은 대화 + TLS 보호", fill=theme.accent, font=F14)

        d.text((PAD, H - PAD - 8), hint or "한 왕복이 기본 단위", fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(0, "클라이언트와 서버"))
    frames.append(draw_scene(1, "요청을 보낸다"))
    frames.append(draw_scene(1, "요청을 보낸다"))
    frames.append(draw_scene(2, "응답을 받는다"))
    frames.append(draw_scene(2, "응답을 받는다"))
    frames.append(draw_scene(3, "암호화가 필요하면 HTTPS"))
    frames.append(draw_scene(3, "암호화가 필요하면 HTTPS"))
    save_gif("net-http.gif", frames, theme, duration=650)


def clip_net_tcp(theme: Theme):
    frames = []
    steps = [
        (0, "연결 전"),
        (1, "SYN → 연결하자"),
        (2, "SYN-ACK → 알겠어"),
        (3, "ACK → 시작"),
        (4, "데이터 전송 가능"),
    ]

    def draw_scene(step, hint):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "TCP: 3-way handshake", fill=theme.ink, font=F18)

        rounded(d, (PAD, 150, 220, 240), theme, fill=theme.soft)
        d.text((PAD + 55, 185), "Client", fill=theme.ink, font=F16)

        rounded(d, (580, 150, 760, 240), theme, fill=theme.soft)
        d.text((620, 185), "Server", fill=theme.ink, font=F16)

        labels = [
            (1, 165, "SYN", theme.orange, True),
            (2, 200, "SYN-ACK", theme.accent, False),
            (3, 235, "ACK", theme.orange, True),
        ]
        for need, y, text, color, to_server in labels:
            if step < need:
                continue
            if to_server:
                d.line((230, y, 560, y), fill=color, width=3)
                d.polygon([(560, y), (548, y - 6), (548, y + 6)], fill=color)
                d.text((340, y - 22), text, fill=color, font=F13)
            else:
                d.line((560, y, 230, y), fill=color, width=3)
                d.polygon([(230, y), (242, y - 6), (242, y + 6)], fill=color)
                d.text((340, y - 22), text, fill=color, font=F13)

        if step >= 4:
            rounded(d, (280, 300, 520, 350), theme, fill=theme.highlight)
            d.text((320, 316), "연결 확립", fill=theme.ink, font=F16)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    for step, hint in steps:
        frames.append(draw_scene(step, hint))
        frames.append(draw_scene(step, hint))
    save_gif("net-tcp.gif", frames, theme, duration=600)


def clip_net_lb(theme: Theme):
    frames = []

    def draw_scene(target=None, hint=""):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "로드밸런서: 요청을 나눈다", fill=theme.ink, font=F18)

        rounded(d, (PAD, 170, 190, 250), theme, fill=theme.soft)
        d.text((PAD + 40, 200), "Client", fill=theme.ink, font=F16)

        d.line((200, 210, 280, 210), fill=theme.ink, width=2)
        d.polygon([(280, 210), (268, 204), (268, 216)], fill=theme.ink)

        rounded(d, (290, 160, 480, 260), theme, fill=theme.highlight)
        d.text((318, 190), "Load Balancer", fill=theme.ink, font=F14)
        d.text((345, 218), "안내", fill=theme.muted, font=F13)

        apps = [("App 1", 120), ("App 2", 200), ("App 3", 280)]
        for i, (label, y) in enumerate(apps):
            active = target == i
            d.line((480, 210, 560, y + 25), fill=theme.orange if active else theme.line, width=3 if active else 2)
            fill = theme.highlight if active else theme.fill
            rounded(d, (560, y, 760, y + 50), theme, fill=fill)
            tw = d.textlength(label, font=F14)
            d.text((560 + (200 - tw) / 2, y + 16), label, fill=theme.ink, font=F14)

        d.text((PAD, H - PAD - 8), hint or "여러 서버에 부하를 분산", fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(None, "요청이 들어온다"))
    for i in range(3):
        frames.append(draw_scene(i, f"이번엔 App {i + 1}으로"))
        frames.append(draw_scene(i, f"이번엔 App {i + 1}으로"))
    frames.append(draw_scene(None, "죽은 서버는 health check로 제외"))
    save_gif("net-lb.gif", frames, theme, duration=550)


def clip_os_schedule(theme: Theme):
    frames = []
    # states: which process is running (0/1), and phase hint
    scenes = [
        (None, ["Ready", "Ready"], "둘 다 Ready 큐에 대기"),
        (0, ["Running", "Ready"], "Skipper가 CPU 사용"),
        (0, ["Running", "Ready"], "시간 할당 거의 끝"),
        (1, ["Ready", "Running"], "context switch → Kowalski"),
        (1, ["Waiting", "Running"], "Skipper는 I/O Waiting"),
        (0, ["Running", "Ready"], "다시 Skipper 실행"),
    ]

    def draw_scene(running, states, hint):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "스케줄링: 누가 CPU를 쓰나", fill=theme.ink, font=F18)

        rounded(d, (300, 110, 500, 170), theme, fill=theme.highlight if running is not None else theme.fill)
        d.text((355, 130), "CPU", fill=theme.ink, font=F16)

        procs = [("Skipper", 120), ("Kowalski", 420)]
        for i, (name, x) in enumerate(procs):
            st = states[i]
            if st == "Running":
                fill = theme.highlight
            elif st == "Waiting":
                fill = theme.soft
            else:
                fill = theme.fill
            rounded(d, (x, 220, x + 200, 300), theme, fill=fill)
            d.text((x + 55, 240), name, fill=theme.ink, font=F14)
            tw = d.textlength(st, font=F13)
            d.text((x + (200 - tw) / 2, 268), st, fill=theme.orange if st == "Running" else theme.muted, font=F13)
            if running == i:
                d.line((x + 100, 220, 400, 170), fill=theme.orange, width=3)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    for running, states, hint in scenes:
        frames.append(draw_scene(running, states, hint))
        frames.append(draw_scene(running, states, hint))
    save_gif("os-schedule.gif", frames, theme, duration=600)


def clip_os_pagefault(theme: Theme):
    frames = []

    def draw_scene(step, hint):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "가상 메모리: 페이지 폴트", fill=theme.ink, font=F18)

        rounded(d, (PAD, 130, 360, 280), theme, fill=theme.soft)
        d.text((PAD + 110, 145), "RAM (책상)", fill=theme.ink, font=F14)
        pages = ["P1", "P2", "·"]
        for i, p in enumerate(pages):
            x = PAD + 30 + i * 100
            fill = theme.highlight if (step >= 3 and i == 2) else theme.fill
            label = "P3" if (step >= 3 and i == 2) else p
            rounded(d, (x, 190, x + 80, 250), theme, fill=fill)
            tw = d.textlength(label, font=F14)
            d.text((x + (80 - tw) / 2, 212), label, fill=theme.ink if label != "·" else theme.muted, font=F14)

        rounded(d, (440, 130, 760, 280), theme, fill=theme.fill)
        d.text((520, 145), "Disk (서가)", fill=theme.ink, font=F14)
        disk_pages = ["P3", "P4", "P5"]
        for i, p in enumerate(disk_pages):
            x = 470 + i * 90
            fill = theme.highlight if (step == 1 and i == 0) else theme.fill
            if step >= 3 and i == 0:
                fill = theme.line
            rounded(d, (x, 190, x + 70, 250), theme, fill=fill)
            color = theme.muted if (step >= 3 and i == 0) else theme.ink
            tw = d.textlength(p if not (step >= 3 and i == 0) else "·", font=F14)
            label = "·" if (step >= 3 and i == 0) else p
            d.text((x + (70 - tw) / 2, 212), label, fill=color, font=F14)

        if step == 1:
            d.text((PAD, 310), "접근하려던 P3가 RAM에 없음 → page fault", fill=theme.orange, font=F14)
        if step == 2:
            d.line((470, 220, 320, 220), fill=theme.orange, width=3)
            d.polygon([(320, 220), (332, 214), (332, 226)], fill=theme.orange)
            d.text((340, 310), "디스크로 가져와 RAM에 올림", fill=theme.accent, font=F14)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(0, "필요한 페이지만 RAM에 둔다"))
    frames.append(draw_scene(1, "없는 페이지에 접근"))
    frames.append(draw_scene(1, "없는 페이지에 접근"))
    frames.append(draw_scene(2, "디스크로 가져오는 중"))
    frames.append(draw_scene(2, "디스크로 가져오는 중"))
    frames.append(draw_scene(3, "이제 RAM에서 이어서 실행"))
    frames.append(draw_scene(3, "이제 RAM에서 이어서 실행"))
    save_gif("os-pagefault.gif", frames, theme, duration=650)


def clip_os_sync(theme: Theme):
    frames = []

    def draw_scene(step, hint):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "동기화: 동시에 고치면 꼬인다", fill=theme.ink, font=F18)

        rounded(d, (300, 120, 500, 190), theme, fill=theme.highlight if step >= 1 else theme.fill)
        val = {0: "0", 1: "0", 2: "1?", 3: "1", 4: "2"}.get(step, "2")
        d.text((355, 135), "공유 변수", fill=theme.muted, font=F13)
        tw = d.textlength(val, font=F18)
        d.text((400 - tw / 2, 155), val, fill=theme.ink, font=F18)

        rounded(d, (PAD, 230, 260, 320), theme, fill=theme.soft)
        d.text((PAD + 70, 255), "A", fill=theme.ink, font=F16)
        a_act = ["대기", "읽기 0", "쓰기 1", "대기", "락 후 +1"][min(step, 4)]
        d.text((PAD + 50, 285), a_act, fill=theme.orange if step in (1, 2, 4) else theme.muted, font=F13)

        rounded(d, (540, 230, 760, 320), theme, fill=theme.soft)
        d.text((620, 255), "B", fill=theme.ink, font=F16)
        b_act = ["대기", "읽기 0", "쓰기 1", "덮어씀", "대기"][min(step, 4)]
        d.text((590, 285), b_act, fill=theme.orange if step in (1, 2, 3) else theme.muted, font=F13)

        if step >= 4:
            d.text((PAD, 350), "락으로 한 명씩 → 결과가 맞다", fill=theme.accent, font=F14)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(0, "초기값 0"))
    frames.append(draw_scene(1, "둘 다 동시에 읽음"))
    frames.append(draw_scene(1, "둘 다 동시에 읽음"))
    frames.append(draw_scene(2, "각자 1을 쓰려 함"))
    frames.append(draw_scene(3, "한쪽 결과가 사라질 수 있음"))
    frames.append(draw_scene(3, "한쪽 결과가 사라질 수 있음"))
    frames.append(draw_scene(4, "락으로 critical section 보호"))
    frames.append(draw_scene(4, "락으로 critical section 보호"))
    save_gif("os-sync.gif", frames, theme, duration=650)


def clip_os_deadlock(theme: Theme):
    frames = []

    def draw_scene(step, hint):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "데드락: 서로 기다리며 멈춤", fill=theme.ink, font=F18)

        rounded(d, (120, 120, 300, 200), theme, fill=theme.highlight if step >= 1 else theme.fill)
        d.text((165, 140), "Skipper", fill=theme.ink, font=F14)
        d.text((155, 168), "펜 보유" if step >= 1 else "대기", fill=theme.muted, font=F13)

        rounded(d, (520, 120, 700, 200), theme, fill=theme.highlight if step >= 2 else theme.fill)
        d.text((560, 140), "Kowalski", fill=theme.ink, font=F14)
        d.text((555, 168), "노트 보유" if step >= 2 else "대기", fill=theme.muted, font=F13)

        rounded(d, (120, 270, 300, 340), theme, fill=theme.fill)
        d.text((155, 295), "노트 대기" if step >= 3 else "·", fill=theme.ink if step >= 3 else theme.muted, font=F14)

        rounded(d, (520, 270, 700, 340), theme, fill=theme.fill)
        d.text((560, 295), "펜 대기" if step >= 3 else "·", fill=theme.ink if step >= 3 else theme.muted, font=F14)

        if step >= 1:
            d.line((210, 200, 210, 270), fill=theme.line, width=2)
        if step >= 2:
            d.line((610, 200, 610, 270), fill=theme.line, width=2)
        if step >= 3:
            d.line((300, 160, 520, 160), fill=theme.orange, width=3)
            d.polygon([(520, 160), (508, 154), (508, 166)], fill=theme.orange)
            d.text((360, 130), "노트 원함", fill=theme.orange, font=F13)
            d.line((520, 305, 300, 305), fill=theme.orange, width=3)
            d.polygon([(300, 305), (312, 299), (312, 311)], fill=theme.orange)
            d.text((370, 315), "펜 원함", fill=theme.orange, font=F13)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(0, "자원을 나누어 쓰기 전"))
    frames.append(draw_scene(1, "Skipper가 펜을 듦"))
    frames.append(draw_scene(2, "Kowalski가 노트를 듦"))
    frames.append(draw_scene(2, "Kowalski가 노트를 듦"))
    frames.append(draw_scene(3, "서로 상대 것을 기다림 → 데드락"))
    frames.append(draw_scene(3, "서로 상대 것을 기다림 → 데드락"))
    save_gif("os-deadlock.gif", frames, theme, duration=650)


def clip_os_syscall(theme: Theme):
    frames = []

    def draw_scene(step, hint):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "시스템 콜: 커널에 부탁한다", fill=theme.ink, font=F18)

        rounded(d, (PAD, 130, 360, 250), theme, fill=theme.soft if step < 2 else theme.fill)
        d.text((PAD + 100, 155), "User mode", fill=theme.ink, font=F14)
        d.text((PAD + 110, 190), "App", fill=theme.muted, font=F16)
        if step == 0:
            d.text((PAD + 70, 220), "read() 호출", fill=theme.orange, font=F13)

        rounded(d, (440, 130, 760, 250), theme, fill=theme.highlight if step >= 1 else theme.fill)
        d.text((530, 155), "Kernel mode", fill=theme.ink, font=F14)
        d.text((545, 190), "OS", fill=theme.muted, font=F16)
        if step >= 1:
            d.text((500, 220), "파일/디스크 처리", fill=theme.orange, font=F13)

        if step >= 1:
            d.line((370, 180, 430, 180), fill=theme.orange, width=3)
            d.polygon([(430, 180), (418, 174), (418, 186)], fill=theme.orange)
            d.text((375, 145), "syscall", fill=theme.orange, font=F13)
        if step >= 2:
            d.line((430, 210, 370, 210), fill=theme.accent, width=3)
            d.polygon([(370, 210), (382, 204), (382, 216)], fill=theme.accent)
            d.text((375, 220), "결과", fill=theme.accent, font=F13)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(0, "앱은 하드웨어를 직접 안 만진다"))
    frames.append(draw_scene(0, "앱은 하드웨어를 직접 안 만진다"))
    frames.append(draw_scene(1, "커널로 진입"))
    frames.append(draw_scene(1, "커널로 진입"))
    frames.append(draw_scene(2, "결과를 유저 모드로 반환"))
    frames.append(draw_scene(2, "결과를 유저 모드로 반환"))
    save_gif("os-syscall.gif", frames, theme, duration=650)


def clip_db_index(theme: Theme):
    frames = []
    rows = ["A", "B", "C", "D", "E"]

    def draw_scene(mode, highlight=None, hint=""):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "인덱스: 색인으로 찾기", fill=theme.ink, font=F18)

        d.text((PAD, 110), "테이블", fill=theme.muted, font=F13)
        for i, r in enumerate(rows):
            x = PAD + i * 70
            fill = theme.highlight if highlight == i else theme.fill
            rounded(d, (x, 140, x + 58, 190), theme, fill=fill)
            tw = d.textlength(r, font=F14)
            d.text((x + (58 - tw) / 2, 158), r, fill=theme.ink, font=F14)

        if mode == "scan":
            d.text((PAD, 230), "Full scan: 한 칸씩 확인", fill=theme.orange, font=F14)
        else:
            rounded(d, (PAD, 230, 280, 290), theme, fill=theme.soft)
            d.text((PAD + 20, 245), "Index", fill=theme.ink, font=F14)
            d.text((PAD + 20, 268), "C → 쪽수 3", fill=theme.muted, font=F13)
            d.line((290, 260, 360, 165), fill=theme.orange, width=3)
            d.polygon([(360, 165), (348, 168), (355, 176)], fill=theme.orange)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene("scan", 0, "처음부터 훑기"))
    frames.append(draw_scene("scan", 1, "아직 아님"))
    frames.append(draw_scene("scan", 2, "찾음 (느릴 수 있음)"))
    frames.append(draw_scene("scan", 2, "찾음 (느릴 수 있음)"))
    frames.append(draw_scene("index", 2, "색인으로 바로 이동"))
    frames.append(draw_scene("index", 2, "색인으로 바로 이동"))
    save_gif("db-index.gif", frames, theme, duration=550)


def clip_db_transaction(theme: Theme):
    frames = []
    # 0 시작 → 1 A만 차감 → 2 실패 롤백 → 3 재시도 A → 4 B 반영 → 5 커밋
    scenes = [
        ("100", "50", None, "이체 시작 전", False, False),
        ("70", "50", "−30", "A만 차감 (아직 미완료)", True, False),
        ("100", "50", "ROLLBACK", "실패 → 전부 원상복구", False, False),
        ("70", "50", "−30", "다시 시도: A 차감", True, False),
        ("70", "80", "+30", "B에도 반영", True, True),
        ("70", "80", "COMMIT", "성공 → 커밋으로 확정", True, True),
    ]

    def draw_scene(a_val, b_val, mid, hint, a_on, b_on):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "트랜잭션: 커밋 / 롤백", fill=theme.ink, font=F18)

        rounded(d, (PAD, 140, 300, 240), theme, fill=theme.highlight if a_on else theme.fill)
        d.text((PAD + 90, 160), "Account A", fill=theme.ink, font=F14)
        d.text((PAD + 110, 195), a_val, fill=theme.ink, font=F18)

        rounded(d, (500, 140, 760, 240), theme, fill=theme.highlight if b_on else theme.fill)
        d.text((560, 160), "Account B", fill=theme.ink, font=F14)
        d.text((590, 195), b_val, fill=theme.ink, font=F18)

        if mid:
            color = theme.accent if mid == "COMMIT" else theme.orange
            d.text((310, 175), mid, fill=color, font=F16)
            if mid == "COMMIT":
                d.line((310, 210, 490, 210), fill=theme.accent, width=3)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    for a_val, b_val, mid, hint, a_on, b_on in scenes:
        frames.append(draw_scene(a_val, b_val, mid, hint, a_on, b_on))
        frames.append(draw_scene(a_val, b_val, mid, hint, a_on, b_on))
    save_gif("db-transaction.gif", frames, theme, duration=550)


def clip_pattern_strategy(theme: Theme):
    frames = []
    strategies = ["최단", "최소 요금", "고속도로 회피"]

    def draw_scene(idx, hint):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "Strategy: 행동만 교체", fill=theme.ink, font=F18)
        rounded(d, (PAD, 130, 280, 230), theme, fill=theme.soft)
        d.text((PAD + 70, 160), "Navigator", fill=theme.ink, font=F14)
        d.text((PAD + 55, 190), "findRoute()", fill=theme.muted, font=F13)
        d.line((290, 180, 360, 180), fill=theme.ink, width=2)
        d.polygon([(360, 180), (348, 174), (348, 186)], fill=theme.ink)
        for i, name in enumerate(strategies):
            y = 120 + i * 70
            fill = theme.highlight if i == idx else theme.fill
            rounded(d, (380, y, 720, y + 55), theme, fill=fill)
            d.text((420, y + 16), name, fill=theme.ink, font=F14)
        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    for i, name in enumerate(strategies):
        frames.append(draw_scene(i, f"전략 → {name}"))
        frames.append(draw_scene(i, f"전략 → {name}"))
    save_gif("pattern-strategy.gif", frames, theme, duration=600)


def clip_pattern_observer(theme: Theme):
    frames = []

    def draw_scene(step, hint):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "Observer: 사건을 알림", fill=theme.ink, font=F18)
        rounded(d, (300, 110, 500, 190), theme, fill=theme.highlight if step >= 1 else theme.fill)
        d.text((355, 135), "Subject", fill=theme.ink, font=F14)
        d.text((340, 160), "upload()" if step >= 1 else "대기", fill=theme.orange if step >= 1 else theme.muted, font=F13)

        subs = [("Sub A", 100), ("Sub B", 320), ("Sub C", 540)]
        for i, (name, x) in enumerate(subs):
            active = step >= 2
            rounded(d, (x, 260, x + 160, 340), theme, fill=theme.highlight if active else theme.soft)
            d.text((x + 45, 285), name, fill=theme.ink, font=F14)
            d.text((x + 35, 310), "알림!" if active else "구독", fill=theme.orange if active else theme.muted, font=F13)
            if step >= 2:
                d.line((400, 190, x + 80, 260), fill=theme.orange, width=2)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(0, "구독자들이 등록됨"))
    frames.append(draw_scene(1, "사건 발생"))
    frames.append(draw_scene(1, "사건 발생"))
    frames.append(draw_scene(2, "모두에게 알림"))
    frames.append(draw_scene(2, "모두에게 알림"))
    save_gif("pattern-observer.gif", frames, theme, duration=600)


def clip_db_isolation(theme: Theme):
    frames = []

    def draw_scene(step, hint):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "격리: 커밋 전 값을 볼까?", fill=theme.ink, font=F18)

        bal = ["100", "100", "70", "100"][step]
        rounded(d, (300, 120, 500, 200), theme, fill=theme.highlight if step >= 2 else theme.fill)
        d.text((355, 140), "잔액", fill=theme.muted, font=F13)
        tw = d.textlength(bal, font=F18)
        d.text((400 - tw / 2, 165), bal, fill=theme.ink, font=F18)

        rounded(d, (PAD, 240, 280, 330), theme, fill=theme.soft)
        d.text((PAD + 70, 260), "Tx A", fill=theme.ink, font=F14)
        a = ["읽기 100", "−30 미커밋", "−30 미커밋", "롤백"][step]
        d.text((PAD + 40, 295), a, fill=theme.orange, font=F13)

        rounded(d, (520, 240, 760, 330), theme, fill=theme.soft)
        d.text((590, 260), "Tx B", fill=theme.ink, font=F14)
        b = ["대기", "대기", "70 읽음?", "다시 100"][step]
        d.text((560, 295), b, fill=theme.orange if step == 2 else theme.muted, font=F13)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(0, "둘 다 시작"))
    frames.append(draw_scene(1, "A가 아직 커밋 전"))
    frames.append(draw_scene(1, "A가 아직 커밋 전"))
    frames.append(draw_scene(2, "Dirty read: B가 미커밋 값을 봄"))
    frames.append(draw_scene(2, "Dirty read: B가 미커밋 값을 봄"))
    frames.append(draw_scene(3, "높은 격리는 이런 읽기를 막는다"))
    frames.append(draw_scene(3, "높은 격리는 이런 읽기를 막는다"))
    save_gif("db-isolation.gif", frames, theme, duration=650)


def clip_db_lock(theme: Theme):
    frames = []

    def draw_scene(step, hint):
        img, d = new_frame(theme)
        d.text((PAD, PAD), "락: 같은 행을 동시에 못 고침", fill=theme.ink, font=F18)

        rounded(d, (300, 120, 500, 200), theme, fill=theme.highlight if step >= 1 else theme.fill)
        d.text((355, 145), "row #42", fill=theme.ink, font=F16)
        lock = ["UNLOCKED", "LOCKED", "LOCKED", "UNLOCKED"][step]
        d.text((340, 175), lock, fill=theme.orange if step in (1, 2) else theme.muted, font=F13)

        rounded(d, (PAD, 240, 280, 330), theme, fill=theme.soft)
        d.text((PAD + 70, 260), "Tx A", fill=theme.ink, font=F14)
        a = ["요청", "락 획득", "수정 중", "커밋·해제"][step]
        d.text((PAD + 55, 295), a, fill=theme.orange if step in (1, 2) else theme.muted, font=F13)

        rounded(d, (520, 240, 760, 330), theme, fill=theme.soft)
        d.text((590, 260), "Tx B", fill=theme.ink, font=F14)
        b = ["대기", "대기", "락 대기…", "이어서 수정"][step]
        d.text((560, 295), b, fill=theme.orange if step == 2 else theme.muted, font=F13)

        d.text((PAD, H - PAD - 8), hint, fill=theme.muted, font=F13)
        return img

    frames.append(draw_scene(0, "같은 행을 둘 다 쓰려 함"))
    frames.append(draw_scene(1, "먼저 온 A가 락"))
    frames.append(draw_scene(1, "먼저 온 A가 락"))
    frames.append(draw_scene(2, "B는 대기"))
    frames.append(draw_scene(2, "B는 대기"))
    frames.append(draw_scene(3, "A가 끝나면 B 진행"))
    frames.append(draw_scene(3, "A가 끝나면 B 진행"))
    save_gif("db-lock.gif", frames, theme, duration=600)


CLIPS = [
    clip_array,
    clip_stack,
    clip_queue,
    clip_hash,
    clip_binary_search,
    clip_dfs_bfs,
    clip_two_pointer,
    clip_net_dns,
    clip_net_http,
    clip_net_tcp,
    clip_net_lb,
    clip_os_schedule,
    clip_os_pagefault,
    clip_os_sync,
    clip_os_deadlock,
    clip_os_syscall,
    clip_db_index,
    clip_db_transaction,
    clip_db_isolation,
    clip_db_lock,
    clip_pattern_strategy,
    clip_pattern_observer,
]


if __name__ == "__main__":
    for theme in THEMES:
        for fn in CLIPS:
            fn(theme)
    print("done")
