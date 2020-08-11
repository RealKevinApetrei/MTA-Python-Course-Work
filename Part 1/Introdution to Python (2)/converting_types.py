favorite_number = "7"  # String Variable
fav_num_type = type(favorite_number)

print(f"The type for favorite_number is: {fav_num_type}")

favorite_number_as_number = float(favorite_number)

print(f"favorite_number_as_number: {favorite_number_as_number}")
print(
    f"The type for favorite_number_as_number is: {type(favorite_number_as_number)}")

age = 12

print(f"age: {age}")
print(f"The type for age is: {type(age)}")

age_str = str(age)

print(f"age_str: {age_str}")
print(f"The type for age_str is: {type(age_str)}")

likes_cheese = 0.0

print(f"as boolean: {bool(likes_cheese)}")


# BAD!!!

number = 'print("cheese and stuff")'
number_as_a_number = eval(number)
print(f"number_as_a_number: {number_as_a_number}")
print(f"type: {type(number_as_a_number)}")
