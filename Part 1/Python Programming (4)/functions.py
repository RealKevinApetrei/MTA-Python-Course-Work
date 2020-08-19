def add(num, another_num):
    return num + another_num


def print_three(param):
    print(param)
    print(param)
    print(param)


def print_num_times(what, how_many):
    if type(what) == str and type(how_many) == int:
        print(what * how_many)
    else:
        print("First: NOT STR")
        print("Second: NOT INT")

if __name__ == "__main__":
    user_input = input("What is your name? ")
    num_times = int(input("How many times? "))
    print_num_times(user_input, num_times)
