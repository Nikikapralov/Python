import asyncio


async def main():
    await asyncio.gather(*[coroutine() for i in range(3)])


async def coroutine():
    await wait(1)
    await wait(2)
    await wait(3)


async def wait(delay=0):
    print(f"Waiting for {delay}")
    await asyncio.sleep(delay)


if __name__ == "__main__":
    asyncio.run(main())

"""
Asynchronous programming makes use of a drop in Event Loop. 
The event loop runs on one core, but makes the execution of I/O bound tasks asynchronous, to a point
where they are done almost in parallel.
The await word signals a coroutine, a point in the code where the control will be given to the event loop 
to run a different coroutine before it then returns control as well. As soon as the coroutine returns and the event loop
has the ability, the first function that had called await will continue down its execution.
Unless await, yield, or return are used at the start of each line, that line is blocking.

Use await asyncio.sleep(0) to give control back to the event loop.
Use .gather(tasks, tasks) to wait for all tasks inside to resolve before moving on, or do:
.as_completed(tasks, tasks) to get the result and start an operation on it as soon as it is done, without waiting for all to
complete first.
"""
