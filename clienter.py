from random import choice, randint
from contenter import Content


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

    def __init__(self, themes, content=[]):
        self.id = hash(randint(0, 10000000) + randint(0, 10000000))
        self.current_themes = []
        while len(self.current_themes) < 3:
            tmp_theme = choice(themes)
            if tmp_theme not in self.current_themes:
                self.current_themes.append(tmp_theme)
        self.sub_list_len = 0
        self.current_subscriptions = []

        if content != []:
            self.sub_list_len = randint(0,3)
            tmp_content = []
            while len(tmp_content) != self.sub_list_len:
                tmp_cont_type = randint(0, 1)
                if tmp_cont_type == 0:
                    tmp_manual_list = []
                    for i in range(len(content.manual_list)):
                        if content.manual_list[i].theme in self.current_themes:
                            tmp_manual_list.append(content.manual_list[i])
                    tmp_cont_number = randint(0, len(tmp_manual_list)-1)
                    tmp_cont = tmp_manual_list[tmp_cont_number]
                else:
                    tmp_course_list = []
                    for i in range(len(content.course_list)):
                        if content.course_list[i].theme in self.current_themes:
                            tmp_course_list.append(content.course_list[i])
                    tmp_cont_number = randint(0, len(tmp_course_list)-1)
                    tmp_cont = tmp_course_list[tmp_cont_number]
                    tmp_cont = [tmp_cont, randint(0, len(tmp_cont.lessons)-1)]
                tmp_content.append(tmp_cont)

            self.current_subscriptions = tmp_content
        
        self.statistics = {
            'ID': self.id,
            'wentToPortal': None,
            'outOfPortal': None,
            'MPST': randint(1, 48) * 30,
            'content': None,
            'studiedResources': [{
                'resource': None,
                'ST': None,
                'ET': None
            }], # ресурсы, которые были полностью изучены
        }

    def __repr__(self):
        return f'client:{self.id}\nstatistic:{self.statistics}\n' \
            f' themes:{[theme.name for theme in self.current_themes]}' \
            f' \n current_subscriptions: {[[sub.type, sub.theme, sub.name] for sub in self.current_subscriptions]}\n'

if __name__ == '__main__':
    print('clienter.py')