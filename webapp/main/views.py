import os

from starlette.responses import FileResponse, PlainTextResponse

from ..dirs import images


async def show_favicon(request):
    if request.method == 'GET':
        return FileResponse(
            os.path.join(images, 'favicon.ico'))


async def show_robots(request):
    return PlainTextResponse('User-agent: *\nDisallow: /')


async def show_index(request):
    return request.app.jinja.TemplateResponse(
        'main/index.html',
        {'request': request})
