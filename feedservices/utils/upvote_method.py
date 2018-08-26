from feedservices.utils.answer_method import get_answer_dict

def get_upvote_dict(upvote_object):
    response = {"string":upvote_object.username,
                "answer":get_answer_dict(upvote_object.answer),
                "created_on":upvote_object.created_on.strftime("%d%m%y"),
                "is_active": upvote_object.is_active
                }
    return response