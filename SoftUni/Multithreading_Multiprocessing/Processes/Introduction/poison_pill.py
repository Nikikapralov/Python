import multiprocessing
from math import sqrt
"""
The poison pill method is a way of communication with the processes through a special task in the Queue
which signals the end of the process. To successfully implement the poison pill method, add a special task
to signal the end of the process at the end of the Queue for each process.
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
                 tasks_queue, daemon=False, *args, **kwargs):
        super().__init__(daemon=daemon, *args, **kwargs)
        self.name = name
        self.result_queue = result_queue
        self.task_queue = tasks_queue

    def run(self):
        while not self.task_queue.empty():
            task = self.task_queue.get()
            if task is None:
                self.task_queue.task_done()
                return
            print(f"{multiprocessing.current_process()} starting with task: {task}")
            result = task.process()
            self.result_queue.put(result)
            self.task_queue.task_done()

    def __str__(self):
        return f"Process {self.name} (alive: {self.is_alive()}) with PID: {self.pid}"

if __name__ == "__main__":
    tasks = [Task(i) for i in range(3000)]
    task_queue = multiprocessing.JoinableQueue()
    result_queue = multiprocessing.Queue()
    processes = [CustomProcess(name=str(i), result_queue=result_queue, tasks_queue=task_queue) for i in range(6)]
    [task_queue.put(entry) for entry in tasks]
    [task_queue.put(None) for i in range(6)] #adding poison pills
    [process.start() for process in processes]
    task_queue.join()
    results = [result_queue.get() for i in range(result_queue.qsize())]
    print(results)
    """
    Here we have the scheduling problem. Instantiated processes get priority over later instantiated and as such
    just a few processes do all the work. We can solve this in the following ways:
    Task stealing.
    Dynamic task allocation.
    
    """