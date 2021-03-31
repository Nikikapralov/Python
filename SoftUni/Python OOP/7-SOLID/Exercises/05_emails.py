from abc import ABC, abstractmethod


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class Formatter(ABC):
    @abstractmethod
    def format(self, content):
        pass


class IContent(ABC):
    @abstractmethod
    def set_content(self):
        pass


class MyContent(IContent):
    def __init__(self, content, format):
        self.content = content
        self.format = format

    def set_content(self):
        result = self.format.format(self, self.content)
        return result


class MyMl(Formatter):
    def format(self, content):
        return content + 'MyMl'


class Email(IEmail):
    def __init__(self, protocol, content_type):
        self.protocol = protocol
        self.content_type = content_type
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        result = content.set_content()
        self.__content = result

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM', 'MyML')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(MyContent('Hello, there', MyMl))


print(email)

