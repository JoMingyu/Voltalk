# -*- coding: utf-8 -*

import fbchat


class FB:
    target_uid = '126982884508007'

    def __init__(self):
        self.client = fbchat.Client('city7311@naver.com', 'uursty199')

    def send(self, target_uid, message):
        self.client.send(target_uid, message)

    def getThreadInfo(self, target_uid, index):
        return self.client.getThreadInfo(target_uid, index)

client = FB()
