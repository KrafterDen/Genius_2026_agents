"""Minimal decision vocabulary with an explicit unknown-evidence state."""

from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ACCEPT = "ACCEPT"
    REVIEW = "REVIEW"
    NOT_ELIGIBLE = "NOT_ELIGIBLE_FOR_THIS_PROFILE"


@dataclass(frozen=True)
class RoutingResult:
    sample_id: str
    decision: Decision
    reason: str
    profile_id: str | None = None
    evidence_source: str | None = None


def make_review_result(sample_id: str, reason: str = "No validated spectrum or profile") -> RoutingResult:
    """Return a conservative placeholder, without inferring fibre composition."""
    if not sample_id.strip():
        raise ValueError("sample_id must be nonempty")
    if not reason.strip():
        raise ValueError("reason must be nonempty")
    return RoutingResult(sample_id=sample_id, decision=Decision.REVIEW, reason=reason)
