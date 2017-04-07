# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
import fbchat
import time


class ChatBot(Resource):
    target_uid = '126982884508007'

    def get(self):
        client = fbchat.Client('city7311@naver.com', 'uursty199')
        msg = request.args.get('msg')
        client.send(self.target_uid, msg)
        time.sleep(2)
        recieved_msg = client.getThreadInfo(self.target_uid, 3)
        s = '부터'
        print('부터'.encode('utf-8'))

        if '부터' in msg or '까지' in msg:
            # period
            for msg in recieved_msg:
                if 'period_usage' in msg.body:
                    data = {'message': msg.body.split(':')[1] + '만큼 사용했습니다.'}
                    return data
        elif '어제' in msg or '그저께' in msg:
            # today_usage
            for msg in recieved_msg:
                if 'today_usage' in msg.body:
                    data = {'message': msg.body.split(':')[1] + '만큼 사용되었습니다.'}
                    return data
        else:
            # site_usage
            for msg in recieved_msg:
                if 'site_usage' in msg.body:
                    data = {'message': msg.body.split(':')[1] + '만큼 사용 중입니다.'}
                    return data
