class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __sub__(self, other):
        if not isinstance(other, (Point, int, float)):
            raise TypeError("Subtraction not supported for a Point and {}".format(type(other)))
        if isinstance(other, (int, float)):
            return Point(self.x - other, self.y - other)
        else:
            return (self.x - other.x, self.y - other.y)
    
    def __rsub__(self, other):
        if not isinstance(other, (Point)):
            raise TypeError("Try the reverse order. Be careful your difference may change.")
        return self.__sub__(other)

    def __isub__(self, other):
        print("In place")
        return self.__sub__(other)


p1 = Point(0, 0)
p2 = Point(1, 3)
p3 = Point(-2, -4)