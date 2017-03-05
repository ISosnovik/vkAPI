# Notifications methods
from ..api import call, parse_response


def get(count=None, start_from=None, filters=None, start_time=None, end_time=None,\
        from_=None, offset=None):
    """
    Returns a list of notifications about other users' feedback
    to the current user's wall posts.
    https://vk.com/dev/notifications.get
    """
    params = {
        'count': count,
        'start_from': start_from,
        'filters': filters,
        'start_time': start_time,
        'end_time': end_time,
        'from_': from_,
        'offset': offset
    }
    result = call('notifications.get', **params)
    return parse_response(result)


def markAsViewed():
    """
    Resets the counter of new notifications about other
    users' feedback to the current user's wall posts.
    https://vk.com/dev/notifications.markAsViewed
    """
    params = {
    }
    result = call('notifications.markAsViewed', **params)
    return parse_response(result)


