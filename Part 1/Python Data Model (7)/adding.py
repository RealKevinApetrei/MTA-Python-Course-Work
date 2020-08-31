class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __add__(self, other):
        if isinstance(other, (float, int)):
            return Point(self.x + other, self.y + other)
        else:
            return Point(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        if isinstance(other, (float, int)):
            return Point(self.x + other, self.y + other)
        else:
            return self.__add__(other)
        
    def __iadd__(self, other):
        if isinstance(other, (float, int)):
            self.x += other
            self.y += other
        else:
            self.x += other.x
            self.y += other.y
        return self



p1 = Point(0, 0)
p2 = Point(1, 3)
p3 = Point(-2, -4)