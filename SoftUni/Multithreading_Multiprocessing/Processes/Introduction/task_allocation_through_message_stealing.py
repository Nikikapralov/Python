import math
import multiprocessing
from collections import deque
from math import sqrt
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
    def __init__(self, name, task_queue_lock=None, steal_queues=None, daemon=False, *args, **kwargs):
        super().__init__(daemon=daemon, *args, **kwargs)
        self.name = name
        self.task_queue_lock = task_queue_lock
        self.steal_queues = steal_queues
        self.current_steal_queue_lock = None

    def run(self):
        while True:
            task_queue = self.task_queue_lock["queue"]
            lock = self.task_queue_lock["lock"]
            while not task_queue.empty():
                with lock:
                    if task_queue.empty():
                        break
                    task = task_queue.get()
                task_queue.task_done()
                if task == self.name:
                    print(f"Poison pill eaten. {self.name} is dead.")
                    return
                try:
                    print(task.process(), multiprocessing.current_process().name)
                except Exception:
                    print("Wrong poison pill for process.")
            self.current_steal_queue_lock = self.steal_queues.popleft()
            current_queue = self.current_steal_queue_lock["queue"]
            current_lock = self.current_steal_queue_lock["lock"]
            self.steal_queues.append(self.current_steal_queue_lock)

            while not current_queue.empty():
                print(f"{self.name} is stealing processes.")
                with current_lock:
                    if current_queue.empty():
                        break
                    task = current_queue.get()
                    current_queue.task_done()
                try:
                    print(task.process(), multiprocessing.current_process().name)
                except Exception:
                    print("Wrong pill")
                    current_queue.put(task)
                    break

    def __str__(self):
        return f"Process {self.name} (alive: {self.is_alive()}) with PID: {self.pid}"


if __name__ == "__main__":
    tasks = [Task(i) for i in range(3001)]
    processes = [CustomProcess(name=str(i)) for i in
                 range(2)]
    task_queues = [{"queue": multiprocessing.JoinableQueue(), "lock": multiprocessing.Lock()} for process in processes]
    chunk = math.floor(len(tasks) / len(processes))
    start = 0
    current_chunk = chunk

    for index, process in enumerate(processes):
        process.task_queue_lock = task_queues[index]
        # Making steal queues by excluding current task queue
        process.steal_queues = deque(task_queues[:index] + task_queues[index + 1:])

        for i in range(start, current_chunk):
            # Adding chunk of tasks to process
            process.task_queue_lock["queue"].put(tasks[i])

        # Adding remaining tasks to last process
        if index == len(processes) - 1:
            for i in range(current_chunk, len(tasks)):
                process.task_queue_lock["queue"].put(tasks[i])


        start = current_chunk
        current_chunk += chunk
        print(process.task_queue_lock["queue"].qsize(), start, chunk)

    [process.start() for process in processes]
    [queue["queue"].join() for queue in task_queues]

    # Adding poison pill
    for process in processes:
        process.task_queue_lock["queue"].put(process.name)
        print(f"Added poison pill for queue: {process.task_queue_lock['queue']}")

    # Check if processes are dead, queues are empty but leave them enough time to process the poison.
    sleep(3)
    [print("alive", process.name, process.is_alive()) for process in processes]
    [print(process.task_queue_lock["queue"].empty()) for process in processes]


    """
    Here we have the scheduling problem. Instantiated processes get priority over later instantiated and as such
    just a few processes do all the work. We can solve this in the following ways:
    Task stealing.
    Dynamic task allocation.
    """