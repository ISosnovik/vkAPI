# Status methods
from ..api import call, parse_response


def get(user_id=None, group_id=None):
    """
    Returns data required to show the status of a user or
    community.
    https://vk.com/dev/status.get
    """
    params = {
        'user_id': user_id,
        'group_id': group_id
    }
    result = call('status.get', **params)
    return parse_response(result)


def set(text=None, group_id=None):
    """
    Sets a new status for the current user.
    https://vk.com/dev/status.set
    """
    params = {
        'text': text,
        'group_id': group_id
    }
    result = call('status.set', **params)
    return parse_response(result)


