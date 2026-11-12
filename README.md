# Vindicta Engine

<!-- BADGES:START -->
![CI](https://github.com/vindicta-platform/vindicta-engine/actions/workflows/ci.yml/badge.svg) ![License](https://img.shields.io/github/license/vindicta-platform/vindicta-engine) ![Version](https://img.shields.io/github/v/release/vindicta-platform/vindicta-engine?include_prereleases) ![Issues](https://img.shields.io/github/issues/vindicta-platform/vindicta-engine) ![PRs](https://img.shields.io/github/issues-pr/vindicta-platform/vindicta-engine)
<!-- BADGES:END -->

> **Status:** active, pre-1.0. Partial implementation (dice rolling, entropy buffer, evaluator scaffolding); no code changed between March and November 2026, when work resumed with the dice core (spec 002). Single maintainer.

Core physics, dice rolling, and AI simulation engine for the Vindicta Platform.

## Documentation

> **📌 Important:** Architectural decisions and game logic axioms for the engine are documented in [**vindicta-foundation**](https://github.com/vindicta-platform/vindicta-foundation).

## Installation


```bash
uv add vindicta-engine
```

## Features

- **Dice Physics**: Trusted RNG and True-Random entropy integration.
- **Combat Simulation**: Monte Carlo simulation for attack sequences.
- **AI Primitives**: Base classes for tactical AI.

## Independence

This is a personal project by Brandon Fox, built on my own time and equipment. It is not affiliated with, endorsed by, or derived from the work of any employer, current or former, and does not represent their views, products or practices. Licensed under the MIT License; principles at [First-ADE/PRINCIPLES.md](https://github.com/First-ADE/.github/blob/main/PRINCIPLES.md).
