# Exercise 1

class Birds:
    def __init__(self, name, colors):
        self.name = name
        self.colors = colors

    def singing(self):
        print(f"The {self.colors} {self.name} are singing!")

    def flying(self):
        print(f"The {self.colors} {self.name} are flying!")

# Exercise 2

pigeons = Birds("Pigeons", "Green and Yellow")
pigeons.singing()
pigeons.flying()

eagles = Birds("Eagles", "Black and White")
eagles.singing()
eagles.flying()

budgies = Birds("Budgies", "Green and Blue")
budgies.singing()
budgies.flying()

# Exercise 3

# class Teacher:
#     def __init__(self, name, gender, age, subject):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.subject = subject

#     def info(self):
#         print(f"{self.name.title()} is a {self.gender} and is {self.age} years old. They teach {self.subject}. We are proud of them!")


# missJames = Teacher("Miss James", "Female", "29", "English")
# missJames.info()

# mrRacket = Teacher("Mr Racket", "Male", "34", "Maths")
# mrRacket.info()

# Exercise 4

class Teacher:
    def __init__(self, name, gender, age, subject, monthly_pay):
        self.name = name
        self.gender = gender
        self.age = age
        self.subject = subject
        self.monthly_pay = monthly_pay

    def info(self):
        print(f"{self.name.title()} is a {self.gender} and is {self.age} years old. They teach {self.subject} and they get payed {self.monthly_pay} per month. We are proud of them!")

missJames = Teacher("Miss James", "Female", "29", "English", "£2000")
missJames.info()

mrRacket = Teacher("Mr Racket", "Male", "34", "Maths", "£1039")
mrRacket.info()