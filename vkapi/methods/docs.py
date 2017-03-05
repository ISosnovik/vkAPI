# Docs methods
from ..api import call, parse_response


def add(owner_id=None, doc_id=None, access_key=None):
    """
    Copies a document to a user's or community's document
    list.
    https://vk.com/dev/docs.add
    """
    params = {
        'owner_id': owner_id,
        'doc_id': doc_id,
        'access_key': access_key
    }
    result = call('docs.add', **params)
    return parse_response(result)


def delete(owner_id=None, doc_id=None):
    """
    Deletes a user or community document.
    https://vk.com/dev/docs.delete
    """
    params = {
        'owner_id': owner_id,
        'doc_id': doc_id
    }
    result = call('docs.delete', **params)
    return parse_response(result)


def edit(owner_id=None, doc_id=None, title=None, tags=None):
    """
    Edits a document.
    https://vk.com/dev/docs.edit
    """
    params = {
        'owner_id': owner_id,
        'doc_id': doc_id,
        'title': title,
        'tags': tags
    }
    result = call('docs.edit', **params)
    return parse_response(result)


def get(count=None, offset=None, type=None, owner_id=None):
    """
    Returns detailed information about user or community
    documents.
    https://vk.com/dev/docs.get
    """
    params = {
        'count': count,
        'offset': offset,
        'type': type,
        'owner_id': owner_id
    }
    result = call('docs.get', **params)
    return parse_response(result)


def getById(docs=None):
    """
    Returns information about documents by their IDs.
    https://vk.com/dev/docs.getById
    """
    params = {
        'docs': docs
    }
    result = call('docs.getById', **params)
    return parse_response(result)


def getTypes(owner_id=None):
    """
    Returns documents types available for current user.
    https://vk.com/dev/docs.getTypes
    """
    params = {
        'owner_id': owner_id
    }
    result = call('docs.getTypes', **params)
    return parse_response(result)


def getUploadServer(group_id=None):
    """
    Returns the server address for document upload.
    https://vk.com/dev/docs.getUploadServer
    """
    params = {
        'group_id': group_id
    }
    result = call('docs.getUploadServer', **params)
    return parse_response(result)


def getWallUploadServer(group_id=None):
    """
    Returns the server address for document upload onto
    a user's or community's wall.
    https://vk.com/dev/docs.getWallUploadServer
    """
    params = {
        'group_id': group_id
    }
    result = call('docs.getWallUploadServer', **params)
    return parse_response(result)


def save(file=None, title=None, tags=None):
    """
    Saves a document after uploading it to a server.
    https://vk.com/dev/docs.save
    """
    params = {
        'file': file,
        'title': title,
        'tags': tags
    }
    result = call('docs.save', **params)
    return parse_response(result)


def search(q=None, count=None, offset=None):
    """
    Returns a list of documents matching the search criteria.
    https://vk.com/dev/docs.search
    """
    params = {
        'q': q,
        'count': count,
        'offset': offset
    }
    result = call('docs.search', **params)
    return parse_response(result)


