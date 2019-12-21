from random import choice, randint
from resource import Subscription

class Client(object):
    """
    Клиент

    themes - предпочтения по тематикам (3 темы)
    max_time - максимальное время на портале за одну симуляцию
    id - уникальный идентификатор пользователя
    current_subscriptions - list текущих подписок, которые юзер может начать смотреть
        состоит только из курсов/уроков
        Или пустой
            Он заполняться не будет
        Или занятый
            Заполняется следующим образом: берётся курс(ы) (случайно от 1 до 3),
            который существует на портале, берётся урок из этого курса (случайно),
            который пользователь посмотрел последним, начинает смотреть следующий урок
    """

    def __init__(self, themes, subs=[]):
        if len(themes) > 3:
            self.current_themes = []
            while len(self.current_themes) < 3:
                tmp_theme = choice(themes)
                if tmp_theme not in self.current_themes:
                    self.current_themes.append(tmp_theme)
        else:
            self.current_themes = themes

        if not subs:
            self.sub_list_len = randint(0,3)
            for i in range(len(self.sub_list_len)):
                self.current_subscriptions.append(Subscription(choice(self.current_themes), randint(0, 3)))

        self.id = hash(randint(0, 10000000) + randint(0, 10000000))
        self.statistics = {
            'id': self.id,
            'went to portal': None,
            'out of portal': None,
            'spend time': None,
            'studied resources': [{
                'resource': None,
                'start time': None,
                'end time': None
            }], # ресурсы, которые были полностью изучены
        }

    def __repr__(self):
        return f'client:{self.id}\nstatistic:{self.statistics}\n' \
            f' themes:{[theme.name for theme in self.current_themes]}' \
            f' \n current_subscriptions: {[[sub.type, sub.theme, sub.name] for sub in self.current_subscriptions]}\n'

if __name__ == '__main__':
    print('client.py')