from abc import ABC, abstractmethod


class Worker(ABC):
    """
    Abstract worker.
    """
    def __init__(self):
        pass

    @abstractmethod
    def work(self):
        pass


class SimulationRunner(Worker):
    def __init__(self, task):
        super().__init__()
        self.task = task
    def work(self):
        print(f"Runs simulations. {self.task}")

class Notifier(Worker):

    def __init__(self, api):
        super().__init__()
        self.api = api

    def work(self):
        print("Notifying.")
        self.api.send()


class Emailer:
    def send(self):
        print("Sending email.")


class PostProcessor(Worker):

    def work(self):
        print("Post processing.")


class WorkerFactory:

    def __init__(self, workers):
        self.workers = workers


    def initialize(self):
        print('Initializing complex factory set up.')
        for worker in self.workers:
            worker.work()

        print('Performing complex factory clean up.')
