# Gifts methods
from ..api import call, parse_response


def get(user_id=None, count=None, offset=None):
    """
    Returns a list of user gifts.
    https://vk.com/dev/gifts.get
    """
    params = {
        'user_id': user_id,
        'count': count,
        'offset': offset
    }
    result = call('gifts.get', **params)
    return parse_response(result)


