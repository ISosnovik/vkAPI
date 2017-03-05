# Search methods
from ..api import call, parse_response


def getHints(q=None, limit=None, filters=None, search_global=None):
    """
    Allows the programmer to do a quick search for any substring.
    https://vk.com/dev/search.getHints
    """
    params = {
        'q': q,
        'limit': limit,
        'filters': filters,
        'search_global': search_global
    }
    result = call('search.getHints', **params)
    return parse_response(result)


