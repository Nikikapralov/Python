from abc import ABC, abstractmethod

class AbstractHandler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class Handler(AbstractHandler):
    _next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next:
            return self._next.handle(request)
        print("No more handlers")
        raise BaseException


class FirstHandler(Handler):

    def handle(self, request):
        if request.get("first", None):
            return "Handled by first!"
        return super().handle(request)


class SecondHandler(Handler):

    def handle(self, request):
        if request.get("second", None):
            return "Handled by second!"
        return super().handle(request)


class ThirdHandler(Handler):

    def handle(self, request):
        if request.get("third", None):
            return "Handled by third!"
        return super().handle(request)
