from __future__ import annotations
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: extract_pdf_text.py <src.pdf> <out.txt>")
        return 2
    src = Path(argv[1]).expanduser().resolve()
    dst = Path(argv[2]).expanduser().resolve()
    try:
        from pdfminer.high_level import extract_text
    except Exception as e:
        print("Missing dependency: pdfminer.six. Please install it (e.g., pixi run python -m pip install pdfminer.six)")
        print(f"Details: {e}")
        return 3

    if not src.exists():
        print(f"Source PDF not found: {src}")
        return 4

    dst.parent.mkdir(parents=True, exist_ok=True)
    text = extract_text(str(src)) or ""
    dst.write_text(text, encoding="utf-8")
    print(f"Wrote {dst} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
