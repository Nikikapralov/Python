import asyncio
import time
import multiprocessing


async def blocking_sleep_async():
    time.sleep(5)


def blocking_sleep():
    time.sleep(5)


async def async_print(word):
    print(word)
    await asyncio.sleep(0)


async def main():
    await asyncio.gather(blocking_sleep_async(),
                         async_print("Hello main"),
                         async_print("Im starting a heavy duty process main wait 5 seconds"))


async def run_process():
    process = multiprocessing.Process(target=blocking_sleep)
    process.start()
    print("Before giving way")
    await asyncio.sleep(0)
    print("After giving way and queue coming back to function")


async def main_process():
    await asyncio.gather(run_process(),
                         async_print("Hello main_process"),
                         async_print("Im starting a heavy duty process main_process wait 5 seconds"))
if __name__ == "__main__":
    asyncio.run(main())
    print("_____Other option______")
    asyncio.run(main_process())