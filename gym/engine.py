"""Gym & Fitness Club Membership Lifecycle Engine for Frappe Framework."""

from datetime import datetime, date, timedelta
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class MembershipPlan(BaseModel):
    plan_name: str  # Monthly, Quarterly, Annual
    duration_months: int
    base_fee: float
    includes_trainer: bool = False


class GymMember(BaseModel):
    member_id: str
    full_name: str
    phone: str
    plan_name: str
    membership_start: str  # YYYY-MM-DD
    membership_end: str
    assigned_trainer: Optional[str] = None
    status: str = "Active"  # Active, Expired, Frozen


class GymEngine:
    """Manages member check-in validation, subscription renewals, and trainer slots."""

    def __init__(self):
        self.plans: Dict[str, MembershipPlan] = {
            "Monthly": MembershipPlan(plan_name="Monthly", duration_months=1, base_fee=2500.0),
            "Quarterly": MembershipPlan(plan_name="Quarterly", duration_months=3, base_fee=6500.0),
            "Annual": MembershipPlan(plan_name="Annual", duration_months=12, base_fee=18000.0, includes_trainer=True),
        }
        self.members: Dict[str, GymMember] = {}

    def enroll_member(self, member_id: str, name: str, phone: str, plan_name: str, start_date_str: Optional[str] = None) -> GymMember:
        if plan_name not in self.plans:
            raise ValueError(f"Plan {plan_name} not available")

        plan = self.plans[plan_name]
        start_dt = datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else date.today()
        # Approx 30 days per month
        end_dt = start_dt + timedelta(days=plan.duration_months * 30)

        member = GymMember(
            member_id=member_id,
            full_name=name,
            phone=phone,
            plan_name=plan_name,
            membership_start=start_dt.strftime("%Y-%m-%d"),
            membership_end=end_dt.strftime("%Y-%m-%d"),
            status="Active",
        )
        self.members[member_id] = member
        return member

    def validate_turnstile_access(self, member_id: str, check_date_str: Optional[str] = None) -> Dict[str, Any]:
        """Validate whether member turnstile barcode/RFID should open or lock."""
        if member_id not in self.members:
            return {"access_granted": False, "reason": "Unregistered Member ID"}

        mem = self.members[member_id]
        chk_dt = datetime.strptime(check_date_str, "%Y-%m-%d").date() if check_date_str else date.today()
        end_dt = datetime.strptime(mem.membership_end, "%Y-%m-%d").date()

        if chk_dt > end_dt:
            mem.status = "Expired"
            return {
                "access_granted": False,
                "reason": f"Membership expired on {mem.membership_end}. Renewal required.",
                "member_name": mem.full_name,
            }

        return {
            "access_granted": True,
            "member_name": mem.full_name,
            "plan": mem.plan_name,
            "days_remaining": (end_dt - chk_dt).days,
        }
