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
    img, d = canvas(720, 500, theme)
    d.text((PAD, PAD), "프로세스 메모리 레이아웃", fill=theme.ink, font=F_TITLE)

    # 위 = 높은 주소: 스택은 아래로, 힙은 위로 자란다
    regions = [
        ("Stack", "함수 호출 · 지역 변수", theme.highlight, "↓ 성장"),
        ("Heap", "동적 할당 (new / malloc)", theme.fill, "↑ 성장"),
        ("Data / BSS", "전역 · 정적 변수", theme.soft, ""),
        ("Text (Code)", "실행 코드", theme.fill, ""),
    ]
    x0, y0, bw, bh = 180, 110, 320, 70
    for i, (title, desc, fill, growth) in enumerate(regions):
        y = y0 + i * (bh + 12)
        box(d, (x0, y, x0 + bw, y + bh), theme, fill=fill)
        d.text((x0 + 18, y + 14), title, fill=theme.ink, font=F_BODY)
        d.text((x0 + 18, y + 40), desc, fill=theme.muted, font=F_SMALL)
        if growth:
            d.text((x0 + bw + 16, y + 24), growth, fill=theme.orange, font=F_SMALL)

    d.text((x0 - 8, y0 - 22), "높은 주소", fill=theme.muted, font=F_SMALL)
    d.text((x0 - 8, y0 + 4 * (bh + 12) - 8), "낮은 주소", fill=theme.muted, font=F_SMALL)
    d.text((PAD, 440), "위가 높은 주소. 스택은 아래·힙은 위로 가운데를 향해 자란다", fill=theme.accent, font=F_HINT)
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


def diagram_net_layers(theme: Theme):
    img, d = canvas(720, 420, theme)
    d.text((PAD, PAD), "TCP/IP 계층: 역할을 층으로", fill=theme.ink, font=F_TITLE)
    layers = [
        ("Application", "HTTP · DNS · SSH", theme.highlight),
        ("Transport", "TCP / UDP · 포트", theme.fill),
        ("Internet", "IP 주소 · 라우팅", theme.soft),
        ("Link", "같은 구간 전달", theme.fill),
    ]
    x0, y0, bw, bh = 160, 100, 400, 58
    for i, (title, desc, fill) in enumerate(layers):
        y = y0 + i * (bh + 10)
        box(d, (x0, y, x0 + bw, y + bh), theme, fill=fill)
        d.text((x0 + 18, y + 10), title, fill=theme.ink, font=F_BODY)
        d.text((x0 + 18, y + 34), desc, fill=theme.muted, font=F_SMALL)
    d.text((PAD, 370), "위는 말의 내용, 아래는 실어 나르는 방법", fill=theme.accent, font=F_HINT)
    save("net-layers.png", img, theme)


def diagram_net_dns_port(theme: Theme):
    img, d = canvas(860, 360, theme)
    d.text((PAD, PAD), "DNS → IP, 그리고 포트", fill=theme.ink, font=F_TITLE)

    box(d, (PAD, 120, 250, 200), theme, fill=theme.soft)
    center_text(d, 150, 148, "example.com", F_BODY, theme.ink)
    center_text(d, 150, 176, "이름", F_SMALL, theme.muted)

    d.line((260, 160, 330, 160), fill=theme.ink, width=2)
    d.polygon([(330, 160), (318, 154), (318, 166)], fill=theme.ink)
    d.text((265, 128), "DNS", fill=theme.orange, font=F_SMALL)

    box(d, (340, 120, 520, 200), theme, fill=theme.highlight)
    center_text(d, 430, 148, "93.184.216.34", F_BODY, theme.ink)
    center_text(d, 430, 176, "IP 주소", F_SMALL, theme.muted)

    d.line((530, 160, 600, 160), fill=theme.ink, width=2)
    d.polygon([(600, 160), (588, 154), (588, 166)], fill=theme.ink)
    d.text((535, 128), "+ port", fill=theme.orange, font=F_SMALL)

    box(d, (610, 120, 800, 200), theme, fill=theme.fill)
    center_text(d, 705, 148, ":443", F_BODY, theme.ink)
    center_text(d, 705, 176, "HTTPS 문", F_SMALL, theme.muted)

    d.text((PAD, 250), "건물(IP) + 호수(포트)로 서비스에 도착한다", fill=theme.accent, font=F_HINT)
    d.text((PAD, 290), "DNS는 상호(이름)를 주소로 바꿔 주는 전화부", fill=theme.muted, font=F_SMALL)
    save("net-dns-port.png", img, theme)


def diagram_net_http(theme: Theme):
    img, d = canvas(820, 360, theme)
    d.text((PAD, PAD), "HTTP: 요청 한 번, 응답 한 번", fill=theme.ink, font=F_TITLE)

    box(d, (PAD, 120, 260, 220), theme, fill=theme.soft)
    center_text(d, 158, 150, "Client", F_BODY, theme.ink)
    center_text(d, 158, 180, "Browser / App", F_SMALL, theme.muted)

    box(d, (560, 120, 760, 220), theme, fill=theme.soft)
    center_text(d, 660, 150, "Server", F_BODY, theme.ink)
    center_text(d, 660, 180, "API / Web", F_SMALL, theme.muted)

    d.line((270, 145, 540, 145), fill=theme.orange, width=3)
    d.polygon([(540, 145), (528, 139), (528, 151)], fill=theme.orange)
    d.text((330, 112), "Request  GET /users", fill=theme.orange, font=F_SMALL)

    d.line((540, 195, 270, 195), fill=theme.accent, width=3)
    d.polygon([(270, 195), (282, 189), (282, 201)], fill=theme.accent)
    d.text((330, 210), "Response  200 JSON", fill=theme.accent, font=F_SMALL)

    d.text((PAD, 280), "HTTPS는 이 대화를 TLS로 감싼다", fill=theme.accent, font=F_HINT)
    save("net-http.png", img, theme)


def diagram_net_lb(theme: Theme):
    img, d = canvas(820, 400, theme)
    d.text((PAD, PAD), "로드밸런서: 요청을 나누어 전달", fill=theme.ink, font=F_TITLE)

    box(d, (PAD, 160, 200, 230), theme, fill=theme.soft)
    center_text(d, 128, 193, "Client", F_BODY, theme.ink)

    d.line((210, 195, 300, 195), fill=theme.ink, width=2)
    d.polygon([(300, 195), (288, 189), (288, 201)], fill=theme.ink)

    box(d, (310, 150, 500, 240), theme, fill=theme.highlight)
    center_text(d, 405, 180, "Load Balancer", F_BODY, theme.ink)
    center_text(d, 405, 208, "안내 데스크", F_SMALL, theme.muted)

    targets = [("App 1", 120), ("App 2", 195), ("App 3", 270)]
    for label, y in targets:
        d.line((500, 195, 580, y + 25), fill=theme.line, width=2)
        box(d, (580, y, 760, y + 50), theme, fill=theme.fill)
        center_text(d, 670, y + 23, label, F_BODY, theme.ink)

    d.text((PAD, 340), "죽은 인스턴스는 health check로 빼 둔다", fill=theme.accent, font=F_HINT)
    save("net-lb.png", img, theme)


def diagram_db_keys(theme: Theme):
    img, d = canvas(860, 400, theme)
    d.text((PAD, PAD), "관계형: PK와 FK", fill=theme.ink, font=F_TITLE)

    box(d, (PAD, 110, 360, 300), theme, fill=theme.soft)
    d.text((PAD + 20, 125), "users", fill=theme.ink, font=F_BODY)
    headers = [("id PK", True), ("name", False)]
    for i, (h, pk) in enumerate(headers):
        x = PAD + 20 + i * 140
        fill = theme.highlight if pk else theme.fill
        box(d, (x, 170, x + 120, 210), theme, fill=fill)
        center_text(d, x + 60, 188, h, F_SMALL, theme.ink)
    box(d, (PAD + 20, 230, PAD + 140, 270), theme, fill=theme.fill)
    center_text(d, PAD + 80, 248, "1", F_BODY, theme.ink)
    box(d, (PAD + 160, 230, PAD + 280, 270), theme, fill=theme.fill)
    center_text(d, PAD + 220, 248, "Skipper", F_SMALL, theme.ink)

    box(d, (480, 110, 820, 300), theme, fill=theme.soft)
    d.text((500, 125), "orders", fill=theme.ink, font=F_BODY)
    for i, (h, fk) in enumerate([("id PK", False), ("user_id FK", True)]):
        x = 500 + i * 150
        fill = theme.highlight if fk else theme.fill
        box(d, (x, 170, x + 130, 210), theme, fill=fill)
        center_text(d, x + 65, 188, h, F_SMALL, theme.ink)
    box(d, (500, 230, 630, 270), theme, fill=theme.fill)
    center_text(d, 565, 248, "10", F_BODY, theme.ink)
    box(d, (650, 230, 780, 270), theme, fill=theme.highlight)
    center_text(d, 715, 248, "1", F_BODY, theme.ink)

    # FK(orders) → PK(users)
    d.line((470, 250, 370, 250), fill=theme.orange, width=3)
    d.polygon([(370, 250), (382, 244), (382, 256)], fill=theme.orange)
    d.text((380, 220), "FK → PK", fill=theme.orange, font=F_SMALL)
    d.text((PAD, 340), "FK는 다른 표의 PK를 가리킨다", fill=theme.accent, font=F_HINT)
    save("db-keys.png", img, theme)


def diagram_db_normalize(theme: Theme):
    img, d = canvas(860, 420, theme)
    d.text((PAD, PAD), "정규화: 중복을 표로 분리", fill=theme.ink, font=F_TITLE)

    d.text((PAD, 100), "Before", fill=theme.muted, font=F_SMALL)
    box(d, (PAD, 125, 400, 250), theme, fill=theme.fill)
    d.text((PAD + 16, 140), "order + address 한 줄에 반복", fill=theme.ink, font=F_SMALL)
    d.text((PAD + 16, 175), "10 | Skipper | Seoul", fill=theme.muted, font=F_SMALL)
    d.text((PAD + 16, 205), "11 | Skipper | Seoul", fill=theme.muted, font=F_SMALL)
    d.text((PAD + 16, 235), "주소 바뀌면 여러 줄 수정", fill=theme.orange, font=F_SMALL)

    d.line((420, 190, 470, 190), fill=theme.ink, width=2)
    d.polygon([(470, 190), (458, 184), (458, 196)], fill=theme.ink)

    d.text((490, 100), "After", fill=theme.muted, font=F_SMALL)
    box(d, (490, 125, 800, 185), theme, fill=theme.soft)
    center_text(d, 645, 145, "users: 1 Skipper Seoul", F_SMALL, theme.ink)
    box(d, (490, 205, 800, 280), theme, fill=theme.highlight)
    d.text((510, 220), "orders: 10 → user 1", fill=theme.ink, font=F_SMALL)
    d.text((510, 248), "orders: 11 → user 1", fill=theme.ink, font=F_SMALL)

    d.text((PAD, 340), "한 곳만 고치면 전체가 맞는다", fill=theme.accent, font=F_HINT)
    save("db-normalize.png", img, theme)


def diagram_db_join(theme: Theme):
    img, d = canvas(860, 380, theme)
    d.text((PAD, PAD), "조인: 표를 조건으로 이어 붙임", fill=theme.ink, font=F_TITLE)

    box(d, (PAD, 120, 280, 260), theme, fill=theme.soft)
    center_text(d, 168, 150, "users", F_BODY, theme.ink)
    d.text((PAD + 30, 190), "1 Skipper", fill=theme.muted, font=F_SMALL)
    d.text((PAD + 30, 220), "2 Kowalski", fill=theme.muted, font=F_SMALL)

    box(d, (320, 120, 540, 260), theme, fill=theme.soft)
    center_text(d, 430, 150, "orders", F_BODY, theme.ink)
    d.text((340, 190), "10 → 1", fill=theme.muted, font=F_SMALL)
    d.text((340, 220), "11 → 1", fill=theme.muted, font=F_SMALL)

    d.line((550, 190, 600, 190), fill=theme.ink, width=2)
    d.polygon([(600, 190), (588, 184), (588, 196)], fill=theme.ink)

    box(d, (610, 120, 820, 260), theme, fill=theme.highlight)
    center_text(d, 715, 150, "결과", F_BODY, theme.ink)
    d.text((630, 190), "10 Skipper", fill=theme.ink, font=F_SMALL)
    d.text((630, 220), "11 Skipper", fill=theme.ink, font=F_SMALL)

    d.text((PAD, 310), "user_id = id 로 맞춘다. 양이 크면 비용이 난다", fill=theme.accent, font=F_HINT)
    save("db-join.png", img, theme)


def diagram_db_nosql(theme: Theme):
    img, d = canvas(860, 400, theme)
    d.text((PAD, PAD), "관계형 vs NoSQL 모양", fill=theme.ink, font=F_TITLE)

    box(d, (PAD, 110, 380, 300), theme, fill=theme.soft)
    center_text(d, 218, 140, "Relational", F_BODY, theme.ink)
    d.text((PAD + 30, 180), "표 · 행 · 조인", fill=theme.muted, font=F_SMALL)
    d.text((PAD + 30, 215), "강한 스키마 · ACID", fill=theme.muted, font=F_SMALL)
    d.text((PAD + 30, 250), "복잡한 관계에 강함", fill=theme.ink, font=F_SMALL)

    box(d, (460, 110, 800, 300), theme, fill=theme.highlight)
    center_text(d, 630, 140, "NoSQL 예", F_BODY, theme.ink)
    d.text((480, 180), "Document: JSON 한 덩어리", fill=theme.ink, font=F_SMALL)
    d.text((480, 215), "Key-Value: 키로 바로 조회", fill=theme.ink, font=F_SMALL)
    d.text((480, 250), "유연한 스키마 · 확장 패턴", fill=theme.muted, font=F_SMALL)

    d.text((PAD, 340), "데이터 모양과 접근 패턴에 맞는 도구를 고른다", fill=theme.accent, font=F_HINT)
    save("db-nosql.png", img, theme)


def diagram_pattern_solid(theme: Theme):
    img, d = canvas(860, 420, theme)
    d.text((PAD, PAD), "SOLID: 바꾸기 쉬운 역할 나누기", fill=theme.ink, font=F_TITLE)
    items = [
        ("S", "한 가지 이유로 변경"),
        ("O", "확장에 열고 수정에 닫기"),
        ("L", "하위 타입 교체 가능"),
        ("I", "얇은 인터페이스"),
        ("D", "추상에 의존"),
    ]
    for i, (letter, desc) in enumerate(items):
        y = 100 + i * 52
        box(d, (PAD, y, PAD + 70, y + 40), theme, fill=theme.highlight)
        center_text(d, PAD + 35, y + 18, letter, F_BODY, theme.ink)
        box(d, (PAD + 90, y, 780, y + 40), theme, fill=theme.fill)
        d.text((PAD + 110, y + 10), desc, fill=theme.ink, font=F_SMALL)
    d.text((PAD, 375), "암기보다 ‘어디를 고치면 무엇이 깨지나’", fill=theme.accent, font=F_HINT)
    save("pattern-solid.png", img, theme)


def diagram_pattern_singleton(theme: Theme):
    img, d = canvas(780, 360, theme)
    d.text((PAD, PAD), "Singleton: 인스턴스 하나", fill=theme.ink, font=F_TITLE)
    box(d, (280, 120, 500, 220), theme, fill=theme.highlight)
    center_text(d, 390, 155, "Config", F_BODY, theme.ink)
    center_text(d, 390, 185, "유일한 인스턴스", F_SMALL, theme.muted)
    for x, label in [(100, "A"), (340, "B"), (580, "C")]:
        box(d, (x, 260, x + 100, 310), theme, fill=theme.soft)
        center_text(d, x + 50, 282, label, F_BODY, theme.ink)
        d.line((x + 50, 260, 390, 220), fill=theme.line, width=2)
    d.text((PAD, 320), "모두가 같은 하나를 가리킨다", fill=theme.accent, font=F_HINT)
    save("pattern-singleton.png", img, theme)


def diagram_pattern_factory(theme: Theme):
    img, d = canvas(820, 360, theme)
    d.text((PAD, PAD), "Factory: 생성 책임을 분리", fill=theme.ink, font=F_TITLE)
    box(d, (PAD, 140, 220, 240), theme, fill=theme.soft)
    center_text(d, 138, 180, "Client", F_BODY, theme.ink)
    d.line((230, 190, 300, 190), fill=theme.ink, width=2)
    d.polygon([(300, 190), (288, 184), (288, 196)], fill=theme.ink)
    box(d, (310, 140, 510, 240), theme, fill=theme.highlight)
    center_text(d, 410, 170, "Factory", F_BODY, theme.ink)
    center_text(d, 410, 200, "create()", F_SMALL, theme.muted)
    d.line((520, 190, 590, 190), fill=theme.ink, width=2)
    d.polygon([(590, 190), (578, 184), (578, 196)], fill=theme.ink)
    box(d, (600, 140, 780, 240), theme, fill=theme.fill)
    center_text(d, 690, 180, "Product", F_BODY, theme.ink)
    d.text((PAD, 290), "호출부는 new 세부 조건을 몰라도 된다", fill=theme.accent, font=F_HINT)
    save("pattern-factory.png", img, theme)


def diagram_pattern_adapter(theme: Theme):
    img, d = canvas(820, 360, theme)
    d.text((PAD, PAD), "Adapter: 입구를 맞춰 연결", fill=theme.ink, font=F_TITLE)
    box(d, (PAD, 140, 240, 240), theme, fill=theme.soft)
    center_text(d, 148, 170, "Our API", F_BODY, theme.ink)
    center_text(d, 148, 200, "pay()", F_SMALL, theme.muted)
    d.line((250, 190, 320, 190), fill=theme.ink, width=2)
    d.polygon([(320, 190), (308, 184), (308, 196)], fill=theme.ink)
    box(d, (330, 140, 520, 240), theme, fill=theme.highlight)
    center_text(d, 425, 170, "Adapter", F_BODY, theme.ink)
    center_text(d, 425, 200, "번역", F_SMALL, theme.muted)
    d.line((530, 190, 600, 190), fill=theme.ink, width=2)
    d.polygon([(600, 190), (588, 184), (588, 196)], fill=theme.ink)
    box(d, (610, 140, 800, 240), theme, fill=theme.fill)
    center_text(d, 705, 170, "Legacy SDK", F_BODY, theme.ink)
    center_text(d, 705, 200, "charge()", F_SMALL, theme.muted)
    d.text((PAD, 290), "기존 것을 바꾸지 않고 인터페이스만 맞춤", fill=theme.accent, font=F_HINT)
    save("pattern-adapter.png", img, theme)


def diagram_pattern_decorator(theme: Theme):
    img, d = canvas(820, 400, theme)
    d.text((PAD, PAD), "Decorator: 감싸서 기능 추가", fill=theme.ink, font=F_TITLE)
    layers = [
        (200, "Logging", theme.highlight),
        (280, "Auth", theme.soft),
        (360, "Handler", theme.fill),
    ]
    for y, label, fill in layers:
        box(d, (220, y - 40, 580, y + 20), theme, fill=fill)
        center_text(d, 400, y - 12, label, F_BODY, theme.ink)
    d.text((PAD, 330), "같은 인터페이스를 유지한 채 겹겹이 확장", fill=theme.accent, font=F_HINT)
    save("pattern-decorator.png", img, theme)


def diagram_pattern_mvc(theme: Theme):
    img, d = canvas(860, 380, theme)
    d.text((PAD, PAD), "MVC / 계층: 역할을 나눔", fill=theme.ink, font=F_TITLE)
    cols = [
        (PAD, "Controller", "요청·응답", theme.soft),
        (310, "Service", "업무 규칙", theme.highlight),
        (560, "Repository", "저장", theme.fill),
    ]
    for x, title, desc, fill in cols:
        box(d, (x, 130, x + 220, 260), theme, fill=fill)
        center_text(d, x + 110, 175, title, F_BODY, theme.ink)
        center_text(d, x + 110, 215, desc, F_SMALL, theme.muted)
    d.line((270, 195, 300, 195), fill=theme.ink, width=2)
    d.polygon([(300, 195), (288, 189), (288, 201)], fill=theme.ink)
    d.line((530, 195, 560, 195), fill=theme.ink, width=2)
    d.polygon([(560, 195), (548, 189), (548, 201)], fill=theme.ink)
    d.text((PAD, 310), "한쪽 변화가 전체에 덜 번지게", fill=theme.accent, font=F_HINT)
    save("pattern-mvc.png", img, theme)


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
    diagram_net_layers,
    diagram_net_dns_port,
    diagram_net_http,
    diagram_net_lb,
    diagram_db_keys,
    diagram_db_normalize,
    diagram_db_join,
    diagram_db_nosql,
    diagram_pattern_solid,
    diagram_pattern_singleton,
    diagram_pattern_factory,
    diagram_pattern_adapter,
    diagram_pattern_decorator,
    diagram_pattern_mvc,
]


if __name__ == "__main__":
    for theme in THEMES:
        for fn in ALL:
            fn(theme)
    print("done")
