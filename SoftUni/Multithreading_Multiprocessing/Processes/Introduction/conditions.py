"""
Conditions are like events but make it much easier when one wants to notify all processes, instead of a specific one
to which the event belongs.
When using conditions, capture them with a "with" statement,
then do a condition.wait() to wait for the condition to be triggered before proceeding and
condition.notify_all() to send a signal to all other processes that the condition has been satisfied.

For example, we launch multiple processes but many of those have to wait for one specific to run a precondition
that is scheduled to run later in time. Before the precondition is met, the already started processes should
block and wait.
"""
import multiprocessing
from time import sleep


class CustomProcess(multiprocessing.Process):
    def __init__(self, name, function, function_kwargs, daemon=False, *args, **kwargs):
        super().__init__(daemon=daemon, *args, **kwargs)
        self.name = name
        self.function = function
        self.function_kwargs = function_kwargs

    def run(self):
        self.function(**self.function_kwargs)

    def __str__(self):
        return f"Process {self.name} (alive: {self.is_alive()}) with PID: {self.pid}"


def precondition_function(precondition):
    print("Precondition reached, notifying all.")
    with precondition:
        sleep(2)
        precondition.notify_all()


def work_function(precondition):
    with precondition:
        print(f"Process {multiprocessing.current_process().name} is checking precondition...")
        precondition.wait()
        print(f"Process {multiprocessing.current_process().name} has met the precondition and exits.")


if __name__ == "__main__":
    precondition = multiprocessing.Condition()
    processes = [CustomProcess(name="Post " + str(i), function=work_function,
                                         function_kwargs={"precondition": precondition}) for i in range(4)]
    [process.start() for process in processes]
    sleep(5)
    process_with_precondition = CustomProcess(name="Precondition", function=precondition_function, function_kwargs={"precondition": precondition})
    process_with_precondition.start()
