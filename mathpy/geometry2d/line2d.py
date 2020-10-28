class LineCartesian2d:
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c

    def __repr__(self):
        return f"Line: {self.A} x + {self.B} y + {self.C} = 0"

class LinePolar:
    def __init__(self):
        pass