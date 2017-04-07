from flask_restful import Resource
from flask import request

import requests
from enertalk_infos import info


class Site(Resource):
    def get(self):
        where = request.args.get('where')

        return '', 200


class Device(Resource):
    def get(self):
        pass