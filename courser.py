from random import randint, random, choice


class Course(object):
    """
    Курс - набор уроков (от 4 до 16) по определенной Тематике;
    Тематика - одна из списка тематик
    Урок - объект, имеющий след. характеристики:
        Номер в курсе
        Тип урока:
            Видео (долгое, среднее, короткое)
            Текст (долгий, средний, короткий)
            Тест с ограничением по времени (долгий, средний, короткий)
        Длительность полного изучения:
            У Короткого: от 5 минут до 20 минут
            У Среднего: от 30 минут до 50 минут
            У Длинного: от 60 минут до 120 минут
        Сложность обработки для системы:
            У Текста: 1
            У Видео: 2
            У Теста: 3
    """

    def __init__(self, name='', duration=0):
        self.theme = self.choice_theme()
        self.name = self.choice_name('data/'+self.theme+'course_names.txt')
        self.lessons_count = randint(4, 16)
        self.lesson_duraion_type = randint(0, 2)
        self.lessons = self.create_lessons()
        self.type = 'Course'
    
    def choice_theme(self, filename='data/themes.txt'):
        with open(filename, 'r', encoding='utf-8') as reader:
            course_themes_list = []
            for theme in reader:
                course_themes_list.append(theme.strip('\n'))
        return choice(course_themes_list)

    def choice_name(self, filename):
        with open(filename, 'r', encoding='utf-8') as reader:
            course_names_list = []
            for course in reader:
                course_names_list.append(course.strip('\n'))
        return choice(course_names_list)

    def create_lessons(self):
        types = ['text', 'video', 'quiz']
        tmp_lessons = []
        for i in range(self.lessons_count):
            difficulty = randint(0, 4)
            if difficulty == 4:
                difficulty = 2
            elif difficulty == 0:
                difficulty = 0
            else:
                difficulty = 1
            tmp_lessons.append({
                'number': i+1,
                'type': types[difficulty],
                'difficulty': difficulty+2,
                'duration': self.duration()
            })

        return tmp_lessons

    def duration(self):
        duration = 0
        if self.lesson_duraion_type == 0:
            duration = randint(5, 20)
        elif self.lesson_duraion_type == 1:
            duration = randint(30, 50)
        else:
            duration = randint(60, 120)
        return duration

    def __repr__(self):
        return f' type: {self.type} | theme: {self.theme} | name: {self.name} | lessons_count: {self.lessons_count} | lesson_duraion_type: {self.lesson_duraion_type}\n'


if __name__ == '__main__':
    print('courser.py')