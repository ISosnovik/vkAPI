# Newsfeed methods
from ..api import call, parse_response


def addBan(user_ids=None, group_ids=None):
    """
    Prevents news from specified users and communities from
    appearing in the current user's newsfeed.
    https://vk.com/dev/newsfeed.addBan
    """
    params = {
        'user_ids': user_ids,
        'group_ids': group_ids
    }
    result = call('newsfeed.addBan', **params)
    return parse_response(result)


def deleteBan(user_ids=None, group_ids=None):
    """
    Allows news from previously banned users and communities
    to be shown in the current user's newsfeed.
    https://vk.com/dev/newsfeed.deleteBan
    """
    params = {
        'user_ids': user_ids,
        'group_ids': group_ids
    }
    result = call('newsfeed.deleteBan', **params)
    return parse_response(result)


def deleteList(list_id=None):
    """
    
    https://vk.com/dev/newsfeed.deleteList
    """
    params = {
        'list_id': list_id
    }
    result = call('newsfeed.deleteList', **params)
    return parse_response(result)


def get(filters=None, return_banned=None, start_time=None, end_time=None,\
        max_photos=None, source_ids=None, start_from=None, count=None, fields=None,\
        from_=None, offset=None):
    """
    Returns data required to show newsfeed for the current
    user.
    https://vk.com/dev/newsfeed.get
    """
    params = {
        'filters': filters,
        'return_banned': return_banned,
        'start_time': start_time,
        'end_time': end_time,
        'max_photos': max_photos,
        'source_ids': source_ids,
        'start_from': start_from,
        'count': count,
        'fields': fields,
        'from_': from_,
        'offset': offset
    }
    result = call('newsfeed.get', **params)
    return parse_response(result)


def getBanned(extended=None, fields=None, name_case=None):
    """
    Returns a list of users and communities banned from
    the current user's newsfeed.
    https://vk.com/dev/newsfeed.getBanned
    """
    params = {
        'extended': extended,
        'fields': fields,
        'name_case': name_case
    }
    result = call('newsfeed.getBanned', **params)
    return parse_response(result)


def getComments(count=None, filters=None, reposts=None, start_time=None,\
                end_time=None, last_comments_count=None, start_from=None,\
                fields=None, from_=None, last_comments=None):
    """
    TODO
    https://vk.com/dev/newsfeed.getComments
    """
    params = {
        'count': count,
        'filters': filters,
        'reposts': reposts,
        'start_time': start_time,
        'end_time': end_time,
        'last_comments_count': last_comments_count,
        'start_from': start_from,
        'fields': fields,
        'from_': from_,
        'last_comments': last_comments
    }
    result = call('newsfeed.getComments', **params)
    return parse_response(result)


def getLists(list_ids=None, extended=None):
    """
    Returns a list of newsfeeds followed by the current
    user.
    https://vk.com/dev/newsfeed.getLists
    """
    params = {
        'list_ids': list_ids,
        'extended': extended
    }
    result = call('newsfeed.getLists', **params)
    return parse_response(result)


def getMentions(owner_id=None, start_time=None, end_time=None, offset=None,\
                count=None):
    """
    Returns a list of posts on user walls in which the current
    user is mentioned. 
    https://vk.com/dev/newsfeed.getMentions
    """
    params = {
        'owner_id': owner_id,
        'start_time': start_time,
        'end_time': end_time,
        'offset': offset,
        'count': count
    }
    result = call('newsfeed.getMentions', **params)
    return parse_response(result)


def getRecommended(start_time=None, end_time=None, max_photos=None, start_from=None,\
                   count=None, fields=None, from_=None, offset=None):
    """
    TODO
    https://vk.com/dev/newsfeed.getRecommended
    """
    params = {
        'start_time': start_time,
        'end_time': end_time,
        'max_photos': max_photos,
        'start_from': start_from,
        'count': count,
        'fields': fields,
        'from_': from_,
        'offset': offset
    }
    result = call('newsfeed.getRecommended', **params)
    return parse_response(result)


def getSuggestedSources(offset=None, count=None, shuffle=None, fields=None):
    """
    Returns communities and users that current user is suggested
    to follow.
    https://vk.com/dev/newsfeed.getSuggestedSources
    """
    params = {
        'offset': offset,
        'count': count,
        'shuffle': shuffle,
        'fields': fields
    }
    result = call('newsfeed.getSuggestedSources', **params)
    return parse_response(result)


def ignoreItem(type=None, owner_id=None, item_id=None):
    """
    Hides an item from the newsfeed.
    https://vk.com/dev/newsfeed.ignoreItem
    """
    params = {
        'type': type,
        'owner_id': owner_id,
        'item_id': item_id
    }
    result = call('newsfeed.ignoreItem', **params)
    return parse_response(result)


def saveList(list_id=None, title=None, source_ids=None, no_reposts=None):
    """
    Creates and edits user newsfeed lists
    https://vk.com/dev/newsfeed.saveList
    """
    params = {
        'list_id': list_id,
        'title': title,
        'source_ids': source_ids,
        'no_reposts': no_reposts
    }
    result = call('newsfeed.saveList', **params)
    return parse_response(result)


def search(q=None, extended=None, count=None, latitude=None, longitude=None,\
           start_time=None, end_time=None, start_from=None, fields=None,\
           start_id=None, offset=None):
    """
    Returns search results by statuses. 
    https://vk.com/dev/newsfeed.search
    """
    params = {
        'q': q,
        'extended': extended,
        'count': count,
        'latitude': latitude,
        'longitude': longitude,
        'start_time': start_time,
        'end_time': end_time,
        'start_from': start_from,
        'fields': fields,
        'start_id': start_id,
        'offset': offset
    }
    result = call('newsfeed.search', **params)
    return parse_response(result)


def unignoreItem(type=None, owner_id=None, item_id=None):
    """
    Returns a hidden item to the newsfeed.
    https://vk.com/dev/newsfeed.unignoreItem
    """
    params = {
        'type': type,
        'owner_id': owner_id,
        'item_id': item_id
    }
    result = call('newsfeed.unignoreItem', **params)
    return parse_response(result)


def unsubscribe(type=None, owner_id=None, item_id=None):
    """
    Unsubscribes the current user from specified newsfeeds.
    https://vk.com/dev/newsfeed.unsubscribe
    """
    params = {
        'type': type,
        'owner_id': owner_id,
        'item_id': item_id
    }
    result = call('newsfeed.unsubscribe', **params)
    return parse_response(result)


