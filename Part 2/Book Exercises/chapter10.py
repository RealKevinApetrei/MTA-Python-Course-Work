# Exercise 1

inmate1 = {
            "name":"Rob", 
            "gender":"Male", 
            "crime":"Robbery",
            "due for release":"12 Sep 2021", 
            "option of fine":"No"
        }

# Exercise 2

inmate2 = {
            "name":"Banks", 
            "gender":"Male", 
            "crime":"Inside Trading",
            "due for release":"9 Aug 2029", 
            "option of fine":"No"
        }

for key, value in inmate1.items():
    print(f"{key}: {value}\n")

for key, value in inmate1.items():
    print(f"{key}: {value}\n")

# Exercise 3

total_prisoners = ["Murray", "Tim", "Frank", "Rob", "Banks"]
due_for_release = ["Murray", "Tim", "Frank"]
released = ["Murray"]

for prisoner in due_for_release:
    if prisoner not in released:
        print("We are sorry, you can be released soon.")
    else:
        print("Your sentence has not expired yet. Good Luck!")

# Exercise 4

to_find = ["Tim", "Fog", "Murray"]

for prisoner in to_find:
    if prisoner in total_prisoners:
        print("Prisoner in Jail!")
    else:
        print("Prisoner NOT in jail!")