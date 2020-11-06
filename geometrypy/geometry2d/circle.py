import math

from geometrypy.geometry2d.point2d import Point2d
from geometrypy.geometry2d.line2d import Line2d


class Circle:
    def __init__(self, center: Point2d, radius: float):
        self.center = center
        self.radius = radius

    def get_standard(self):
        return 1, 1, -2 * self.center.x, -2 * self.center.y, self.center.x ** 2 + self.center.y ** 2 - self.radius ** 2

    def init_from_standard(self, a, b, c, d, e):
        pass

    def intersection_with_line2d(self, line: Line2d):
        a2 = line.A ** 2
        b2 = line.B ** 2
        c2 = line.C ** 2

        a = self.center.x
        b = self.center.y

        A = a2 + b2
        B = 2 * line.A * (line.C + b * line.B - a * b2)
        C = b2 * (a ** 2 + b ** 2 - self.radius ** 2) + c2 - 2 * b * line.B * line.C

        delta = B ** 2 - 4 * A * C

        if delta < 0:
            return None
        elif delta == 0:
            x = -B / A / 2
            y = -(line.A * x + line.C) / line.B
            return Point2d(x, y)
        else:
            delta_half = math.sqrt(delta)
            x1 = (delta_half - B) / A / 2
            x2 = (delta_half + B) / A / 2
            return Point2d(x1, -(line.A * x1 + line.C) / line.B), Point2d(x2, -(line.A * x2 + line.C) / line.B)
