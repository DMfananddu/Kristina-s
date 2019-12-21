from random import random
from courser import Course
from manualer import Manual


class Content(object):
    """
    Создатель контента, набора контента, со всем подряд,
        что будет доступно юзеру при заходе на сайт
    """
    def __init__(self, course_count, manual_count):
        self.course_list = []
        self.manual_list = []
        tmp_course_names = []
        tmp_manual_names = []
        tmp_course = None
        tmp_manual = None
        while len(self.course_list) != course_count:
            tmp_course = Course()
            if tmp_course.name not in tmp_course_names:
                self.course_list.append(tmp_course)
                tmp_course_names.append(tmp_course.name)

        while len(self.manual_list) != manual_count:
            tmp_manual = Manual()
            if tmp_manual.name not in tmp_manual_names:
                self.manual_list.append(tmp_manual)
                tmp_manual_names.append(tmp_manual.name)
        
    def __repr__(self):
        ret_str = ''
        for i in range(manual_count):
            ret_str += f'\n\t{i+1}-й справочник:\n'
            ret_str += f'{self.manual_list[i]}\n'
        for i in range(course_count):
            ret_str += f'\n\t{i+1}-й курс:\n'
            ret_str += f'{self.course_list[i]}\n'
            for j in range(len(self.course_list[i].lessons)):
                ret_str += f'\t{self.course_list[i].lessons[j]}\n'
            ret_str += f'\n'
        return ret_str

if __name__ == '__main__':
    course_count = 7
    manual_count = 10
    test_content = Content(course_count, manual_count)
    print(test_content)
        