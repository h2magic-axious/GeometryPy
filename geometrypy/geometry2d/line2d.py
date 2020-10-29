from math import hypot

from geometrypy.vector import Vector
from geometrypy.geometry2d.point2d import Point2d


class Line2d:
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

    def vertical(self, line):
        try:
            v = line.vector()
            return v * self.vector() == 0
        except ValueError("Input must be Line2d") as error:
            raise error

    def intersect(self, line):
        try:
            a1b2_a2b1 = self.A * line.B - line.A * self.B
            c1a2_c2a1 = self.C * line.A - line.C * self.A
            c2b1_c1b2 = line.C * self.B - self.C * line.B

            return Point2d(c2b1_c1b2 / a1b2_a2b1, c1a2_c2a1 / a1b2_a2b1)
        except ValueError("Input must be Line2d") as error:
            raise error
