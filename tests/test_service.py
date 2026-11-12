"""Tests for the service helpers, AI base models and dice model helpers."""

import hashlib

import pytest
from pydantic import ValidationError

from vindicta_engine.ai import BaseAIProfile, BaseTacticalDecision, BaseTacticalEngine
from vindicta_engine.dice.engine import DiceEngine
from vindicta_engine.dice.models import BatchRollResult, CombatResult, DiceRoll
from vindicta_engine.health import check_health
from vindicta_engine.integrity import verify_integrity


def test_check_health_reports_ok() -> None:
    """Health check names the realm and carries a numeric timestamp."""
    health = check_health()
    assert health["status"] == "ok"
    assert health["realm"] == "vindicta-engine"
    assert isinstance(health["timestamp"], float)


def test_verify_integrity_reports_operational() -> None:
    """Integrity check reports operational with an ISO timestamp string."""
    report = verify_integrity()
    assert report["status"] == "operational"
    assert isinstance(report["timestamp"], str)
    assert report["metrics"] == {"engine_status": "online", "active_tasks": 0}


def test_tactical_decision_validates_confidence() -> None:
    """Confidence outside 0..1 is rejected; a valid decision keeps its fields."""
    decision = BaseTacticalDecision(confidence=0.75, reasoning="cover", action_type="move")
    assert decision.target_id is None
    with pytest.raises(ValidationError):
        BaseTacticalDecision(confidence=1.5, reasoning="x", action_type="move")


def test_ai_profile_defaults() -> None:
    """A profile needs only a name; the tendencies default to the midpoint."""
    profile = BaseAIProfile(name="Cautious")
    assert profile.aggression == 0.5
    assert profile.risk_tolerance == 0.5


def test_tactical_engine_is_abstract() -> None:
    """The engine interface cannot be instantiated until both methods exist."""
    with pytest.raises(TypeError):
        BaseTacticalEngine()  # type: ignore[abstract]

    class Fixed(BaseTacticalEngine):
        def evaluate_state(self, game_state: object) -> float:
            return 0.0

        def decide_next_action(self, game_state: object) -> BaseTacticalDecision:
            return BaseTacticalDecision(confidence=1.0, reasoning="fixed", action_type="hold")

    engine = Fixed()
    assert engine.evaluate_state(None) == 0.0
    assert engine.decide_next_action(None).action_type == "hold"


def test_dice_roll_str_and_verify() -> None:
    """A roll prints as D<sides>: <value> and verifies against its own entropy only."""
    entropy = b"entropy-under-test"
    proof = hashlib.sha256(entropy).hexdigest()[:16]
    roll = DiceRoll(value=4, sides=6, entropy_proof=proof)
    assert str(roll) == "D6: 4"
    assert roll.verify(entropy)
    assert not roll.verify(b"other entropy")


def test_batch_values_and_combat_str() -> None:
    """Batch results expose their values; a combat result prints its funnel."""
    batch = DiceEngine(b"batch-seed").roll_batch(5)
    assert isinstance(batch, BatchRollResult)
    assert batch.values == [r.value for r in batch.rolls]
    assert batch.total == sum(batch.values)
    result = CombatResult(attacks=2, hit_on=3, wound_on=4, save=5, damage=1)
    assert str(result).startswith("2A")


def test_combat_rerolls_are_recorded() -> None:
    """With rerolls on, failed hit and wound rolls are rolled again and recorded.

    The seed makes the sequence repeatable, so the counts below are stable.
    """
    engine = DiceEngine(b"reroll-seed")
    result = engine.combat_roll(
        attacks=120, hit_on=4, wound_on=4, save=4, damage=2, hit_reroll=True, wound_reroll=True
    )
    assert len(result.hit_rolls) > result.attacks
    assert len(result.wound_rolls) > result.hits
    assert result.hits <= result.attacks
    assert result.wounds <= result.hits
    assert result.saves_failed <= result.wounds
    assert result.damage_dealt == result.saves_failed * 2
    assert result.hits == sum(1 for r in result.hit_rolls if r.value >= 4)
