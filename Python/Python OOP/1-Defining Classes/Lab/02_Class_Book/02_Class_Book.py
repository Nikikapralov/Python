class Book:
    def __init__(self, name, author, pages):
        self.pages = pages
        self.author = author
        self.name = name

book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
