from twisted.trial.reporter import _AnsiColorizer

from flask_restful import Resource
from flask import json, request, jsonify

from feedservices.service_api_handler import upvote_post_handler, upvote_get_handler
from feedservices.utils import upvote_method


class Upvote(Resource):
    def post(self):
        data = request.get_json()

        upvote_object = upvote_post_handler.create_upvote(data)
        response = upvote_method.get_upvote_dict(upvote_object)

        return jsonify({"upvot":response})


    def get(self, upvote_id=None):
        if upvote_id:
            answer_object= upvote_get_handler.get_single_upvote(upvote_id)

            if answer_object:
                response_dict = upvote_method.get_upvote_dict(answer_object)
                return jsonify({"upvote":response_dict})
        filters = request.args


