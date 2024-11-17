import os

from datetime import datetime

from starlette.config import Config

base = os.path.dirname(__file__)
templates = os.path.join(base, 'templates')
static = os.path.join(base, 'static')
images = os.path.join(static, 'images')
settings = Config(os.path.join(os.path.dirname(base), '.env'))
footer = None
if settings.get('SDATE', cast=int) < datetime.now().year:
    footer = '&copy; {0}, {1}&ndash;{2} гг.'.format(
        settings.get('SNAME'),
        settings.get('SDATE', cast=int),
        datetime.now().year)
else:
    footer = f'&copy; {settings.get("SNAME")}, {datetime.now().year} г.'
settings.file_values['FOOTER'] = footer
