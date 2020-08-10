numbers = [1, 2, 3, 4, 5]
words = {"The", "Cheese", "Is", "Good"}
user = ("Vonne", "Smith", 23, "Pizza")
foods = dict(pizza=True, onions=False, olives=False, salami=True)

# print(numbers)
# print(words)
# print(user)
# print(foods)

# The Standard "For Loop" in Python

# for element in words:
#     print(element)

# for index in range(0, len(user)):
#     element = user[index]
#     print(element)

# For Loops and Dictionaries

for key, value in foods.items():
    print(key, value)
