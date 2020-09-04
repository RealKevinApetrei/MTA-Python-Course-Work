from copy import deepcopy


class Taco:
    def __init__(self, protein, toppings):
        self.protein = protein
        self.toppings = toppings

    def __repr__(self):
        return f"<Taco: (protein={self.protein})>"

    def __copy__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        new_taco = Taco(self.protein, self.toppings)
        new_taco.cheese = "cheddar"
        return new_taco

    def __deepcopy__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        new_taco = Taco(self.protein, deepcopy(self.toppings))
        new_taco.has_guac = True
        return new_taco


taco = Taco("steak", ["tomatoes", "sour cream"])