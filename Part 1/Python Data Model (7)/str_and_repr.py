class Taco:
    def __init__(self, shell, protein, toppings=[]):
        self.shell = shell
        self.protein = protein
        self.toppings = toppings

    def __bytes__(self):
        message = "".join(hex(ord(char)) for char in self.__str__())
        return message.encode()

    def __repr__(self):
        return (f"<Taco toppings={self.toppings} protein={self.protein}, shell={self.shell}>"
                + " @ "  + str(id(self)))

    def __str__(self):
        toppings = (f" with toppings {','.join(self.toppings)}" if self.toppings else '')
        return (f"{self.shell} shell, {self.protein} taco, {toppings}")

    def __format__(self, fmt_spec):
        if fmt_spec.endswith("d"):
            return str(sum(ord(char) for char in self.__str__()))
        if fmt_spec.endswith("taco"):
            return self.__repr__().upper() + "!!!!"
        return super().__format__(fmt_spec)


t1 = Taco("hard", "chicken")


t2 = Taco("soft", "tofu", toppings=["cheese", "lettuce", "sour cream"])