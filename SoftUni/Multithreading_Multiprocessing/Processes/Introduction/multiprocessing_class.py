from multiprocessing import Process
from time import sleep


class CustomProcess(Process):
    def __init__(self, name, function, function_kwargs, daemon=False, *args, **kwargs):
        super().__init__(daemon=daemon, *args, **kwargs)
        self.name = name
        self.function = function
        self.function_kwargs = function_kwargs

    def run(self):
        self.function(**self.function_kwargs)

    def __str__(self):
        return f"Process {self.name} (alive: {self.is_alive()}) with PID: {self.pid}"

processes = [CustomProcess(name="A", daemon=True, function=sleep, function_kwargs={"secs": 10}),
             CustomProcess(name="B", daemon=True, function=sleep, function_kwargs={"secs": 10})]
[process.start() for process in processes]
processes[0].terminate()
processes[0].join()
"""
Call process.join() right after calling .terminate() to force an update of .is_alive(). If not called,
the is_alive() function will return True which is of course, incorrect.
"""
[print(process) for process in processes]

