import aiohttp
import asyncio
import aiofiles

urls = [
    r'https://httpstat.us/200?sleep=5000',
    r'https://httpstat.us/400?sleep=5500',
    r'https://httpstat.us/404?sleep=4000',
    r'https://httpstat.us/408',
    r'https://httpstat.us/500',
    r'https://httpstat.us/524'
]
async def get(session, url):
    async with session.get(url) as result:
        await write_to_file(data=result)
        return await result.text()

async def get_html(url):
    async with aiohttp.ClientSession() as session:
        html = await get(session=session, url=url)
        return html

async def write_to_file(data):
    async with aiofiles.open("result", "a") as file:
        while True:
            chunk = await data.content.read(1024)
            if not chunk:
                break
            await file.write(chunk.decode() + "\n")
            print(chunk.decode())

    """
    While a session is open, download 1024 bytes sized chunk of data and save it to the file, then
    await (get back in loop) and download another file. Do it in chunks to regularly give conrol back to the 
    event loop.
    """

async def main(urls):
    futures = [get_html(url) for url in urls]
    for future_result in asyncio.as_completed(futures):
        await future_result


if __name__ == "__main__":
    asyncio.run(main(urls=urls))