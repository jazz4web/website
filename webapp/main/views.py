import os

from starlette.responses import FileResponse, PlainTextResponse

from ..dirs import images
from ..common.flashed import get_flashed, set_flashed
from ..common.pg import get_conn


async def show_favicon(request):
    if request.method == 'GET':
        return FileResponse(
            os.path.join(images, 'favicon.ico'))


async def show_robots(request):
    return PlainTextResponse('User-agent: *\nDisallow: /')


async def show_index(request):
    conn = await get_conn(request.app.config)
    amount = await conn.fetchval('SELECT count(*) FROM users')
    await conn.close()
    await set_flashed(request, f'Известно пользователей: {amount}.')
    return request.app.jinja.TemplateResponse(
        'main/index.html',
        {'request': request,
         'flashed': await get_flashed(request)})
