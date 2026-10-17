# Local Development

## Prerequisites (macOS Apple Silicon verified)
Go ≥ 1.25 · Node ≥ 20 (24 verified) · pnpm · uv (Python 3.12+ managed by uv) · Docker + Compose ·
make. Optional: OpenSpec CLI (`npm install -g @fission-ai/openspec@latest`).

## Setup
```bash
cp .env.example .env
make setup
make db-up          # PostgreSQL on :5432 (not yet used by the API in bootstrap)
```

## Run
```bash
make api            # http://localhost:8080/v1/health
make dashboard      # http://localhost:3000
make monitor        # emits simulated events to stdout (mock camera + telemetry)
```

## Checks
```bash
make lint test build-dashboard compose-check
make contracts-lint   # needs network (npx @redocly/cli)
make check            # everything except contracts-lint
```
