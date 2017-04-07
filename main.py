from flask import Flask
from flask_restful import Api

from restful_modules import sites

app = Flask(__name__)
api = Api(app)

tmp = sites.Sites()
tmp.get()

api.add_resource(sites.Sites, '/sites')

# if __name__ == "__main__":
#     print('-- Server Started -- ')
#     app.run(host='192.168.0.33', port=80)
