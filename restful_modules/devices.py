from flask_restful import Resource
from flask import request

import requests
from enertalk_infos import info


class Devices(Resource):
    def get(self):
        where = request.args.get('where')
        site_id = info.ids[where]

        response = requests.get(info.URL + 'sites/' + site_id + '/devices', headers=info.headers)
        return response.text
