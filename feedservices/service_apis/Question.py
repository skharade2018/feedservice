from flask_restful import Resource
from flask import request

class Question(Resource):
    def get(self):
        data=request.args
    def post(self):
        pass
    def put(self):
        pass

