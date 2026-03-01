"""Tests for the physics/dice engine."""

from vindicta_engine.physics.engine import DiceEngine
from vindicta_engine.dice.models import DiceRoll, CombatResult


def test_dice_roll_defaults() -> None:
    """DiceEngine should produce valid D6 rolls."""
    engine = DiceEngine()
    roll = engine.roll_d6()

    assert isinstance(roll, DiceRoll)
    assert 1 <= roll.value <= 6
    assert roll.sides == 6
    assert roll.entropy_proof  # Non-empty proof string
    assert roll.roll_id is not None  # UUID from dataclass


def test_deterministic_seed() -> None:
    """Same seed should produce same roll sequence."""
    seed = b"test_seed_123"
    engine1 = DiceEngine(seed)
    engine2 = DiceEngine(seed)

    roll1 = engine1.roll_d6()
    roll2 = engine2.roll_d6()

    assert roll1.value == roll2.value
    assert roll1.entropy_proof == roll2.entropy_proof


def test_combat_roll_logic() -> None:
    """Combat roll should respect attack count constraints."""
    engine = DiceEngine()

    result = engine.combat_roll(
        attacks=10,
        hit_on=2,
        wound_on=2,
        save=6,  # Hard save
        damage=1,
    )

    assert isinstance(result, CombatResult)
    assert result.attacks == 10
    # Hit rolls may be more than attacks due to reroll appends
    assert len(result.hit_rolls) >= 10
    assert result.hits <= result.attacks
    assert result.damage_dealt >= 0


def test_batch_roll() -> None:
    """Batch roll should produce correct number of results."""
    engine = DiceEngine()
    batch = engine.roll_batch(count=10, sides=6)

    assert len(batch.rolls) == 10
    assert batch.total == sum(r.value for r in batch.rolls)
