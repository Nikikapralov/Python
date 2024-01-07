from subsystem import WorkerFactory, Notifier, SimulationRunner

class SubsystemTasksFacade:
    """
    A simple interface to a complex system.
    """

    def __init__(self, tasks, api, post_processor):
        self.tasks = tasks
        self.api = api
        self.post_processor = post_processor

    def complete_tasks(self):
        """
        A facade that will complete the tasks. It hides the complexity of the subsystem from the user
        by providing them with a simple interface "complete_tasks". The underlying subsystem spreads the
        tasks among users, incorporates a notifier with an e-mail API and a post processor. All of them
        are decoupled and are given to the Facade through dependency injection, but the implementation is
        hidden. In reality, such a system may be very complex, may use multithreading/multiprocessing, may
        call different libraries, cache the results and do a lot of nice stuff for the user that will remain
        hidden.
        """
        workers = [SimulationRunner(task) for task in self.tasks]
        notifier = Notifier(api=self.api)
        master = WorkerFactory(workers)
        master.initialize()  # Can use multiprocessing here without the user having any clue.
        notifier.work()  # Can use asyncio to notify.
        self.post_processor.work()  # Can fuse data from multiple processes into one file.

        """
        The calls above may be implemented in a Chain of Responsibility.
        """


