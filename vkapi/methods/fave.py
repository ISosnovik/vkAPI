# Fave methods
from ..api import call, parse_response


def addGroup(group_id=None):
    """
    Adds a community to user faves.
    https://vk.com/dev/fave.addGroup
    """
    params = {
        'group_id': group_id
    }
    result = call('fave.addGroup', **params)
    return parse_response(result)


def addLink(link=None, text=None):
    """
    Adds a link to user faves.
    https://vk.com/dev/fave.addLink
    """
    params = {
        'link': link,
        'text': text
    }
    result = call('fave.addLink', **params)
    return parse_response(result)


def addUser(user_id=None):
    """
    Adds a profile to user faves.
    https://vk.com/dev/fave.addUser
    """
    params = {
        'user_id': user_id
    }
    result = call('fave.addUser', **params)
    return parse_response(result)


def getLinks(offset=None, count=None):
    """
    Returns a list of links that the current user has bookmarked.
    https://vk.com/dev/fave.getLinks
    """
    params = {
        'offset': offset,
        'count': count
    }
    result = call('fave.getLinks', **params)
    return parse_response(result)


def getMarketItems(count=None, offset=None, extended=None):
    """
    Returns market items bookmarked by current user.
    https://vk.com/dev/fave.getMarketItems
    """
    params = {
        'count': count,
        'offset': offset,
        'extended': extended
    }
    result = call('fave.getMarketItems', **params)
    return parse_response(result)


def getPhotos(offset=None, count=None, photo_sizes=None):
    """
    Returns a list of photos that the current user has liked.
    https://vk.com/dev/fave.getPhotos
    """
    params = {
        'offset': offset,
        'count': count,
        'photo_sizes': photo_sizes
    }
    result = call('fave.getPhotos', **params)
    return parse_response(result)


def getPosts(offset=None, count=None, extended=None):
    """
    Returns a list of wall posts that the current user has
    liked.
    https://vk.com/dev/fave.getPosts
    """
    params = {
        'offset': offset,
        'count': count,
        'extended': extended
    }
    result = call('fave.getPosts', **params)
    return parse_response(result)


def getUsers(offset=None, count=None):
    """
    Returns a list of users whom the current user has bookmarked.
    https://vk.com/dev/fave.getUsers
    """
    params = {
        'offset': offset,
        'count': count
    }
    result = call('fave.getUsers', **params)
    return parse_response(result)


def getVideos(offset=None, count=None, extended=None):
    """
    Returns a list of videos that the current user has liked.
    https://vk.com/dev/fave.getVideos
    """
    params = {
        'offset': offset,
        'count': count,
        'extended': extended
    }
    result = call('fave.getVideos', **params)
    return parse_response(result)


def removeGroup(group_id=None):
    """
    Removes a community from user faves.
    https://vk.com/dev/fave.removeGroup
    """
    params = {
        'group_id': group_id
    }
    result = call('fave.removeGroup', **params)
    return parse_response(result)


def removeLink(link_id=None):
    """
    Removes link from the user's faves.
    https://vk.com/dev/fave.removeLink
    """
    params = {
        'link_id': link_id
    }
    result = call('fave.removeLink', **params)
    return parse_response(result)


def removeUser(user_id=None):
    """
    Removes a profile from user faves.
    https://vk.com/dev/fave.removeUser
    """
    params = {
        'user_id': user_id
    }
    result = call('fave.removeUser', **params)
    return parse_response(result)


