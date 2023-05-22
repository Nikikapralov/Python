"""
Locks are designed to prevent Race Conditions. A race condition is when the program depends on the result from
process A to not be modified by process C before process B acquires it and modifies it.
For example, why is the queue.empty() function unreliable? Well while checking if queue.empty() might return false for
process A and B, assuming that the queue has just 1 element inside, both processes will go into the logic and attempt
to do calculations. There is just 1 element though, and by the time process A accesses it, process B may have already
taken it.

To prevent this race condition, we can use a lock and specify that while process A is working on a queue item,
no other process can access the Queue. Well great, that just made our program sequential :)

Locks also do not lock anything. Should a process choose to ignore the lock, it will be able to access the resource
freely. Locks have to be built in the data structures.
"""
import multiprocessing
import time


class PoliteProcess(multiprocessing.Process):

    def __init__(self, name, lock, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.lock = lock
        self.data = data

    def run(self) -> None:
        with self.lock:
            print(f"Im process {self.name} and im printing the values of {self.data}")
            time.sleep(5)


class MeanieProcess(PoliteProcess):
    def run(self) -> None:
        print(f"Im process {self.name} and I ignore locks. Im printing the values of {self.data}")


class LockBasedData:
    def __init__(self, data):
        self.data = data
        self.lock = multiprocessing.Lock()

    @property
    def data(self):
        with self.lock:
            time.sleep(5)
            return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __repr__(self):
        return str(self.data)


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    data = "MegaSecret"
    polite_1 = PoliteProcess("polite_1", lock, data)
    polite_2 = PoliteProcess("polite_2", lock, data)
    meanie = MeanieProcess("meanie", lock, data)

    polite_1.start()
    polite_2.start()
    meanie.start()
    polite_1.join()
    polite_2.join()
    meanie.join()

    #If the data does not implement locking within itself, a malicious process can simply choose not to implement locking and get access.
    # For example - linux permissions escalations through the creation of a new file.


    """
    Here, since we used a locked DS, even though meanie does not respect locks, he still has to wait :)
    """
    print("-" * 50)

    lock = multiprocessing.Lock()
    data = LockBasedData("MegaSecret")
    polite_1 = PoliteProcess("polite_1", lock, data)
    polite_2 = PoliteProcess("polite_2", lock, data)
    meanie = MeanieProcess("meanie", lock, data)

    polite_1.start()
    polite_2.start()
    meanie.start()


