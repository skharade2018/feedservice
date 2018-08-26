from feedservices.db.feed_models.models import Question


def get_single_question(question_id):
    try:
        question_object=Question.objects.get(id=question_id)
        return question_object
    except Exception as e:
        print e
        return None


def get_question_by_filter(filters):
    criteria={}  #####Need more practice here
    if 'topicId' in filters:
        criteria['topic_id__in']=filters.getlist('topicId')

    question_objects = Question.objects.filter(**criteria)
    return question_objects

