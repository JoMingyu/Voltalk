# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
import json

import requests
from enertalk_infos import info


class Devices(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]

        response = requests.get(info.URL + 'sites/' + site_id + '/devices', headers=info.headers)
        return json.loads(response.text)
