# Membership Tests

edutainers = ["Vonne", "Justin", "Aubri", "Ronnie"]

print(f"Daniel in Edutainers: {'Daniel' in edutainers}")
print(f"Vonne in Edutainers: {'Vonne' in edutainers}")

print(f"Daniel not in Edutainers: {'Daniel' not in edutainers}")

# Identity Tests

favorite_food = "cheese"
lunch_today = "cheese"

print(favorite_food is lunch_today)

other_edutainers = ["Vonne", "Justin", "Aubri", "Ronnie"]

print(edutainers is other_edutainers)

# Not operator

print(not 1 == 1)
print(1 != 1)

# Precedence

print(3 * 2 ** 2)
