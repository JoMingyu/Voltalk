# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
import time

from support import fb_account


class ChatBot(Resource):
    target_uid = '126982884508007'

    def get(self):
        msg = request.args.get('msg')
        fb_account.client.send(self.target_uid, msg)
        time.sleep(1)
        recieved_msg = fb_account.client.getThreadInfo(self.target_uid, 3)

        if '부터' in msg or '까지' in msg:
            # period
            for msg in recieved_msg:
                print(msg.body)
                if 'period_usage' in msg.body:
                    data = {'message': msg.body.split(':')[1] + '만큼 사용했습니다.'}
                    return data
        elif '어제' in msg or '그저께' in msg or '오늘' in msg:
            # today_usage
            for msg in recieved_msg:
                if 'today_usage' in msg.body:
                    data = {'message': msg.body.split(':')[1] + '만큼 사용되었습니다.'}
                    return data
        elif ('현재' in msg or '지금' in msg) and '소비전력' not in msg:
            # site_usage
            for msg in recieved_msg:
                if 'site_usage' in msg.body:
                    data = {'message': msg.body.split(':')[1] + '만큼 사용 중입니다.'}
                    return data
        elif '소비전력' in msg:
            # 소비전력
            for msg in recieved_msg:
                if '입니다' in msg.body:
                    data = {'message': msg.body}
                    return data
        elif '전기절약' in msg or '팁' in msg or '조언' in msg:
            # 팁
            for msg in recieved_msg:
                if '세요.' in msg.body:
                    data = {'message': msg.body}
                    return data
        elif '전기요금' in msg or '전기세' in msg or '전기 사용료' in msg or\
                        '전력 사용료' in msg or '전력사용료' in msg or '전기사용료' in msg:
            # 전기요금
            for msg in recieved_msg:
                if '입니다' in msg.body:
                    data = {'message': msg.body}
                    return data
