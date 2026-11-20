"""Replace plain <img src="...assets/..."> with light/dark <picture> in cs/*.md."""
import re
from pathlib import Path

CS = Path(__file__).resolve().parent.parent / "cs"

IMG_RE = re.compile(
    r'<img\s+src="(\.\./assets/(?:sections|diagrams|videos)/([^"]+))"([^>]*)/>',
    re.MULTILINE,
)


def dark_src(filename: str) -> str:
    if "." not in filename:
        return f"{filename}-dark"
    stem, ext = filename.rsplit(".", 1)
    if stem.endswith("-dark"):
        return filename
    return f"{stem}-dark.{ext}"


def replacer(match: re.Match) -> str:
    full = match.group(1)
    name = match.group(2)
    attrs = match.group(3)
    if "-dark." in name:
        return match.group(0)
    folder = full.rsplit("/", 1)[0]
    dark = f"{folder}/{dark_src(name)}"
    # keep width/alt on img; picture wraps both
    return (
        "<picture>\n"
        f'  <source media="(prefers-color-scheme: dark)" srcset="{dark}" />\n'
        f'  <img src="{full}"{attrs}/>\n'
        "</picture>"
    )


def main():
    for path in sorted(CS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "<picture>" in text:
            # idempotent: strip existing picture wrappers first? skip if already done
            print("skip (already has picture):", path.name)
            continue
        new = IMG_RE.sub(replacer, text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            print("updated", path.name)
        else:
            print("no img change:", path.name)


if __name__ == "__main__":
    main()
