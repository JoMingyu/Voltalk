from flask_restful import Resource
from flask import request

import requests
from support import time_manager
from enertalk_infos import info


class SiteRealTime(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]

        response = requests.get(info.URL + 'sites/' + site_id + '/usages/realtime', headers=info.headers)
        return response.text


class SitePeriod(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        start = time_manager.datetime_to_timestamp(request.args.get('start'))
        end = time_manager.datetime_to_timestamp(request.args.get('end'))


        pass


class DeviceRealTime(Resource):
    def get(self):
        device = request.args.get('device')

        response = requests.get(info.URL + 'devices/' + device + '/usages/realtime', headers=info.headers)
        return response.text


class DevicePeriod(Resource):
    def get(self):
        device = request.args.get('device')
        start = request.args.get('start')
        end = request.args.get('end')

        pass


class TagRealTime(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        tag_id = request.args.get('tag')

        response = requests.get(info.URL + 'sites/' + site_id + '/tags/' + tag_id + '/usages/realtime', headers=info.headers)
        pass


class TagPeriod(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        tag_id = request.args.get('tag')
        start = request.args.get('start')
        end = request.args.get('end')

        pass