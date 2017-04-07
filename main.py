from flask import Flask
from flask_restful import Api

from restful_modules import sites
# site : 가장 큰 개념, 건물 단위

from restful_modules import devices
# tag : 하나의 디바이스

from restful_modules import usage

app = Flask(__name__)
api = Api(app)

api.add_resource(sites.Sites, '/sites')
api.add_resource(devices.Devices, '/devices')
# 1분마다 전기 사용량 체크, 이상하면 메시지

api.add_resource(usage.Site, '/usage/site')
api.add_resource(usage.Device, '/usage/device')

if __name__ == "__main__":
    print('-- Server Started -- ')
    app.run(host='192.168.0.33', port=80)
