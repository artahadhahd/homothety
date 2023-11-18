from dataclasses import dataclass

# a vector has  to derive from this class (i will turn it into a metaclass) and it should have _dimensions implemented
@dataclass
class _Vector:
    _dimensions: int

class vec2(_Vector):
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y
        self._dimensions = 2
    
    def __mul__[T: (float, complex, int)](self, other: T):
        if isinstance(other, _Vector):
            raise ValueError("Cannot multiply a vector by a vector")
        return vec2(self.x * other, self.y * other)

    def __rmul__[T: (float, complex, int)](self, other: T):
        return self.__mul__(other)
    
    def __add__(self, other: _Vector) -> _Vector:
        if not isinstance(other, _Vector):
            raise ValueError(f"Can only add vectors to vectors, not {other.__class__}")
        if other._dimensions != self._dimensions:
            raise ValueError(f"Cannot add a vector with dimension {self._dimensions} with one with dimension {other._dimensions}")
        return vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: _Vector) -> _Vector:
        if not isinstance(other, _Vector):
            raise ValueError(f"Can only subtrace vectors to vectors, not {other.__class__}")
        if other._dimensions != self._dimensions:
            raise ValueError(f"Cannot subtract a vector with dimension {self._dimensions} with one with dimension {other._dimensions}")
        return vec2(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other: _Vector) -> bool:
        return (self._dimensions == other._dimensions) and isinstance(other, _Vector) and (self.x == other.x and self.y == other.y)
    
    def __str__(self) -> str:
        return f"( {self.x} | {self.y} )"
    
    __repr__ = __str__

    def __getitem__(self, index):
        return (self.x, self.y)[index]
    
    def __iter__(self):
        return iter((self.x, self.y))
    
    def __abs__(self):
        return vec2(abs(self.x), abs(self.y))