likes_cheese = False
favorite_number = 7


if likes_cheese:
    print(f"My favorite number is {favorite_number}")

if likes_cheese and favorite_number > 3:
    print("That is a big number!")

elif not likes_cheese and favorite_number > 3:
    print("Hello Vonne!")

else:
    print("Hello to everyone out there!") # printing some stuff


# The following determines some printout based on
# the value of favorite_number
if favorite_number > 0:
    print("zero")

if favorite_number > 3:
    print("three")

if favorite_number > 5:
    print("five")

else:
    print("not five")
