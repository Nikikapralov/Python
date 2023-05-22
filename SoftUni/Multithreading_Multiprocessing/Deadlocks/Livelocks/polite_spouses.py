"""
The polite spouses problem illustrates a Livelock situation where one process will notice that the other is able
to take the resource and allow it to do so. Simultaneously, the second process will notice that the first is also
free and will allow it to access the resource. In the end, both processes simply give each other infinite right
of way.
"""
import multiprocessing
import time


class Spouse(multiprocessing.Process):
    def __init__(self, name, other_spouse=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.available = multiprocessing.Event()
        self.available.set()
        self.other_spouse = other_spouse
    def run(self):
        while True:
            if self.other_spouse.available.is_set():
                print(f"Im {self.name}. My {self.other_spouse.name} is free and I will let them do the calculations.\n"
                      f"I will try later.")
                time.sleep(5)
            else:
                self.available.clear()
                print(f"Im {self.name} and im doing calculations.")
                time.sleep(5)
                return

if __name__ == "__main__":
    husband = Spouse("husband")
    wife = Spouse("wife")
    husband.other_spouse = wife
    wife.other_spouse = husband
    wife.start()
    husband.start()

    """
    This program illustrates a livelock situation. Both processes are free, but both are instructed to give way
    to a different process if it is free. It usually occurs in solutions which try to solve the deadlock problem
    by implementing grace (should one process have the ability acquire a resource and do work, than it should be
    given the ability to do so, even if I as a process should wait.). When both processes are implementing grace,
    a livelock situation will happen.
    """
