"""Generate light + dark lecture diagrams (PNG) with Korean-safe fonts."""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from _theme import THEMES, Theme, themed_name  # noqa: E402

OUT = Path(__file__).resolve().parent
PAD = 56
N = ["Skipper", "Kowalski", "Private", "Rico"]


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


def diagram_array(theme: Theme):
    img, d = canvas(780, 280, theme)
    d.text((PAD, PAD), "배열: 인덱스로 바로 접근", fill=theme.ink, font=F_TITLE)
    x0, y0, cw, ch = PAD, 100, 150, 70
    for i, label in enumerate(N):
        x = x0 + i * (cw + 16)
        box(d, (x, y0, x + cw, y0 + ch), theme)
        center_text(d, x + cw / 2, y0 + 28, label, F_BODY, theme.ink)
        center_text(d, x + cw / 2, y0 + ch + 20, f"[{i}]", F_SMALL, theme.muted)
    d.text((PAD, 230), "index 2 → Private  (O(1))", fill=theme.accent, font=F_HINT)
    save("ds-array.png", img, theme)


def diagram_linked(theme: Theme):
    img, d = canvas(820, 270, theme)
    d.text((PAD, PAD), "연결 리스트: 링크로 이어짐", fill=theme.ink, font=F_TITLE)
    nodes = N[:3]
    x0, y0, nw, nh, gap = PAD, 110, 150, 64, 50
    for i, label in enumerate(nodes):
        x = x0 + i * (nw + gap)
        box(d, (x, y0, x + nw - 34, y0 + nh), theme)
        center_text(d, x + (nw - 34) / 2, y0 + nh / 2 - 2, label, F_BODY, theme.ink)
        box(d, (x + nw - 34, y0, x + nw, y0 + nh), theme, fill=theme.soft, radius=0)
        if i < len(nodes) - 1:
            x1, x2 = x + nw + 4, x + nw + gap - 8
            y = y0 + nh / 2
            d.line((x1, y, x2, y), fill=theme.ink, width=2)
            d.polygon([(x2, y), (x2 - 10, y - 6), (x2 - 10, y + 6)], fill=theme.ink)
        else:
            d.text((x + nw + 14, y0 + nh / 2 - 10), "null", fill=theme.muted, font=F_SMALL)
    d.text((PAD, 220), "n번째 접근은 처음부터 따라가야 함  (O(n))", fill=theme.accent, font=F_HINT)
    save("ds-linked-list.png", img, theme)


def diagram_stack(theme: Theme):
    img, d = canvas(700, 360, theme)
    d.text((PAD, PAD), "스택: LIFO (나중에 넣은 것이 먼저)", fill=theme.ink, font=F_TITLE)
    layers = [("Rico", theme.orange), ("Kowalski", theme.fill), ("Skipper", theme.fill)]
    bx, by, bw, bh = 250, 100, 170, 48
    for i, (label, fill) in enumerate(layers):
        y = by + i * (bh + 12)
        box(d, (bx, y, bx + bw, y + bh), theme, fill=fill)
        color = theme.white if fill == theme.orange else theme.ink
        center_text(d, bx + bw / 2, y + bh / 2 - 2, label, F_BODY, color)
    d.text((460, 120), "← pop / peek", fill=theme.muted, font=F_SMALL)
    d.text((460, 240), "↑ push", fill=theme.muted, font=F_SMALL)
    d.text((PAD, 310), "맨 위만 넣고 뺀다", fill=theme.accent, font=F_HINT)
    save("ds-stack.png", img, theme)


def diagram_queue(theme: Theme):
    img, d = canvas(820, 290, theme)
    d.text((PAD, PAD), "큐: FIFO (먼저 넣은 것이 먼저)", fill=theme.ink, font=F_TITLE)
    items = N[:3]
    x0, y0, qw, qh = 160, 120, 140, 60
    d.text((PAD, 138), "out", fill=theme.orange, font=F_BODY)
    d.line((100, 150, 145, 150), fill=theme.orange, width=2)
    d.polygon([(145, 150), (135, 144), (135, 156)], fill=theme.orange)
    for i, label in enumerate(items):
        x = x0 + i * (qw + 16)
        box(d, (x, y0, x + qw, y0 + qh), theme)
        center_text(d, x + qw / 2, y0 + qh / 2 - 2, label, F_BODY, theme.ink)
    end_x = x0 + 3 * (qw + 16) - 16
    d.line((end_x, 150, end_x + 40, 150), fill=theme.ink, width=2)
    d.polygon([(end_x + 40, 150), (end_x + 30, 144), (end_x + 30, 156)], fill=theme.ink)
    d.text((end_x + 50, 138), "in", fill=theme.accent, font=F_BODY)
    d.text((PAD, 230), "앞(dequeue)에서 빼고, 뒤(enqueue)에 넣는다", fill=theme.accent, font=F_HINT)
    save("ds-queue.png", img, theme)


def diagram_hash(theme: Theme):
    img, d = canvas(820, 330, theme)
    d.text((PAD, PAD), "해시 테이블: 키 → 위치", fill=theme.ink, font=F_TITLE)
    box(d, (PAD, 120, 180, 180), theme)
    center_text(d, 114, 148, '"Skipper"', F_BODY, theme.ink)
    d.line((190, 150, 250, 150), fill=theme.ink, width=2)
    d.polygon([(250, 150), (240, 144), (240, 156)], fill=theme.ink)
    box(d, (260, 120, 380, 180), theme, fill=theme.soft)
    center_text(d, 320, 148, "hash()", F_BODY, theme.ink)
    d.line((390, 150, 460, 150), fill=theme.ink, width=2)
    d.polygon([(460, 150), (450, 144), (450, 156)], fill=theme.ink)
    for i, val in enumerate(["…", "25", "…"]):
        y = 90 + i * 52
        box(d, (480, y, 530, y + 40), theme, fill=theme.fill, outline=theme.line, width=1, radius=6)
        center_text(d, 505, y + 18, str(i), F_SMALL, theme.muted)
        fill = theme.highlight if i == 1 else theme.fill
        box(d, (545, y, 700, y + 40), theme, fill=fill)
        center_text(d, 622, y + 18, val, F_BODY, theme.ink if val != "…" else theme.muted)
    d.text((PAD, 270), "평균 조회 O(1) - 같은 칸에 모이면 충돌", fill=theme.accent, font=F_HINT)
    save("ds-hash.png", img, theme)


def diagram_tree(theme: Theme):
    img, d = canvas(700, 420, theme)
    d.text((PAD, PAD), "이진 트리: 계층 구조", fill=theme.ink, font=F_TITLE)

    def node(cx, cy, label, w=130):
        box(d, (cx - w / 2, cy - 24, cx + w / 2, cy + 24), theme)
        center_text(d, cx, cy - 2, label, F_BODY, theme.ink)

    node(350, 110, "Skipper")
    d.line((350, 134, 210, 170), fill=theme.ink, width=2)
    d.line((350, 134, 490, 170), fill=theme.ink, width=2)
    node(210, 200, "Kowalski", 140)
    node(490, 200, "Private", 130)
    d.line((210, 224, 130, 260), fill=theme.ink, width=2)
    node(130, 290, "Rico", 110)
    d.text((PAD, 360), "루트에서 시작해 왼쪽/오른쪽으로 갈라진다", fill=theme.accent, font=F_HINT)
    save("ds-tree.png", img, theme)


def diagram_bst(theme: Theme):
    img, d = canvas(700, 420, theme)
    d.text((PAD, PAD), "BST: 왼쪽 < 나 < 오른쪽", fill=theme.ink, font=F_TITLE)

    def circ(cx, cy, label):
        d.ellipse((cx - 26, cy - 26, cx + 26, cy + 26), fill=theme.fill, outline=theme.ink, width=2)
        center_text(d, cx, cy - 2, label, F_BODY, theme.ink)

    circ(350, 110, "5")
    d.line((350, 136, 220, 170), fill=theme.ink, width=2)
    d.line((350, 136, 480, 170), fill=theme.ink, width=2)
    circ(220, 200, "3")
    circ(480, 200, "7")
    d.line((220, 226, 150, 260), fill=theme.ink, width=2)
    d.line((220, 226, 290, 260), fill=theme.ink, width=2)
    circ(150, 290, "1")
    circ(290, 290, "4")
    d.text((PAD, 360), "균형이면 반씩 줄여 탐색  (O(log n))", fill=theme.accent, font=F_HINT)
    save("ds-bst.png", img, theme)


def diagram_graph(theme: Theme):
    img, d = canvas(700, 420, theme)
    d.text((PAD, PAD), "그래프: 정점과 간선", fill=theme.ink, font=F_TITLE)
    coords = {
        "Skipper": (200, 150),
        "Kowalski": (500, 140),
        "Rico": (510, 290),
        "Private": (190, 300),
    }
    for a, b in [("Skipper", "Kowalski"), ("Skipper", "Private"), ("Kowalski", "Rico")]:
        d.line((*coords[a], *coords[b]), fill=theme.accent, width=2)
    for name, (cx, cy) in coords.items():
        w = 140 if name == "Kowalski" else 120
        box(d, (cx - w / 2, cy - 24, cx + w / 2, cy + 24), theme)
        center_text(d, cx, cy - 2, name, F_BODY, theme.ink)
    d.text((PAD, 360), "관계는 그물처럼 이어질 수 있다 (트리 ⊂ 그래프)", fill=theme.accent, font=F_HINT)
    save("ds-graph.png", img, theme)


def diagram_choose(theme: Theme):
    img, d = canvas(700, 400, theme)
    d.text((PAD, PAD), "선택 기준: 한눈에", fill=theme.ink, font=F_TITLE)
    rows = [
        ("순번으로 찾기", "배열"),
        ("최근 것부터", "스택"),
        ("대기 순서", "큐"),
        ("키로 찾기", "해시"),
        ("계층", "트리"),
        ("복잡한 관계", "그래프"),
    ]
    for i, (left, right) in enumerate(rows):
        y = 100 + i * 42
        box(d, (PAD, y, 290, y + 36), theme, outline=theme.line, width=1, radius=6)
        d.text((PAD + 14, y + 8), left, fill=theme.ink, font=F_SMALL)
        d.line((305, y + 18, 355, y + 18), fill=theme.muted, width=2)
        d.polygon([(355, y + 18), (345, y + 12), (345, y + 24)], fill=theme.muted)
        box(d, (365, y, 580, y + 36), theme, fill=theme.soft, radius=6)
        center_text(d, 472, y + 16, right, F_BODY, theme.ink)
    save("ds-choose.png", img, theme)


def diagram_bigo(theme: Theme):
    img, d = canvas(820, 420, theme)
    d.text((PAD, PAD), "Big-O: 커질수록 얼마나 느려지나", fill=theme.ink, font=F_TITLE)
    ox, oy, top, right = 100, 330, 110, 720
    d.line((ox, top, ox, oy), fill=theme.line, width=2)
    d.line((ox, oy, right, oy), fill=theme.line, width=2)
    d.text((PAD, top), "시간", fill=theme.muted, font=F_SMALL)
    d.text((right + 10, oy - 8), "n", fill=theme.muted, font=F_SMALL)

    blue = (96, 165, 250) if theme.name == "dark" else (37, 99, 235)
    green = (74, 222, 128) if theme.name == "dark" else (22, 163, 74)

    pts2 = []
    for i in range(0, 210, 3):
        x = ox + i
        y = oy - (i * i) / 200
        pts2.append((x, max(top + 6, y)))
    d.line(pts2, fill=theme.orange, width=3)
    d.text((ox + 90, top + 12), "O(n²)", fill=theme.orange, font=F_SMALL)

    ptsn = [(ox, oy), (ox + 360, oy - 180)]
    d.line(ptsn, fill=theme.accent, width=3)
    d.text((ox + 300, oy - 200), "O(n)", fill=theme.accent, font=F_SMALL)

    ptsl = []
    for i in range(1, 400, 4):
        x = ox + i
        y = oy - 26 * math.log2(i + 1)
        ptsl.append((x, y))
    d.line(ptsl, fill=blue, width=3)
    mid_log = ptsl[len(ptsl) // 2]
    d.text((mid_log[0] + 8, mid_log[1] - 24), "O(log n)", fill=blue, font=F_SMALL)

    d.line((ox, oy - 26, ox + 360, oy - 26), fill=green, width=3)
    d.text((ox + 200, oy - 48), "O(1)", fill=green, font=F_SMALL)

    d.text((PAD, 370), "입력 n이 커질 때 기울기 감각만 잡으면 충분하다", fill=theme.accent, font=F_HINT)
    save("algo-bigo.png", img, theme)


def diagram_recursion(theme: Theme):
    img, d = canvas(740, 420, theme)
    d.text((PAD, PAD), "재귀: 같은 모양의 작은 문제로", fill=theme.ink, font=F_TITLE)

    def node(cx, cy, label, w=150, fill=None):
        box(d, (cx - w / 2, cy - 22, cx + w / 2, cy + 22), theme, fill=fill)
        center_text(d, cx, cy - 2, label, F_BODY, theme.ink)

    cx = 370
    node(cx, 100, "fact(4)", 130, theme.highlight)
    d.line((cx, 122, cx, 148), fill=theme.ink, width=2)
    node(cx, 175, "4 × fact(3)", 160)
    d.line((cx, 197, cx, 223), fill=theme.ink, width=2)
    node(cx, 250, "3 × fact(2)", 160)
    d.line((cx, 272, cx, 298), fill=theme.ink, width=2)
    node(cx, 325, "… → 1", 120, theme.soft)
    d.text((PAD, 370), "기저 조건(멈추는 조건)이 있어야 끝난다", fill=theme.accent, font=F_HINT)
    save("algo-recursion.png", img, theme)


def diagram_greedy(theme: Theme):
    img, d = canvas(780, 340, theme)
    d.text((PAD, PAD), "탐욕: 매 순간 좋아 보이는 선택", fill=theme.ink, font=F_TITLE)
    coins = [("500", True), ("100", True), ("50", False), ("10", True)]
    x0, y0 = PAD + 20, 110
    for i, (label, pick) in enumerate(coins):
        x = x0 + i * 160
        fill = theme.highlight if pick else theme.fill
        box(d, (x, y0, x + 120, y0 + 70), theme, fill=fill)
        center_text(d, x + 60, y0 + 22, f"{label}원", F_BODY, theme.ink)
        center_text(
            d,
            x + 60,
            y0 + 48,
            "선택" if pick else "건너뜀",
            F_SMALL,
            theme.orange if pick else theme.muted,
        )
    d.text((PAD, 230), "목표 610원 → 500 + 100 + 10", fill=theme.accent, font=F_HINT)
    d.text((PAD, 270), "항상 최적은 아님. 동전처럼 ‘증명된 규칙’일 때 강하다", fill=theme.muted, font=F_SMALL)
    save("algo-greedy.png", img, theme)


def diagram_dp(theme: Theme):
    img, d = canvas(820, 420, theme)
    d.text((PAD, PAD), "DP: 겹치는 부분 문제를 저장", fill=theme.ink, font=F_TITLE)
    d.text((PAD + 30, 100), "재계산 많음", fill=theme.muted, font=F_SMALL)
    nodes = [
        (180, 150, "f(5)"),
        (120, 215, "f(4)"),
        (240, 215, "f(3)"),
        (70, 290, "f(3)"),
        (170, 290, "f(2)"),
    ]
    for cx, cy, lab in nodes:
        box(d, (cx - 36, cy - 18, cx + 36, cy + 18), theme, outline=theme.line, width=1, radius=6)
        center_text(d, cx, cy - 2, lab, F_SMALL, theme.ink)
    d.line((180, 168, 120, 197), fill=theme.line, width=1)
    d.line((180, 168, 240, 197), fill=theme.line, width=1)
    d.line((120, 233, 70, 272), fill=theme.line, width=1)
    d.line((120, 233, 170, 272), fill=theme.line, width=1)
    d.line((300, 215, 380, 215), fill=theme.ink, width=2)
    d.polygon([(380, 215), (370, 209), (370, 221)], fill=theme.ink)
    d.text((420, 100), "메모에 저장 후 재사용", fill=theme.muted, font=F_SMALL)
    vals = [("f(1)", "1"), ("f(2)", "1"), ("f(3)", "2"), ("f(4)", "3"), ("f(5)", "5")]
    for i, (k, v) in enumerate(vals):
        y = 130 + i * 40
        box(d, (420, y, 520, y + 32), theme, outline=theme.line, width=1, radius=6)
        center_text(d, 470, y + 14, k, F_SMALL, theme.ink)
        fill = theme.highlight if i == 4 else theme.fill
        box(d, (540, y, 640, y + 32), theme, fill=fill, radius=6)
        center_text(d, 590, y + 14, v, F_BODY, theme.ink)
    d.text((PAD, 360), "한 번 구한 답은 다시 계산하지 않는다", fill=theme.accent, font=F_HINT)
    save("algo-dp.png", img, theme)


def diagram_sort(theme: Theme):
    img, d = canvas(820, 340, theme)
    d.text((PAD, PAD), "정렬: 섞인 데이터를 순서로", fill=theme.ink, font=F_TITLE)
    before = [7, 2, 9, 1]
    after = [1, 2, 7, 9]
    d.text((PAD + 20, 95), "Before", fill=theme.muted, font=F_SMALL)
    for i, v in enumerate(before):
        x = PAD + 20 + i * 72
        box(d, (x, 125, x + 56, 175), theme)
        center_text(d, x + 28, 148, str(v), F_BODY, theme.ink)
    d.line((360, 150, 420, 150), fill=theme.ink, width=2)
    d.polygon([(420, 150), (410, 144), (410, 156)], fill=theme.ink)
    d.text((450, 95), "After", fill=theme.muted, font=F_SMALL)
    for i, v in enumerate(after):
        x = 450 + i * 72
        fill = theme.highlight if i == 0 else theme.fill
        box(d, (x, 125, x + 56, 175), theme, fill=fill)
        center_text(d, x + 28, 148, str(v), F_BODY, theme.ink)
    d.text((PAD, 230), "비교 기반 정렬은 보통 평균 O(n log n)이 실무 기본선", fill=theme.accent, font=F_HINT)
    d.text((PAD, 270), "선택/삽입/버블은 이해용, 병합/퀵/힙은 성능용 (퀵 최악 n²)", fill=theme.muted, font=F_SMALL)
    save("algo-sort.png", img, theme)


def diagram_os_process_thread(theme: Theme):
    img, d = canvas(860, 420, theme)
    d.text((PAD, PAD), "프로세스 vs 스레드", fill=theme.ink, font=F_TITLE)

    # Process A
    box(d, (PAD, 100, 390, 300), theme, fill=theme.soft, outline=theme.line, width=2, radius=12)
    d.text((PAD + 18, 112), "Process A", fill=theme.ink, font=F_BODY)
    d.text((PAD + 18, 142), "자체 메모리 공간", fill=theme.muted, font=F_SMALL)
    for i, label in enumerate(["Thread 1", "Thread 2"]):
        x = PAD + 30 + i * 150
        box(d, (x, 190, x + 130, 250), theme, fill=theme.highlight if i == 0 else theme.fill)
        center_text(d, x + 65, 218, label, F_SMALL, theme.ink)
    d.text((PAD + 30, 268), "스레드는 메모리 공유", fill=theme.accent, font=F_SMALL)

    # Process B
    box(d, (450, 100, 800, 300), theme, fill=theme.soft, outline=theme.line, width=2, radius=12)
    d.text((468, 112), "Process B", fill=theme.ink, font=F_BODY)
    d.text((468, 142), "격리된 주소 공간", fill=theme.muted, font=F_SMALL)
    box(d, (500, 190, 750, 250), theme, fill=theme.fill)
    center_text(d, 625, 218, "Thread 1", F_SMALL, theme.ink)
    d.text((500, 268), "프로세스는 서로 분리", fill=theme.accent, font=F_SMALL)

    d.text((PAD, 340), "상자 = 프로세스, 상자 안 일꾼 = 스레드", fill=theme.accent, font=F_HINT)
    d.text((PAD, 372), "같은 상자 안에서는 공유, 다른 상자와는 격리", fill=theme.muted, font=F_SMALL)
    save("os-process-thread.png", img, theme)


def diagram_os_memory_layout(theme: Theme):
    img, d = canvas(720, 480, theme)
    d.text((PAD, PAD), "프로세스 메모리 레이아웃", fill=theme.ink, font=F_TITLE)

    regions = [
        ("Stack", "함수 호출 · 지역 변수", theme.highlight, "↑ 성장"),
        ("Heap", "동적 할당 (new / malloc)", theme.fill, "↓ 성장"),
        ("Data / BSS", "전역 · 정적 변수", theme.soft, ""),
        ("Text (Code)", "실행 코드", theme.fill, ""),
    ]
    x0, y0, bw, bh = 180, 100, 320, 70
    for i, (title, desc, fill, growth) in enumerate(regions):
        y = y0 + i * (bh + 12)
        box(d, (x0, y, x0 + bw, y + bh), theme, fill=fill)
        d.text((x0 + 18, y + 14), title, fill=theme.ink, font=F_BODY)
        d.text((x0 + 18, y + 40), desc, fill=theme.muted, font=F_SMALL)
        if growth:
            d.text((x0 + bw + 16, y + 24), growth, fill=theme.orange, font=F_SMALL)

    d.text((PAD, 420), "높은 주소 ↔ 낮은 주소. 스택과 힙이 가운데로 자란다", fill=theme.accent, font=F_HINT)
    save("os-memory-layout.png", img, theme)


def diagram_os_deadlock(theme: Theme):
    img, d = canvas(820, 420, theme)
    d.text((PAD, PAD), "데드락: 서로 기다리며 멈춤", fill=theme.ink, font=F_TITLE)

    # Two actors
    box(d, (120, 130, 300, 210), theme, fill=theme.highlight)
    center_text(d, 210, 158, "Skipper", F_BODY, theme.ink)
    center_text(d, 210, 186, "펜 보유", F_SMALL, theme.muted)

    box(d, (520, 130, 700, 210), theme, fill=theme.highlight)
    center_text(d, 610, 158, "Kowalski", F_BODY, theme.ink)
    center_text(d, 610, 186, "노트 보유", F_SMALL, theme.muted)

    # Resources
    box(d, (120, 280, 300, 340), theme, fill=theme.fill)
    center_text(d, 210, 308, "노트 대기", F_BODY, theme.ink)

    box(d, (520, 280, 700, 340), theme, fill=theme.fill)
    center_text(d, 610, 308, "펜 대기", F_BODY, theme.ink)

    # Cycle arrows
    d.line((300, 170, 520, 170), fill=theme.orange, width=3)
    d.polygon([(520, 170), (508, 164), (508, 176)], fill=theme.orange)
    d.text((360, 140), "노트 원함", fill=theme.orange, font=F_SMALL)

    d.line((520, 310, 300, 310), fill=theme.orange, width=3)
    d.polygon([(300, 310), (312, 304), (312, 316)], fill=theme.orange)
    d.text((360, 320), "펜 원함", fill=theme.orange, font=F_SMALL)

    d.line((210, 210, 210, 280), fill=theme.line, width=2)
    d.line((610, 210, 610, 280), fill=theme.line, width=2)

    d.text((PAD, 370), "순환 대기: A→B, B→A. 네 조건이 겹치면 데드락", fill=theme.accent, font=F_HINT)
    save("os-deadlock.png", img, theme)


ALL = [
    diagram_array,
    diagram_linked,
    diagram_stack,
    diagram_queue,
    diagram_hash,
    diagram_tree,
    diagram_bst,
    diagram_graph,
    diagram_choose,
    diagram_bigo,
    diagram_recursion,
    diagram_greedy,
    diagram_dp,
    diagram_sort,
    diagram_os_process_thread,
    diagram_os_memory_layout,
    diagram_os_deadlock,
]


if __name__ == "__main__":
    for theme in THEMES:
        for fn in ALL:
            fn(theme)
    print("done")
