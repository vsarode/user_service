from flask import request
from flask_restful import Resource

from user_service.service_api_handlers import user_post_handler


class UserHandler(Resource):
    def post(self):
        request_data = request.get_json()
        result = user_post_handler.create_user(request_data)
        if result:
            return {"success": "User successfully created !!!"}
        else:
            return {"success": False}

    def get(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass
