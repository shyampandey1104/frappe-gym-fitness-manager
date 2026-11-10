"""Unit tests for GymEngine."""

from gym.engine import GymEngine


def test_gym_enrollment_and_access():
    engine = GymEngine()
    mem = engine.enroll_member(
        member_id="GYM-089",
        name="Vikram Singh",
        phone="9811223344",
        plan_name="Monthly",
        start_date_str="2026-11-01",
    )
    assert mem.status == "Active"

    # Valid check-in on Nov 10
    chk1 = engine.validate_turnstile_access("GYM-089", check_date_str="2026-11-10")
    assert chk1["access_granted"] is True
    assert chk1["days_remaining"] > 0

    # Expired check-in on Dec 15
    chk2 = engine.validate_turnstile_access("GYM-089", check_date_str="2026-12-15")
    assert chk2["access_granted"] is False
    assert "expired" in chk2["reason"].lower()
