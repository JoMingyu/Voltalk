from flask import Flask
from flask_restful import Api

from restful_modules import sites
# site : 가장 큰 개념, 건물 단위

from restful_modules import tags
# tag : 하나의 디바이스

from restful_modules import usage

app = Flask(__name__)
api = Api(app)

# tmp = sites.Sites()
# tmp.get()

api.add_resource(sites.Sites, '/sites')
api.add_resource()
api.add_resource((usage.Usage, '/chat/usage'))

# if __name__ == "__main__":
#     print('-- Server Started -- ')
#     app.run(host='192.168.0.33', port=80)
