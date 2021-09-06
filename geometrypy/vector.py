import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("Vector add another Vector")

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise ValueError("Vector minus another Vector")

    def __rsub__(self, other):
        return -(self - other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            try:
                return Vector(self.x * other, self.y * other, self.z * other)
            except (ValueError, TypeError) as error:
                raise error

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    # Vector(x,y,z) x Vector(x1, y1, z1)
    def x_mul(self, other):
        try:
            return Vector(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        except:
            raise ValueError("Vector x mul another vector")

    def length_to_one(self):
        length = self.length()
        return Vector(self.x / length, self.y / length, self.z / length)

    def rx_mul(self, other):
        return -self.x_mul(other)

    def collinear(self, other):
        bool_xy = self.x * other.y == self.y * other.x
        bool_xz = self.x * other.z == self.z * other.x
        bool_yz = self.y * other.z == self.z * other.y
        return bool_xy and bool_xz and bool_yz

    def vertical(self, other):
        try:
            return math.isclose(self * other, 0)
        except:
            raise ValueError("Vector x mul another vector")
