"""
We can use and async thread pool executor to run functions that have no async equivalent in an async program as a separate thread.
"""
import asyncio
import concurrent.futures
import time


async def async_print(word):
    print(word)
    await asyncio.sleep(1)


async def main():
    loop = asyncio.get_event_loop()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = loop.run_in_executor(executor,
                                  time.sleep,
                                  5)
    await asyncio.gather(future, async_print("Hello"), async_print("Bye"), async_print("HelloBye"))


async def blocking_sleep():
    time.sleep(5)

async def main_blocking():
    await asyncio.gather(blocking_sleep(), async_print("Hello"), async_print("Bye"), async_print("HelloBye"))

if __name__ == "__main__":
    print("Commence blocking.")
    asyncio.run(main_blocking())
    """
    When main_blocking, the blocking sleep will be executed first and block the event loop for 5 seconds. - no prints.
    In main, the sleep will be executed in a separate thread, thus not blocking control of the event loop which will
    finish the other tasks (prints) and then come back when the sleep is done.
    """
    print("Commence non blocking.")
    asyncio.run(main())