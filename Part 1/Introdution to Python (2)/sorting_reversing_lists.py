numbers = [31, 2, 43, 0, 9, 10]
letters= ["b", "c", "e", "d"]
edutainers= ["Jo", "Justin", "Vonne", "Cherokee"]

print(f"Numbers: {numbers}")
print(f"Letters: {letters}")
print(f"Edutainers: {edutainers}")

# How do I put a list in "ascending" order?

# numbers.sort()
sorted_numbers = sorted(numbers)

print(f"Sorted Numbers: {sorted_numbers}")
print(f"Numbers: {numbers}")

sorted_edutainers = sorted(edutainers)

print(f"Sorted Edutainers: {sorted_edutainers}")
print(f"Edutainers: {edutainers}")

# How do I put a list in "descending" order?

sorted_letters = sorted(letters)
des_letters = sorted(letters, reverse=True)

print(f"Letters: {letters}")
print(f"Sorted Letters: {sorted_letters}")
print(f"Descending Letters: {des_letters}")

# How do I flip a list? (Reversing, not sorting)

reversed_edutainers = list(reversed(edutainers))

print(f"Edutainers: {edutainers}")
print(f"Reversed Edutainers: {reversed_edutainers}")

edutainers.reverse()

print(f"New Reversed Edutainers: {edutainers}")
