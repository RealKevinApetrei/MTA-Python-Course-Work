# Exercise 1
    
    # Example 1 (Text File: './chapter16.txt')

with open("Part 2/Book Exercises/Chapter 16/chapter16.txt", "r") as FileOut:
    contents = FileOut.read()
    print(contents)

    # Example 2 (Text File: 'Book Exercises/Chapter 16b/chapter16b.txt')

with open("Part 2/Book Exercises/Chapter 16b/chapter16b.txt", "r") as DistantOut:
    contents = DistantOut.read()
    print(contents)

    # Example 3 (Text File: './chapter16.txt')

with open("Part 2/Book Exercises/Chapter 16/chapter16.txt") as FileOut:
    contents = FileOut.read()
    contents = contents.replace("My", "Your")

    print(contents)

    # Example 4 (Text File: './chapter16.txt')

file_name = "Part 2/Book Exercises/Chapter 16/chapter16.txt"

with open(file_name, "w") as File:
    File.write("Nothing here...\n")
    File.write("What just happened!")

with open(file_name, "r") as Output:
    output = Output.read()
    print(output)


with open(file_name, "a") as Append:
    Append.write("\nWOW! WOW! WOW!")

with open(file_name, "r") as Read:
    print(Read.read())

