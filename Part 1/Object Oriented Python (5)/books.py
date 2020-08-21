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

class A:
    def say_my_name(self):
        print("A")

class B(A):
    pass

class C(A):
    def say_my_name(self):
        print("C")

class D(C, B):
    pass

a = A()
b = B()
c = C()
d = D()

a.say_my_name()
b.say_my_name()
c.say_my_name()
d.say_my_name()
