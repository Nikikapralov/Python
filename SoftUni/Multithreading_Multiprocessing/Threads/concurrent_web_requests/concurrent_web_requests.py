import threading
from queue import Queue

import requests

urls = [
    r'https://httpstat.us/200',
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

# Declaring the thread class.


class PingThread(threading.Thread):

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

threads = [PingThread(name=url) for url in urls]
[thread.start() for thread in threads]
[thread.join() for thread in threads]