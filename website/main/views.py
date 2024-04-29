import os

from starlette.responses import FileResponse

from ..dirs import static
from ..common.pg import get_conn


async def show_index(request):
    query = None
    if username := request.query_params.get('username'):
        conn = await get_conn(request.app.config)
        query = await conn.fetchrow(
            'SELECT id, username, message FROM users WHERE username = $1',
            username)
        await conn.close()
    return request.app.jinja.TemplateResponse(
        'main/index.html',
        {'request': request,
         'data': query})


async def show_favicon(request):
    if request.method == 'GET':
        return FileResponse(
            os.path.join(static, 'images', 'favicon.ico'))
