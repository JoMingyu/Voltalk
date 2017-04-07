# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
import json
import requests

from enertalk_infos import info


class Tags(Resource):
    def get(self):
        site_id = info.site_ids[request.args.get('where')]

        response = requests.get(info.URL + 'sites/' + site_id + '/tags', headers=info.headers)
        return json.loads(response.text)
