with open("/media/kevinapetrei/KEVIN USB/Files/Programming/MTA Python Course Work/Part 1/Introdution to Python (2)/Reading Files/data.txt") as file:
    text = file.read()

    # Back to beginning
    file.seek(0)

    print(text)

    lines = file.readlines()
    print(lines)
