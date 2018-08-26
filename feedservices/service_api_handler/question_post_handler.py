from feedservices.db.feed_models.models import Question, Topic

def create_question(data):
    try:
        string = data['string']
        topic_id = data['topicId']
        user_name=data['username']
    except Exception as e:
        print e
        raise e
    try:
        topic_object = Topic.objects.get(topic_id=topic_id)
    except Exception as e:
        raise e

    question_object = Question.objects.create(string=string,
                                              topic=topic_object,
                                              username=user_name)

    return question_object