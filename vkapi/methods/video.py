# Video methods
from ..api import call, parse_response


def add(target_id=None, video_id=None, owner_id=None):
    """
    Adds a video to a user or community page.
    https://vk.com/dev/video.add
    """
    params = {
        'target_id': target_id,
        'video_id': video_id,
        'owner_id': owner_id
    }
    result = call('video.add', **params)
    return parse_response(result)


def addAlbum(group_id=None, title=None, privacy=None):
    """
    Creates an empty album for videos.
    https://vk.com/dev/video.addAlbum
    """
    params = {
        'group_id': group_id,
        'title': title,
        'privacy': privacy
    }
    result = call('video.addAlbum', **params)
    return parse_response(result)


def addToAlbum(target_id=None, album_id=None, album_ids=None, owner_id=None,\
               video_id=None):
    """
    
    https://vk.com/dev/video.addToAlbum
    """
    params = {
        'target_id': target_id,
        'album_id': album_id,
        'album_ids': album_ids,
        'owner_id': owner_id,
        'video_id': video_id
    }
    result = call('video.addToAlbum', **params)
    return parse_response(result)


def createComment(owner_id=None, video_id=None, message=None, attachments=None,\
                  from_group=None, reply_to_comment=None, sticker_id=None,\
                  guid=None):
    """
    Adds a new comment on a video.
    https://vk.com/dev/video.createComment
    """
    params = {
        'owner_id': owner_id,
        'video_id': video_id,
        'message': message,
        'attachments': attachments,
        'from_group': from_group,
        'reply_to_comment': reply_to_comment,
        'sticker_id': sticker_id,
        'guid': guid
    }
    result = call('video.createComment', **params)
    return parse_response(result)


def delete(video_id=None, owner_id=None, target_id=None):
    """
    Deletes a video from a user or community page.
    https://vk.com/dev/video.delete
    """
    params = {
        'video_id': video_id,
        'owner_id': owner_id,
        'target_id': target_id
    }
    result = call('video.delete', **params)
    return parse_response(result)


def deleteAlbum(group_id=None, album_id=None):
    """
    Deletes a video album.
    https://vk.com/dev/video.deleteAlbum
    """
    params = {
        'group_id': group_id,
        'album_id': album_id
    }
    result = call('video.deleteAlbum', **params)
    return parse_response(result)


def deleteComment(owner_id=None, comment_id=None):
    """
    Deletes a comment on a video.
    https://vk.com/dev/video.deleteComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id
    }
    result = call('video.deleteComment', **params)
    return parse_response(result)


def edit(owner_id=None, video_id=None, name=None, desc=None, privacy_view=None,\
         privacy_comment=None, no_comments=None, repeat=None):
    """
    Edits information about a video on a user or community
    page.
    https://vk.com/dev/video.edit
    """
    params = {
        'owner_id': owner_id,
        'video_id': video_id,
        'name': name,
        'desc': desc,
        'privacy_view': privacy_view,
        'privacy_comment': privacy_comment,
        'no_comments': no_comments,
        'repeat': repeat
    }
    result = call('video.edit', **params)
    return parse_response(result)


def editAlbum(group_id=None, album_id=None, title=None, privacy=None):
    """
    Edits the title of a video album.
    https://vk.com/dev/video.editAlbum
    """
    params = {
        'group_id': group_id,
        'album_id': album_id,
        'title': title,
        'privacy': privacy
    }
    result = call('video.editAlbum', **params)
    return parse_response(result)


def editComment(owner_id=None, comment_id=None, message=None, attachments=None):
    """
    Edits the text of a comment on a video.
    https://vk.com/dev/video.editComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id,
        'message': message,
        'attachments': attachments
    }
    result = call('video.editComment', **params)
    return parse_response(result)


def get(owner_id=None, videos=None, album_id=None, count=None, offset=None,\
        extended=None):
    """
    Returns detailed information about videos.
    https://vk.com/dev/video.get
    """
    params = {
        'owner_id': owner_id,
        'videos': videos,
        'album_id': album_id,
        'count': count,
        'offset': offset,
        'extended': extended
    }
    result = call('video.get', **params)
    return parse_response(result)


def getAlbumById(owner_id=None, album_id=None):
    """
    Returns video album info
    https://vk.com/dev/video.getAlbumById
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id
    }
    result = call('video.getAlbumById', **params)
    return parse_response(result)


def getAlbums(owner_id=None, offset=None, count=None, extended=None, need_system=None):
    """
    Returns a list of video albums owned by a user or community.
    https://vk.com/dev/video.getAlbums
    """
    params = {
        'owner_id': owner_id,
        'offset': offset,
        'count': count,
        'extended': extended,
        'need_system': need_system
    }
    result = call('video.getAlbums', **params)
    return parse_response(result)


def getAlbumsByVideo(target_id=None, owner_id=None, video_id=None, extended=None):
    """
    
    https://vk.com/dev/video.getAlbumsByVideo
    """
    params = {
        'target_id': target_id,
        'owner_id': owner_id,
        'video_id': video_id,
        'extended': extended
    }
    result = call('video.getAlbumsByVideo', **params)
    return parse_response(result)


def getCatalog(count=None, items_count=None, from_=None, extended=None,\
               filters=None, grouped=None):
    """
    Returns video catalog
    https://vk.com/dev/video.getCatalog
    """
    params = {
        'count': count,
        'items_count': items_count,
        'from_': from_,
        'extended': extended,
        'filters': filters,
        'grouped': grouped
    }
    result = call('video.getCatalog', **params)
    return parse_response(result)


def getCatalogSection(section_id=None, from_=None, count=None, extended=None):
    """
    Returns a separate catalog section
    https://vk.com/dev/video.getCatalogSection
    """
    params = {
        'section_id': section_id,
        'from_': from_,
        'count': count,
        'extended': extended
    }
    result = call('video.getCatalogSection', **params)
    return parse_response(result)


def getComments(owner_id=None, video_id=None, need_likes=None, start_comment_id=None,\
                offset=None, count=None, sort=None, extended=None):
    """
    Returns a list of comments on a video.
    https://vk.com/dev/video.getComments
    """
    params = {
        'owner_id': owner_id,
        'video_id': video_id,
        'need_likes': need_likes,
        'start_comment_id': start_comment_id,
        'offset': offset,
        'count': count,
        'sort': sort,
        'extended': extended
    }
    result = call('video.getComments', **params)
    return parse_response(result)


def getNewTags(offset=None, count=None):
    """
    Returns a list of videos with tags that have not been
    viewed.
    https://vk.com/dev/video.getNewTags
    """
    params = {
        'offset': offset,
        'count': count
    }
    result = call('video.getNewTags', **params)
    return parse_response(result)


def getTags(owner_id=None, video_id=None):
    """
    Returns a list of tags on a video.
    https://vk.com/dev/video.getTags
    """
    params = {
        'owner_id': owner_id,
        'video_id': video_id
    }
    result = call('video.getTags', **params)
    return parse_response(result)


def getUserVideos(user_id=None, offset=None, count=None, extended=None):
    """
    Returns list of videos in which the user is tagged.
    https://vk.com/dev/video.getUserVideos
    """
    params = {
        'user_id': user_id,
        'offset': offset,
        'count': count,
        'extended': extended
    }
    result = call('video.getUserVideos', **params)
    return parse_response(result)


def hideCatalogSection(section_id=None):
    """
    Hides a video catalog section from a user.
    https://vk.com/dev/video.hideCatalogSection
    """
    params = {
        'section_id': section_id
    }
    result = call('video.hideCatalogSection', **params)
    return parse_response(result)


def putTag(user_id=None, owner_id=None, video_id=None, tagged_name=None):
    """
    Adds a tag on a video.
    https://vk.com/dev/video.putTag
    """
    params = {
        'user_id': user_id,
        'owner_id': owner_id,
        'video_id': video_id,
        'tagged_name': tagged_name
    }
    result = call('video.putTag', **params)
    return parse_response(result)


def removeFromAlbum(target_id=None, album_id=None, album_ids=None, owner_id=None,\
                    video_id=None):
    """
    
    https://vk.com/dev/video.removeFromAlbum
    """
    params = {
        'target_id': target_id,
        'album_id': album_id,
        'album_ids': album_ids,
        'owner_id': owner_id,
        'video_id': video_id
    }
    result = call('video.removeFromAlbum', **params)
    return parse_response(result)


def removeTag(tag_id=None, owner_id=None, video_id=None):
    """
    Removes a tag from a video.
    https://vk.com/dev/video.removeTag
    """
    params = {
        'tag_id': tag_id,
        'owner_id': owner_id,
        'video_id': video_id
    }
    result = call('video.removeTag', **params)
    return parse_response(result)


def reorderAlbums(owner_id=None, album_id=None, before=None, after=None):
    """
    Reorders the album in the list of user video albums.
    https://vk.com/dev/video.reorderAlbums
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'before': before,
        'after': after
    }
    result = call('video.reorderAlbums', **params)
    return parse_response(result)


def reorderVideos(target_id=None, album_id=None, owner_id=None, video_id=None,\
                  before_owner_id=None, before_video_id=None, after_owner_id=None,\
                  after_video_id=None):
    """
    Reorders the video in the video album.
    https://vk.com/dev/video.reorderVideos
    """
    params = {
        'target_id': target_id,
        'album_id': album_id,
        'owner_id': owner_id,
        'video_id': video_id,
        'before_owner_id': before_owner_id,
        'before_video_id': before_video_id,
        'after_owner_id': after_owner_id,
        'after_video_id': after_video_id
    }
    result = call('video.reorderVideos', **params)
    return parse_response(result)


def report(owner_id=None, video_id=None, reason=None, comment=None, search_query=None):
    """
    Reports (submits a complaint about) a video.
    https://vk.com/dev/video.report
    """
    params = {
        'owner_id': owner_id,
        'video_id': video_id,
        'reason': reason,
        'comment': comment,
        'search_query': search_query
    }
    result = call('video.report', **params)
    return parse_response(result)


def reportComment(owner_id=None, comment_id=None, reason=None):
    """
    Reports (submits a complaint about) a comment on a video.
    
    https://vk.com/dev/video.reportComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id,
        'reason': reason
    }
    result = call('video.reportComment', **params)
    return parse_response(result)


def restore(video_id=None, owner_id=None):
    """
    Restores a previously deleted video.
    https://vk.com/dev/video.restore
    """
    params = {
        'video_id': video_id,
        'owner_id': owner_id
    }
    result = call('video.restore', **params)
    return parse_response(result)


def restoreComment(owner_id=None, comment_id=None):
    """
    Restores a previously deleted comment on a video.
    https://vk.com/dev/video.restoreComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id
    }
    result = call('video.restoreComment', **params)
    return parse_response(result)


def save(name=None, description=None, is_private=None, wallpost=None, link=None,\
         group_id=None, album_id=None, privacy_view=None, privacy_comment=None,\
         no_comments=None, repeat=None):
    """
    Returns a server address (required for upload) and video
    data.
    https://vk.com/dev/video.save
    """
    params = {
        'name': name,
        'description': description,
        'is_private': is_private,
        'wallpost': wallpost,
        'link': link,
        'group_id': group_id,
        'album_id': album_id,
        'privacy_view': privacy_view,
        'privacy_comment': privacy_comment,
        'no_comments': no_comments,
        'repeat': repeat
    }
    result = call('video.save', **params)
    return parse_response(result)


def search(q=None, sort=None, hd=None, adult=None, filters=None, search_own=None,\
           offset=None, longer=None, shorter=None, count=None, extended=None):
    """
    Returns a list of videos under the set search criterion.
    https://vk.com/dev/video.search
    """
    params = {
        'q': q,
        'sort': sort,
        'hd': hd,
        'adult': adult,
        'filters': filters,
        'search_own': search_own,
        'offset': offset,
        'longer': longer,
        'shorter': shorter,
        'count': count,
        'extended': extended
    }
    result = call('video.search', **params)
    return parse_response(result)


