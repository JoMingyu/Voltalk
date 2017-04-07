# -*- coding: utf8 -*-

from flask_restful import Resource
from flask import request
import fbchat


class ChatBot(Resource):
    target_uid = '126982884508007'

    def get(self):
        self.client = fbchat.Client('city7311@naver.com', 'uursty199')
        msg = request.args.get('msg')
        self.client.send(self.target_uid, msg)
        # time.sleep(3)
        recieved_msg = self.client.getThreadInfo(self.target_uid, 1)[0].body
        data = {'message': recieved_msg}

        return data
