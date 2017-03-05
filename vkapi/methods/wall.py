# Wall methods
from ..api import call, parse_response


def createComment(owner_id=None, post_id=None, from_group=None, message=None,\
                  reply_to_comment=None, attachments=None, sticker_id=None,\
                  guid=None):
    """
    Adds a comment to a post on a user wall or community
    wall.
    https://vk.com/dev/wall.createComment
    """
    params = {
        'owner_id': owner_id,
        'post_id': post_id,
        'from_group': from_group,
        'message': message,
        'reply_to_comment': reply_to_comment,
        'attachments': attachments,
        'sticker_id': sticker_id,
        'guid': guid
    }
    result = call('wall.createComment', **params)
    return parse_response(result)


def delete(owner_id=None, post_id=None):
    """
    Deletes a post from a user wall or community wall.
    https://vk.com/dev/wall.delete
    """
    params = {
        'owner_id': owner_id,
        'post_id': post_id
    }
    result = call('wall.delete', **params)
    return parse_response(result)


def deleteComment(owner_id=None, comment_id=None):
    """
    Deletes a comment on a post on a user wall or community
    wall. 
    https://vk.com/dev/wall.deleteComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id
    }
    result = call('wall.deleteComment', **params)
    return parse_response(result)


def edit(owner_id=None, post_id=None, friends_only=None, message=None, attachments=None,\
         services=None, signed=None, publish_date=None, lat=None, long=None,\
         place_id=None, mark_as_ads=None):
    """
    Edits a post on a user wall or community wall.
    https://vk.com/dev/wall.edit
    """
    params = {
        'owner_id': owner_id,
        'post_id': post_id,
        'friends_only': friends_only,
        'message': message,
        'attachments': attachments,
        'services': services,
        'signed': signed,
        'publish_date': publish_date,
        'lat': lat,
        'long': long,
        'place_id': place_id,
        'mark_as_ads': mark_as_ads
    }
    result = call('wall.edit', **params)
    return parse_response(result)


def editComment(owner_id=None, comment_id=None, message=None, attachments=None):
    """
    Edits a comment on a user wall or community wall. 
    https://vk.com/dev/wall.editComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id,
        'message': message,
        'attachments': attachments
    }
    result = call('wall.editComment', **params)
    return parse_response(result)


def get(owner_id=None, domain=None, offset=None, count=None, filter=None,\
        extended=None, fields=None):
    """
    Returns a list of posts on a user wall or community
    wall.
    https://vk.com/dev/wall.get
    """
    params = {
        'owner_id': owner_id,
        'domain': domain,
        'offset': offset,
        'count': count,
        'filter': filter,
        'extended': extended,
        'fields': fields
    }
    result = call('wall.get', **params)
    return parse_response(result)


def getById(posts=None, extended=None, copy_history_depth=None, fields=None):
    """
    Returns a list of posts from user or community walls
    by their IDs.
    https://vk.com/dev/wall.getById
    """
    params = {
        'posts': posts,
        'extended': extended,
        'copy_history_depth': copy_history_depth,
        'fields': fields
    }
    result = call('wall.getById', **params)
    return parse_response(result)


def getComments(owner_id=None, post_id=None, need_likes=None, start_comment_id=None,\
                offset=None, count=None, sort=None, preview_length=None,\
                extended=None):
    """
    Returns a list of comments on a post on a user wall
    or community wall.
    https://vk.com/dev/wall.getComments
    """
    params = {
        'owner_id': owner_id,
        'post_id': post_id,
        'need_likes': need_likes,
        'start_comment_id': start_comment_id,
        'offset': offset,
        'count': count,
        'sort': sort,
        'preview_length': preview_length,
        'extended': extended
    }
    result = call('wall.getComments', **params)
    return parse_response(result)


def getReposts(owner_id=None, post_id=None, offset=None, count=None):
    """
    Returns information about reposts of a post on user
    wall or community wall.
    https://vk.com/dev/wall.getReposts
    """
    params = {
        'owner_id': owner_id,
        'post_id': post_id,
        'offset': offset,
        'count': count
    }
    result = call('wall.getReposts', **params)
    return parse_response(result)


def pin(owner_id=None, post_id=None):
    """
    Pins the post on wall.
    https://vk.com/dev/wall.pin
    """
    params = {
        'owner_id': owner_id,
        'post_id': post_id
    }
    result = call('wall.pin', **params)
    return parse_response(result)


def post(owner_id=None, friends_only=None, from_group=None, message=None,\
         attachments=None, services=None, signed=None, publish_date=None,\
         lat=None, long=None, place_id=None, post_id=None, guid=None, mark_as_ads=None):
    """
    Adds a new post on a user wall or community wall. Can
    also be used to publish suggested or scheduled posts.
    https://vk.com/dev/wall.post
    """
    params = {
        'owner_id': owner_id,
        'friends_only': friends_only,
        'from_group': from_group,
        'message': message,
        'attachments': attachments,
        'services': services,
        'signed': signed,
        'publish_date': publish_date,
        'lat': lat,
        'long': long,
        'place_id': place_id,
        'post_id': post_id,
        'guid': guid,
        'mark_as_ads': mark_as_ads
    }
    result = call('wall.post', **params)
    return parse_response(result)


def reportComment(owner_id=None, comment_id=None, reason=None):
    """
    Reports (submits a complaint about) a comment on a post
    on a user wall or community wall. 
    https://vk.com/dev/wall.reportComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id,
        'reason': reason
    }
    result = call('wall.reportComment', **params)
    return parse_response(result)


def reportPost(owner_id=None, post_id=None, reason=None):
    """
    Reports (submits a complaint about) a post on a user
    wall or community wall. 
    https://vk.com/dev/wall.reportPost
    """
    params = {
        'owner_id': owner_id,
        'post_id': post_id,
        'reason': reason
    }
    result = call('wall.reportPost', **params)
    return parse_response(result)


def repost(object=None, message=None, group_id=None, mark_as_ads=None):
    """
    Reposts (copies) an object to a user wall or community
    wall.
    https://vk.com/dev/wall.repost
    """
    params = {
        'object': object,
        'message': message,
        'group_id': group_id,
        'mark_as_ads': mark_as_ads
    }
    result = call('wall.repost', **params)
    return parse_response(result)


def restore(owner_id=None, post_id=None):
    """
    Restores a post deleted from a user wall or community
    wall.
    https://vk.com/dev/wall.restore
    """
    params = {
        'owner_id': owner_id,
        'post_id': post_id
    }
    result = call('wall.restore', **params)
    return parse_response(result)


def restoreComment(owner_id=None, comment_id=None):
    """
    Restores a comment deleted from a user wall or community
    wall. 
    https://vk.com/dev/wall.restoreComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id
    }
    result = call('wall.restoreComment', **params)
    return parse_response(result)


def search(owner_id=None, domain=None, query=None, owners_only=None, count=None,\
           offset=None, extended=None, fields=None):
    """
    Allows to search posts on user or community walls.
    https://vk.com/dev/wall.search
    """
    params = {
        'owner_id': owner_id,
        'domain': domain,
        'query': query,
        'owners_only': owners_only,
        'count': count,
        'offset': offset,
        'extended': extended,
        'fields': fields
    }
    result = call('wall.search', **params)
    return parse_response(result)


def unpin(owner_id=None, post_id=None):
    """
    Unpins the post on wall.
    https://vk.com/dev/wall.unpin
    """
    params = {
        'owner_id': owner_id,
        'post_id': post_id
    }
    result = call('wall.unpin', **params)
    return parse_response(result)


