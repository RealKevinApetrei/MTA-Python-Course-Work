from random import randint

class Car:
    __slots__ = ("color", "year")
    def __init__(self, color, year):
        self.color = color
        self.year = year
        # self.id = randint(0, 1000000000)
    
    # def __hash__(self):
    #     return hash((self.color, self.year, self.id))

    # def __eq__(self, other):
    #     return (
    #         self.__class__ == other.__class__ and
    #         self.color == other.color and
    #         self.year == other.year and
    #         self.id == other.id
    #     )


first = Car("red", 1997)
second = Car("blue", 2001)
third = Car("red", 1997)

reviews = {}

reviews[first] = "Awesome!"
reviews[second] = "Meh..."
reviews[third] = "It's okay."