# Messages methods
from ..api import call, parse_response


def addChatUser(chat_id=None, user_id=None):
    """
    Adds a new user to a chat.
    https://vk.com/dev/messages.addChatUser
    """
    params = {
        'chat_id': chat_id,
        'user_id': user_id
    }
    result = call('messages.addChatUser', **params)
    return parse_response(result)


def allowMessagesFromGroup(group_id=None, key=None):
    """
    Allows sending messages from community to the current
    user.
    https://vk.com/dev/messages.allowMessagesFromGroup
    """
    params = {
        'group_id': group_id,
        'key': key
    }
    result = call('messages.allowMessagesFromGroup', **params)
    return parse_response(result)


def createChat(user_ids=None, title=None):
    """
    Creates a chat with several participants.
    https://vk.com/dev/messages.createChat
    """
    params = {
        'user_ids': user_ids,
        'title': title
    }
    result = call('messages.createChat', **params)
    return parse_response(result)


def delete(message_ids=None, spam=None):
    """
    Deletes one or more messages.
    https://vk.com/dev/messages.delete
    """
    params = {
        'message_ids': message_ids,
        'spam': spam
    }
    result = call('messages.delete', **params)
    return parse_response(result)


def deleteChatPhoto(chat_id=None):
    """
    Deletes a chat's cover picture.
    https://vk.com/dev/messages.deleteChatPhoto
    """
    params = {
        'chat_id': chat_id
    }
    result = call('messages.deleteChatPhoto', **params)
    return parse_response(result)


def deleteDialog(user_id=None, peer_id=None, offset=None, count=None):
    """
    Deletes all private messages in a conversation.
    https://vk.com/dev/messages.deleteDialog
    """
    params = {
        'user_id': user_id,
        'peer_id': peer_id,
        'offset': offset,
        'count': count
    }
    result = call('messages.deleteDialog', **params)
    return parse_response(result)


def denyMessagesFromGroup(group_id=None):
    """
    Denies sending message from community to the current
    user.
    https://vk.com/dev/messages.denyMessagesFromGroup
    """
    params = {
        'group_id': group_id
    }
    result = call('messages.denyMessagesFromGroup', **params)
    return parse_response(result)


def editChat(chat_id=None, title=None):
    """
    Edits the title of a chat.
    https://vk.com/dev/messages.editChat
    """
    params = {
        'chat_id': chat_id,
        'title': title
    }
    result = call('messages.editChat', **params)
    return parse_response(result)


def get(out=None, offset=None, count=None, time_offset=None, filters=None,\
        preview_length=None, last_message_id=None):
    """
    Returns a list of the current user's incoming or outgoing
    private messages.
    https://vk.com/dev/messages.get
    """
    params = {
        'out': out,
        'offset': offset,
        'count': count,
        'time_offset': time_offset,
        'filters': filters,
        'preview_length': preview_length,
        'last_message_id': last_message_id
    }
    result = call('messages.get', **params)
    return parse_response(result)


def getById(message_ids=None, preview_length=None):
    """
    Returns messages by their IDs.
    https://vk.com/dev/messages.getById
    """
    params = {
        'message_ids': message_ids,
        'preview_length': preview_length
    }
    result = call('messages.getById', **params)
    return parse_response(result)


def getChat(chat_id=None, chat_ids=None, fields=None, name_case=None):
    """
    Returns information about a chat.
    https://vk.com/dev/messages.getChat
    """
    params = {
        'chat_id': chat_id,
        'chat_ids': chat_ids,
        'fields': fields,
        'name_case': name_case
    }
    result = call('messages.getChat', **params)
    return parse_response(result)


def getChatUsers(chat_id=None, chat_ids=None, fields=None, name_case=None):
    """
    Returns a list of IDs of users participating in a chat.
    https://vk.com/dev/messages.getChatUsers
    """
    params = {
        'chat_id': chat_id,
        'chat_ids': chat_ids,
        'fields': fields,
        'name_case': name_case
    }
    result = call('messages.getChatUsers', **params)
    return parse_response(result)


def getDialogs(offset=None, count=None, start_message_id=None, preview_length=None,\
               unread=None, important=None, unanswered=None, user_id=None):
    """
    Returns a list of the current user's conversations.
    https://vk.com/dev/messages.getDialogs
    """
    params = {
        'offset': offset,
        'count': count,
        'start_message_id': start_message_id,
        'preview_length': preview_length,
        'unread': unread,
        'important': important,
        'unanswered': unanswered,
        'user_id': user_id
    }
    result = call('messages.getDialogs', **params)
    return parse_response(result)


def getHistory(offset=None, count=None, user_id=None, peer_id=None, start_message_id=None,\
               rev=None):
    """
    Returns message history for the specified user or group
    chat.
    https://vk.com/dev/messages.getHistory
    """
    params = {
        'offset': offset,
        'count': count,
        'user_id': user_id,
        'peer_id': peer_id,
        'start_message_id': start_message_id,
        'rev': rev
    }
    result = call('messages.getHistory', **params)
    return parse_response(result)


def getHistoryAttachments(peer_id=None, media_type=None, start_from=None,\
                          count=None, photo_sizes=None, fields=None):
    """
    Returns media files from the dialog or group chat.
    https://vk.com/dev/messages.getHistoryAttachments
    """
    params = {
        'peer_id': peer_id,
        'media_type': media_type,
        'start_from': start_from,
        'count': count,
        'photo_sizes': photo_sizes,
        'fields': fields
    }
    result = call('messages.getHistoryAttachments', **params)
    return parse_response(result)


def getLastActivity(user_id=None):
    """
    Returns a user's current status and date of last activity.
    https://vk.com/dev/messages.getLastActivity
    """
    params = {
        'user_id': user_id
    }
    result = call('messages.getLastActivity', **params)
    return parse_response(result)


def getLongPollHistory(ts=None, pts=None, preview_length=None, onlines=None,\
                       fields=None, events_limit=None, msgs_limit=None,\
                       max_msg_id=None):
    """
    Returns updates in user's private messages.
    https://vk.com/dev/messages.getLongPollHistory
    """
    params = {
        'ts': ts,
        'pts': pts,
        'preview_length': preview_length,
        'onlines': onlines,
        'fields': fields,
        'events_limit': events_limit,
        'msgs_limit': msgs_limit,
        'max_msg_id': max_msg_id
    }
    result = call('messages.getLongPollHistory', **params)
    return parse_response(result)


def getLongPollServer(use_ssl=None, need_pts=None):
    """
    Returns data required for connection to a Long Poll
    server.
    https://vk.com/dev/messages.getLongPollServer
    """
    params = {
        'use_ssl': use_ssl,
        'need_pts': need_pts
    }
    result = call('messages.getLongPollServer', **params)
    return parse_response(result)


def isMessagesFromGroupAllowed(group_id=None, user_id=None):
    """
    Returns information whether sending messages from the
    community to current user is allowed.
    https://vk.com/dev/messages.isMessagesFromGroupAllowed
    """
    params = {
        'group_id': group_id,
        'user_id': user_id
    }
    result = call('messages.isMessagesFromGroupAllowed', **params)
    return parse_response(result)


def markAsAnsweredDialog(peer_id=None, answered=None):
    """
    
    https://vk.com/dev/messages.markAsAnsweredDialog
    """
    params = {
        'peer_id': peer_id,
        'answered': answered
    }
    result = call('messages.markAsAnsweredDialog', **params)
    return parse_response(result)


def markAsImportant(message_ids=None, important=None):
    """
    Marks and unmarks messages as important (starred).
    https://vk.com/dev/messages.markAsImportant
    """
    params = {
        'message_ids': message_ids,
        'important': important
    }
    result = call('messages.markAsImportant', **params)
    return parse_response(result)


def markAsImportantDialog(peer_id=None, important=None):
    """
    
    https://vk.com/dev/messages.markAsImportantDialog
    """
    params = {
        'peer_id': peer_id,
        'important': important
    }
    result = call('messages.markAsImportantDialog', **params)
    return parse_response(result)


def markAsRead(message_ids=None, peer_id=None, start_message_id=None):
    """
    Marks messages as read.
    https://vk.com/dev/messages.markAsRead
    """
    params = {
        'message_ids': message_ids,
        'peer_id': peer_id,
        'start_message_id': start_message_id
    }
    result = call('messages.markAsRead', **params)
    return parse_response(result)


def removeChatUser(chat_id=None, user_id=None):
    """
    Allows the current user to leave a chat or, if the current
    user started the chat, allows the user to remove
    another user from the chat.
    https://vk.com/dev/messages.removeChatUser
    """
    params = {
        'chat_id': chat_id,
        'user_id': user_id
    }
    result = call('messages.removeChatUser', **params)
    return parse_response(result)


def restore(message_id=None):
    """
    Restores a deleted message.
    https://vk.com/dev/messages.restore
    """
    params = {
        'message_id': message_id
    }
    result = call('messages.restore', **params)
    return parse_response(result)


def search(q=None, peer_id=None, date=None, preview_length=None, offset=None,\
           count=None):
    """
    Returns a list of the current user's private messages
    that match search criteria.
    https://vk.com/dev/messages.search
    """
    params = {
        'q': q,
        'peer_id': peer_id,
        'date': date,
        'preview_length': preview_length,
        'offset': offset,
        'count': count
    }
    result = call('messages.search', **params)
    return parse_response(result)


def searchDialogs(q=None, limit=None, fields=None):
    """
    Returns a list of the current user's conversations that
    match search criteria.
    https://vk.com/dev/messages.searchDialogs
    """
    params = {
        'q': q,
        'limit': limit,
        'fields': fields
    }
    result = call('messages.searchDialogs', **params)
    return parse_response(result)


def send(user_id=None, random_id=None, peer_id=None, domain=None, chat_id=None,\
         user_ids=None, message=None, lat=None, long=None, attachment=None,\
         forward_messages=None, sticker_id=None, notification=None, guid=None):
    """
    Sends a message.
    https://vk.com/dev/messages.send
    """
    params = {
        'user_id': user_id,
        'random_id': random_id,
        'peer_id': peer_id,
        'domain': domain,
        'chat_id': chat_id,
        'user_ids': user_ids,
        'message': message,
        'lat': lat,
        'long': long,
        'attachment': attachment,
        'forward_messages': forward_messages,
        'sticker_id': sticker_id,
        'notification': notification,
        'guid': guid
    }
    result = call('messages.send', **params)
    return parse_response(result)


def setActivity(user_id=None, type=None, peer_id=None):
    """
    Changes the status of a user as typing in a conversation.
    https://vk.com/dev/messages.setActivity
    """
    params = {
        'user_id': user_id,
        'type': type,
        'peer_id': peer_id
    }
    result = call('messages.setActivity', **params)
    return parse_response(result)


def setChatPhoto(file=None):
    """
    Sets a previously-uploaded picture as the cover picture
    of a chat.
    https://vk.com/dev/messages.setChatPhoto
    """
    params = {
        'file': file
    }
    result = call('messages.setChatPhoto', **params)
    return parse_response(result)


