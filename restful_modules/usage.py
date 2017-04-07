# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
import json

import requests
from support import time_manager
from enertalk_infos import info


class SiteRealTime(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]

        response = requests.get(info.URL + 'sites/' + site_id + '/usages/realtime', headers=info.headers)
        return json.loads(response.text)


class SitePeriod(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        start = time_manager.datetime_to_timestamp(request.args.get('start'))
        end = time_manager.datetime_to_timestamp(request.args.get('end'))

        params = {'start': start, 'end': end}
        response = requests.get(info.URL + 'sites/' + site_id + '/usages/periodic', headers=info.headers, params=params)
        return json.loads(response.text)


class DeviceRealTime(Resource):
    def get(self):
        device = request.args.get('device')

        response = requests.get(info.URL + 'devices/' + device + '/usages/realtime', headers=info.headers)
        return json.loads(response.text)


class DevicePeriod(Resource):
    def get(self):
        device = request.args.get('device')
        start = time_manager.datetime_to_timestamp(request.args.get('start'))
        end = time_manager.datetime_to_timestamp(request.args.get('end'))

        params = {'start': start, 'end': end}
        response = requests.get(info.URL + 'devices/' + device + '/usages/periodic', headers=info.headers, params=params)
        return json.loads(response.text)


class TagRealTime(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        tag_id = request.args.get('tag')

        response = requests.get(info.URL + 'sites/' + site_id + '/tags/' + tag_id + '/usages/realtime', headers=info.headers)
        return json.loads(response.text)


class TagPeriod(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        tag_id = request.args.get('tag')
        start = time_manager.datetime_to_timestamp(request.args.get('start'))
        end = time_manager.datetime_to_timestamp(request.args.get('end'))

        params = {'start': start, 'end': end}
        response = requests.get(info.URL + 'sites/' + site_id + '/tags/' + tag_id + '/usages/periodic', headers=info.headers, params=params)
        return json.loads(response.text)
