class Binary:
    def __init__(self, number):
        self.number = number
        self._binnumber = bin(number)

    def __repr__(self):
        return f"<Binary Number={self.number} BinNumber={self._binnumber}>"

    def __lshift__(self, other):
        return Binary(self.number << other.number)

    def __rlshift__(self, other):
        return Binary(self.number << other.number)

    def __ilshift__(self, other):
        self.number <<= other.number
        self._binnumber = bin(self.number)
        return self

    def __rshift__(self, other):
        return Binary(self.number >> other.number)

    def __rrshift__(self, other):
        if isinstance(other, (int)):
            return Binary(self.number >> other)
        return Binary(self.number >> other.number)

    def __irshift__(self, other):
        self.number >>= other.number
        self._binnumber = bin(self.number)
        return self


b = Binary(2)
b1 = Binary(32)