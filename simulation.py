import simpy
from clienter import Client
import pickle
from contenter import Content
import datetime
from random import randint, choice


COURSE_COUNT = 7
MANUAL_COUNT = 10
CLIENT_COUNT = 1000
CLIENT_GEN_TIMEOUT = 1
SERVER_COUNT = 10


class ClientSim(object):
    def __init__(self, env, theme_list: list, content: Content):
        self.client = Client(theme_list, content)
        self.env = env
        self.content = content
        self.action = env.process(self.run())

    def run(self):
        with server.request() as req:
            self.client.statistics['wentToPortal'] = self.env.now
            self.client.StartTime = self.client.statistics['wentToPortal']
            # self.client.statistics['content'] = self.content
            yield req
            yield self.env.process(self.watch_content())
            # print(self.client.statistics['studiedResources'])

    def watch_content(self):
        tmp_cont = self.choice_content()
        if tmp_cont is not None:
            for cont, ln in tmp_cont:
                st_time = self.env.now - self.client.statistics['wentToPortal']
                if st_time<0:
                    print('23e23e23e')
                self.chosen_content, lesson_num = cont, ln
                self.client.statistics['watchedContent'] = True
                if self.chosen_content.type == 'Course':
                    self.client.statistics['studiedResources'].append({
                        'resource': self.chosen_content,
                        'lessonNumber': lesson_num+1,
                        'lessonDifficulty': \
                            self.chosen_content.lessons[lesson_num]['difficulty'],
                        'ST': st_time,
                        'ET': st_time + self.chosen_content.lessons[lesson_num]['duration']
                    })
                    self.client.StartTime += \
                        self.chosen_content.lessons[lesson_num]['duration'] + \
                        self.chosen_content.lessons[lesson_num]['difficulty']
                    yield self.env.timeout(self.chosen_content.lessons[lesson_num]['difficulty'])
                else:
                    self.client.statistics['studiedResources'].append({
                        'resource': self.chosen_content,
                        'lessonNumber': lesson_num,
                        'lessonDifficulty': self.chosen_content.difficulty,
                        'ST': st_time,
                        'ET': st_time + self.chosen_content.duration
                    })
                    self.client.StartTime += self.chosen_content.duration + \
                        self.chosen_content.difficulty
                    yield self.env.timeout(self.chosen_content.difficulty)
            self.client.statistics['outOfPortal'] = self.client.StartTime
            

    def new_now(self, now):
        return datetime.datetime.combine(datetime.date.today() +
            datetime.timedelta(days=(round(now) // 60) // 24),  # точный день
            datetime.time((round(now) // 60) % 24, round(now) % 60)
        )
    

    def choice_content(self):
        start_watching = self.client.statistics['wentToPortal']
        tmp_content = []
        for el, lesson_num in self.client.current_subscriptions:
            course_dict = dict([(sub.name, sub) for sub in self.content.course_list])
            manual_dict = dict([(sub.name, sub) for sub in self.content.manual_list])
            if el.name in course_dict.keys():
                ln = lesson_num
                while True:
                    if ln != course_dict[el.name].lessons_count:
                        if course_dict[el.name].lessons[ln]['duration'] <= \
                                self.client.MPST - start_watching:
                            tmp_content.append([course_dict[el.name], ln])
                            self.client.MPST -= course_dict[el.name].lessons[ln]['duration']
                            ln += 1
                        else:
                            break
                    else:
                        break
            if el.name in manual_dict.keys():
                if manual_dict[el.name].duration <= self.client.MPST - start_watching:
                    tmp_content.append([manual_dict[el.name], lesson_num])

        return tmp_content         # возвращаем пустоту, если для клиента нет подходящего ресурса


daily_content = Content(MANUAL_COUNT, COURSE_COUNT)
print(daily_content)


def get_theme_list(filename='themes.txt'):
    with open(filename, 'r', encoding='utf-8') as reader:
        themes_list = []
        for theme in reader:
            themes_list.append(theme.strip('\n'))
    return themes_list


env = simpy.Environment()
server = simpy.Resource(env, capacity=SERVER_COUNT)
themes = get_theme_list()
clients = []
def client_creating(env, clients):
    for i in range(CLIENT_COUNT):
        client = ClientSim(env, themes, daily_content)
        clients.append(client)
        yield env.timeout(CLIENT_GEN_TIMEOUT)
env.process(client_creating(env, clients))
env.run(until=1440) # сутки моделировали-моделировали, да не вымоделировали

# Перенос статистики в файл
statistic = []
for i in range(clients.__len__()):
    statistic.append(clients[i].client.statistics)
with open('sim.pickle', 'wb') as writer:
    pickle.dump(statistic, writer)
