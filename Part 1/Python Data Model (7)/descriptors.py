class Car:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        print("Some calculation")
        return self._color
    
    @color.setter
    def color(self, value):
        if value not in {"red" , "green", "blue"}:
            raise ValueError(f"The color '{value}' is not valid.")
        self._color = value

    @color.deleter
    def color(self):
        raise AttributeError("You cannot delete 'color'.")
        # del self._color
    


car = Car("red")