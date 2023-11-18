from typing import Sequence
from vector import vec2


class Shape:
    def __init__(self, *points: Sequence[vec2]):
        self.points = tuple(points)

    def __str__(self) -> str:
        out = "{ "
        for point in self.points:
            out += str(point) + ", "
        out += " }"
        return out
