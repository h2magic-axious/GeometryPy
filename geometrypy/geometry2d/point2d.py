from math import hypot


class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def vector(self, other):
        if isinstance(other, Point2d):
            return

    def distance(self, point):
        if isinstance(point, Point2d):
            return hypot(self.x - point.x, self.y - point.y)
        else:
            return None