import math

from geometrypy.geometry2d.line2d import Line2d
from geometrypy.geometry2d.point2d import Point2d


class ParabolaX:
    def __init__(self, a, b, c):
        #  y = a x^2 + b x + c
        self.a = a
        self.b = b
        self.c = c

        self.eccentricity = 1
        self.focus = Point2d()

    def derivative(self):
        return Line2d(2 * self.a, -1, self.b)

    def __repr__(self):
        return f"Parabola: y = {self.a} x^2 + {self.b} x + {self.c}"