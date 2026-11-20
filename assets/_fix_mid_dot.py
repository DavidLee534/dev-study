from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
files = list((root / "cs").rglob("*.md")) + [
    root / "assets" / "diagrams" / "_build.py",
    root / "assets" / "videos" / "_build_clips.py",
    root / "cs" / "_make_preview.py",
    root / ".cursor" / "rules" / "markdown-profile-style.mdc",
    root / "assets" / "sections" / "banner-cs.svg",
]

pairs = [
    ("삽입 - 삭제 - 조회", "삽입/삭제/조회"),
    ("삽입 - 삭제", "삽입/삭제"),
    ("이해 - 구현", "이해/구현"),
    ("면접 - 시험", "면접/시험"),
    ("탐색 - 삽입", "탐색/삽입"),
    ("연결 - 사이클", "연결/사이클"),
    ("왼쪽 - 오른쪽", "왼쪽/오른쪽"),
    ("시간 - 공간", "시간/공간"),
    ("행 - 열 - 기본키 - 외래키", "행/열/기본키/외래키"),
    ("스택 - 힙", "스택/힙"),
    ("단순 - 속도", "단순/속도"),
    ("실행 - 메모리 - 파일 - 동시성", "실행/메모리/파일/동시성"),
    ("백엔드 - 모바일 - 인프라", "백엔드/모바일/인프라"),
    ("순서 보장 - 메모리 - 구현", "순서 보장/메모리/구현"),
    ("라이트 - 슬레이트", "라이트 슬레이트"),
    ("그림자 - 둥근", "그림자/둥근"),
    ("Lecture notes - concepts first", "Lecture notes / concepts first"),
    ("다이어그램 - 짧은 영상", "다이어그램과 짧은 영상"),
    ("`01 -` 번호", "`01.` 번호"),
    ("### 01 - 제목", "### 01. 제목"),
    ("- **Label** - 설명", "- **Label**: 설명"),
]


def fix(text: str) -> str:
    text = re.sub(r"(#{1,6}\s*)(\d{2})\s*-\s+", r"\1\2. ", text)
    text = re.sub(r"(\[\s*)(\d{2})\s*-\s+", r"\1\2. ", text)
    text = re.sub(r"(\*\*[^*]+\*\*)\s*-\s+", r"\1: ", text)
    for a, b in pairs:
        text = text.replace(a, b)
    text = text.replace("Lecture notes - concepts first", "Lecture notes / concepts first")
    return text


for p in files:
    if not p.exists():
        continue
    old = p.read_text(encoding="utf-8")
    new = fix(old)
    if new != old:
        p.write_text(new, encoding="utf-8")
        print("fixed", p.relative_to(root))
