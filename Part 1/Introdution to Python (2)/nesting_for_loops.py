numbers = [1, 2, 3, 4]
letters = "abcd"

# for number, letter in zip(numbers, letters):
#     print(f"{number}, {letter}")

# for number in numbers:
#     for letter in letters:
#         print(number, letter)
#         if letter == "a" and number == 1:
#             for i in range(9):
#                 print(number, letter, i)

days = [
    list(range(3)),
    list(range(4)),
    list(range(5))
]

print(days)

total = 0

for day in days:
    for sale in day:
        print(f"Total: {total} | Sale: {sale}")
        total = total + sale
