class Car:
    def __init__(self):
        self.running = False
        self.odometer = 0
        self.direction = 90

    def __enter__(self):
        self.running = True
        return self

    def __exit__(self, *args, **kwargs):
        self.running = False
        print(f"You have moved ({car.odometer}) miles.")
        print(f"You are facing ({car.direction}) degrees.")

    def move(self, amount):
        if self.running:
            self.odometer += amount

    def _turn(self, amount):
        if self.running:
            self.direction += amount

    def turn_right(self):
        self._turn(90)
    
    def turn_around(self):
        self._turn(180)


# car = Car()

# car.running = True

# car.move(10)
# car.turn_right()
# car.move(10)
# car.turn_around()

# car.running = False

# print(f"You have moved ({car.odometer}) miles.")
# print(f"You are facing ({car.direction}) degrees.")

with Car() as car:
    car.move(10)
    car.turn_right()
    car.move(10)
    car.turn_around()

