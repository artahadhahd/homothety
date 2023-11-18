from shape import Shape
from vector import vec2
import matplotlib.pyplot as plt


class NoShapeFound(Exception):
    pass


def _plot(shape: Shape, ax, color):
    if not shape:
        return
    pts = [*shape.points, shape.points[0]]
    for i in range(len(shape.points)):
        ax.plot(
            (pts[i][0], pts[i + 1][0]),
            (pts[i][1], pts[i + 1][1]),
            marker="o",
            color=color,
        )


class Graph:
    def __init__(self, Z: vec2, k: float):
        self.Z = Z
        self.k = k
        self._shapes = {}
        self._color = {}
        self._max = [-15, 15]

    def add_shape(self, id: str, shape: Shape, *, color: str = "r"):
        self._shapes[id] = shape
        self._color[id] = color

    def get_shape(self, id: str) -> Shape:
        try:
            return self._shapes[id]
        except KeyError:
            raise NoShapeFound(
                f"No shape found with {id = }. All ids: {self._shapes.keys()}"
            )

    def plot(self):
        if not self._shapes:
            return
        ax = plt
        ax.plot(*self.Z, color="b", marker="o")
        ax.xlim(self._max)
        ax.ylim(self._max)
        ax.axline((0, 0), slope=0, color="black", linestyle=":")
        ax.axvline(color="black", linestyle=":")
        for shape in self._shapes:
            sh = self.get_shape(shape)
            _plot(sh, ax, self._color[shape])

    def show(_self):
        plt.show()
