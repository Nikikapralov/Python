import asyncio
import aiohttp


urls = [
    r'https://httpstat.us/200?sleep=5000',
    r'https://httpstat.us/400?sleep=5050',
    r'https://httpstat.us/404?sleep=4000',
    r'https://httpstat.us/408',
    r'https://httpstat.us/500',
    r'https://httpstat.us/524'
]

async def get(session, url):
    """
    Asynchronously start a get request to a website.
    The result - result is received asynchronously.
    """
    async with session.get(url, ssl=False) as result:
        return result.status

async def get_result(url):
    async with aiohttp.ClientSession() as session:
        result = await get(session=session, url=url)
        print(result)
        return result

async def main(urls):
    """
    With a separate session for each url, send a get request and await its result.
    We send asynchronous get requests.
    """
    futures = await asyncio.gather(*[get_result(url) for url in urls])
    print(futures)


if __name__ == "__main__":
    asyncio.run(main(urls))

    """
    Asyncio gather returns a future that must be ran in the event loop. Gather simply returns a future that waits
    for all functions inside it to complete before moving on. If you want to register one task, use
    .create_task()
    If you want to do something as soon as the future is completed, run as_completed.
    for coroutine in asyncio.as_completed(coroutines)
    (each must be a coroutine function)
    """