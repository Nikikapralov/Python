from datetime import datetime
import threading
from collections import deque


class CustomThread(threading.Thread):
    def __init__(self, function, task_queue, name):
        super().__init__()
        self.function = function
        self.lock = threading.Lock()
        self.task_queue = task_queue
        self.name = name

    def run(self):
        while self.task_queue:
            with self.lock:
                entry = self.task_queue.popleft()
            print(f"{self.name} started.")
            self.function(entry)
            print(f"{self.name} finished.")


def time_it(function):
    def inner(up_to):
        start = datetime.now()
        function(up_to)
        end = datetime.now()
        print("Process finished", end - start)
    return inner

@time_it
def loop(up_to):
    collector = []
    for i in range(up_to):
        collector.append(i)


task_queue = deque([9**8 for i in range(2)])
thread_A = CustomThread(name="A", function=loop, task_queue=task_queue)
thread_B = CustomThread(name="B", function=loop, task_queue=task_queue)
thread_A.start()
thread_B.start()
thread_B.join()
thread_A.join()

"""
Here, you can easily see the GIL in action.
Start the program with a task_queue of 1 element and it will finish in 14 seconds (for me).
Start it with 2, and it will finish for 28. Wait, but we have 2 threads and both start immediately,
why don't we finish in 14 seconds? Because of the GIL. While one thread is running, another cannot run!
Sounds stupid yeah, but it makes sense in the context of an interpreted language. So basically, the
program switches between looping through A and B constantly. Threads are best used when our programs have to
wait for an answer from a server for example.
"""
