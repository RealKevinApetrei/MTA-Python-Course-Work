# Exercise 1

print("~~ I will multiply any 2 numbers! ~~")
print("Type 'e' to exit...")

while True:
    num1 = input("Number 1: ")

    if num1.lower() == "e":
        break

    num2 = input("Number 2: ")

    if num2.lower() == "e":
        break

    try:
        print(f"Answer: {int(num1) * int(num2)}")
    except ValueError:
        print("Oops. That doesn't make a valid number operation!")