#!/usr/bin/env python3
"""Exercise the import and truthful no-model decision contract."""

import json
from textileroute import Decision, make_review_result


def main() -> None:
    result = make_review_result("synthetic-smoke-001")
    assert result.decision is Decision.REVIEW
    assert result.profile_id is None and result.evidence_source is None
    print(json.dumps({"sample_id": result.sample_id, "decision": result.decision.value,
                      "reason": result.reason, "synthetic": True}))


if __name__ == "__main__":
    main()
