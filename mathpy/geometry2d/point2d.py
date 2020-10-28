from math import hypot, sin, cos, atan, sqrt, pow


# from mathpy.vector import Vector
# from mathpy.utils import float_equal


# def check_base_vector(e1, e2):
#     if isinstance(e1, Vector) and isinstance(e2, Vector):
#         if float_equal(e1.length(), 1) and float_equal(e2.length(), 1):
#             return e1.collinear(e2)


class PointCartesian2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Cartesian coordinate system: Point({self.x}, {self.y})"

    def polar(self):
        return hypot(self.x, self.y), atan(self.y / self.x)


class PointPolar:
    def __init__(self, rho, theta):
        self.rho = rho
        self.theta = theta

    def __repr__(self):
        return f"Polar coordinate system: Point({self.rho}, {self.theta})"

    def cartesian(self):
        return self.rho * cos(self.theta), self.rho * sin(self.theta)


# class PointAffine2d:
#     def __init__(self, e1, e2, x, y):
#         if check_base_vector(e1, e2):
#             self.e1 = e1
#             self.e2 = e2
#             self.x = x
#             self.y = y
#         else:
#             raise ValueError("Base vector is unvaild")
#
#     def __repr__(self):
#         return f"Affine coordinate system base on <{self.e1}, {self.e2}>: Point({self.x}, {self.y})"


def distance_cartesian(point1: PointCartesian2d, point2: PointCartesian2d):
    return hypot(point1.x - point2.x, point1.y - point2.y)


def distance_cartesian_polar(point1: PointCartesian2d, point2: PointPolar):
    x, y = point2.cartesian()
    return hypot(point1.x - x, point1.y - y)


def distance_polar(point1: PointPolar, point2: PointPolar):
    p1 = pow(point1.rho, 2) + pow(point2.rho, 2)
    p2 = 2 * point1.rho * point2.rho * cos(point1.theta - point2.theta)
    return sqrt(p1 - p2)
