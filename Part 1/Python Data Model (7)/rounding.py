class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __round__(self, n=0):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return round(distance, n)   

p = Point(3, 4)
p1 = Point(3, 7)