def find_sum(num, second_num):
    sum = 0
    counter = num
    while counter <= second_num:
        sum += counter
        counter += 1
    return sum


def for_find_sum(start, stop):
    sum = 0
    for element in range(start, stop + 1):
        sum += element
    return sum


if __name__ == "__main__":
    while True:
        user_input = input("Fruit? (Type Q to Quit): ")
        if user_input == "Q":
            break
        else:
            print(user_input * 100)
