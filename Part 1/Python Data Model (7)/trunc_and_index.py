from math import trunc


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point: (x={self.x}, y={self.y})>"

    def __trunc__(self):
        return Point(trunc(self.x), trunc(self.y))


p = Point(3.1, 2.7)

####################

class Character:
    first = "A"
    def __init__(self, char):
        self.char = char
    
    def __repr__(self):
        return f"Character: ('{self.char}'')"

    def __index__(self):
        return ord(self.char) - ord(self.__class__.first)

    def __int__(self):
        return ord(self.char) - ord(self.__class__.first)


a = Character("A")
b = Character("B")
p = Character("P")

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# letters[Character("A":Character("P"))]