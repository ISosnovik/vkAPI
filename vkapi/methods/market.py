# Market methods
from ..api import call, parse_response


def add(owner_id=None, name=None, description=None, category_id=None, price=None,\
        deleted=None, main_photo_id=None, photo_ids=None):
    """
    Ads a new item to the market.
    https://vk.com/dev/market.add
    """
    params = {
        'owner_id': owner_id,
        'name': name,
        'description': description,
        'category_id': category_id,
        'price': price,
        'deleted': deleted,
        'main_photo_id': main_photo_id,
        'photo_ids': photo_ids
    }
    result = call('market.add', **params)
    return parse_response(result)


def addAlbum(owner_id=None, title=None, photo_id=None, main_album=None):
    """
    Creates new collection of items
    https://vk.com/dev/market.addAlbum
    """
    params = {
        'owner_id': owner_id,
        'title': title,
        'photo_id': photo_id,
        'main_album': main_album
    }
    result = call('market.addAlbum', **params)
    return parse_response(result)


def addToAlbum(owner_id=None, item_id=None, album_ids=None):
    """
    Adds an item to one or multiple collections.
    https://vk.com/dev/market.addToAlbum
    """
    params = {
        'owner_id': owner_id,
        'item_id': item_id,
        'album_ids': album_ids
    }
    result = call('market.addToAlbum', **params)
    return parse_response(result)


def createComment(owner_id=None, item_id=None, message=None, attachments=None,\
                  from_group=None, reply_to_comment=None, sticker_id=None,\
                  guid=None):
    """
    Creates a new comment for an item.
    https://vk.com/dev/market.createComment
    """
    params = {
        'owner_id': owner_id,
        'item_id': item_id,
        'message': message,
        'attachments': attachments,
        'from_group': from_group,
        'reply_to_comment': reply_to_comment,
        'sticker_id': sticker_id,
        'guid': guid
    }
    result = call('market.createComment', **params)
    return parse_response(result)


def delete(owner_id=None, item_id=None):
    """
    Deletes an item.
    https://vk.com/dev/market.delete
    """
    params = {
        'owner_id': owner_id,
        'item_id': item_id
    }
    result = call('market.delete', **params)
    return parse_response(result)


def deleteAlbum(owner_id=None, album_id=None):
    """
    Deletes a collection of items.
    https://vk.com/dev/market.deleteAlbum
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id
    }
    result = call('market.deleteAlbum', **params)
    return parse_response(result)


def deleteComment(owner_id=None, comment_id=None):
    """
    Deletes an item's comment
    https://vk.com/dev/market.deleteComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id
    }
    result = call('market.deleteComment', **params)
    return parse_response(result)


def edit(owner_id=None, item_id=None, name=None, description=None, category_id=None,\
         price=None, deleted=None, main_photo_id=None, photo_ids=None):
    """
    Edits an item.
    https://vk.com/dev/market.edit
    """
    params = {
        'owner_id': owner_id,
        'item_id': item_id,
        'name': name,
        'description': description,
        'category_id': category_id,
        'price': price,
        'deleted': deleted,
        'main_photo_id': main_photo_id,
        'photo_ids': photo_ids
    }
    result = call('market.edit', **params)
    return parse_response(result)


def editAlbum(owner_id=None, album_id=None, title=None, photo_id=None, main_album=None):
    """
    Edits a collection of items
    https://vk.com/dev/market.editAlbum
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'title': title,
        'photo_id': photo_id,
        'main_album': main_album
    }
    result = call('market.editAlbum', **params)
    return parse_response(result)


def editComment(owner_id=None, comment_id=None, message=None, attachments=None):
    """
    Chages item comment's text
    https://vk.com/dev/market.editComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id,
        'message': message,
        'attachments': attachments
    }
    result = call('market.editComment', **params)
    return parse_response(result)


def get(owner_id=None, album_id=None, count=None, offset=None, extended=None):
    """
    Returns items list for a community.
    https://vk.com/dev/market.get
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'count': count,
        'offset': offset,
        'extended': extended
    }
    result = call('market.get', **params)
    return parse_response(result)


def getAlbumById(owner_id=None, album_ids=None):
    """
    Returns items album's data
    https://vk.com/dev/market.getAlbumById
    """
    params = {
        'owner_id': owner_id,
        'album_ids': album_ids
    }
    result = call('market.getAlbumById', **params)
    return parse_response(result)


def getAlbums(owner_id=None, offset=None, count=None):
    """
    Returns community's collections list.
    https://vk.com/dev/market.getAlbums
    """
    params = {
        'owner_id': owner_id,
        'offset': offset,
        'count': count
    }
    result = call('market.getAlbums', **params)
    return parse_response(result)


def getById(item_ids=None, extended=None):
    """
    Returns information about market items by their ids.
    https://vk.com/dev/market.getById
    """
    params = {
        'item_ids': item_ids,
        'extended': extended
    }
    result = call('market.getById', **params)
    return parse_response(result)


def getCategories(count=None, offset=None):
    """
    Returns a list of market categories.
    https://vk.com/dev/market.getCategories
    """
    params = {
        'count': count,
        'offset': offset
    }
    result = call('market.getCategories', **params)
    return parse_response(result)


def getComments(owner_id=None, item_id=None, need_likes=None, start_comment_id=None,\
                offset=None, count=None, sort=None, extended=None, fields=None):
    """
    Returns comments list for an item.
    https://vk.com/dev/market.getComments
    """
    params = {
        'owner_id': owner_id,
        'item_id': item_id,
        'need_likes': need_likes,
        'start_comment_id': start_comment_id,
        'offset': offset,
        'count': count,
        'sort': sort,
        'extended': extended,
        'fields': fields
    }
    result = call('market.getComments', **params)
    return parse_response(result)


def removeFromAlbum(owner_id=None, item_id=None, album_ids=None):
    """
    Removes an item from one or multiple collections.
    https://vk.com/dev/market.removeFromAlbum
    """
    params = {
        'owner_id': owner_id,
        'item_id': item_id,
        'album_ids': album_ids
    }
    result = call('market.removeFromAlbum', **params)
    return parse_response(result)


def reorderAlbums(owner_id=None, album_id=None, before=None, after=None):
    """
    Reorders the collections list.
    https://vk.com/dev/market.reorderAlbums
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'before': before,
        'after': after
    }
    result = call('market.reorderAlbums', **params)
    return parse_response(result)


def reorderItems(owner_id=None, album_id=None, item_id=None, before=None,\
                 after=None):
    """
    Changes item place in a collection.
    https://vk.com/dev/market.reorderItems
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'item_id': item_id,
        'before': before,
        'after': after
    }
    result = call('market.reorderItems', **params)
    return parse_response(result)


def report(owner_id=None, item_id=None, reason=None):
    """
    Sends a complaint to the item.
    https://vk.com/dev/market.report
    """
    params = {
        'owner_id': owner_id,
        'item_id': item_id,
        'reason': reason
    }
    result = call('market.report', **params)
    return parse_response(result)


def reportComment(owner_id=None, comment_id=None, reason=None):
    """
    Sends a complaint to the item's comment.
    https://vk.com/dev/market.reportComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id,
        'reason': reason
    }
    result = call('market.reportComment', **params)
    return parse_response(result)


def restore(owner_id=None, item_id=None):
    """
    Restores recently deleted item
    https://vk.com/dev/market.restore
    """
    params = {
        'owner_id': owner_id,
        'item_id': item_id
    }
    result = call('market.restore', **params)
    return parse_response(result)


def restoreComment(owner_id=None, comment_id=None):
    """
    Restores a recently deleted comment
    https://vk.com/dev/market.restoreComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id
    }
    result = call('market.restoreComment', **params)
    return parse_response(result)


def search(owner_id=None, album_id=None, q=None, price_from=None, price_to=None,\
           tags=None, sort=None, rev=None, offset=None, count=None, extended=None):
    """
    Searches market items in a community's catalog
    https://vk.com/dev/market.search
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'q': q,
        'price_from': price_from,
        'price_to': price_to,
        'tags': tags,
        'sort': sort,
        'rev': rev,
        'offset': offset,
        'count': count,
        'extended': extended
    }
    result = call('market.search', **params)
    return parse_response(result)


