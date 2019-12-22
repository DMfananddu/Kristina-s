import simpy
from clienter import Client
import pickle
from contenter import Content
import datetime
from random import randint


COURSE_COUNT = 7
MANUAL_COUNT = 10
CLIENT_COUNT = 3500
CLIENT_GEN_TIMEOUT = 0.5


class ClientSim(object):
    def __init__(self, env, sub_list: list, content: Content):
        self.client = Client(sub_list, content)
        self.env = env
        self.content = content
        self.action = env.process(self.run())

    def run(self):
        pass