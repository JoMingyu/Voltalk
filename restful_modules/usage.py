# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
import json
import requests

from support import time_manager
from support import unit_conversion
from enertalk_infos import info


class SiteRealTime(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]

        response = requests.get(info.URL + 'sites/' + site_id + '/usages/realtime', headers=info.headers)
        json_obj = json.loads(response.text)
        print(json_obj)
        json_obj['activePower'] = unit_conversion.convert(json_obj['activePower'])
        return json_obj


class SitePeriod(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        start = time_manager.date_to_timestamp(request.args.get('start'))
        end = time_manager.date_to_timestamp(request.args.get('end'))

        params = {'start': start, 'end': end}
        response = requests.get(info.URL + 'sites/' + site_id + '/usages/periodic', headers=info.headers, params=params)
        json_obj = json.loads(response.text)
        json_obj['usage'] = unit_conversion.convert(json_obj['usage'])
        return json_obj


class SiteToday(Resource):
    def get(self):
        # 오늘 에너지 사용량 조회
        site_id = info.site_ids[request.args.get('where')]
        start = time_manager.date_to_timestamp(request.args.get('date'))
        end = time_manager.datetime_to_timestamp(time_manager.get_cur_datetime())

        params = {'start': start, 'end': end}
        response = requests.get(info.URL + 'sites/' + site_id + '/usages/periodic', headers=info.headers, params=params)
        json_obj = json.loads(response.text)
        print(json_obj)
        json_obj['usage'] = unit_conversion.convert(json_obj['usage'])
        return json_obj


class DeviceRealTime(Resource):
    def get(self):
        device = request.args.get('device')

        response = requests.get(info.URL + 'devices/' + device + '/usages/realtime', headers=info.headers)
        json_obj = json.loads(response.text)
        json_obj['activePower'] = unit_conversion.convert(json_obj['activePower'])
        return json_obj


class DevicePeriod(Resource):
    def get(self):
        device = request.args.get('device')
        start = time_manager.date_to_timestamp(request.args.get('start'))
        end = time_manager.date_to_timestamp(request.args.get('end'))

        params = {'start': start, 'end': end}
        response = requests.get(info.URL + 'devices/' + device + '/usages/periodic', headers=info.headers, params=params)
        json_obj = json.loads(response.text)
        json_obj['usage'] = unit_conversion.convert(json_obj['usage'])
        return json_obj


class DeviceToday(Resource):
    def get(self):
        device = request.args.get('device')
        start = time_manager.date_to_timestamp(request.args.get('date'))
        end = time_manager.datetime_to_timestamp(time_manager.get_cur_datetime())
        # today

        params = {'start': start, 'end': end}
        response = requests.get(info.URL + 'devices/' + device + '/usages/periodic', headers=info.headers, params=params)
        json_obj = json.loads(response.text)
        json_obj['usage'] = unit_conversion.convert(json_obj['usage'])
        return json_obj


class TagRealTime(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        tag_id = request.args.get('tag')

        response = requests.get(info.URL + 'sites/' + site_id + '/tags/' + tag_id + '/usages/realtime', headers=info.headers)
        json_obj = json.loads(response.text)
        json_obj['activePower'] = unit_conversion.convert(json_obj['activePower'])
        return json_obj


class TagPeriod(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        tag_id = request.args.get('tag')
        start = time_manager.date_to_timestamp(request.args.get('start'))
        end = time_manager.date_to_timestamp(request.args.get('end'))

        params = {'start': start, 'end': end}
        response = requests.get(info.URL + 'sites/' + site_id + '/tags/' + tag_id + '/usages/periodic', headers=info.headers, params=params)
        json_obj = json.loads(response.text)
        json_obj['usage'] = unit_conversion.convert(json_obj['usage'])
        return json_obj


class TagToday(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        tag_id = request.args.get('tag')
        start = time_manager.date_to_timestamp(request.args.get('date'))
        end = time_manager.datetime_to_timestamp(time_manager.get_cur_datetime())
        # today

        params = {'start': start, 'end': end}
        response = requests.get(info.URL + 'sites/' + site_id + '/tags/' + tag_id + '/usages/periodic', headers=info.headers, params=params)
        json_obj = json.loads(response.text)
        json_obj['usage'] = unit_conversion.convert(json_obj['usage'])
        return json_obj
