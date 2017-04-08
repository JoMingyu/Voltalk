from flask_restful import Resource
from flask import request


class Topic(Resource):
    def post(self):
        topic = request.form['topic']
        return '', 200