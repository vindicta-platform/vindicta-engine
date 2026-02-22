<!--
Sync Impact Report:
- Version change: 0.1.0 -> 1.0.0
- List of modified principles (old title -> new title if renamed):
  - MCP-First Mandate -> I. MCP-First Mandate (Tool & Operational Rules)
  - Spec-Driven Development (SDD) -> II. Spec-Driven Development (SDD) Mandate
  - Zero-Issue Stability -> III. Zero-Issue Stability and Testing Discipline
  - Tech Standards -> IV. Tech Standards and Modern Tooling
  - Domain Isolation -> V. Domain Isolation and Concurrency Safety
- Added sections:
  - Principle added: VI. Foundation Reliance and Implementation Mandate
  - Additional Constraints: Git isolation and repository mechanics
  - Development Workflow: Agent-driven task definition
  - Governance: Validation and amendment process
- Removed sections: None
- Templates requiring updates: None required.
- Follow-up TODOs: None.
-->
# Vindicta Engine Constitution

## Core Principles

### I. MCP-First Mandate (Tool & Operational Rules)
All development interactions MUST prioritize specialized tools and Model Context Protocol (MCP) endpoints (e.g., github-mcp-server) over generic terminal commands. This ensures cross-platform compatibility and avoids string encoding or runtime path bugs.

### II. Spec-Driven Development (SDD) Mandate
Development MUST follow the Speckit workflow. Features begin as high-level `spec.md`, unfold into a concrete `plan.md`, and execute via `tasks.md`. Architectural decisions are first modeled conceptually before code implementation begins.

### III. Zero-Issue Stability and Testing Discipline
Test-Driven Development (TDD) principles apply. Tests MUST be written or updated before core implementations merge. Local validation (formatting via `ruff`, linting via `mypy`, coverage via `pytest`) MUST pass locally prior to generating pull requests or committing to stable branches.

### IV. Tech Standards and Modern Tooling
The vindicta-engine strictly relies on Python >= 3.12, utilizing `uv` for package management, `pytest` for testing, `hatchling` for builds, and Pydantic V2 for domain modeling. Code MUST adhere strictly to these ecosystem components.

### V. Domain Isolation and Concurrency Safety
A strict multi-agent concurrent environment requires absolute git isolation. Using `git add .` or blanket commits is strictly prohibited. Commits MUST be atomic, signed, and strictly scoped to modifying only the explicitly targeted feature domains.

### VI. Foundation Reliance and Implementation Mandate
The Engine's implementation (`dice/engine.py`, `dice/models.py`, etc.) MUST rely entirely upon and seamlessly integrate with the `vindicta-foundation` base models. The Engine exists strictly to provide implementations for the abstract `vindicta-foundation` interfaces and MUST NOT redefine, shadow, or overlap the foundational Zero-Order Axioms and First-Order Postulates.

## Additional Constraints

- **Trunk-Based Development**: All feature work branches off `upstream/main` with appropriate prefixes (`feat/`, `chore/`, `fix/`).
- **Strict Main Branch Protection**: Direct commits to `main` are restricted. Code incorporates into `main` exclusively through formally formatted pull requests.
- **Git Commit Signing**: All commits MUST carry a verified cryptographic signature utilizing workspace SSH keys.

## Development Workflow

1. Use `/speckit.specify` to encode the raw feature requirement.
2. Use `/speckit.plan` to develop technical designs.
3. Use `/speckit.tasks` to enumerate discrete, dependency-ordered work objects.
4. Execute implementations in strict bounds of defined tasks.
5. All completed pull request bodies must be detailed in markdown via `--body-file`.

## Governance

This Constitution and the `vindicta-foundation` Axioms supersede all other practices.
Any modification to these principles constitutes a major Semantic Version bump.
All PRs and code reviews MUST verify compliance with these principles prior to merge.

**Version**: 1.0.0 | **Ratified**: 2026-02-21 | **Last Amended**: 2026-02-22
