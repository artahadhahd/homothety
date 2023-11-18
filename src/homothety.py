from dataclasses import dataclass
from vector import vec2
from shape import Shape


@dataclass
class Homothety:
    Z: vec2
    k: float


def apply_homothety(system: Homothety, shape: Shape) -> Shape:
    """Do a homothety on a shape and return the output"""
    _rotate = lambda P: P - (system.Z - P) * (system.k - 1)  # *1
    return Shape(*map(_rotate, shape.points))


# *1: How this works is really cool
# First, we calculate the distance of point P from Z. [system.Z - P]
# then we multiply it by k - 1 (try removing the -1 to see what happens) so now
# we get the total distance that has to be travelled in order to get to the final point.
# you can look at it as dy and dx in separate components.
# last thing we gotta do, is to subtract the point's coordinates from the traversing distance.
