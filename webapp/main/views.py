import os

from starlette.responses import FileResponse, PlainTextResponse

from ..dirs import images
from ..common.flashed import get_flashed, set_flashed


async def show_favicon(request):
    if request.method == 'GET':
        return FileResponse(
            os.path.join(images, 'favicon.ico'))


async def show_robots(request):
    return PlainTextResponse('User-agent: *\nDisallow: /')


async def show_index(request):
    await set_flashed(request, 'Сайт ещё не готов...')
    return request.app.jinja.TemplateResponse(
        'main/index.html',
        {'request': request,
         'flashed': await get_flashed(request)})
