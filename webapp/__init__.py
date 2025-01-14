import jinja2
import typing

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.routing import Mount, Route
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles
from starlette.types import Receive, Scope, Send
from starlette.templating import Jinja2Templates
from webassets import Environment as AssetsEnvironment
from webassets.ext.jinja2 import assets

from .dirs import settings, static, templates
from .errors import show_error
from .main.views import show_avatar, show_favicon, show_index, show_robots

try:
    from .tuning import SECRET_KEY, SDESC
    if SECRET_KEY:
        settings.file_values['SECRET_KEY'] = SECRET_KEY
    if SDESC:
        settings.file_values['SDESC'] = SDESC
except ModuleNotFoundError:
    pass

DI = '''typing.Union[str, os.PathLike[typing.AnyStr],
typing.Sequence[typing.Union[str,
os.PathLike[typing.AnyStr]]]]'''.replace('\n', ' ')


class J2Templates(Jinja2Templates):
    def _create_env(
            self,
            directory: DI, **env_options: typing.Any) -> "jinja2.Environment":
        loader = jinja2.FileSystemLoader(directory)
        assets_env = AssetsEnvironment(static, '/static')
        assets_env.debug = settings.get('ASSETS_DEBUG', cast=bool)
        env_options.setdefault("loader", loader)
        env_options.setdefault("autoescape", True)
        env_options.setdefault("extensions", [assets])
        env = jinja2.Environment(**env_options)
        env.assets_environment = assets_env
        env.globals["config"] = settings
        return env


class StApp(Starlette):
    async def __call__(
            self, scope: Scope, receive: Receive, send: Send) -> None:
        scope["app"] = self
        self.config = settings
        self.jinja = J2Templates(directory=templates)
        if self.middleware_stack is None:
            self.middleware_stack = self.build_middleware_stack()
        await self.middleware_stack(scope, receive, send)

errs = {403: show_error,
        404: show_error,
        405: show_error}

middleware = [
    Middleware(
        SessionMiddleware,
        secret_key=settings('SECRET_KEY'),
        max_age=settings.get('SESSION_LIFETIME', cast=int))]


app = StApp(
    debug=settings.get('DEBUG', cast=bool),
    routes=[
        Route('/', show_index, name='index'),
        Route('/favicon.ico', show_favicon, name='favicon'),
        Route('/robots.txt', show_robots, name='robots.txt'),
        Route('/ava/{username}/{size:int}', show_avatar, name='ava'),
        Mount('/static', app=StaticFiles(directory=static), name='static')],
    middleware=middleware,
    exception_handlers=errs)
