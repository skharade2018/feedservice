from flask import Flask
from flask_restful import Api
import django
django.setup()

from feedservices.service_apis.answer import Answer
from feedservices.service_apis.question import Question
from feedservices.service_apis.upvote import Upvote


app=Flask(__name__)

api = Api(app=app, prefix='/feedservice/')
api.add_resource(Question, 'question', 'question/<int:question_id>')
api.add_resource(Answer, 'answer', 'answer/<int:answer_id>')
api.add_resource(Upvote, 'upvote','upvote/<int:upvote_id>')


if __name__=="__main__":
    app.run(host='localhost',port=2005,debug=True)
