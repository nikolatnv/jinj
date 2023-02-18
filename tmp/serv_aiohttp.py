import asyncio
from aiohttp import web
import json


async def handle_command(request):
    data = await request.json()
    print(request.json)
    cmd = data['cmd']

    # Implement command processing here
    # .....

    return web.Response(text=json.dumps({'cmd': cmd}))


@web.middleware
async def middleware_factory(request, handler):
    response = await handler(request)
    response.headers['Content-Type'] = 'application/json'
    return response


# Change "app" to the name of your application
app = web.Application(middlewares=[middleware_factory])

# Change "route" and "handle_command" to the appropriate routes and command handlers
app.add_routes([web.post('/route', handle_command)])

web.run_app(app, host='127.0.0.1', port=3000)