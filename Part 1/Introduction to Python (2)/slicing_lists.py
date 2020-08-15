letters = list("abcdefghijklmnop")

print(letters)

# How do I get the letters "c" through "f"?

selected = letters[2:6]

print(f"Selected: {selected}")

# How do I get every other letter from the list?

every_other = letters[1::2]

print(f"Every Other: {every_other}")

# Bonus: Reverse with Slices

reversed_letters = letters[::-1]

print(f"Reversed Letters: {reversed_letters}")
print(f"Letters: {letters}")


# [
# (START (DEFAULT=0))
# :
# (STOP (DEFAULT=END))
# :
# (STEP (DEFAULT=1))
# ]
