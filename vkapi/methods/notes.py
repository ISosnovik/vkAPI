# Notes methods
from ..api import call, parse_response


def add(title=None, text=None, privacy_view=None, privacy_comment=None,\
        privacy=None, comment_privacy=None):
    """
    Creates a new note for the current user.
    https://vk.com/dev/notes.add
    """
    params = {
        'title': title,
        'text': text,
        'privacy_view': privacy_view,
        'privacy_comment': privacy_comment,
        'privacy': privacy,
        'comment_privacy': comment_privacy
    }
    result = call('notes.add', **params)
    return parse_response(result)


def createComment(note_id=None, owner_id=None, reply_to=None, message=None,\
                  guid=None):
    """
    Adds a new comment on a note.
    https://vk.com/dev/notes.createComment
    """
    params = {
        'note_id': note_id,
        'owner_id': owner_id,
        'reply_to': reply_to,
        'message': message,
        'guid': guid
    }
    result = call('notes.createComment', **params)
    return parse_response(result)


def delete(note_id=None):
    """
    Deletes a note of the current user.
    https://vk.com/dev/notes.delete
    """
    params = {
        'note_id': note_id
    }
    result = call('notes.delete', **params)
    return parse_response(result)


def deleteComment(comment_id=None, owner_id=None):
    """
    Deletes a comment on a note.
    https://vk.com/dev/notes.deleteComment
    """
    params = {
        'comment_id': comment_id,
        'owner_id': owner_id
    }
    result = call('notes.deleteComment', **params)
    return parse_response(result)


def edit(note_id=None, title=None, text=None, privacy_view=None, privacy_comment=None,\
         privacy=None, comment_privacy=None):
    """
    Edits a note of the current user.
    https://vk.com/dev/notes.edit
    """
    params = {
        'note_id': note_id,
        'title': title,
        'text': text,
        'privacy_view': privacy_view,
        'privacy_comment': privacy_comment,
        'privacy': privacy,
        'comment_privacy': comment_privacy
    }
    result = call('notes.edit', **params)
    return parse_response(result)


def editComment(comment_id=None, owner_id=None, message=None):
    """
    Edits a comment on a note.
    https://vk.com/dev/notes.editComment
    """
    params = {
        'comment_id': comment_id,
        'owner_id': owner_id,
        'message': message
    }
    result = call('notes.editComment', **params)
    return parse_response(result)


def get(note_ids=None, user_id=None, offset=None, count=None, sort=None):
    """
    Returns a list of notes created by a user.
    https://vk.com/dev/notes.get
    """
    params = {
        'note_ids': note_ids,
        'user_id': user_id,
        'offset': offset,
        'count': count,
        'sort': sort
    }
    result = call('notes.get', **params)
    return parse_response(result)


def getById(note_id=None, owner_id=None, need_wiki=None):
    """
    Returns a note by its ID.
    https://vk.com/dev/notes.getById
    """
    params = {
        'note_id': note_id,
        'owner_id': owner_id,
        'need_wiki': need_wiki
    }
    result = call('notes.getById', **params)
    return parse_response(result)


def getComments(note_id=None, owner_id=None, sort=None, offset=None, count=None):
    """
    Returns a list of comments on a note.
    https://vk.com/dev/notes.getComments
    """
    params = {
        'note_id': note_id,
        'owner_id': owner_id,
        'sort': sort,
        'offset': offset,
        'count': count
    }
    result = call('notes.getComments', **params)
    return parse_response(result)


def restoreComment(comment_id=None, owner_id=None):
    """
    Restores a deleted comment on a note.
    https://vk.com/dev/notes.restoreComment
    """
    params = {
        'comment_id': comment_id,
        'owner_id': owner_id
    }
    result = call('notes.restoreComment', **params)
    return parse_response(result)


