numbers = [1, 2, 3, 4, 5, 6]
# other = []

# print(numbers)
# print(other)

# Add 3 to each number

# for number in numbers:
#     other.append(number + 3)

other = [number + 3 for number in numbers if number % 2 == 0]

print(numbers)
print(other)
