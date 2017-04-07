# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource


class Test(Resource):
    def get(self):
        print(request.args.get('test'))
        return '', 200
