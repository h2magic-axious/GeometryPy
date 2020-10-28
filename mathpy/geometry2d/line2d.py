from math import hypot

from mathpy.vector import Vector
from mathpy.geometry2d.point2d import Point2d


class Line2D:
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c

    def __repr__(self):
        return f"Line: {self.A} x + {self.B} y + {self.C} = 0"

    def vector(self):
        return Vector(-self.B, self.A, 0)

    def distance_with_point(self, point: Point2d):
        abs_value = abs(self.A * point.x + self.B * point.y + self.C)
        hyp_value = hypot(self.A, self.B)

        return abs_value / hyp_value

    def vertical_with(self, line):
        if isinstance(line, Line2D):
            v = line.vector()
            return v * self.vector() == 0
        else:
            return False
