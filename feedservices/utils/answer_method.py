


def get_answer_dict(answer_object):
    response = {"string":answer_object.string,
                "username":answer_object.username,
                "id" : answer_object.id,
                "question_id" :answer_object.question_id,
                "created_on":answer_object.created_on.strftime("%d%m%Y")
             }
    return response