class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Pair(x={self.x}, y={self.y})>"

    def __bool__(self):
        return (bool(self.y / self.x)) if self.x != 0 else bool(self.y / (self.x + 1))


p1 = Pair(0, 0)
p2 = Pair(1, 3)