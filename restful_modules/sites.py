from flask_restful import Resource
import requests


class Sites(Resource):
    URL = 'http://api2.enertalk.com/sites'

    def get(self):
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer 7c1cbc4c116f033c41d1e47b2caa0f957e9d1a3f89d2c7caefadb6a1017998ff2626b0ad986f72c6ac16be64386ffd3863a8a181754c16060d923ec92cb5f290'}
        response = requests.get(self.URL, headers=headers)

        return response.text
