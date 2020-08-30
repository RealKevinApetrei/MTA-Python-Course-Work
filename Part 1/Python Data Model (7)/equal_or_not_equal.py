class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)


p1 = Point(0, 0)
p2 = Point(0, 0)
p3 = Point(1, -4)
        