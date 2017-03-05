# Apps methods
from ..api import call, parse_response


def deleteAppRequests():
    """
    Deletes all request notifications from the current app.
    https://vk.com/dev/apps.deleteAppRequests
    """
    params = {
    }
    result = call('apps.deleteAppRequests', **params)
    return parse_response(result)


def get(app_id=None, app_ids=None, platform=None, extended=None, return_friends=None,\
        fields=None, name_case=None):
    """
    Returns applications data.
    https://vk.com/dev/apps.get
    """
    params = {
        'app_id': app_id,
        'app_ids': app_ids,
        'platform': platform,
        'extended': extended,
        'return_friends': return_friends,
        'fields': fields,
        'name_case': name_case
    }
    result = call('apps.get', **params)
    return parse_response(result)


def getCatalog(sort=None, offset=None, count=None, platform=None, extended=None,\
               return_friends=None, fields=None, name_case=None, q=None,\
               genre_id=None, filter=None):
    """
    Returns a list of applications (apps) available to users
    in the App Catalog.
    https://vk.com/dev/apps.getCatalog
    """
    params = {
        'sort': sort,
        'offset': offset,
        'count': count,
        'platform': platform,
        'extended': extended,
        'return_friends': return_friends,
        'fields': fields,
        'name_case': name_case,
        'q': q,
        'genre_id': genre_id,
        'filter': filter
    }
    result = call('apps.getCatalog', **params)
    return parse_response(result)


def getFriendsList(extended=None, count=None, offset=None, type=None, fields=None):
    """
    Creates friends list for requests and invites in current
    app.
    https://vk.com/dev/apps.getFriendsList
    """
    params = {
        'extended': extended,
        'count': count,
        'offset': offset,
        'type': type,
        'fields': fields
    }
    result = call('apps.getFriendsList', **params)
    return parse_response(result)


def getLeaderboard(type=None, global_=None, extended=None):
    """
    Returns players rating in the game.
    https://vk.com/dev/apps.getLeaderboard
    """
    params = {
        'type': type,
        'global_': global_,
        'extended': extended
    }
    result = call('apps.getLeaderboard', **params)
    return parse_response(result)


def getScore(user_id=None):
    """
    Returns user score in app
    https://vk.com/dev/apps.getScore
    """
    params = {
        'user_id': user_id
    }
    result = call('apps.getScore', **params)
    return parse_response(result)


def sendRequest(user_id=None, text=None, type=None, name=None, key=None,\
                separate=None):
    """
    Sends a request to another user in an app that uses
    VK authorization.
    https://vk.com/dev/apps.sendRequest
    """
    params = {
        'user_id': user_id,
        'text': text,
        'type': type,
        'name': name,
        'key': key,
        'separate': separate
    }
    result = call('apps.sendRequest', **params)
    return parse_response(result)


