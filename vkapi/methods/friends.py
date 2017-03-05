# Friends methods
from ..api import call, parse_response


def add(user_id=None, text=None, follow=None):
    """
    Approves or creates a friend request.
    https://vk.com/dev/friends.add
    """
    params = {
        'user_id': user_id,
        'text': text,
        'follow': follow
    }
    result = call('friends.add', **params)
    return parse_response(result)


def addList(name=None, user_ids=None):
    """
    Creates a new friend list for the current user.
    https://vk.com/dev/friends.addList
    """
    params = {
        'name': name,
        'user_ids': user_ids
    }
    result = call('friends.addList', **params)
    return parse_response(result)


def areFriends(user_ids=None, need_sign=None):
    """
    Checks the current user's friendship status with other
    specified users.
    https://vk.com/dev/friends.areFriends
    """
    params = {
        'user_ids': user_ids,
        'need_sign': need_sign
    }
    result = call('friends.areFriends', **params)
    return parse_response(result)


def delete(user_id=None):
    """
    Declines a friend request or deletes a user from the
    current user's friend list.
    https://vk.com/dev/friends.delete
    """
    params = {
        'user_id': user_id
    }
    result = call('friends.delete', **params)
    return parse_response(result)


def deleteAllRequests():
    """
    Marks all incoming friend requests as viewed.
    https://vk.com/dev/friends.deleteAllRequests
    """
    params = {
    }
    result = call('friends.deleteAllRequests', **params)
    return parse_response(result)


def deleteList(list_id=None):
    """
    Deletes a friend list of the current user.
    https://vk.com/dev/friends.deleteList
    """
    params = {
        'list_id': list_id
    }
    result = call('friends.deleteList', **params)
    return parse_response(result)


def edit(user_id=None, list_ids=None):
    """
    Edits the friend lists of the selected user.
    https://vk.com/dev/friends.edit
    """
    params = {
        'user_id': user_id,
        'list_ids': list_ids
    }
    result = call('friends.edit', **params)
    return parse_response(result)


def editList(name=None, list_id=None, user_ids=None, add_user_ids=None,\
             delete_user_ids=None):
    """
    Edits a friend list of the current user.
    https://vk.com/dev/friends.editList
    """
    params = {
        'name': name,
        'list_id': list_id,
        'user_ids': user_ids,
        'add_user_ids': add_user_ids,
        'delete_user_ids': delete_user_ids
    }
    result = call('friends.editList', **params)
    return parse_response(result)


def get(user_id=None, order=None, list_id=None, count=None, offset=None,\
        fields=None, name_case=None):
    """
    Returns a list of user IDs or detailed information about
    a user's friends.
    https://vk.com/dev/friends.get
    """
    params = {
        'user_id': user_id,
        'order': order,
        'list_id': list_id,
        'count': count,
        'offset': offset,
        'fields': fields,
        'name_case': name_case
    }
    result = call('friends.get', **params)
    return parse_response(result)


def getAppUsers():
    """
    Returns a list of IDs of the current user's friends
    who installed the application.
    https://vk.com/dev/friends.getAppUsers
    """
    params = {
    }
    result = call('friends.getAppUsers', **params)
    return parse_response(result)


def getAvailableForCall(fields=None, name_case=None):
    """
    Returns a list of friends who can be called by the current
    user.
    https://vk.com/dev/friends.getAvailableForCall
    """
    params = {
        'fields': fields,
        'name_case': name_case
    }
    result = call('friends.getAvailableForCall', **params)
    return parse_response(result)


def getByPhones(phones=None, fields=None):
    """
    Returns a list of the current user's friends whose phone
    numbers, validated or specified in a profile, are
    in a given list.
    https://vk.com/dev/friends.getByPhones
    """
    params = {
        'phones': phones,
        'fields': fields
    }
    result = call('friends.getByPhones', **params)
    return parse_response(result)


def getLists(user_id=None, return_system=None):
    """
    Returns a list of the user's friend lists.
    https://vk.com/dev/friends.getLists
    """
    params = {
        'user_id': user_id,
        'return_system': return_system
    }
    result = call('friends.getLists', **params)
    return parse_response(result)


def getMutual(source_uid=None, target_uid=None, target_uids=None, order=None,\
              count=None, offset=None):
    """
    Returns a list of user IDs of the mutual friends of
    two users.
    https://vk.com/dev/friends.getMutual
    """
    params = {
        'source_uid': source_uid,
        'target_uid': target_uid,
        'target_uids': target_uids,
        'order': order,
        'count': count,
        'offset': offset
    }
    result = call('friends.getMutual', **params)
    return parse_response(result)


def getOnline(user_id=None, list_id=None, online_mobile=None, order=None,\
              count=None, offset=None):
    """
    Returns a list of user IDs of a user's friends who are
    online.
    https://vk.com/dev/friends.getOnline
    """
    params = {
        'user_id': user_id,
        'list_id': list_id,
        'online_mobile': online_mobile,
        'order': order,
        'count': count,
        'offset': offset
    }
    result = call('friends.getOnline', **params)
    return parse_response(result)


def getRecent(count=None):
    """
    Returns a list of user IDs of the current user's recently
    added friends.
    https://vk.com/dev/friends.getRecent
    """
    params = {
        'count': count
    }
    result = call('friends.getRecent', **params)
    return parse_response(result)


def getRequests(offset=None, count=None, extended=None, need_mutual=None,\
                out=None, sort=None, need_viewed=None, suggested=None):
    """
    Returns information about the current user's incoming
    and outgoing friend requests.
    https://vk.com/dev/friends.getRequests
    """
    params = {
        'offset': offset,
        'count': count,
        'extended': extended,
        'need_mutual': need_mutual,
        'out': out,
        'sort': sort,
        'need_viewed': need_viewed,
        'suggested': suggested
    }
    result = call('friends.getRequests', **params)
    return parse_response(result)


def getSuggestions(filter=None, count=None, offset=None, fields=None, name_case=None):
    """
    Returns a list of profiles of users whom the current
    user may know.
    https://vk.com/dev/friends.getSuggestions
    """
    params = {
        'filter': filter,
        'count': count,
        'offset': offset,
        'fields': fields,
        'name_case': name_case
    }
    result = call('friends.getSuggestions', **params)
    return parse_response(result)


def search(user_id=None, q=None, fields=None, name_case=None, offset=None,\
           count=None):
    """
    Returns a list of friends matching the search criteria.
    https://vk.com/dev/friends.search
    """
    params = {
        'user_id': user_id,
        'q': q,
        'fields': fields,
        'name_case': name_case,
        'offset': offset,
        'count': count
    }
    result = call('friends.search', **params)
    return parse_response(result)


