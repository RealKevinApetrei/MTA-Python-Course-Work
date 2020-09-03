from concurrent.futures import ProcessPoolExecutor


class Adder:
    def __init__(self, add_number):
        self.number = add_number

    def __call__(self, value):
        return self.number + value


def make_add(x):
    def add(y):
        return x + y
    return add

add_one = Adder(1)
add_three = Adder(3)

numbers = [1, 2, 3, 4, 5]

# print([add(x, y) for x, y in zip(numbers, numbers[1:])])
# print([add_one(x) for x in numbers])
# print([add_three(x) for x in numbers])

with ProcessPoolExecutor() as e:
    results = e.map(add_one, numbers)
    print(list(results))