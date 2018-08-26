from feedservices.utils.topic_methods import get_topic_dict


def get_question_dict(question_object):
    response = {"string" : question_object.string,
                "id":question_object.id,
                "username":question_object.username,
                "topic":get_topic_dict(question_object.topic),
                "createOn":question_object.created_on.strftime('%d%m%Y'),
                "vies":question_object.views
                }
    return response