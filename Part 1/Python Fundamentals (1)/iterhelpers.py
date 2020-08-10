foods = ["pizza", "tacos", "onions", "cheese"]
numbers = range(1, 11)
letters = "abcd"

for food, letter, row_num in zip(foods, letters, numbers):
    print(f"Row # {row_num}: {letter} likes {food}")

letter_foods = dict(zip(letters, foods))
print(letter_foods)

for index, food in enumerate(foods):
    letter = letters[index]
    print(food, letter)

shenanigans = [(index, food, letters[index])
               for index, food in enumerate(foods)]

print(shenanigans)
