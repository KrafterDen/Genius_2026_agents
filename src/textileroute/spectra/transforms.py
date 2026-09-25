"""Source-specific per-piece transforms and a guarded fold-fitted standardizer.

The supplied mean reflectance vector is preserved as the identity baseline. The
source PLS transform follows the original article's stated order; its numerical
conventions are separately documented in the B04 protocol.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Sequence


class SpectrumContractError(ValueError):
    """A spectrum or fitting boundary violates the frozen protocol."""


@dataclass(frozen=True)
class ProcessedSpectrum:
    wavelengths_nm: tuple[float, ...]
    values: tuple[float, ...]
    representation: str
    reflectance_floor_count: int = 0


def _finite_vector(values: Sequence[float], label: str) -> tuple[float, ...]:
    vector = tuple(float(value) for value in values)
    if not vector or any(not math.isfinite(value) for value in vector):
        raise SpectrumContractError(f"{label} must be nonempty and finite")
    return vector


def identity_reflectance(
    wavelengths_nm: Sequence[float], reflectance: Sequence[float]
) -> ProcessedSpectrum:
    """Retain the author's provided mean spectrum, without fitted processing."""
    wavelengths = _finite_vector(wavelengths_nm, "wavelengths")
    values = _finite_vector(reflectance, "reflectance")
    if len(wavelengths) != len(values):
        raise SpectrumContractError("wavelength and reflectance lengths differ")
    if any(a >= b for a, b in zip(wavelengths, wavelengths[1:])):
        raise SpectrumContractError("wavelengths must increase in nm")
    if any(value < 0 for value in values):
        raise SpectrumContractError("negative reflectance requires source investigation")
    return ProcessedSpectrum(wavelengths, values, "source_mean_reflectance")


def source_pls_preprocess(
    wavelengths_nm: Sequence[float], reflectance: Sequence[float]
) -> ProcessedSpectrum:
    """Absorbance, SG(9,2), fixed band range and per-piece SNV; no fitted state.

    SciPy is imported only when this optional research transform is requested.
    The returned floor count makes the log-floor convention visible.
    """
    raw = identity_reflectance(wavelengths_nm, reflectance)
    if len(raw.values) < 9:
        raise SpectrumContractError("Savitzky-Golay window 9 needs at least 9 bands")
    floor = 1e-6
    floored = sum(value < floor for value in raw.values)
    absorbance = [-math.log10(max(value, floor)) for value in raw.values]
    try:
        from scipy.signal import savgol_filter
    except ImportError as exc:
        raise SpectrumContractError(
            "source PLS preprocessing requires project-local SciPy; identity works without it"
        ) from exc
    smoothed = savgol_filter(absorbance, window_length=9, polyorder=2,
                             deriv=0, mode="interp")
    selected = [index for index, nm in enumerate(raw.wavelengths_nm)
                if 1411.0 <= nm <= 2536.0]
    if len(selected) < 9:
        raise SpectrumContractError("source 1411–2536 nm band interval unavailable")
    wavelengths = tuple(raw.wavelengths_nm[index] for index in selected)
    values = [float(smoothed[index]) for index in selected]
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    if variance <= 0 or not math.isfinite(variance):
        raise SpectrumContractError("per-piece SNV variance is zero or invalid")
    standard_deviation = math.sqrt(variance)
    normalized = tuple((value - mean) / standard_deviation for value in values)
    return ProcessedSpectrum(
        wavelengths, normalized, "absorbance_sg9p2_1411_2536_snv",
        reflectance_floor_count=floored,
    )


@dataclass(frozen=True)
class FoldFeatureStandardizer:
    """Training-group-only feature centering for a later model pipeline.

    Passing the outer held-out IDs is required at fit time. This guard cannot
    prove unrecorded supplier batches are independent; the split manifest must
    still be used by the caller.
    """

    means: tuple[float, ...]
    scales: tuple[float, ...]
    training_groups: frozenset[str]
    held_out_groups: frozenset[str]
    constant_feature_count: int

    @classmethod
    def fit(
        cls,
        rows: Sequence[Sequence[float]],
        group_ids: Sequence[str],
        held_out_group_ids: set[str] | frozenset[str],
    ) -> FoldFeatureStandardizer:
        if not rows or len(rows) != len(group_ids):
            raise SpectrumContractError("nonempty feature rows and group IDs must align")
        train_groups = frozenset(group_ids)
        held_out = frozenset(held_out_group_ids)
        if not train_groups or not held_out or train_groups & held_out:
            raise SpectrumContractError("fit groups overlap held-out groups or boundary is empty")
        matrix = tuple(_finite_vector(row, "feature row") for row in rows)
        width = len(matrix[0])
        if any(len(row) != width for row in matrix):
            raise SpectrumContractError("feature widths differ")
        means = tuple(sum(row[column] for row in matrix) / len(matrix)
                      for column in range(width))
        variances = tuple(sum((row[column] - means[column]) ** 2 for row in matrix) / len(matrix)
                          for column in range(width))
        scales = tuple(math.sqrt(variance) if variance > 0 else 1.0
                       for variance in variances)
        return cls(means, scales, train_groups, held_out,
                   sum(variance == 0 for variance in variances))

    def transform(self, rows: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
        transformed = []
        for row in rows:
            values = _finite_vector(row, "feature row")
            if len(values) != len(self.means):
                raise SpectrumContractError("feature width changed after fold fit")
            transformed.append(tuple((value - mean) / scale
                                     for value, mean, scale in zip(values, self.means, self.scales)))
        return tuple(transformed)
