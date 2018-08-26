from feedservices.db.feed_models.models import Answer, Upvote


def get_single_upvote(upvote_id):
    try:
        upvote_object = Upvote.objects.get(id=upvote_id)
        return upvote_object
    except Exception as e:
        print e

def get_upvotes_by_filter(filters):
    pass