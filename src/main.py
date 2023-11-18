import matplotlib.pyplot as plt
from shape import Shape
from graph import Graph
from vector import vec2
from homothety import apply_homothety, Homothety

if __name__ == "__main__":
    Z = 5, 1
    k = 2

    t1 = Shape(vec2(-2, 0), vec2(4, 0), vec2(0, 2))
    graph = Graph(vec2(*Z), k)
    graph.add_shape("t1", t1, color="g")
    t2 = apply_homothety(Homothety(vec2(*Z), k), t1)
    graph.add_shape("t2", t2, color="b")
    graph.plot()
    graph.show()
