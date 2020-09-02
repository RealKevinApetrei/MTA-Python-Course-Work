from math import ceil, floor


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __float__(self):
        return self.x + self.y

    # def __floor__(self):
        # s = self.x + self.y
        # return floor(s)
        
    # def __ceil__(self):
    #     s = self.x + self.y
    #     return ceil(s)


p = Point(3.6, 2.7)
