import time
import threading

"""
The previous 2 solutions failed because they didn't give equal priority to both sides.
It was either readers preference or writers preference. This solution will provide equal priorities
to both sides and guarantee a fair access to the resource. It will implement a service lock, that both readers
and writers must acquire to access the data. Once the service lock is acquired, the readers that are reading will 
finish but no new readers will begin before the writer that has the lock finishes writing.

The way this works is:
We implement a service lock that has to be acquired by both the readers and the writers, but the service lock
has to be acquired only for the most minimal amount of time, just so that the scheduling will work and not allow
preference.
The writers acquire the service lock long enough to acquire the resource lock. Then it is released and while a 
writer is writing, another thread can acquire the service log.
The readers acquire the service lock long enough to acquire the counter lock then they release it so that 
someone else may acquire it. 


At the end, to escape from starvation, we must implement fairness to the access of the resourcess.
Potential solutions as quoted from the book Masterring Concurrency:
Increasing the priority of low-priority threads: As we did with the writer
threads in the second approach and the reader threads in the third approach to
the readers-writers problem, prioritizing the threads that would otherwise not
have any opportunity to access the shared resource can successfully eliminate
starvation.
First-in-first-out thread queue: To ensure that a thread that started waiting for
the shared resource before another thread will be able to acquire the resource
before the other thread, we can keep track of the threads requesting access in a
first-in-first-out queue.
Other methods: Several methods can also be implemented to balance the
selection frequency of different threads. For example, a priority queue that also
gives gradually increasing priority to threads that have been waiting in the
queue for a long time, or if a thread has been able to access the shared resource
for many times, it will be given less priority, and so on.
"""

class Writer(threading.Thread):
    def __init__(self, name, lock, service_lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.lock = lock
        self.service_lock = service_lock

    def run(self):
        while True:
            with self.service_lock:
                self.lock.acquire()
            print(f"Writing being done by thread {self.name}: I wrote this. \n")
            self.lock.release()


class Reader(threading.Thread):
    def __init__(self, name, lock, counters_lock, service_lock, readers_count, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.lock = lock
        self.readers_count = readers_count
        self.counters_lock = counters_lock
        self.service_lock = service_lock

    def run(self):
        while True:
            with self.service_lock:
                self.counters_lock.acquire()
            self.readers_count["readers_count"] += 1
            if self.readers_count["readers_count"] == 1:
                self.lock.acquire()
            self.counters_lock.release()
            print(f"Reading being done by thread {self.name}: I read this.")
            with self.counters_lock:
                self.readers_count["readers_count"] -= 1
                if self.readers_count["readers_count"] == 0:
                    self.lock.release()

if __name__ == "__main__":
    readers_count = {"readers_count": 0}
    resource_lock = threading.Lock()
    counters_lock = threading.Lock()
    service_lock = threading.Lock()
    readers = [Reader(str(i), resource_lock, counters_lock, service_lock, readers_count) for i in range(3)]
    writers = [Writer(str(i), resource_lock, service_lock) for i in range(3)]
    [writer.start() for writer in writers]
    [reader.start() for reader in readers]