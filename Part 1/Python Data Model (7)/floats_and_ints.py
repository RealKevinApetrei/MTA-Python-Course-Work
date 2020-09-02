class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __int__(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return int(distance)

    def __float__(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return float(distance)


# BAD!!!!!!
class Shoe:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def __float__(self):
        return float(self.size)

    
p1 = Point(3, 5)

shoe = Shoe(10.5, "blue")
