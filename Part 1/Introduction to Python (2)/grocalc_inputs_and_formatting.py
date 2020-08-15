foods_prompt = """
Which food are you purchasing?
A) Banana ($0.30/piece)
B) Apple ($1.00/piece)
C) Cheese ($3.00/pack)
D) Pickles ($2.99/jar)

Q) To Quit

> """

qty_prompt = """
How many do you need?

(Enter a number)

> """

while True:
    food = input(foods_prompt)

    if food == "Q":
        print("\nGoodbye! Come Again!")
        break

    if food not in ["A", "B", "C", "D"]:
        print("Invalid Option... Try Again")
    else:
        quantity = int(input(qty_prompt))
        if quantity < 0:
            print("\nQuantity Wrong!\n")

        if food == "A":
            cost = 0.30
            food_label = "Banana(s)"
        elif food == "B":
            cost = 1.00
            food_label = "Apple(s)"
        elif food == "C":
            cost = 3.00
            food_label = "Cheese(s)"
        else:
            cost = 2.99
            food_label = "Pickle(s)"

        total = cost * quantity
        result = "You are buying {} {} for ${}".format(quantity, food_label, total)

        print(result)
