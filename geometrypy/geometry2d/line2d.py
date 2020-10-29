import math

from geometrypy.vector import Vector
from geometrypy.geometry2d.point2d import Point2d


class Line2d:
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c

    def __repr__(self):
        return f"Line: ({self.A}) x + ({self.B}) y + ({self.C}) = 0"

    def vector(self):
        return Vector(-self.B, self.A, 0)

    def distance_with_point(self, point: Point2d):
        abs_value = abs(self.A * point.x + self.B * point.y + self.C)
        hyp_value = math.hypot(self.A, self.B)

        return abs_value / hyp_value

    def distance_with_line(self, line):
        try:
            if self.parallel(line):
                temp = math.gcd(self.A, line.A)
                return abs(self.C / temp - line.C / temp) / math.hypot(self.A / temp, self.B / temp)
            else:
                return 0
        except:
            raise ValueError("Input must be Line2d")

    def angle_with_line(self, line):
        try:
            if self.parallel(line):
                return 0
            elif self.vertical(line):
                return math.pi / 2
            else:
                v1 = self.vector()
                v2 = line.vector()

                return math.acos(v1 * v2 / (v1.length() * v2.length()))

        except:
            raise ValueError("Input must be Line2d")

    def vertical(self, line):
        try:
            return line.vector() * self.vector() == 0
        except:
            raise ValueError("Input must be Line2d")

    def parallel(self, line):
        try:
            return self.vector().collinear(line.vector())
        except:
            raise ValueError("Input must be Line2d")

    def intersect(self, line):
        try:
            a1b2_a2b1 = self.A * line.B - line.A * self.B
            c1a2_c2a1 = self.C * line.A - line.C * self.A
            c2b1_c1b2 = line.C * self.B - self.C * line.B

            return Point2d(c2b1_c1b2 / a1b2_a2b1, c1a2_c2a1 / a1b2_a2b1)
        except:
            raise ValueError("Input must be Line2d")


if __name__ == '__main__':
    line1 = Line2d(1, 0, -1)
    line2 = Line2d(0, 1, -1)
    print(line1.angle_with_line(line2))
