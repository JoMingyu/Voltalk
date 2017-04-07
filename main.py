# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api

from restful_modules import sites
# site : 가장 큰 개념, 건물 단위

from restful_modules import devices
# device : 하나의 에너톡 디바이스

from restful_modules import tags
# tag : 디바이스에 등록되는 하나의 기기

from restful_modules import usage

from restful_modules import fare

from support import observer

app = Flask(__name__)
api = Api(app)

api.add_resource(sites.Sites, '/sites')
api.add_resource(devices.Devices, '/devices')
api.add_resource(tags.Tags, '/tags')
# 1분마다 전기 사용량 체크, 이상하면 메시지

api.add_resource(usage.SiteRealTime, '/usage/site')
api.add_resource(usage.SitePeriod, '/usage/site/period')
api.add_resource(usage.SiteToday, '/usage/site/today')

api.add_resource(usage.DeviceRealTime, '/usage/device')
api.add_resource(usage.DevicePeriod, '/usage/device/period')
api.add_resource(usage.DeviceToday, '/usage/device/today')

api.add_resource(usage.TagRealTime, '/usage/tag')
api.add_resource(usage.TagPeriod, '/usage/tag/period')
api.add_resource(usage.TagToday, '/usage/site/today')

api.add_resource(fare.SiteCurrent, '/fare/site')
api.add_resource(fare.DeviceCurrent, '/fare/device')

if __name__ == "__main__":
    print('-- Server Started -- ')
    observer.Observer().start()
    app.run(host='192.168.0.33', port=80)
