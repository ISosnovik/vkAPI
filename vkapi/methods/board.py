# Board methods
from ..api import call, parse_response


def addTopic(group_id=None, title=None, text=None, from_group=None, attachments=None):
    """
    Creates a new topic on a community's discussion board.
    https://vk.com/dev/board.addTopic
    """
    params = {
        'group_id': group_id,
        'title': title,
        'text': text,
        'from_group': from_group,
        'attachments': attachments
    }
    result = call('board.addTopic', **params)
    return parse_response(result)


def closeTopic(group_id=None, topic_id=None):
    """
    Closes a topic on a community's discussion board so
    that comments cannot be posted.
    https://vk.com/dev/board.closeTopic
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id
    }
    result = call('board.closeTopic', **params)
    return parse_response(result)


def createComment(group_id=None, topic_id=None, message=None, attachments=None,\
                  from_group=None, sticker_id=None, guid=None):
    """
    Adds a comment on a topic on a community's discussion
    board.
    https://vk.com/dev/board.createComment
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id,
        'message': message,
        'attachments': attachments,
        'from_group': from_group,
        'sticker_id': sticker_id,
        'guid': guid
    }
    result = call('board.createComment', **params)
    return parse_response(result)


def deleteComment(group_id=None, topic_id=None, comment_id=None):
    """
    Deletes a comment on a topic on a community's discussion
    board.
    https://vk.com/dev/board.deleteComment
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id,
        'comment_id': comment_id
    }
    result = call('board.deleteComment', **params)
    return parse_response(result)


def deleteTopic(group_id=None, topic_id=None):
    """
    Deletes a topic from a community's discussion board.
    https://vk.com/dev/board.deleteTopic
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id
    }
    result = call('board.deleteTopic', **params)
    return parse_response(result)


def editComment(group_id=None, topic_id=None, comment_id=None, message=None,\
                attachments=None):
    """
    Edits a comment on a topic on a community's discussion
    board.
    https://vk.com/dev/board.editComment
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id,
        'comment_id': comment_id,
        'message': message,
        'attachments': attachments
    }
    result = call('board.editComment', **params)
    return parse_response(result)


def editTopic(group_id=None, topic_id=None, title=None):
    """
    Edits the title of a topic on a community's discussion
    board.
    https://vk.com/dev/board.editTopic
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id,
        'title': title
    }
    result = call('board.editTopic', **params)
    return parse_response(result)


def fixTopic(group_id=None, topic_id=None):
    """
    Pins a topic (fixes its place) to the top of a community's
    discussion board.
    https://vk.com/dev/board.fixTopic
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id
    }
    result = call('board.fixTopic', **params)
    return parse_response(result)


def getComments(group_id=None, topic_id=None, need_likes=None, start_comment_id=None,\
                offset=None, count=None, extended=None, sort=None):
    """
    Returns a list of comments on a topic on a community's
    discussion board.
    https://vk.com/dev/board.getComments
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id,
        'need_likes': need_likes,
        'start_comment_id': start_comment_id,
        'offset': offset,
        'count': count,
        'extended': extended,
        'sort': sort
    }
    result = call('board.getComments', **params)
    return parse_response(result)


def getTopics(group_id=None, topic_ids=None, order=None, offset=None, count=None,\
              extended=None, preview=None, preview_length=None):
    """
    Returns a list of topics on a community's discussion
    board.
    https://vk.com/dev/board.getTopics
    """
    params = {
        'group_id': group_id,
        'topic_ids': topic_ids,
        'order': order,
        'offset': offset,
        'count': count,
        'extended': extended,
        'preview': preview,
        'preview_length': preview_length
    }
    result = call('board.getTopics', **params)
    return parse_response(result)


def openTopic(group_id=None, topic_id=None):
    """
    Re-opens a previously closed topic on a community's
    discussion board.
    https://vk.com/dev/board.openTopic
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id
    }
    result = call('board.openTopic', **params)
    return parse_response(result)


def restoreComment(group_id=None, topic_id=None, comment_id=None):
    """
    Restores a comment deleted from a topic on a community's
    discussion board.
    https://vk.com/dev/board.restoreComment
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id,
        'comment_id': comment_id
    }
    result = call('board.restoreComment', **params)
    return parse_response(result)


def unfixTopic(group_id=None, topic_id=None):
    """
    Unpins a pinned topic from the top of a community's
    discussion board.
    https://vk.com/dev/board.unfixTopic
    """
    params = {
        'group_id': group_id,
        'topic_id': topic_id
    }
    result = call('board.unfixTopic', **params)
    return parse_response(result)


