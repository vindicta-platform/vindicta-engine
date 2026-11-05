# Vindicta Engine

> **Status:** partial implementation (dice rolling, entropy buffer, evaluator scaffolding) from the Vindicta design record; development stopped March 2026. Single maintainer.

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
