from math import pi, cos, sin


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __complex__(self):
        return complex(self.x, self.y)


class Voltage:
    def __init__(self, base_voltage, frequency):
        self.base_voltage = base_voltage
        self.afrequency = 2 * pi * frequency

    def __complex__(self):
        real = cos(self.afrequency) * self.base_voltage
        imag = sin(self.afrequency) * self.base_voltage
        return complex(real, imag)

    def at(self, t=0):
        real = cos(self.afrequency * t) * self.base_voltage
        imag = sin(self.afrequency * t) * self.base_voltage
        return complex(real, imag)


v = Vector2D(1, 1)