class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(book: Book) -> str:
        return book.content


class Product:
    def __init__(self, book: Book, formatter=None):
        self.book = book
        self.formatter = formatter


class Printer:
    def __init__(self, product):
        self.product = product

    def get_book(self):
        return self.product
