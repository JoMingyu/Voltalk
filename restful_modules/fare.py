# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
import json

import requests
import datetime
from support import time_manager
from enertalk_infos import info


class SiteCurrent(Resource):
    def get(self):
        # 이번 달 1일부터 현재까지 site의 전기 사용량 조회
        site_id = info.site_ids[request.args.get('where')]
        first_date_of_month = time_manager.date_to_timestamp(datetime.datetime.now().strftime('%Y-%m-' + '01'))
        # 이번 달 1일의 날짜
        
        now = time_manager.datetime_to_timestamp(time_manager.get_cur_datetime())
        # 현재 timestamp

        params = {'start': first_date_of_month, 'end': now}
        response = requests.get(info.URL + 'sites/' + site_id + '/usages/billing', headers=info.headers, params=params)
        json_obj = json.loads(response.text)
        data = {'charge': json_obj['bill']['charge']}
        return data


class DeviceCurrent(Resource):
    def get(self):
        # 이번 달 1일부터 현재까지 device의 전기 사용량 조회
        device = request.args.get('device')
        first_date_of_month = time_manager.date_to_timestamp(datetime.datetime.now().strftime('%Y-%m-' + '01'))
        # 이번 달 1일의 날짜

        now = time_manager.datetime_to_timestamp(time_manager.get_cur_datetime())
        # 현재 timestamp

        params = {'start': first_date_of_month, 'end': now}
        response = requests.get(info.URL + 'devices/' + device + '/usages/billing', headers=info.headers, params=params)
        json_obj = json.loads(response.text)
        data = {'charge': json_obj['bill']['charge']}
        return data


class Forecast(Resource):
    pass
