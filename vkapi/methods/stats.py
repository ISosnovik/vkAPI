# Stats methods
from ..api import call, parse_response


def get(group_id=None, app_id=None, date_from=None, date_to=None):
    """
    Returns statistics of a community or an application.
    https://vk.com/dev/stats.get
    """
    params = {
        'group_id': group_id,
        'app_id': app_id,
        'date_from': date_from,
        'date_to': date_to
    }
    result = call('stats.get', **params)
    return parse_response(result)


def getPostReach(owner_id=None, post_id=None):
    """
    Returns stats for a wall post.
    https://vk.com/dev/stats.getPostReach
    """
    params = {
        'owner_id': owner_id,
        'post_id': post_id
    }
    result = call('stats.getPostReach', **params)
    return parse_response(result)


def trackVisitor():
    """
    
    https://vk.com/dev/stats.trackVisitor
    """
    params = {
    }
    result = call('stats.trackVisitor', **params)
    return parse_response(result)


