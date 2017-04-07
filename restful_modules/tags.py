from flask_restful import Resource
from flask import request

import requests
from enertalk_infos import info


class Tags(Resource):
    where = request.args.get('where')