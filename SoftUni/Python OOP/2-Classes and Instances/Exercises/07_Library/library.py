class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def add_user(self, user):
        if user not in Library.user_records:
            Library.user_records.append(user)
        else:
            return f'User with id = {user.user_id} already registered in the library!'

    def remove_user(self, user):
        if user not in Library.user_records:
            return f'We could not find such user to remove!'
        Library.user_records.remove(user)
        if user.username in Library.rented_books:
            Library.rented_books.pop(user.username)

    def change_username(self, user_id, new_username):
        for user_object in Library.user_records:
            if user_object.user_id == user_id:
                if user_object.username != new_username:
                    old_username = user_object.username
                    user_object.username = new_username
                    if old_username in Library.rented_books:
                        Library.rented_books[new_username] = Library.rented_books[old_username]
                        Library.rented_books.pop(old_username)
                    return f'Username successfully changed to: {new_username} for userid: {user_id}'
                else:
                    return f'Please check again the provided username - it should be different than the username used so far!'
        return f'There is no user with id = {user_id}!'

