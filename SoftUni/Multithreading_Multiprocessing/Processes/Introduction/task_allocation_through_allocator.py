import multiprocessing
from math import sqrt
from random import shuffle
from time import sleep

"""
Dynamic task allocation through the use of an allocator.
If no dynamic task allocation is used, since the tasks take very little time and priority is given to
first started processes, we end up with the situation of just 1 process doing all the work and repeatedly snatching
new tasks from the Queue. We have implemented task allocation through an allocator.

The allocator checks which processes are alive and if they are currently doing any work. If so,
it finds a process that is not doing any work and gives it permission to start working. As soon as a process
finishes working, it waits for permission from the allocator to resume working.
The method is a little slower but it distributes the work more evenly around the processes.
"""

class Task():
    def __init__(self, x):
        self.x = x

    def process(self):
        if self.x < 2:
            return '%i is not a prime number.' % self.x
        if self.x == 2:
            return '%i is a prime number.' % self.x
        if self.x % 2 == 0:
            return '%i is not a prime number.' % self.x
        limit = int(sqrt(self.x)) + 1
        for i in range(3, limit, 2):
            if self.x % i == 0:
                return '%i is not a prime number.' % self.x
        return '%i is a prime number.' % self.x

    def __str__(self):
        return 'Checking if %i is a prime or not.' % self.x


class CustomProcess(multiprocessing.Process):
    def __init__(self, name, result_queue,
                 tasks_queue, daemon=False, event_allowed=multiprocessing.Event(),
                 event_working=multiprocessing.Event(), *args, **kwargs):
        super().__init__(daemon=daemon, *args, **kwargs)
        self.name = name
        self.result_queue = result_queue
        self.task_queue = tasks_queue
        self.event_allowed = event_allowed
        self.event_working = event_working

    def run(self):
        while True:
            if self.event_allowed.is_set():
                self.event_working.set()
                task = self.task_queue.get()
                if task is None:
                    self.event_working.clear()
                    self.event_allowed.clear()
                    self.task_queue.task_done()
                    return
                print(f"{multiprocessing.current_process()} starting with task: {task}")
                result = task.process()
                self.result_queue.put(result)
                self.task_queue.task_done()
                self.event_working.clear()
                self.event_allowed.clear()

    def __str__(self):
        return f"Process {self.name} (alive: {self.is_alive()}) with PID: {self.pid}"


if __name__ == "__main__":
    tasks = [Task(i) for i in range(3000)]
    task_queue = multiprocessing.JoinableQueue()
    result_queue = multiprocessing.Queue()
    [task_queue.put(entry) for entry in tasks]
    processes = [CustomProcess(name=str(i), result_queue=result_queue, tasks_queue=task_queue) for i in
                 range(6)]
    [task_queue.put(None) for entry in processes]
    [process.start() for process in processes]

    while not task_queue.empty():
        processes = [process for process in processes if process.is_alive()]
        shuffle(processes)
        for process in processes:
            if not process.event_working.is_set():
                process.event_allowed.set()

    task_queue.join()
    results = [result_queue.get() for i in range(result_queue.qsize())]
    print(results)
    """
    Here we have the scheduling problem. Instantiated processes get priority over later instantiated and as such
    just a few processes do all the work. We can solve this in the following ways:
    Task stealing.
    Dynamic task allocation.
    """