# Repository Guidelines

## Project Structure

- `backend/`: FastAPI backend
  - `app_template/`: main package
    - `main.py`: app entrypoint
    - `api/`: HTTP routes (health, items)
    - `services/`: business logic
    - `domain/`: models, schemas
    - `core/`: config, utilities
  - `tests/`: pytest tests
- `frontend/`: Next.js UI
  - `app/`: App Router pages
- `devops/`: Docker, CI config
  - `backend.dockerfile`: production backend image
  - `frontend.dockerfile`: production frontend image
  - `.pre-commit-config.yaml`: linting hooks

## Build, Test, Dev

- Task runner: `just`
- Install deps: `just install`
- Run backend: `just run-backend` (port 8000)
- Run frontend: `just run-frontend` (port 3000)
- Run tests: `just test`
- Run tests with coverage: `just test-cov 80`
- Lint all: `just lint`
- Type check: `just typecheck`

## Python Dependencies

- Managed by `uv` (`pyproject.toml` + `uv.lock`)
- Sync deps: `uv sync`
- Add dep: `uv add <package>`

## Docker

- Build images: `just docker-build`
- Run containers: `just docker-up`
- Production mode: `just docker-prod`
- Logs: `just docker-logs`

## Coding Style

- Python: `ruff` for formatting/linting, `mypy` strict mode
- 4 spaces, `snake_case` for functions/modules, `PascalCase` for classes
- Keep API handlers thin, business logic in `services/`
- Use Pydantic models in `domain/` for validation

## API Conventions

- Health endpoint: `GET /health`
- Readiness endpoint: `GET /ready`
- API routes prefixed with `/api`
- OpenAPI docs at `/docs` and `/redoc`

## Frontend

- Next.js App Router
- Fetch API base from `NEXT_PUBLIC_API_BASE_URL` env var
- Standalone output for Docker deployment

## CI/CD

- GitHub Actions in `.github/workflows/`
- CI: runs on push/PR, tests + lint + build
- CD: triggered by version tags (`v*`), pushes to GHCR

## Adding New Features

1. Create domain model in `backend/app_template/domain/`
2. Add service logic in `backend/app_template/services/`
3. Create API router in `backend/app_template/api/`
4. Register router in `main.py`
5. Add tests in `backend/tests/`
6. Update frontend as needed
