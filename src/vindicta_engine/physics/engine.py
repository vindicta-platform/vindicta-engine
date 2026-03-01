"""Physics engine — re-exports DiceEngine from dice.engine.

The core dice-rolling logic lives in ``vindicta_engine.dice.engine``.
This module provides a convenience import so that downstream code can
continue to use ``from vindicta_engine.physics.engine import DiceEngine``.
"""

from vindicta_engine.dice.engine import DiceEngine

__all__ = ["DiceEngine"]
