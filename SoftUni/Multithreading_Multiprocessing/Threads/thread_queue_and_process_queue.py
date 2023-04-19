"""
Alternative implementation of thread scheduling.

P.S. Ok, this doesn't work since someone decided that threads can only be started once and then they have
to be recreated. I can work around that, but at this point its obvious this is not a desired approach.
Still gonna leave the code though.
"""

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

    def start(self, value):
        self.value = value
        super().start()

    def run(self):
        print(f"{self.name} started.")
        self.function(self.value)
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


task_queue = deque([9**7 for i in range(6)])
thread_A = CustomThread(name="A", function=loop, task_queue=task_queue)
thread_B = CustomThread(name="B", function=loop, task_queue=task_queue)
thread_queue = deque([thread_B, thread_A])

while task_queue:
    value = task_queue.popleft()
    while True:
        thread = thread_queue.popleft()
        thread_queue.append(thread)
        if not thread.is_alive():
            thread.start(value=value)
            break
