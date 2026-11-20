"""Generate *-dark.svg section headers from light SVGs."""
from pathlib import Path

OUT = Path(__file__).resolve().parent

REPLACEMENTS = [
    ("#F8FAFC", "#0B1220"),
    ("#FFFFFF", "#111827"),
    ("#0F172A", "#E2E8F0"),
    ("#64748B", "#94A3B8"),
]


def main():
    for path in sorted(OUT.glob("*.svg")):
        if path.name.endswith("-dark.svg") or path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        dark = OUT / f"{path.stem}-dark.svg"
        dark.write_text(text, encoding="utf-8")
        print("wrote", dark.name)


if __name__ == "__main__":
    main()
