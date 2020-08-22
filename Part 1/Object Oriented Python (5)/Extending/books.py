# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return "<Book: {} by {}>".format(self.title, self.author)
#
#
# class TextBook(Book):
#     def __init__(self, title, author, edition):
#         super().__init__(title, author)
#         self.edition = edition
#
   #  def __init__(self, title, author, edition):
   #      self.title = title
   #      self.author = author
   #      self.edition = edition
   #
   #  def __str__(self):
   #     return "<TextBook: {} by {} ({} edition)>".format(self.title,
   #                                                       self.author,
   #                                                       self.edition
   #                                                       )
#
# book = Book(title="All the light", author="some person")
# print(book)
#
# textbook = TextBook(title="Physics", author="Physics Author", edition=5)
# print(textbook)

# class A:
#     def say_my_name(self):
#         print("A")
#
# class B(A):
#     pass
#
# class C(A):
#     def say_my_name(self):
#         print("C")
#
# class D(C, B):
#     pass
#
# a = A()
# b = B()
# c = C()
# d = D()
#
# a.say_my_name()
# b.say_my_name()
# c.say_my_name()
# d.say_my_name()
#
# class  Writeable:
#     def write(self, data):
#         with open(self.filepath, "w") as f:
#             f.write(data)
#
# class JSONSerializable:
#     def to_json(self):
#         import json
#         print(json.dumps(self.__dict__))
#
# class Readable:
#     def read(self):
#         with open(self.filepath, "r") as f:
#             print(f.read())
#
# class Book(Writeable, Readable, JSONSerializable):
#     def __init__(self, title, author, filepath):
#         self.title = title
#         self.author = author
#         self.filepath = filepath
import json


class Reader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath, "r") as f:
            print(f.read())


class Writer:
    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, data):
        with open(self.filepath, "w") as f:
            f.write(data)


class JSONSerializer:
    def to_json(self, obj):
        print(json.dumps(obj))


class Book:
    def __init__(self, title, author, filepath):
        self.title = title
        self.author = author
        self.filepath = filepath

        self.reader = Reader(filepath)
        self.writer = Writer(filepath)
        self.serializer = JSONSerializer()

    def read(self):
        self.reader.read()

    def write(self, data):
        self.writer.write(data)

    def to_json(self):
        self.serializer.to_json(dict(
                                title=self.title,
                                author=self.author,
                                filepath=self.filepath
                            ))


book = Book(title="something", author="someone", filepath="/media/kevinapetrei/KEVIN USB/Programming/Python Programs/MTA Python Course Work/Part 1/Object Oriented Python (5)/Extending/some_book.txt")
book.write("Here is the first line!")
book.read()
book.write("Some more things")
book.read()
book.to_json()
