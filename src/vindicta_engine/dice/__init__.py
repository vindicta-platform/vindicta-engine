"""Dice-Engine: Cryptographically secure dice rolling.

Provides CSPRNG-backed dice rolling with entropy proofs
for fair gameplay in the Vindicta Platform.
"""

from vindicta_engine.dice.engine import DiceEngine
from vindicta_engine.dice.models import DiceRoll, CombatResult

__version__ = "1.0.0"

__all__ = [
    "DiceEngine",
    "DiceRoll",
    "CombatResult",
]
