class Taco:
    def __init__(self, shell, toppings=[]):
        self.shell = shell
        self.toppings = toppings
        self.index = -1

    def __iter__(self):
        return (t for t in self.toppings)

    def __len__(self):
        return len(self.toppings)

    def __reversed__(self):
        return self.toppings[::-1]

    # def __next__(self):
    #     self.index += 1
    #     if self.index >= len(self.toppings):
    #         self.index = -1
    #         raise StopIteration()
    #     return self.toppings[self.index]


taco = Taco("soft", ["sour cream", "tomatoes"])
