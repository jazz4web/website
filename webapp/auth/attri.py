USERNAME_PATTERN = r'^[A-ZА-ЯЁa-zа-яё][A-ZА-ЯЁa-zа-яё0-9\-_.]{2,15}$'


class groups:
    pariah = 'Изгои'
    reader = 'Читатели'
    commentator = 'Комментаторы'
    commentatorpro = 'Комментаторы+'
    blogger = 'Писатели'
    bloggerpro = 'Писатели+'
    keeper = 'Хранители'
    keeperpro = 'Хранители+'
    root = 'Администраторы'

    @classmethod
    def weigh(cls, group):
        if group == cls.pariah:         ## Запрет на вход в сервис
            return 0
        if group == cls.reader:         ## Чтение, Профиль, Лента, Лайки
            return 30
        if group == cls.commentator:    ##+ Комментарии, Приваты
            return 45
        if group == cls.commentatorpro: ##+ Дизлайки, Ссылки
            return 55
        if group == cls.blogger:        ##+ Свой блог, Объявления
            return 100
        if group == cls.bloggerpro:     ##+ Хостинг картинок
            return 150
        if group == cls.keeper:         ##+ Смена группы другим
            return 200
        if group == cls.keeperpro:      ##+ Литовка блогов
            return 250
        if group == cls.root:           ## Без ограничений
            return 255
        return 0
