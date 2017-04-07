from flask_restful import Resource
import json

import requests
from enertalk_infos import info


class Sites(Resource):
    def get(self):
        response = requests.get(info.URL + 'sites', headers=info.headers)
        return json.loads(response.text)
