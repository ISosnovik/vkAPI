# Groups methods
from ..api import call, parse_response


def addLink(group_id=None, link=None, text=None):
    """
    Allows to add a link to the community.
    https://vk.com/dev/groups.addLink
    """
    params = {
        'group_id': group_id,
        'link': link,
        'text': text
    }
    result = call('groups.addLink', **params)
    return parse_response(result)


def approveRequest(group_id=None, user_id=None):
    """
    Allows to approve join request to the community.
    https://vk.com/dev/groups.approveRequest
    """
    params = {
        'group_id': group_id,
        'user_id': user_id
    }
    result = call('groups.approveRequest', **params)
    return parse_response(result)


def banUser(group_id=None, user_id=None, end_date=None, reason=None, comment=None,\
            comment_visible=None):
    """
    Adds a user to a community blacklist.
    https://vk.com/dev/groups.banUser
    """
    params = {
        'group_id': group_id,
        'user_id': user_id,
        'end_date': end_date,
        'reason': reason,
        'comment': comment,
        'comment_visible': comment_visible
    }
    result = call('groups.banUser', **params)
    return parse_response(result)


def create(title=None, description=None, type=None, public_category=None,\
           subtype=None):
    """
    Creates a new community.
    https://vk.com/dev/groups.create
    """
    params = {
        'title': title,
        'description': description,
        'type': type,
        'public_category': public_category,
        'subtype': subtype
    }
    result = call('groups.create', **params)
    return parse_response(result)


def deleteLink(group_id=None, link_id=None):
    """
    Allows to delete a link from the community.
    https://vk.com/dev/groups.deleteLink
    """
    params = {
        'group_id': group_id,
        'link_id': link_id
    }
    result = call('groups.deleteLink', **params)
    return parse_response(result)


def edit(group_id=None, title=None, description=None, screen_name=None,\
         access=None, website=None, subject=None, email=None, phone=None,\
         rss=None, event_start_date=None, event_finish_date=None, event_group_id=None,\
         public_category=None, public_subcategory=None, public_date=None,\
         wall=None, topics=None, photos=None, video=None, audio=None, links=None,\
         events=None, places=None, contacts=None, docs=None, wiki=None,\
         messages=None, age_limits=None, market=None, market_comments=None,\
         market_country=None, market_city=None, market_currency=None, market_contact=None,\
         market_wiki=None, obscene_filter=None, obscene_stopwords=None,\
         obscene_words=None):
    """
    Edits a community.
    https://vk.com/dev/groups.edit
    """
    params = {
        'group_id': group_id,
        'title': title,
        'description': description,
        'screen_name': screen_name,
        'access': access,
        'website': website,
        'subject': subject,
        'email': email,
        'phone': phone,
        'rss': rss,
        'event_start_date': event_start_date,
        'event_finish_date': event_finish_date,
        'event_group_id': event_group_id,
        'public_category': public_category,
        'public_subcategory': public_subcategory,
        'public_date': public_date,
        'wall': wall,
        'topics': topics,
        'photos': photos,
        'video': video,
        'audio': audio,
        'links': links,
        'events': events,
        'places': places,
        'contacts': contacts,
        'docs': docs,
        'wiki': wiki,
        'messages': messages,
        'age_limits': age_limits,
        'market': market,
        'market_comments': market_comments,
        'market_country': market_country,
        'market_city': market_city,
        'market_currency': market_currency,
        'market_contact': market_contact,
        'market_wiki': market_wiki,
        'obscene_filter': obscene_filter,
        'obscene_stopwords': obscene_stopwords,
        'obscene_words': obscene_words
    }
    result = call('groups.edit', **params)
    return parse_response(result)


def editLink(group_id=None, link_id=None, text=None):
    """
    Allows to edit a link in the community.
    https://vk.com/dev/groups.editLink
    """
    params = {
        'group_id': group_id,
        'link_id': link_id,
        'text': text
    }
    result = call('groups.editLink', **params)
    return parse_response(result)


def editManager(group_id=None, user_id=None, role=None, is_contact=None,\
                contact_position=None, contact_phone=None, contact_email=None):
    """
    Allows to add, remove or edit the community manager
    .
    https://vk.com/dev/groups.editManager
    """
    params = {
        'group_id': group_id,
        'user_id': user_id,
        'role': role,
        'is_contact': is_contact,
        'contact_position': contact_position,
        'contact_phone': contact_phone,
        'contact_email': contact_email
    }
    result = call('groups.editManager', **params)
    return parse_response(result)


def editPlace(group_id=None, title=None, address=None, country_id=None,\
              city_id=None, latitude=None, longitude=None):
    """
    Edits the place in community.
    https://vk.com/dev/groups.editPlace
    """
    params = {
        'group_id': group_id,
        'title': title,
        'address': address,
        'country_id': country_id,
        'city_id': city_id,
        'latitude': latitude,
        'longitude': longitude
    }
    result = call('groups.editPlace', **params)
    return parse_response(result)


def get(user_id=None, extended=None, filter=None, fields=None, offset=None,\
        count=None):
    """
    Returns a list of the communities to which a user belongs.
    https://vk.com/dev/groups.get
    """
    params = {
        'user_id': user_id,
        'extended': extended,
        'filter': filter,
        'fields': fields,
        'offset': offset,
        'count': count
    }
    result = call('groups.get', **params)
    return parse_response(result)


def getBanned(group_id=None, offset=None, count=None, fields=None, user_id=None):
    """
    Returns a list of users on a community blacklist.
    https://vk.com/dev/groups.getBanned
    """
    params = {
        'group_id': group_id,
        'offset': offset,
        'count': count,
        'fields': fields,
        'user_id': user_id
    }
    result = call('groups.getBanned', **params)
    return parse_response(result)


def getById(group_ids=None, group_id=None, fields=None):
    """
    Returns information about communities by their IDs.
    https://vk.com/dev/groups.getById
    """
    params = {
        'group_ids': group_ids,
        'group_id': group_id,
        'fields': fields
    }
    result = call('groups.getById', **params)
    return parse_response(result)


def getCallbackConfirmationCode(group_id=None):
    """
    Returns Callback API confirmation code for the community.
    https://vk.com/dev/groups.getCallbackConfirmationCode
    """
    params = {
        'group_id': group_id
    }
    result = call('groups.getCallbackConfirmationCode', **params)
    return parse_response(result)


def getCallbackServerSettings(group_id=None):
    """
    Returns Callback API server settings for the community.
    https://vk.com/dev/groups.getCallbackServerSettings
    """
    params = {
        'group_id': group_id
    }
    result = call('groups.getCallbackServerSettings', **params)
    return parse_response(result)


def getCallbackSettings(group_id=None):
    """
    Returns Callback API notifications settings.
    https://vk.com/dev/groups.getCallbackSettings
    """
    params = {
        'group_id': group_id
    }
    result = call('groups.getCallbackSettings', **params)
    return parse_response(result)


def getCatalog(category_id=None, subcategory_id=None):
    """
    Returns communities list for a catalog category.
    https://vk.com/dev/groups.getCatalog
    """
    params = {
        'category_id': category_id,
        'subcategory_id': subcategory_id
    }
    result = call('groups.getCatalog', **params)
    return parse_response(result)


def getCatalogInfo(extended=None, subcategories=None):
    """
    Returns categories list for communities catalog
    https://vk.com/dev/groups.getCatalogInfo
    """
    params = {
        'extended': extended,
        'subcategories': subcategories
    }
    result = call('groups.getCatalogInfo', **params)
    return parse_response(result)


def getInvitedUsers(group_id=None, offset=None, count=None, fields=None,\
                    name_case=None):
    """
    Returns invited users list of a community
    https://vk.com/dev/groups.getInvitedUsers
    """
    params = {
        'group_id': group_id,
        'offset': offset,
        'count': count,
        'fields': fields,
        'name_case': name_case
    }
    result = call('groups.getInvitedUsers', **params)
    return parse_response(result)


def getInvites(offset=None, count=None, extended=None):
    """
    Returns a list of invitations to join communities and
    events.
    https://vk.com/dev/groups.getInvites
    """
    params = {
        'offset': offset,
        'count': count,
        'extended': extended
    }
    result = call('groups.getInvites', **params)
    return parse_response(result)


def getMembers(group_id=None, sort=None, offset=None, count=None, fields=None,\
               filter=None):
    """
    Returns a list of community members.
    https://vk.com/dev/groups.getMembers
    """
    params = {
        'group_id': group_id,
        'sort': sort,
        'offset': offset,
        'count': count,
        'fields': fields,
        'filter': filter
    }
    result = call('groups.getMembers', **params)
    return parse_response(result)


def getRequests(group_id=None, offset=None, count=None, fields=None):
    """
    Returns a list of requests to the community.
    https://vk.com/dev/groups.getRequests
    """
    params = {
        'group_id': group_id,
        'offset': offset,
        'count': count,
        'fields': fields
    }
    result = call('groups.getRequests', **params)
    return parse_response(result)


def getSettings(group_id=None):
    """
    Returns community settings.
    https://vk.com/dev/groups.getSettings
    """
    params = {
        'group_id': group_id
    }
    result = call('groups.getSettings', **params)
    return parse_response(result)


def invite(group_id=None, user_id=None):
    """
    Allows to invite friends to the community.
    https://vk.com/dev/groups.invite
    """
    params = {
        'group_id': group_id,
        'user_id': user_id
    }
    result = call('groups.invite', **params)
    return parse_response(result)


def isMember(group_id=None, user_id=None, user_ids=None, extended=None):
    """
    Returns information specifying whether a user is a member
    of a community.
    https://vk.com/dev/groups.isMember
    """
    params = {
        'group_id': group_id,
        'user_id': user_id,
        'user_ids': user_ids,
        'extended': extended
    }
    result = call('groups.isMember', **params)
    return parse_response(result)


def join(group_id=None, not_sure=None):
    """
    With this method you can join the group or public page,
    and also confirm your participation in an event.
    https://vk.com/dev/groups.join
    """
    params = {
        'group_id': group_id,
        'not_sure': not_sure
    }
    result = call('groups.join', **params)
    return parse_response(result)


def leave(group_id=None):
    """
    With this method you can leave a group, public page,
    or event.
    https://vk.com/dev/groups.leave
    """
    params = {
        'group_id': group_id
    }
    result = call('groups.leave', **params)
    return parse_response(result)


def removeUser(group_id=None, user_id=None):
    """
    Removes a user from the community.
    https://vk.com/dev/groups.removeUser
    """
    params = {
        'group_id': group_id,
        'user_id': user_id
    }
    result = call('groups.removeUser', **params)
    return parse_response(result)


def reorderLink(group_id=None, link_id=None, after=None):
    """
    Allows to reorder links in the community.
    https://vk.com/dev/groups.reorderLink
    """
    params = {
        'group_id': group_id,
        'link_id': link_id,
        'after': after
    }
    result = call('groups.reorderLink', **params)
    return parse_response(result)


def search(q=None, type=None, country_id=None, city_id=None, future=None,\
           market=None, sort=None, offset=None, count=None):
    """
    Returns a list of communities matching the search criteria.
    https://vk.com/dev/groups.search
    """
    params = {
        'q': q,
        'type': type,
        'country_id': country_id,
        'city_id': city_id,
        'future': future,
        'market': market,
        'sort': sort,
        'offset': offset,
        'count': count
    }
    result = call('groups.search', **params)
    return parse_response(result)


def setCallbackServer(group_id=None, server_url=None):
    """
    Allow to set Callback API server URL for the community.
    https://vk.com/dev/groups.setCallbackServer
    """
    params = {
        'group_id': group_id,
        'server_url': server_url
    }
    result = call('groups.setCallbackServer', **params)
    return parse_response(result)


def setCallbackServerSettings(group_id=None, secret_key=None):
    """
    Allow to set Callback API server settings.
    https://vk.com/dev/groups.setCallbackServerSettings
    """
    params = {
        'group_id': group_id,
        'secret_key': secret_key
    }
    result = call('groups.setCallbackServerSettings', **params)
    return parse_response(result)


def setCallbackSettings(group_id=None, message_new=None, message_allow=None,\
                        message_deny=None, photo_new=None, audio_new=None,\
                        video_new=None, wall_reply_new=None, wall_reply_edit=None,\
                        wall_post_new=None, board_post_new=None, board_post_edit=None,\
                        board_post_restore=None, board_post_delete=None,\
                        photo_comment_new=None, video_comment_new=None,\
                        market_comment_new=None, group_join=None, group_leave=None):
    """
    Allow to set notifications settings for Callback API.
    https://vk.com/dev/groups.setCallbackSettings
    """
    params = {
        'group_id': group_id,
        'message_new': message_new,
        'message_allow': message_allow,
        'message_deny': message_deny,
        'photo_new': photo_new,
        'audio_new': audio_new,
        'video_new': video_new,
        'wall_reply_new': wall_reply_new,
        'wall_reply_edit': wall_reply_edit,
        'wall_post_new': wall_post_new,
        'board_post_new': board_post_new,
        'board_post_edit': board_post_edit,
        'board_post_restore': board_post_restore,
        'board_post_delete': board_post_delete,
        'photo_comment_new': photo_comment_new,
        'video_comment_new': video_comment_new,
        'market_comment_new': market_comment_new,
        'group_join': group_join,
        'group_leave': group_leave
    }
    result = call('groups.setCallbackSettings', **params)
    return parse_response(result)


def unbanUser(group_id=None, user_id=None):
    """
    Removes a user from a community blacklist.
    https://vk.com/dev/groups.unbanUser
    """
    params = {
        'group_id': group_id,
        'user_id': user_id
    }
    result = call('groups.unbanUser', **params)
    return parse_response(result)


