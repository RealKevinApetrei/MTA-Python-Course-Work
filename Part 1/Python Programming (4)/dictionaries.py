def split_comma(string):
    split_list = string.split(",")
    return {
        "first_half": split_list[0],
        "second_half": split_list[1]
    }


if __name__ == "__main__":
    # my_dictionary = {
    #     "fav_food": "yoghurt",
    #     "fav_sport": "football",
    #     "fav_day": "friday"
    # }
    #
    # for element in my_dictionary:
    #     print(element)
    #     print(my_dictionary[element])

    # logs = "asdxcvbnmklpoiuytrewqasdfghjkl,mnbvcxsaqwertyuioplkjhgfghnmnbvcdsaqwertyuiolkjhgfcz"
    # logs_count = {}
    # alpha = "abcdefghijklmnopqrstuvwxyz"
    # for letter in alpha:
    #     for char in logs:
    #         if char == letter:
    #             if char in logs_count:
    #                 logs_count[char] += 1
    #             else:
    #                 logs_count[char] = 1
    #
    # print(logs_count)
    #
    # for key, value in logs_count.items():
    #     output = "{}, {}\n".format(key, value)
    #     print(output)

    print(split_comma("tomato, tomatoo"))
