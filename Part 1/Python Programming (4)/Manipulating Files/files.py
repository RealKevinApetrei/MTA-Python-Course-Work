import os

dir = os.getcwd() + "/Part 1/Python Programming (4)/Manipulating Files/"

if __name__ == "__main__":
    with open(dir + "python.txt", "r") as f:
        text = f.read()
        text_list = text.split("\n")


    with open(dir + "new_python.txt", "w") as fw:
        for el in text_list:
            fw.write(el)
            fw.write("\n")
            fw.write("-----")
            fw.write("\n")
