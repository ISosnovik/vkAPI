# Utils methods
from ..api import call, parse_response


def checkLink(url=None):
    """
    Checks whether a link is blocked in VK.
    https://vk.com/dev/utils.checkLink
    """
    params = {
        'url': url
    }
    result = call('utils.checkLink', **params)
    return parse_response(result)


def getServerTime():
    """
    Returns the current time of the VK server.
    https://vk.com/dev/utils.getServerTime
    """
    params = {
    }
    result = call('utils.getServerTime', **params)
    return parse_response(result)


def resolveScreenName(screen_name=None):
    """
    Detects a type of object (e.g., user, community, application)
    and its ID by screen name.
    https://vk.com/dev/utils.resolveScreenName
    """
    params = {
        'screen_name': screen_name
    }
    result = call('utils.resolveScreenName', **params)
    return parse_response(result)


