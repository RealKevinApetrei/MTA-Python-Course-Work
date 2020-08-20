def divmod(a, b):
    # a, b are numbers
    if type(a) == int and type(b) == int:
        # Find quotient a/b
        quotient = a / b
        # Find remainder a%b
        remainder = a %  b

        return (quotient, remainder)
    else:
        return None


def tuple_div_mod(pair_tuple):
    # pair_tuple first and second numbers
    print("Look here")
    if type(pair_tuple) == tuple:
        first, second = pair_tuple
        div = first / second
        rem = first % second
        return (div, rem)
    else:
        return None

if __name__ == "__main__":
    # this = divmod(34, 5849)
    # print(type(this))
    # div, rem = divmod(34, 5849)
    # print(div, rem)
    # print(type(div), type(rem))

    pair = (4, 7)
    div, rem = tuple_div_mod(pair)
    print(div, type(div), rem, type(rem))
