import threading
from queue import Queue
from time import sleep

import requests

urls = [
    r'https://httpstat.us/200?sleep=10000',
    r'https://httpstat.us/400',
    r'https://httpstat.us/404',
    r'https://httpstat.us/408',
    r'https://httpstat.us/500',
    r'https://httpstat.us/524'
]

# Adding all the value inside a thread safe Queue.
my_queue = Queue() #This Queue is thread safe and has an internal locking mechanism.
[my_queue.put(url) for url in urls]

# Declaring the ping function.

def ping(url):
    response = requests.get(url)
    return response

# Declaring the check_timeout function.
def check_timeout(timeout: int, interval: float, threads: list):
    """
    The check timeout function checks if all threads are ready. If all are then exit.
    If any threads are still doing work, then check the timeout. If its bigger than zero,
    wait for the interval and then repeat. If not, the time has passed the alloted timeout and the
    function returns.
    :param timeout: Time to wait for a response.
    :param interval: Time interval between which to check for a response.
    :param threads: Threads which are currently doing the work.
    :return: Returns None.
    """
    timeout_left = timeout
    while any([thread.is_alive() for thread in threads]) and timeout_left > 0:
        timeout_left -= interval
        sleep(interval)
    for thread in [thread for thread in threads if thread.is_alive()]:
        print(f"Thread {thread.name} did not receive a response before timeout {timeout} seconds.")
# Declaring the thread class.


class PingThread(threading.Thread):

    def __init__(self, name, daemon=False, *args, **kwargs):
        super().__init__(daemon=daemon, *args, **kwargs)
        self.name = name

    def run(self):
        while not my_queue.empty():
            print(f"{self.name} attempts ping.")
            url = my_queue.get()
            response = ping(url)
            print(f"{self.name} received response: {response}")


# thread_1 = PingThread(name="A")
# thread_2 = PingThread(name="B")
#
# thread_1.start()
# thread_2.start()
#
# thread_1.join()
# thread_2.join()


INTERVAL = 0.1
TIMEOUT = 15

threads = [PingThread(name=url, daemon=True) for url in urls]
[thread.start() for thread in threads]
check_timeout(timeout=TIMEOUT, interval=INTERVAL, threads=threads)



