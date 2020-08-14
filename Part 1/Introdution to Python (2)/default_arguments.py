def eat(food=None, happy=True):
    if happy:
        print("Yayyyy!!!!")
    if food is None:
        print("Nom nom!!")
    else:
        print("I had some {}.".format(food))


eat("cheese")
eat()
