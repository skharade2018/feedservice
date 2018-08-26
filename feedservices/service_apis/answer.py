from flask_restful import Resource
from flask import request, jsonify, json

from feedservices.service_api_handler import answer_post_handler, answer_get_handler
from feedservices.utils import answer_method


class Answer(Resource):
    def post(self):
        data = request.get_json()
        print data
        answer_object= answer_post_handler.create_answer(data)
        response = answer_method.get_answer_dict(answer_object)

        return jsonify({"answer": response})

    def get(self, answer_id):
        if answer_id:
            answer_object = answer_get_handler.get_single_answer(answer_id)
            if answer_object:
                response_dict = answer_method.get_answer_dict(answer_object)
                return jsonify({"answer": response_dict})
