from feedservices.db.feed_models.models import Question, Answer


def create_answer(data):
    try:
        string = data['string']
        question_id = data['questionId']
        username = data['username']
    except Exception as e:
        print e
        raise e
    try:
        question_object=Question.objects.get(id=question_id)
    except Exception as e:
        print e
        raise e

    answer_objects=Answer.objects.create(string = string,
                                          question=question_object,
                                          username=username)

    return answer_objects