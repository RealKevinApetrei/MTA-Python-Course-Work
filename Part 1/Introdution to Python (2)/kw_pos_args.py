def game(*, starting_score, player_name="Player 1"):
    print("Starting Score: {}".format(starting_score))
    print("Player Name: {}".format(player_name))


game(starting_score=100, player_name="Brandon")


# def example(*args, **kwargs):
#     print(args)
#     first_name = kwargs["first_name"]
#
#
# example(first_name="Justin", last_name="Dennison", age=21)


# def example(first_name="Justin", last_name="Dennison", age=21):
#     print(first_name, last_name, age)
#
#
# example("justin", "dennison", 21)
# example(last_name="dennison", first_name="justin", age=21)
