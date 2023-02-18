import aiohttp
import asyncio


async def main(loop):
    while True:
        try:
            async with aiohttp.ClientSession(loop=loop) as session:
                async with session.get('http://127.0.0.1:8000/send', ssl=False) as response:
                    data = await response.json()
                    if data['command'] == 'on':
                        print("[ON]")
                    elif data['command'] == 'off':
                        print('OFF')
                    elif data['command'] == 'change':
                        print(f"COLOR {data['color']}")
                    elif data['command'] == 'exit':
                        session.close()
                        exit(0)
                        break
                    else:
                        pass

        except ConnectionError as e:
            print('Connection error: {}'.format(e))


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))