Демонстрационное [web-приложение](https://avm4.ru/blogs/programming/t/webapp)
на Python и Starlette. Детальное пошаговое описание процесса разработки можно
найти на моём сайте по ссылке.

Порядок запуска на базе Debian trixie:

```
$ mkdir ~/sites
$ cd ~/sites
$ git clone https://github.com/jazz4web/website.git
$ cd website
$ sudo apt install $(cat deployment/packages)
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ tar xvaf deployment/vendor.tar.gz -C webapp/static
$ cp env_template .env
$ mkdir webapp/static/generic
$ ln -s -T ~/sites/website/webapp/static/vendor/bootstrap/fonts \
  webapp/static/generic/fonts
$ python runserver.py
```

Проект закрыт.
