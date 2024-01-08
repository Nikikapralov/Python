from abc import ABC, abstractmethod


class Button:
    def __init__(self, command):
        self.command = command

    def click(self, request_details: dict):
        print("Button")
        self.command.execute(request_details)


class CoolButton(Button):

    def change_shape(self):
        pass

    def click(self, request_details: dict):
        print("Cool Button")
        self.command.execute(request_details)


class Command(ABC):

    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self, request_details):
        pass


class SaveCommand(Command):

    def execute(self, request_details):
        # This feels like code smell now, but in reality it isn't.
        if request_details["method"] == "Save":
            print("Calling save.")
            self.receiver.save()
        else:
            print("Method not allowed.")


class DeleteCommand(Command):

    def execute(self, request_details):
        if request_details["method"] == "Delete":
            print("Calling delete.")
            self.receiver.delete()
        else:
            print("Method not allowed.")

class Receiver:
    @staticmethod
    def save():
        print("Saved")

    @staticmethod
    def delete():
        print("Deleted")


