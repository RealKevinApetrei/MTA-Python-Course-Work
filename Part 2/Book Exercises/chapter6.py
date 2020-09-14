# Exercise 1

item_list = [1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6, 7]

print(item_list)
print(item_list[::-1])

# Exercise 2

item_list.append(13)
print(item_list)

item_list.insert(0, 999)
print(item_list)

del item_list[0]
print(item_list)

print(item_list.pop(-1))
print(item_list)

item_list.remove(12)
print(item_list)

# Exercise 3

prisoners = [
            "Bob", "James", "Kevin", "Eric", "Anton", 
            "Sammy", "Alan", "Theo", "Pondor", "Chappy"
            ]

parole = []

parole.append(prisoners.pop(0))
print(prisoners)
print(parole)

parole.append(prisoners.pop(0))
print(prisoners)
print(parole)

parole.append(prisoners.pop(0))
print(prisoners)
print(parole)

parole.append(prisoners.pop(0))
print(prisoners)
print(parole)

parole.append(prisoners.pop(0))
print(prisoners)
print(parole)

parole.append(prisoners.pop(0))
print(prisoners)
print(parole)

parole.append(prisoners.pop(0))
print(prisoners)
print(parole)

parole.append(prisoners.pop(0))
print(prisoners)
print(parole)

parole.append(prisoners.pop(0))
print(prisoners)
print(parole)

parole.append(prisoners.pop(0))
print(prisoners)
print(parole)


