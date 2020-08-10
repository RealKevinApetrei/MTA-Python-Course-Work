user = {
    "first_name": "Vonne",
    "last_name": "Smith",
    "age": 24
}
data = (
    ("first_name", "Vonne"),
    ("last_name", "Smith"),
    ("age", 24)
)
user = dict(data)
# user = dict(first_name="Vonne", last_name="Smith", age=24)
stuff = list(("Cheese", "Car", "Sock"))
foods = {0: "Pizza", 1: "Cookie"}

# Getting Elements (Values)

fname = user["first_name"]
print(fname)
f = foods[0]
print(f)

# Set a Value

user["age"] = 23
print(user)
