import multiprocessing

"""
Use a manager to solve this problem!
"""



class CustomProcess(multiprocessing.Process):

    def __init__(self, name, task_queue, result_queue, lock, chunks=2, *args, **kwargs):
        super().__init__(name=name, *args, **kwargs)
        self.name = name
        self.task_queue = task_queue
        self.result_queue = result_queue
        self.chunks = chunks
        self.lock = lock

    def run(self):
        while True:
            """
            Using a lock to avoid a race condition where 2 threads both get a number, then
            both to get another, but it is None so they both put the number back resulting in a result queue
            with bigger size. For example:
            Expected result_queue_size = 500, current_queue_size 499, after summation of 1 and 2 we will add 3 to result queue
            achieving 500.
            With race condition result is 501.
            [1, 2, None, None]
            Thread 1 gets 1.
            Thread 2 gets 2.
            Thread 1 gets None and puts 1 in result queue instead of getting 2 and summing.
            Thread 2 gets None and puts 2 in result queue instead of just getting the first None and returning.
            A lock on both gets removes the race condition.
            """
            with self.lock:
                if not self.task_queue.empty():
                    number_1 = self.task_queue.get()
                    self.task_queue.task_done()
                    if number_1 is None:
                        # Poison pill - terminate.
                        print(f"Terminated {self.name}")
                        return
                else:
                    # Queue empty - terminate.
                    return
                if not self.task_queue.empty():
                    number_2 = self.task_queue.get()
                    self.task_queue.task_done()
                    if number_2 is None:
                        # Cannot compute sum of 1 number so just add number_1 to result_queue and terminate since poison pill
                        # acquired.
                        self.result_queue.put(number_1)
                        print(f"Terminated {self.name}")
                        return
                else:
                    self.result_queue.put(number_1)
                    # Queue empty, put the 1 number in result queue and terminate.
                    return
            self.result_queue.put(number_1 + number_2)


def multiprocess_sum(array):
    if len(array) == 1:
        return array[0]
    lock = multiprocessing.Lock()
    task_queue = multiprocessing.JoinableQueue()
    [task_queue.put(element) for element in to_sum]
    task_queue_size = len(array)

    while task_queue_size > 1:
        print(task_queue.qsize(), task_queue_size)
        result_queue = multiprocessing.JoinableQueue()
        processes = [CustomProcess(name=str(i), task_queue=task_queue, result_queue=result_queue, lock=lock)
                     for i in range(8)]
        [task_queue.put(None) for process in processes]
        [process.start() for process in processes]
        # [process.join() for process in processes]
        task_queue.join()
        task_queue = result_queue
        task_queue_size = task_queue_size // 2 + task_queue_size % 2
    return result_queue.get()


if __name__ == "__main__":
    to_sum = [i for i in range(1350)]
    """
    If range is below 1200, the program will run and compute everything correctly.
    If it is above it, it will hang at the first halving, the moment the first task_queue is empty and the
    result_queue becomes the new task_queue. 
    Computer restart will make the range values fluctuate, yesterday it would hang at 1177 but run fine up to 1776.
    Queue pipe full???
    """
    print(sum(to_sum))
    for i in range(5):
        print(multiprocess_sum(to_sum))
