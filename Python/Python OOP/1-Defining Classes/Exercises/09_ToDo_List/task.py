class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if self.name == new_name:
            return f'Name cannot be the same.'
        self.name = new_name
        return new_name

    def change_due_date(self, new_date):
        if self.due_date == new_date:
            return f'Date cannot be the same.'
        self.due_date = new_date
        return new_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):
        try:
            self.comments[comment_number - 1] = new_comment
            return ', '.join(self.comments)
        except IndexError:
            return f'Cannot find comment.'

    def details(self):
        return f'Name: {self.name} - Due Date: {self.due_date}'
