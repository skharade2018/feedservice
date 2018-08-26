from feedservices.db.feed_models.models import Answer


def get_single_answer(answer_id):
    try:
        answer_object = Answer.objects.get(id=answer_id)
        return answer_object
    except Exception as e:
        print e
        return None



