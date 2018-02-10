from flask import Flask
from flask_restful import Api

from user_service.service_apis.ping import Ping

app = Flask(__name__)

api = Api(app)

api.add_resource(Ping, '/ping')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
