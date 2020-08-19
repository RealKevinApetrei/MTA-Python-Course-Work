if __name__ == "__name__":
    # fav_foods = ["pizza", "spaghetti", "mangos"]
    # words = ["The", "Hammer", "Car", "Pizza"]
    # for word in words:
    #     if word in fav_foods:
    #         print("That is a favorite food of mine also!")
    #     else:
    #         print("I do not like that")
    user_input_list = []
    while True:
        user_input = input("What are some numbers to sum up? Press Q to Quit >>> ")
        if user_input == "Q":
            break
        else:
            user_input = int(user_input)
            user_input_list.append(user_input)

    output = "Your sum is {}".format(sum(user_input_list))
    print(output)
