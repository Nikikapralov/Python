class User:

    def __init__(self, user_id, username):
        self.user_id = int(user_id)
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        if author in library.books_available:
            if book_name in library.books_available[author]:
                self.books.append(book_name)
                library.books_available[author].remove(book_name)
                library.rented_books[self.username] = {}
                library.rented_books[self.username].update({book_name: days_to_return})
                return f'{book_name} successfully rented for the next {days_to_return} days!'
            for user_name in library.rented_books:
                if book_name in library.rented_books[user_name]:
                    return f'The book "{book_name}" is already rented and will be available' \
                           f' in {library.rented_books[user_name][book_name]} days!'

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        library.rented_books[self.username].pop(book_name)

    def info(self):
        rented_books = ', '.join(sorted(self.books))
        return rented_books

    def __str__(self):
        return f'{self.user_id}, {self.username}, {self.books}'

