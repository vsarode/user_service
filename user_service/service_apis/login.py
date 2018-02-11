from flask import request, jsonify
from flask_restful import Resource

from user_service.service_api_handlers import login_post_handler
from user_service.utils.login_entry_methods import get_dict_for_login_object


class Login(Resource):
    def post(self):
        request_data = request.get_json()
        login_entry_object = login_post_handler.create_login_entry(request_data)
        if login_entry_object:
            return jsonify(get_dict_for_login_object(login_entry_object))
        else:
            return {"success": False}
