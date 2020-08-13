import pathlib

current_dir = pathlib.Path()

print(current_dir)

output_filename = f"{current_dir}/output.txt"

# with open(output_filename, "w") as file:
#     file.write("weee!")

# with open(output_filename, "a") as file:
#     file.write("weee!\n")

with open("/media/kevinapetrei/KEVIN USB/Files/Programming/MTA Python Course Work/Part 1/Introdution to Python (2)/Reading Files/data.txt", "r") as input_file, open(output_filename, "w") as output:
    for line in input_file:
        if line != "\n":
            output.write(line)
