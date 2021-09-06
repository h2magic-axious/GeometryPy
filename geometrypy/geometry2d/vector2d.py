from geometrypy.vector import Vector


class Vector2d:
    def __init__(self, vx, vy):
        self.x = vx
        self.y = vy

    def __add__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x + other.x, self.y + other.y)
        else:
            raise ValueError("Vector2d add another Vector2d")

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x - other.x, self.y - other.y)
        else:
            raise ValueError("Vector2d sub other Vector2d")

    def __rsub__(self, other):
        return -(self - other)

    def __neg__(self):
        return Vector2d(-self.x, -self.y)

    def __mul__(self, other):
        if isinstance(other, Vector2d):
            return self.x * other.x + self.y * other.y
        else:
            try:
                return Vector2d(self.x * other, self.y * other)
            except (ValueError, TypeError) as error:
                raise error

    def __rmul__(self, other):
        return self * other

    def x_mul(self, other):
        if isinstance(other, Vector2d):
            return Vector(self.x, self.y, 0).x_mul(Vector(other.x, other.y, 0))
        else:
            raise ValueError("Vector2d x_mul other Vector2d")

if __name__ == '__main__':
    v1 = Vector2d(1,2)
    v2 = Vector2d(3,1)
    print(v1.x_mul(v2))
