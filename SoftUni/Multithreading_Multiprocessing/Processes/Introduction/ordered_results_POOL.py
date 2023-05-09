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
"""
When starting multiple processes at the same time, it is possible that some may finish faster than
others which will inevitably result in an unordered result output. If we want to get an ordered output,
there are 2 popular pats of action:

1. Return a tuple of (PID, Result) from the function, which you can get by calling current_process() inside
the function, then order by PID.
2. Use the Pool class which will return the results in order.
"""

def result_func(secs):
    sleep(secs)
    print(f"Process {multiprocessing.current_process()} is ready.")


processes = [CustomProcess(name="A", daemon=False, function=result_func, function_kwargs={"secs": 5}),
           CustomProcess(name="B", daemon=False, function=result_func, function_kwargs={"secs": 5}),
           CustomProcess(name="C", daemon=False, function=result_func, function_kwargs={"secs": 5}),
           CustomProcess(name="D", daemon=False, function=result_func, function_kwargs={"secs": 5}),
           CustomProcess(name="E", daemon=False, function=result_func, function_kwargs={"secs": 5})]

#No ordering, no Pool.
[process.start() for process in processes]
[process.join() for process in processes]

def result_func_upload_to_Queue(secs, queue):
    sleep(secs)
    process = multiprocessing.current_process()
    print(f"Process {process} is ready. Uploading to Queue...")
    queue.put((process.pid, "RESULT"))

queue = multiprocessing.Queue()
processes = [CustomProcess(name="A", daemon=False, function=result_func_upload_to_Queue, function_kwargs={"secs": 5, 'queue': queue}),
           CustomProcess(name="B", daemon=False, function=result_func_upload_to_Queue, function_kwargs={"secs": 5, 'queue': queue}),
           CustomProcess(name="C", daemon=False, function=result_func_upload_to_Queue, function_kwargs={"secs": 5, 'queue': queue}),
           CustomProcess(name="D", daemon=False, function=result_func_upload_to_Queue, function_kwargs={"secs": 5, 'queue': queue}),
           CustomProcess(name="E", daemon=False, function=result_func_upload_to_Queue, function_kwargs={"secs": 5, 'queue': queue})]

#Ordering of results based on tuple PID
[process.start() for process in processes]
[process.join() for process in processes]
results = [queue.get() for i in range(queue.qsize())]
results = [result[0] for result in sorted(results, key=lambda x: x[0])]
print(results)

#Using multiprocessing.Pool
def result_func_name(secs, name):
    sleep(secs)
    print(name)


tasks = [result_func_name for i in range(5)]
with multiprocessing.Pool(processes=2) as pool:
    tasks = [pool.apply_async(task, args=(3, letter)) for task, letter in zip(tasks, ["A", "B", "C", "D", "E"])]
    [result.get() for result in tasks]

"""
Using multiprocessing Pool we have 8 options:
apply(task, args) - blocks execution and returns result when ready, for one off tasks
map(task, iterable, chunks) - blocks executions, returns iterable of results. Chunks can specify which 
amount of items will be sent to a pool.
starmap(task, iterable) - like map, but in starmap, each iterable item may itself be iterable allowing for 
multiple kwargs to be passed to the function
imap(task, iterable) - lazy .map(). Will complete tasks one by one and will yield results, saving memory.
apply_async() - does not block execution and returns and AsyncObject when ready. To get result, call
AsyncObject.get(timeout=0) - if timeout specified, will wait that much time for the result.
map_async() - an async version of map. Returns AsyncObjects
starmap_async(task, iterable) - same as map_async()
imap_unordered(task, iterable) - same as imap() but tasks are yielded as they are completed, not in order

For some of those you can specify a callback to fire on completion or on Error.
https://superfastpython.com/wp-content/uploads/2022/06/Table-Comparison-of-Issuing-Tasks-to-the-Process-Pool.png
"""



