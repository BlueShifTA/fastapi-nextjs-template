from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def main() -> int:
    (ROOT / ".template-cleaned").write_text(
        "After first successful build, remove template sample routes/components/docs.\n",
        encoding="utf-8",
    )
    print("Wrote .template-cleaned")
    print("Remove template-only items after verifying your real project builds:")
    print("- sample item routes/tests if not needed")
    print("- placeholder branding in README/CLAUDE.md/ProjectMap.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
