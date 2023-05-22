"""
Deadlock conditions:
1. Mutual exclusion - 1 in non shareable state.
2. Hold and wait - needs 2 resources, one it is holding, for the other it will always wait - variation of 1.
3. No preemption - a resource can only be released after a specific command which will not take place.
4. Circular wait - variation of 2 but with multiple threads.
"""
import multiprocessing
import time

"""
Solution to the Dining Philosophers Problem with ranking implementation.
What we must learn from this implementation is that first, locks do not lock anything and the resource (food)
can be accessed without any trouble should the Philosopher (process) choose not to acquire the forks (locks),
but eat directly with his hands. Second, should the processes respect the locks, too many locks in an application
will ultimately result in this application becoming wholly sequential. 
"""


class AcquireLock:
    """
    AcquireLock implements ranking based on id.
    The ranking solution works as such:
    Instead of each philosopher going for his right fork (will result in deadlock), all
    philosophers will reach for the same fork. What that fork is will be determined by the unique id
    of the fork. As such, the first philosopher to acquire the fork is the one that will then be able to
    acquire the second and eat. As we can see by the execution though, this makes our program not as concurrent
    as we may have wished it to be. Only 2 philosophers are able to eat simultaneously, while the other 2 are left
    waiting for the fork to be released.



    Due to the OS scheduler giving priority to firstly launched processes, one Philosopher will rarely be able to
    eat. We need to implement other kinds of limitations to let the other processes have access to the locks. He
    is suffering from starvation.
    """
    def __init__(self, locks):
        self.locks = sorted(locks, key=lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, exc_type, exc_val, exc_tb):
        for lock in reversed(self.locks):
            lock.release()


class Philosopher(multiprocessing.Process):
    def __init__(self, name, locks, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.locks = locks

    def run(self):
        """
        Using the flag variable and artificially slowing the one processor down is enough for the others to get
        a grip on the scheduler and acquire the lock. This results in all philosophers eating, and not just a few.
        """
        while True:
            with AcquireLock(self.locks):
                print(f"Philosopher {self.name} is eating.")
                flag = True
                time.sleep(2)
            if flag:
                time.sleep(0.5)



def philosopher(left_fork, right_fork):
    while True:
        with AcquireLock([left_fork, right_fork]):
            print(f"Philosopher {multiprocessing.current_process()} is eating.")


if __name__ == "__main__":
    locks = [multiprocessing.Lock() for i in range(8)]
    philosophers_array = [Philosopher(str(i), [locks[i], locks[i+1]]) for i in range(4)]
    [philosopher.start() for philosopher in philosophers_array]


