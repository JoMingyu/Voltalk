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
        site_id = info.site_ids[request.args.get('where')]
        cur_month_str = time_manager.date_to_timestamp(datetime.datetime.now().strftime('%Y-%m-' + '01'))
        now = time_manager.datetime_to_timestamp(time_manager.get_cur_datetime())

        params = {'start': cur_month_str, 'end': now}
        response = requests.get(info.URL + 'sites/' + site_id + '/usages/billing', headers=info.headers, params=params)
        return json.loads(response.text)


class DeviceCurrent(Resource):
    def get(self):
        device = request.args.get('device')
        cur_month_str = time_manager.date_to_timestamp(datetime.datetime.now().strftime('%Y-%m-' + '01'))
        now = time_manager.datetime_to_timestamp(time_manager.get_cur_datetime())

        params = {'start': cur_month_str, 'end': now}
        response = requests.get(info.URL + 'devices/' + device + '/usages/billing', headers=info.headers, params=params)
        return json.loads(response.text)


class Forecast(Resource):
    pass
