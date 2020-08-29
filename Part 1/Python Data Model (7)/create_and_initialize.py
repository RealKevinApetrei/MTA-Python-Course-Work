import uuid


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.uuid = uuid.uuid4()
        return obj


person = Person("Mike", 28)