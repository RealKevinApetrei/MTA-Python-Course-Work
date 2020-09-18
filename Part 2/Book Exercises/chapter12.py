# Exercise 1

name = input("What is your name: ")
print(f"Welcome to the Hotel, {name}!")

# Exercise 2
shop_items = {"pencil": 0, "pen": 0, "ruler": 1, "notebook": 1}

print("Here are our shop items:")
for item in shop_items.keys():
    print(f"- {item}")

item = input("Check Item: ").lower()

if item in shop_items:
    if shop_items[item] == 1:
        print("Students require money to buy this item.")
    elif shop_items[item] == 0:
        print("Students are offered this item for free.")
else:
    print("We do not offer or sell this item here.")

# Exercise 3

medicines = {"1495": "not expired", "9134": "expired", "9304": "not expired", "3040": "expired"}

print("Here are our medicine codes:")
for medicine in medicines.keys():
    print(f"- {medicine}")

medicine_code = input("Medicine Code: ")

if medicine_code in medicines:
    print(f"Medicine Code: {medicine_code} is {medicines[medicine_code]}.")
else:
    print("We do not store this code here.")