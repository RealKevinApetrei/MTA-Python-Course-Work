class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.ratings = []
        self.title = name.upper()

    def __repr__(self):
        return f"<Restaurant: (name={self.name}, location={self.location})>"

    def __setattr__(self, name, value):
        if name == "ratings" and hasattr(self, "ratings"):
            print("No!!!")
            return None
        elif name == "name":
            self.title = value.upper()

        self.__dict__[name] = value

    def __delattr__(self, name):
        if name == "location":
            del self.__dict__[name]
        else:
            print("You cannot delete that!")
            return None

    def rate(self, rating):
        self.ratings.append(rating)


restaurant = Restaurant("T'pol's Nom Bar", "Somewhere")