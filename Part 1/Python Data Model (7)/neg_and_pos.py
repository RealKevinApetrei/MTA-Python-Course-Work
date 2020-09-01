from datetime import datetime


class Date(datetime):
    def __pos__(self):
        return self.timestamp()

    def __neg__(self):
        return -self.timestamp()


class KString(str):
    def __pos__(self):
        return float(self)
    
    def __neg__(self):
        return -(float(self))
        


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __pos__(self):
        return self

    def __neg__(self):
        return Point(-self.x, -self.y)


p1 = Point(5, 5)
p2 = Point(1, 3)
p3 = Point(2, 4)