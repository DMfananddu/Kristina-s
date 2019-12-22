import simpy
from clienter import Client
import pickle
from contenter import Content
import datetime
from random import randint, choice


COURSE_COUNT = 7
MANUAL_COUNT = 10
CLIENT_COUNT = 100
CLIENT_GEN_TIMEOUT = 5
SERVER_COUNT = 5


class ClientSim(object):
    def __init__(self, env, theme_list: list, content: Content):
        self.client = Client(theme_list, content)
        self.env = env
        self.content = content
        self.action = env.process(self.run())

    def run(self):
        with server.request() as req:
            self.client.statistics['wentToPortal'] = self.env.now
            yield req
            yield self.env.process(self.watch_content())

    def watch_content(self):
        yield self.env.timeout(0.00001)
    
    def new_now(self, now):
        return datetime.datetime.combine(datetime.date.today() +
            datetime.timedelta(days=(round(now) // 60) // 24),  # точный день
            datetime.time((round(now) // 60) % 24, round(now) % 60)
        )
    
    def choice_content_element(self):
        for i in self.client.current_subscriptions:
            course_dict = dict([(sub.name, sub) for sub in self.content.course_list])
            manual_dict = dict([(sub.name, sub) for sub in self.content.course_list])
            if i.name in course_dict.keys():
                return course_dict[i.name]
            if i.name in manual_dict.keys():
                return manual_dict[i.name]
        return None         # возвращаем пустоту, если для клиента нет подходящего фильма



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
