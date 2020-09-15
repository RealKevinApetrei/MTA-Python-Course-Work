# Exercise 1

vehicles = ["commercial plane", "private plane", "fighter jet"]

for vehicle in vehicles:
    if vehicle == "commercial plane":
        print("You may use the lane.")
    elif vehicle == "private plane":
        print("You may use the lane.")
    elif vehicle == "fighter jet":
        print("You may use the lane.")
    else:
        print("You may NOT use the lane.")

# Exercise 2

for vehicle in vehicles:
    if vehicle != "commercial plane":
        print("You may NOT use the lane.")
    elif vehicle != "private plane":
        print("You may NOT use the lane.")
    elif vehicle != "fighter jet":
        print("You may NOT use the lane.")
    else:
        print("You may use the lane.")

# Exercise 3

shots = [0, 1, 2, 3, 4, 5]


for shot in shots:
    if shot == 0:
        print("You have 3 shots left.")
    elif shot == 1:
        print("You have 2 shots left.")
    elif shot == 2:
        print("You have 1 shots left.")
    elif shot == 3:
        print("You have 0 shot left.")

# Exercise 4

    elif shot < 4:
        print("You are DISQUALIFIED! You tried to shoot without any shots!")

# Exercise 5

for shot in shots:
    if shot == 0:
        print("You have 3 shots left.")
    elif shot == 1:
        print("You have 2 shots left.")
    elif shot == 2:
        print("You have 1 shots left.")
    elif shot == 3:
        print("You have 0 shot left.")
    elif shot == 4:
        print("LAST CHANCE before DISQUALIFICATION!")
    else:
        print("You are DISQUALIFIED!!!")