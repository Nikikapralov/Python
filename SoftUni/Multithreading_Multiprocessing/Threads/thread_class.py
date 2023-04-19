import threading

class CustomThread(threading.Thread):

    def __init__(self, param):
        super().__init__()
        self.param = param

    def run(self):
        """
        Executed when thread.start() is called.
        Write the logic here.
        """
        pass
