"""Camera abstraction. Real frames never leave the device; only events do."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Protocol

import numpy as np


class FrameSource(Protocol):
    def frames(self) -> Iterator[np.ndarray]:
        """Yield BGR frames (H x W x 3, uint8). Ends when the source is exhausted."""
        ...


class MockCamera:
    """Deterministic synthetic frames for tests and camera-less demos."""

    simulated = True

    def __init__(self, count: int = 5, width: int = 64, height: int = 48) -> None:
        self._count, self._shape = count, (height, width, 3)

    def frames(self) -> Iterator[np.ndarray]:
        for i in range(self._count):
            yield np.full(self._shape, i % 256, dtype=np.uint8)
