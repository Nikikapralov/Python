"""
Starvation is marked by a process not getting enough CPU resources to run its task (or access to other resources).
Priority inversion is the situation, where process A depends on process C, but process A has high priority, while
process C has low priority. As such process A will get CPU resources but will hang infinitely since its waiting for
process C that will never finish, due to being starved of resources.

Causes:
 Process C has low priority and does not get CPU attention.
 Process C is waiting for a shareable resource but process A has higher priority and process C never gets access.
"""
import threading

"""
First readers - writers problem describes a situation where 3 reader threads and 3 writer threads must take turns
in reading and writing to a file, as concurrently as possible.
Multiple threads can read from the file simultaneously, as long as no thread is writing to the file.
Only one thread can write to the file and as soon as it is writing to it, no other threads should have access
to the file.
"""

class Writer(threading.Thread):
    def __init__(self, name, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.lock = lock
    def run(self):
        while True:
            with self.lock:
                print(f"Writing being done by thread {self.name}: I wrote this. \n")



class Reader(threading.Thread):
    def __init__(self, name, lock, counters_lock, counters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.lock = lock
        self.counters = counters
        self.counters_lock = counters_lock

    def run(self):
        while True:
            with self.counters_lock:
                self.counters["readers_counter"] += 1
                if self.counters["readers_counter"] == 1:
                    self.lock.acquire()
            print(f"Reading being done by thread {self.name}: I read this.")
            with self.counters_lock:
                self.counters["readers_counter"] -= 1
                if self.counters["readers_counter"] == 0:
                    self.lock.release()





if __name__ == "__main__":
    counters = {"readers_counter": 0}
    resource_lock = threading.Lock()
    counters_lock = threading.Lock()
    readers = [Reader(str(i), resource_lock, counters_lock, counters) for i in range(3)]
    writer = Writer("1", resource_lock)
    writer.start()
    [reader.start() for reader in readers]


"""
As we can see by the results of this program, once the readers get a hold of the lock, they read so fast that
the amount of readers never reaches 0. As such they hog the resource and the writer has no ability to write.
This is called: Readers preference.
"""
