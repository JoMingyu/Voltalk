# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
import random

from support import tips


class Consumptions(Resource):
    def get(self):
        # 소비전력
        data = {'result': tips.consumptions[request.args.get('target')]}

        return data


class Tips(Resource):
    def get(self):
        # 팁
        data = {'result': random.choice(tips.tips)}

        return data
