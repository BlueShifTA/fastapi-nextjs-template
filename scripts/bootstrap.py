from __future__ import annotations

import argparse
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _slug_to_package(slug: str) -> str:
    pkg = slug.replace("-", "_")
    if not re.fullmatch(r"[a-z_][a-z0-9_]*", pkg):
        raise ValueError(f"invalid package name from slug: {slug}")
    return pkg


def _replace(path: pathlib.Path, replacements: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    new = text
    for old, value in replacements.items():
        new = new.replace(old, value)
    if new != text:
        path.write_text(new, encoding="utf-8")
        print(f"updated {path.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-name", default="My App")
    parser.add_argument("--project-slug", default="my-app")
    parser.add_argument("--python-package")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    package_name = args.python_package or _slug_to_package(args.project_slug)
    replacements = {
        "FastAPI + Next.js Template": f"{args.project_name} Template",
        "app_template": package_name,
        "App Template": args.project_name,
        "app-template": args.project_slug,
    }

    src_dir = ROOT / "backend/app_template"
    dst_dir = ROOT / f"backend/{package_name}"
    if src_dir.exists() and dst_dir != src_dir:
        if args.dry_run:
            print(
                f"would rename {src_dir.relative_to(ROOT)} -> {dst_dir.relative_to(ROOT)}"
            )
        else:
            shutil.move(str(src_dir), str(dst_dir))
            print(f"renamed {src_dir.relative_to(ROOT)} -> {dst_dir.relative_to(ROOT)}")

    targets = [
        ROOT / "README.md",
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / "ProjectMap.md",
        ROOT / "pyproject.toml",
        ROOT / "justfile",
    ]
    for path in (ROOT / "backend").rglob("*.py"):
        targets.append(path)
    for path in (ROOT / "backend/tests").rglob("*.py"):
        targets.append(path)

    for path in targets:
        if path.exists():
            if args.dry_run:
                print(f"would update {path.relative_to(ROOT)}")
            else:
                _replace(path, replacements)

    print("Next: just install && just test && just lint, then just template-clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
