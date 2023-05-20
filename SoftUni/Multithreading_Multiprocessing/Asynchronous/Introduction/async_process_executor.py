"""
By using a process executor, we can run blocking tasks as their separate processes to stop the event loop from hanging
for a very long time. (We can use the same with Threads, to run non cpu intensive functions that have no async alternative).
We use the concurrent.futures.ProcessPoolExecutor/ThreadPoolExecutor for those tasks.
"""
import asyncio
import concurrent.futures


async def main_no_exec():
    sums = await asyncio.gather(cpu_intensive_func([i for i in range(10 ** 7)]),
                                cpu_intensive_func([i for i in range(10 ** 7)]),
                                cpu_intensive_func([i for i in range(10 ** 7)]),
                                cpu_intensive_func([i for i in range(10 ** 7)]),
                                )
    print(sums)
    return


async def async_print(word):
    print(word)


async def main_exec():
    loop = asyncio.get_event_loop()
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=4)
    futures = [loop.run_in_executor(executor, cpu_intensive_func_non_async, args) for args in
               [[i for i in range(10 ** 7)] for _ in range(4)]]
    results = await asyncio.gather(*futures, async_print("Hello"), async_print("No hello"))
    print(results)
    return


async def cpu_intensive_func(array):
    print("Getting sum")
    sum = 0
    for i in array:
        sum += i
    print("Sum is ", sum)
    return sum

def cpu_intensive_func_non_async(array):
    print("Getting sum")
    sum = 0
    for i in array:
        sum += i
    print("Sum is ", sum)
    return sum


if __name__ == "__main__":
    # No executor
    asyncio.run(main_no_exec())
    # With executor
    asyncio.run(main_exec())

"""
Hello and No hello will print first even though they are scheduled last by the executor due to the time it takes 
for the other processes to fire up.
"""