"""Read the frozen B04 group allocation without deriving a new split from labels."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

from .open_textile import DataContractError, OpenTextileData


EXPECTED_B04_SPLIT_PLAN_SHA256 = "f39f304523ffecb130541de7194a2bdfb3e3f0564313ab0c137b427aad1196c7"


@dataclass(frozen=True)
class FrozenGroupSplit:
    fold_by_parent_group: tuple[tuple[str, int], ...]
    fold_by_piece: tuple[tuple[str, int], ...]
    fold_count: int
    source_protocol: str

    def group_fold(self, group_id: str) -> int:
        try:
            return dict(self.fold_by_parent_group)[group_id]
        except KeyError as exc:
            raise DataContractError(f"parent group absent from frozen allocation: {group_id}") from exc


def load_frozen_group_split(plan_path: Path, data: OpenTextileData) -> FrozenGroupSplit:
    plan_bytes = plan_path.read_bytes()
    if hashlib.sha256(plan_bytes).hexdigest() != EXPECTED_B04_SPLIT_PLAN_SHA256:
        raise DataContractError("B04 frozen split plan hash changed; amend before preparation")
    plan = json.loads(plan_bytes)
    if plan.get("dataset") != "OpenTextile-NIR v1.0 small tables":
        raise DataContractError("split plan is not for audited OpenTextile v1.0")
    outer = plan.get("outer_design", {})
    if outer.get("fold_count") != 5:
        raise DataContractError("B04 frozen plan requires five outer folds")
    folds = outer.get("group_ids_by_fold", {})
    if set(folds) != {"0", "1", "2", "3", "4"}:
        raise DataContractError("five outer fold IDs must be present exactly once")
    observed_groups = {piece.parent_group_id for piece in data.pieces}
    group_to_fold: dict[str, int] = {}
    for fold_text, group_ids in folds.items():
        if not isinstance(group_ids, list):
            raise DataContractError(f"fold {fold_text} group list is malformed")
        for group_id in group_ids:
            if group_id in group_to_fold:
                raise DataContractError(f"parent group assigned to two folds: {group_id}")
            group_to_fold[group_id] = int(fold_text)
    if set(group_to_fold) != observed_groups:
        missing = observed_groups - set(group_to_fold)
        extra = set(group_to_fold) - observed_groups
        raise DataContractError(f"frozen group map does not match source; missing={sorted(missing)}, extra={sorted(extra)}")
    piece_to_fold = {piece.piece_id: group_to_fold[piece.parent_group_id]
                     for piece in data.pieces}
    return FrozenGroupSplit(
        fold_by_parent_group=tuple(sorted(group_to_fold.items(), key=lambda item: int(item[0]))),
        fold_by_piece=tuple(sorted(piece_to_fold.items())),
        fold_count=5,
        source_protocol="protocol/split_plan.json",
    )
