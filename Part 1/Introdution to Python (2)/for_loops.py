edutainers = ["Aubri", "Adam", "Vonne", "Justin", "Daniel"]
attempts = range(3)

print(f"Edutainers: {edutainers}")

for edutainer in edutainers:
    print(f"Edutainer: {edutainer}")

favorite_number = 7

for _ in attempts:
    guess = int(input("What is Vonne's favorite number? \n"))

    if guess == favorite_number:
        print("YAY! You win!!!")
        break

    else:
        print("Try again...")

print(_)

for index, edutainer in enumerate(edutainers):
    print(f"{index}: {edutainer}")
