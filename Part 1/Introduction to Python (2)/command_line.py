import sys

filename = sys.argv[0]
arguments = sys.argv[1:]

food = arguments[0]
quantity = int(arguments[1])
cost = float(arguments[2])

print("You are buying {} {} for ${}".format(quantity, food, quantity * cost))
