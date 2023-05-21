"""
Daemon threads are threads that will close as soon as the program finishes.
Usually, if we do not join a thread and the program is allowed to finish, then the threads will remain active
in the background until they are resolved. A daemon thread will end the moment the program has ended.
"""
import threading
from time import sleep

thread_1 = threading.Thread(daemon=True, target=lambda: sleep(10))
thread_1.start()
"""
If not daemon, the program will hang until the lambda function is done sleeping.
"""

