numbers = [1, 2, 3, 4, 5]

# for index in range(0, len(numbers)):
#     element = numbers[index]
#     print(element)

# While Loop - Collection - DONT

# index = 0
# numbers_length = len(numbers)
#
# while index < numbers_length:
#     element = numbers[index]
#     print(element)
#     index += 1

# Take user input

words = set()

while len(words) < 5:
    word = input(">> ")  # Blocking until something happens
    words.add(word)
    print("You have typed the following words, ", words)
