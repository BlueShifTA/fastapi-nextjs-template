from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]

CONTENT = """# ProjectMap

Fast search map for `fastapi-nextjs-template`.

## Top-Level Map

```text
fastapi-nextjs-template/
├── CLAUDE.md
├── ProjectMap.md
├── AGENTS.md
├── justfile
├── pyproject.toml
├── backend/
│   ├── app_template/
│   └── tests/
├── frontend/
│   └── app/
├── devops/
└── scripts/
```

## Entrypoints

- Backend: `backend/app_template/main.py`
- Frontend page: `frontend/app/page.js`
- Backend settings: `backend/app_template/core/config.py`

## Commands

- `just install`
- `just run-backend`
- `just run-frontend`
- `just test`
- `just lint`
- `just typecheck`
- `just run-ci`
- `just bootstrap`
- `just template-clean`

## Search Recipes

- Routes: `rg -n "APIRouter|@router" backend/app_template`
- Services: `rg -n "^def |^class " backend/app_template/services`
- Tests: `rg -n "test_" backend/tests`
- Template placeholders: `rg -n "app_template|App Template" .`
"""


def main() -> int:
    (ROOT / "ProjectMap.md").write_text(CONTENT, encoding="utf-8")
    print("Updated ProjectMap.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
