import threading
import time

"""
The problem with the first approach is that, when a reader is accessing the text file and a
writer is waiting for the file to be unlocked, if another reader starts its execution and wants
to access the file, it will be given priority over the writer that has already been waiting.
Additionally, if more and more readers keep requesting access to the file, the writer will be
waiting infinitely, and that was what we observed in our first code example.
To address this problem, we will implement the specification that, once a writer makes a
request to access the file, no reader should be able to jump in line and access the file before
that writer. To do this, we will have an additional lock object in our program, to specify
whether a writer is waiting for the file, and consequently, whether a reader thread can
attempt to read the file. -- quote from the Book Mastering Concurrency.
"""


class Writer(threading.Thread):
    def __init__(self, name, lock, writers_counter_lock, writers_try_lock, writers_count, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.lock = lock
        self.writers_count = writers_count
        self.writers_try_lock = writers_try_lock
        self.writers_counter_lock = writers_counter_lock

    def run(self):
        while True:
            with self.writers_counter_lock:
                self.writers_count["writers_count"] += 1
                if self.writers_count["writers_count"] == 1:
                    self.writers_try_lock.acquire()
            with self.lock:
                print(f"Writing being done by thread {self.name}: I wrote this. \n")
            with self.writers_counter_lock:
                self.writers_count["writers_count"] -= 1
                time.sleep(1)
                if self.writers_count["writers_count"] == 0:
                    self.writers_try_lock.release()


class Reader(threading.Thread):
    def __init__(self, name, lock, counters_lock, writers_try_lock, readers_count, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.lock = lock
        self.readers_count = readers_count
        self.counters_lock = counters_lock
        self.writers_try_lock = writers_try_lock

    def run(self):
        while True:
            with self.writers_try_lock:
                with self.counters_lock:
                    self.readers_count["readers_count"] += 1
                    if self.readers_count["readers_count"] == 1:
                        self.lock.acquire()
                print(f"Reading being done by thread {self.name}: I read this.")
                with self.counters_lock:
                    self.readers_count["readers_count"] -= 1
                    if self.readers_count["readers_count"] == 0:
                        self.lock.release()

if __name__ == "__main__":
    readers_count = {"readers_count": 0}
    writers_count = {"writers_count": 0}
    resource_lock = threading.Lock()
    counters_lock = threading.Lock()
    writers_try_lock = threading.Lock()
    writers_counter_lock = threading.Lock()
    readers = [Reader(str(i), resource_lock, counters_lock, writers_try_lock, readers_count) for i in range(3)]
    writers = [Writer(str(i), resource_lock, writers_counter_lock, writers_try_lock, writers_count) for i in range(3)]
    [writer.start() for writer in writers]
    [reader.start() for reader in readers]

"""
This is an example of writers preference. Here, once the writers acquire the lock, no readers will be able to 
get access of the resource.
"""
