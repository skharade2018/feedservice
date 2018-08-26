from feedservices.db.feed_models.models import Answer, Upvote


def create_upvote(data):
    try:
        username = data['username']
        answer_id = data['answerId']
    except Exception as e:
        print e
        raise e

    try:
        answer_object = Answer.objects.get(id=answer_id)
    except Exception as e:
        print e
        raise e

    upvote_object= Upvote.objects.create(username=username,
                                          answer=answer_object)

    return upvote_object
