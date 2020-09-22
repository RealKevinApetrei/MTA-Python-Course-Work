# Exercise 1 and 2 (drivers.py)

# Exercise 3

from drivers import Drivers, Offenders

user1 = Drivers("Bob", "Mallop", "23", "Sport")
user1.get_info()

user2 = Drivers("James", "Kim", "38", "Truck")
user2.get_info()

offender1 = Offenders("Manely", "Rooster", "21", "Average", 1)
offender1.get_info()
offender1.get_offences()

offender2 = Offenders("Pitt", "Camper", "25", "Sport", 4)
offender2.get_info()
offender2.get_offences()