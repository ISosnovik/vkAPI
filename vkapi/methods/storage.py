# Storage methods
from ..api import call, parse_response


def get(key=None, keys=None, user_id=None, global_=None):
    """
    Returns a value of variable with the name set by key
    parameter.
    https://vk.com/dev/storage.get
    """
    params = {
        'key': key,
        'keys': keys,
        'user_id': user_id,
        'global_': global_
    }
    result = call('storage.get', **params)
    return parse_response(result)


def getKeys(user_id=None, global_=None, offset=None, count=None):
    """
    Returns the names of all variables.
    https://vk.com/dev/storage.getKeys
    """
    params = {
        'user_id': user_id,
        'global_': global_,
        'offset': offset,
        'count': count
    }
    result = call('storage.getKeys', **params)
    return parse_response(result)


def set(key=None, value=None, user_id=None, global_=None):
    """
    Saves a value of variable with the name set by 
    https://vk.com/dev/storage.set
    """
    params = {
        'key': key,
        'value': value,
        'user_id': user_id,
        'global_': global_
    }
    result = call('storage.set', **params)
    return parse_response(result)


