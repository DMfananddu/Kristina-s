from random import randint, random


class Manual(object):
    """
    Справочник - набор текстов, которыми могут пользоваться все пользователи. Имеют стандартный набор характеристик:
        Длительность: 10-20 минут
        Сложность обработки для системы: 1
    """

    def __init__(self, name='', duration=0):
        self.theme = self.choice_theme()
        self.name = self.choice_name(str(self.theme)+'manualer_names.txt')
        self.duration = randint(10, 20)
        self.difficulty = 1
        self.type = 'Manual'
    
    def choice_theme(self, filename='manualer_themes.txt'):
        with open(filename, 'r', encoding='utf-8') as reader:
            manual_themes_list = []
            for theme in reader:
                manual_themes_list.append(theme.strip('\n'))
        return random.choice(manual_themes_list)

    def choice_name(self, filename):
        with open(filename, 'r', encoding='utf-8') as reader:
            manual_names_list = []
            for manual in reader:
                manual_names_list.append(manual.strip('\n'))
        self.name = random.choice(manual_names_list)

    def __repr__(self):
        return f' type: {self.type}\n name: {self.name}\n duration (minutes): {self.duration}\n difficulty: {self.difficulty}\n'


if __name__ == '__main__':
    print('manualer.py')