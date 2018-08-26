from flask_restful import Resource
from flask import request, json, jsonify
from feedservices.service_api_handler import question_post_handler, question_get_handler, question_put_handler
from feedservices.utils import question_methods
from feedservices.db.feed_models.models import Topic

class Question(Resource):
    def post(self):
        data=request.get_json()
        print data
        auth_token=request.cookies.get('authToken')
        question_object = question_post_handler.create_question(data)
        response = question_methods.get_question_dict(question_object)
        return jsonify({"question": response})


    def get(self, question_id=None):
        if question_id:
            question_object=question_get_handler.get_single_question(question_id)
            if question_object:
                response_dict=question_methods.get_question_dict(question_object)
                return jsonify({'questoin': response_dict})

        filters = request.args
        print filters
        question_object = question_get_handler.get_question_by_filter(filters)

        response_dict = [question_methods.get_question_dict(question) for question in question_object]

        return jsonify({"question": response_dict})


    def put(self, question_id):
        question_object=question_get_handler.get_single_question(question_id)
        if question_object:
            data = request.get_json()
            question_object=question_put_handler.update_question(question_object, data)
            response_dict = question_methods.get_question_dict(question_object)
            return jsonify({"question": response_dict})
        else:
            return jsonify({"message": "Question not found !"})
