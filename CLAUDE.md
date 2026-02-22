# FastAPI + Next.js Template

Primary agent guide for this template repository.

## What This Repo Is

A full-stack template with:
- FastAPI backend (`backend/app_template`)
- Next.js frontend (`frontend/`)
- Docker and CI basics
- Standard `just` commands + pre-commit

## Standard Commands

- `just install`
- `just run-backend`
- `just run-frontend`
- `just test`
- `just lint`
- `just format`
- `just typecheck`
- `just run-ci`

## Bootstrap / Template Lifecycle

- Customize placeholders with `just bootstrap`
- Verify build/test/lint
- After first successful build, run `just template-clean`

### Post-First-Build Cleanup (Required)

After your first successful build and smoke test:
1. Run `just template-clean`
2. Remove or replace template sample routes/components/tests not needed for the real project
3. Update `CLAUDE.md` and `ProjectMap.md` so they describe the actual project

## Runtime Layout

- Backend entrypoint: `backend/app_template/main.py`
- Health endpoints: `GET /health`, `GET /ready`
- Frontend entrypoint: `frontend/app/page.js`

## Validation

- `just test`
- `just lint`
- `just typecheck`
- `just run-ci`

## Fast Search

- Routes: `rg -n "APIRouter|@router" backend/app_template`
- Settings: `rg -n "BaseSettings|settings" backend/app_template/core`
- Template placeholders: `rg -n "app_template|App Template" .`
