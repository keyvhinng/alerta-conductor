# ADR-0001: Monorepo with a modular-monolith API
- Status: Accepted (product owner brief)
- Context: Hackathon timeline; multiple AI agents working in parallel; three runtimes (Go, Python, TS).
- Decision: One repo, three apps under `apps/`, shared `contracts/`. The API is one deployable organized by domain. No Nx/Turborepo; a root Makefile is the entry point.
- Consequences: Simple deploys and refactoring; domain boundaries must be enforced by package structure and review, not by network boundaries.
