from flask_restful import Resource
from flask import request

import requests
from enertalk_infos import info


class SiteRealTime(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]

        response = requests.get(info.URL + 'sites/' + site_id + 'usages/realtime')
        return response.text


class SitePeriod(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        start = request.args.get('start')
        end = request.args.get('end')

        
        pass


class TagRealTime(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]

        pass


class TagPeriod(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]
        start = request.args.get('start')
        end = request.args.get('end')


        pass

# class DeviceRealTime(Resource):
#     def get(self):
#         site_id = info.site_ids[request.args.get('where')]
#         device = request.args.get('device')
#
#         response = request.get(info.URL + 'sites/' + site_id + 'usages/realtime')
#         pass
#
#
# class DevicePeriod(Resource):
#     def get(self):
#         site_id = info.site_ids[request.args.get('where')]
#         device = request.args.get('device')
#
#         pass
