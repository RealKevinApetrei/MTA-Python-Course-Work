ingredients = [
    "cheese", # Index 0
    "pepperoni", # Index 1
    "mushrooms", # Index 2
    "onions" # Index 3
]

numbers = [7, 2, 3, 5, 11]
word = ["c", "a", "t"]

print(ingredients)
print(numbers)
print(word)

#

# new_list = ingredients + numbers
# print(new_list)
# new_list = ingredients * ingredients
# print(new_list)

# Accessing Elements and Slicing

second_ingredient = ingredients[1]
print(second_ingredient)
number_of_ingredients = len(ingredients)
print(number_of_ingredients)

# Change the Element

# ingredients[3] = "more cheese"
# del ingredients[3]
# print(ingredients)
justin_ingredients = ingredients[:]
print(justin_ingredients)
justin_ingredients[0:1] = ["bleu cheese"]
print(justin_ingredients)

# List of string to string?

numbers_and_letters = numbers + word
print(numbers_and_letters)
# string_word = "".join(numbers_and_letters)
# print(string_word)
# back_to_list = list(string_word)
# print(back_to_list)
# sum_together = numbers_and_letters[-1] + numbers_and_letters[0]
print(sum_together)
