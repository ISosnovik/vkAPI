# Likes methods
from ..api import call, parse_response


def add(type=None, owner_id=None, item_id=None, access_key=None):
    """
    Adds the specified object tothe 
    https://vk.com/dev/likes.add
    """
    params = {
        'type': type,
        'owner_id': owner_id,
        'item_id': item_id,
        'access_key': access_key
    }
    result = call('likes.add', **params)
    return parse_response(result)


def delete(type=None, owner_id=None, item_id=None):
    """
    Deletes the specified object from the 
    https://vk.com/dev/likes.delete
    """
    params = {
        'type': type,
        'owner_id': owner_id,
        'item_id': item_id
    }
    result = call('likes.delete', **params)
    return parse_response(result)


def getList(type=None, owner_id=None, item_id=None, page_url=None, filter=None,\
            friends_only=None, extended=None, offset=None, count=None, skip_own=None):
    """
    Returns a list of IDs of users who added the specified
    object to their
    https://vk.com/dev/likes.getList
    """
    params = {
        'type': type,
        'owner_id': owner_id,
        'item_id': item_id,
        'page_url': page_url,
        'filter': filter,
        'friends_only': friends_only,
        'extended': extended,
        'offset': offset,
        'count': count,
        'skip_own': skip_own
    }
    result = call('likes.getList', **params)
    return parse_response(result)


def isLiked(user_id=None, type=None, owner_id=None, item_id=None):
    """
    Checks for the object in the 
    https://vk.com/dev/likes.isLiked
    """
    params = {
        'user_id': user_id,
        'type': type,
        'owner_id': owner_id,
        'item_id': item_id
    }
    result = call('likes.isLiked', **params)
    return parse_response(result)


