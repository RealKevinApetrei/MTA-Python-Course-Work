class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __repr__(self):
        return f"<Fraction: (  {self.num}/{self.denom}  )>"

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom)

    def __invert__(self):
        return Fraction(self.denom, self.num)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __abs__(self):
        # return Point(abs(self.x), abs(self.y))
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return distance

    def __invert__(self):
        return Point(self.y, self.x)
    

p1 = Point(1, 2)
p2 = Point(3, 2)
p3 = Point(-5, -4)