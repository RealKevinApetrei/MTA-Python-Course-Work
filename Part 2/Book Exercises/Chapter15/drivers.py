# Exercise 1

class Drivers:
    def __init__(self, first_name, last_name, age, nature_of_vehicle):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nature_of_vehicle = nature_of_vehicle

    def get_info(self):
        print(f"""\
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Age: {self.age}
        Nature of Vehicle: {self.nature_of_vehicle}
        """)
    
# user1 = Drivers("Bob", "Mallop", "23", "Sport")
# user1.get_info()

# user2 = Drivers("James", "Kim", "38", "Truck")
# user2.get_info()

# Exercise 2

class Offenders(Drivers):
    def __init__(self, first_name, last_name, age, nature_of_vehicle, offences):
        super().__init__(first_name, last_name, age, nature_of_vehicle)

        self.offences = offences

    def get_info(self):
        print(f"""\
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Age: {self.age}
        Nature of Vehicle: {self.nature_of_vehicle}
        Offences: {self.offences}
        """)

    def get_offences(self):
        if self.offences == 1:
            print("Driver is a FIRST TIME offender. NO PREVIOUS OFFENCES")
        else:
            print("Driver has AT LEAST 1 PREVIOUS OFFENCE.")

# Exercise 3 (main.py)
