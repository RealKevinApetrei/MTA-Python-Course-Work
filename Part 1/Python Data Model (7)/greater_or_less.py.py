class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __lt__(self, other):
        self_dist = (self.x ** 2 + self.y ** 2) ** 0.5
        other_dist = (other.x ** 2 + other.y ** 2) ** 0.5
        return self_dist < other_dist

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)
        # return self.x != other.x or self.y != other.y


p1 = Point(0, 0)
p2 = Point(0, 0)
p3 = Point(1, -4)
        