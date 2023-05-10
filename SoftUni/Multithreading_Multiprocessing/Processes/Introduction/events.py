"""
To communicate with processes we need to use events. We cannot access the attributes of a process from
outside it (from the main process that started it, parent). We have to use events for that.
We can use events to signal one process from somewhere that something has taken place.
Events can be set, cleared and checked for their settings.
.set()
.clear()
.is_set()
"""
import multiprocessing
from time import sleep


class CustomProcess(multiprocessing.Process):
    def __init__(self, name, daemon=False, *args, **kwargs):
        super().__init__(daemon=daemon, *args, **kwargs)
        self.name = name
        self.on = multiprocessing.Event()
        self.is_working = multiprocessing.Event()
        self.process_kill = multiprocessing.Event()

    def run(self):
        while not self.process_kill.is_set():
            if self.on.is_set():
                self.is_working.set()
            else:
                self.is_working.clear()

    def __str__(self):
        return f"Process {self.name} (alive: {self.is_alive()}) with PID: {self.pid}"

if __name__ == "__main__":
    # First event is turned off.
    process = CustomProcess("A")
    process.start()
    print(process)
    # If we don't wait, the line that checks if the process is running will run while the process is in the run() function, causing it to print yes.
    sleep(1)
    print("Working: ", process.is_working.is_set())
    # Set to turn on to true.
    process.on.set()
    sleep(1)
    print("Working: ", process.is_working.is_set())
    # Event clear to turn to false.
    process.on.clear()
    sleep(1)
    print("Working: ", process.is_working.is_set())
    process.process_kill.set()
    sleep(1)
    print(process)