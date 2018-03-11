import django
from flask import Flask
from flask_restful import Api

from user_service.service_apis.validate import Validate

django.setup()
from user_service.service_apis.ping import Ping
from user_service.service_apis.user import UserHandler
from user_service.service_apis.login import Login

app = Flask(__name__)

api = Api(app)

api.add_resource(Ping, '/ping')
api.add_resource(UserHandler, '/user', '/user/<string:username>')
api.add_resource(Login, '/login')
api.add_resource(Validate, '/validate')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
