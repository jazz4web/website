import asyncio
import functools
import os

from starlette.exceptions import HTTPException
from starlette.responses import FileResponse, PlainTextResponse, Response

from ..dirs import images
from ..common.flashed import get_flashed, set_flashed
from ..common.pg import get_conn
from ..errors import E404
from .tools import resize


async def show_avatar(request):
    size = request.path_params.get('size')
    if size < 22 or size > 160:
        raise HTTPException(status_code=404, detail=E404)
    conn = await get_conn(request.app.config)
    res = await conn.fetchrow(
        'SELECT id, username FROM users WHERE username = $1',
        request.path_params.get('username'))
    if res is None:
        await conn.close()
        raise HTTPException(status_code=404, detail=E404)
    ava = await conn.fetchval(
        'SELECT picture FROM avatars WHERE user_id = $1', res.get('id'))
    await conn.close()
    loop = asyncio.get_running_loop()
    image = await loop.run_in_executor(
        None, functools.partial(resize, size, ava))
    response = Response(image, media_type='image/png')
    if ava is None:
        response.headers.append('cache-control', 'public, max-age=0')
    else:
        reaponse.headers.append(
            'cache-control',
            'public, max-age={0}'.format(
                request.app.config.get(
                    'SEND_FILE_MAX_AGE', cast=int, default=0)))
    return response


async def show_favicon(request):
    if request.method == 'GET':
        response = FileResponse(
            os.path.join(images, 'favicon.ico'))
        response.headers.append(
            'cache-control',
            'public, max-age={0}'.format(
                request.app.config.get(
                    'SEND_FILE_MAX_AGE', cast=int, default=0)))
        return response


async def show_robots(request):
    return PlainTextResponse('User-agent: *\nDisallow: /')


async def show_index(request):
    conn = await get_conn(request.app.config)
    cu = None
    realm = request.query_params.get('realm')
    amount = await conn.fetchval('SELECT count(*) FROM users')
    if cu is None:
        if realm == 'login':
            await conn.close()
            return request.app.jinja.TemplateResponse(
                'main/login.html',
                {'request': request,
                 'listed': False})
    await conn.close()
    await set_flashed(request, f'Известно пользователей: {amount}.')
    return request.app.jinja.TemplateResponse(
        'main/index.html',
        {'request': request,
         'message': 'Читайте меня, читайте..!',
         'listed': True,
         'flashed': await get_flashed(request)})
