from starlette.responses import JSONResponse

E404 = 'Такой страницы у нас нет.'


async def show_error(request, exc):
    if exc.status_code == 403:
        exc.detail = 'Доступ ограничен, недостаточно прав.'
    if exc.status_code == 404:
        exc.detail = E404
    if exc.status_code == 405:
        exc.detail = 'Метод не позволен.'
    if request.method == 'GET':
        return request.app.jinja.TemplateResponse(
            'errors/error.html',
            {'reason': exc.detail,
             'request': request,
             'error': exc.status_code},
            status_code=exc.status_code)
    else:
        res = {'message': exc.detail,
               'error': exc.status_code}
        return JSONResponse(res)
