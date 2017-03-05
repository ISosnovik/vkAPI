# Photos methods
from ..api import call, parse_response


def confirmTag(owner_id=None, photo_id=None, tag_id=None):
    """
    Confirms a tag on a photo.
    https://vk.com/dev/photos.confirmTag
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'tag_id': tag_id
    }
    result = call('photos.confirmTag', **params)
    return parse_response(result)


def copy(owner_id=None, photo_id=None, access_key=None):
    """
    Allows to copy a photo to the "Saved photos" album
    https://vk.com/dev/photos.copy
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'access_key': access_key
    }
    result = call('photos.copy', **params)
    return parse_response(result)


def createAlbum(title=None, group_id=None, description=None, privacy_view=None,\
                privacy_comment=None, upload_by_admins_only=None, comments_disabled=None,\
                privacy=None, comment_privacy=None):
    """
    Creates an empty photo album.
    https://vk.com/dev/photos.createAlbum
    """
    params = {
        'title': title,
        'group_id': group_id,
        'description': description,
        'privacy_view': privacy_view,
        'privacy_comment': privacy_comment,
        'upload_by_admins_only': upload_by_admins_only,
        'comments_disabled': comments_disabled,
        'privacy': privacy,
        'comment_privacy': comment_privacy
    }
    result = call('photos.createAlbum', **params)
    return parse_response(result)


def createComment(owner_id=None, photo_id=None, message=None, attachments=None,\
                  from_group=None, reply_to_comment=None, sticker_id=None,\
                  access_key=None, guid=None):
    """
    Adds a new comment on the photo.
    https://vk.com/dev/photos.createComment
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'message': message,
        'attachments': attachments,
        'from_group': from_group,
        'reply_to_comment': reply_to_comment,
        'sticker_id': sticker_id,
        'access_key': access_key,
        'guid': guid
    }
    result = call('photos.createComment', **params)
    return parse_response(result)


def delete(owner_id=None, photo_id=None):
    """
    Deletes a photo.
    https://vk.com/dev/photos.delete
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id
    }
    result = call('photos.delete', **params)
    return parse_response(result)


def deleteAlbum(album_id=None, group_id=None):
    """
    Deletes a photo album belonging to the current user.
    https://vk.com/dev/photos.deleteAlbum
    """
    params = {
        'album_id': album_id,
        'group_id': group_id
    }
    result = call('photos.deleteAlbum', **params)
    return parse_response(result)


def deleteComment(owner_id=None, comment_id=None):
    """
    Deletes a comment on the photo.
    https://vk.com/dev/photos.deleteComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id
    }
    result = call('photos.deleteComment', **params)
    return parse_response(result)


def edit(owner_id=None, photo_id=None, caption=None, latitude=None, longitude=None,\
         place_str=None, foursquare_id=None, delete_place=None):
    """
    Edits the caption of a photo.
    https://vk.com/dev/photos.edit
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'caption': caption,
        'latitude': latitude,
        'longitude': longitude,
        'place_str': place_str,
        'foursquare_id': foursquare_id,
        'delete_place': delete_place
    }
    result = call('photos.edit', **params)
    return parse_response(result)


def editAlbum(album_id=None, title=None, description=None, owner_id=None,\
              privacy_view=None, privacy_comment=None, upload_by_admins_only=None,\
              comments_disabled=None, privacy=None, comment_privacy=None):
    """
    Edits information about a photo album.
    https://vk.com/dev/photos.editAlbum
    """
    params = {
        'album_id': album_id,
        'title': title,
        'description': description,
        'owner_id': owner_id,
        'privacy_view': privacy_view,
        'privacy_comment': privacy_comment,
        'upload_by_admins_only': upload_by_admins_only,
        'comments_disabled': comments_disabled,
        'privacy': privacy,
        'comment_privacy': comment_privacy
    }
    result = call('photos.editAlbum', **params)
    return parse_response(result)


def editComment(owner_id=None, comment_id=None, message=None, attachments=None):
    """
    Edits a comment on a photo.
    https://vk.com/dev/photos.editComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id,
        'message': message,
        'attachments': attachments
    }
    result = call('photos.editComment', **params)
    return parse_response(result)


def get(owner_id=None, album_id=None, photo_ids=None, rev=None, extended=None,\
        feed_type=None, feed=None, photo_sizes=None, offset=None, count=None):
    """
    Returns a list of a user's or community's photos.
    https://vk.com/dev/photos.get
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'photo_ids': photo_ids,
        'rev': rev,
        'extended': extended,
        'feed_type': feed_type,
        'feed': feed,
        'photo_sizes': photo_sizes,
        'offset': offset,
        'count': count
    }
    result = call('photos.get', **params)
    return parse_response(result)


def getAlbums(owner_id=None, album_ids=None, offset=None, count=None, need_system=None,\
              need_covers=None, photo_sizes=None):
    """
    Returns a list of a user's or community's photo albums.
    https://vk.com/dev/photos.getAlbums
    """
    params = {
        'owner_id': owner_id,
        'album_ids': album_ids,
        'offset': offset,
        'count': count,
        'need_system': need_system,
        'need_covers': need_covers,
        'photo_sizes': photo_sizes
    }
    result = call('photos.getAlbums', **params)
    return parse_response(result)


def getAlbumsCount(user_id=None, group_id=None):
    """
    Returns the number of photo albums belonging to a user
    or community.
    https://vk.com/dev/photos.getAlbumsCount
    """
    params = {
        'user_id': user_id,
        'group_id': group_id
    }
    result = call('photos.getAlbumsCount', **params)
    return parse_response(result)


def getAll(owner_id=None, extended=None, offset=None, count=None, photo_sizes=None,\
           no_service_albums=None, need_hidden=None, skip_hidden=None):
    """
    Returns a list of photos belonging to a user or community,
    in reverse chronological order.
    https://vk.com/dev/photos.getAll
    """
    params = {
        'owner_id': owner_id,
        'extended': extended,
        'offset': offset,
        'count': count,
        'photo_sizes': photo_sizes,
        'no_service_albums': no_service_albums,
        'need_hidden': need_hidden,
        'skip_hidden': skip_hidden
    }
    result = call('photos.getAll', **params)
    return parse_response(result)


def getAllComments(owner_id=None, album_id=None, need_likes=None, offset=None,\
                   count=None):
    """
    Returns a list of comments on a specific photo album
    or all albums of the user sorted in reverse chronological
    order.
    https://vk.com/dev/photos.getAllComments
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'need_likes': need_likes,
        'offset': offset,
        'count': count
    }
    result = call('photos.getAllComments', **params)
    return parse_response(result)


def getById(photos=None, extended=None, photo_sizes=None):
    """
    Returns information about photos by their IDs.
    https://vk.com/dev/photos.getById
    """
    params = {
        'photos': photos,
        'extended': extended,
        'photo_sizes': photo_sizes
    }
    result = call('photos.getById', **params)
    return parse_response(result)


def getChatUploadServer(chat_id=None, crop_x=None, crop_y=None, crop_width=None):
    """
    Returns an upload link for chat cover pictures.
    https://vk.com/dev/photos.getChatUploadServer
    """
    params = {
        'chat_id': chat_id,
        'crop_x': crop_x,
        'crop_y': crop_y,
        'crop_width': crop_width
    }
    result = call('photos.getChatUploadServer', **params)
    return parse_response(result)


def getComments(owner_id=None, photo_id=None, need_likes=None, start_comment_id=None,\
                offset=None, count=None, sort=None, access_key=None, extended=None,\
                fields=None, skip_before_id=None, skip_after_id=None):
    """
    Returns a list of comments on a photo.
    https://vk.com/dev/photos.getComments
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'need_likes': need_likes,
        'start_comment_id': start_comment_id,
        'offset': offset,
        'count': count,
        'sort': sort,
        'access_key': access_key,
        'extended': extended,
        'fields': fields,
        'skip_before_id': skip_before_id,
        'skip_after_id': skip_after_id
    }
    result = call('photos.getComments', **params)
    return parse_response(result)


def getMarketAlbumUploadServer(group_id=None):
    """
    Returns the server address for market album photo upload.
    https://vk.com/dev/photos.getMarketAlbumUploadServer
    """
    params = {
        'group_id': group_id
    }
    result = call('photos.getMarketAlbumUploadServer', **params)
    return parse_response(result)


def getMarketUploadServer(group_id=None, main_photo=None, crop_x=None, crop_y=None,\
                          crop_width=None):
    """
    Returns the server address for market photo upload.
    https://vk.com/dev/photos.getMarketUploadServer
    """
    params = {
        'group_id': group_id,
        'main_photo': main_photo,
        'crop_x': crop_x,
        'crop_y': crop_y,
        'crop_width': crop_width
    }
    result = call('photos.getMarketUploadServer', **params)
    return parse_response(result)


def getMessagesUploadServer():
    """
    Returns the server address for photo upload in a private
    message for a user.
    https://vk.com/dev/photos.getMessagesUploadServer
    """
    params = {
    }
    result = call('photos.getMessagesUploadServer', **params)
    return parse_response(result)


def getNewTags(offset=None, count=None):
    """
    Returns a list of photos with tags that have not been
    viewed.
    https://vk.com/dev/photos.getNewTags
    """
    params = {
        'offset': offset,
        'count': count
    }
    result = call('photos.getNewTags', **params)
    return parse_response(result)


def getOwnerPhotoUploadServer(owner_id=None):
    """
    Returns an upload server address for a profile or community
    photo.
    https://vk.com/dev/photos.getOwnerPhotoUploadServer
    """
    params = {
        'owner_id': owner_id
    }
    result = call('photos.getOwnerPhotoUploadServer', **params)
    return parse_response(result)


def getTags(owner_id=None, photo_id=None, access_key=None):
    """
    Returns a list of tags on a photo.
    https://vk.com/dev/photos.getTags
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'access_key': access_key
    }
    result = call('photos.getTags', **params)
    return parse_response(result)


def getUploadServer(album_id=None, group_id=None):
    """
    Returns the server address for photo upload.
    https://vk.com/dev/photos.getUploadServer
    """
    params = {
        'album_id': album_id,
        'group_id': group_id
    }
    result = call('photos.getUploadServer', **params)
    return parse_response(result)


def getUserPhotos(user_id=None, offset=None, count=None, extended=None,\
                  sort=None):
    """
    Returns a list of photos in which a user is tagged.
    https://vk.com/dev/photos.getUserPhotos
    """
    params = {
        'user_id': user_id,
        'offset': offset,
        'count': count,
        'extended': extended,
        'sort': sort
    }
    result = call('photos.getUserPhotos', **params)
    return parse_response(result)


def getWallUploadServer(group_id=None):
    """
    Returns the server address for photo upload onto a user's
    wall.
    https://vk.com/dev/photos.getWallUploadServer
    """
    params = {
        'group_id': group_id
    }
    result = call('photos.getWallUploadServer', **params)
    return parse_response(result)


def makeCover(owner_id=None, photo_id=None, album_id=None):
    """
    Makes a photo into an album cover.
    https://vk.com/dev/photos.makeCover
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'album_id': album_id
    }
    result = call('photos.makeCover', **params)
    return parse_response(result)


def move(owner_id=None, target_album_id=None, photo_id=None):
    """
    Moves a photo from one album to another.
    https://vk.com/dev/photos.move
    """
    params = {
        'owner_id': owner_id,
        'target_album_id': target_album_id,
        'photo_id': photo_id
    }
    result = call('photos.move', **params)
    return parse_response(result)


def putTag(owner_id=None, photo_id=None, user_id=None, x=None, y=None, x2=None,\
           y2=None):
    """
    Adds a tag on the photo.
    https://vk.com/dev/photos.putTag
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'user_id': user_id,
        'x': x,
        'y': y,
        'x2': x2,
        'y2': y2
    }
    result = call('photos.putTag', **params)
    return parse_response(result)


def removeTag(owner_id=None, photo_id=None, tag_id=None):
    """
    Removes a tag from a photo.
    https://vk.com/dev/photos.removeTag
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'tag_id': tag_id
    }
    result = call('photos.removeTag', **params)
    return parse_response(result)


def reorderAlbums(owner_id=None, album_id=None, before=None, after=None):
    """
    Reorders the album in the list of user albums.
    https://vk.com/dev/photos.reorderAlbums
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'before': before,
        'after': after
    }
    result = call('photos.reorderAlbums', **params)
    return parse_response(result)


def reorderPhotos(owner_id=None, photo_id=None, before=None, after=None):
    """
    Reorders the photo in the list of photos of the user
    album.
    https://vk.com/dev/photos.reorderPhotos
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'before': before,
        'after': after
    }
    result = call('photos.reorderPhotos', **params)
    return parse_response(result)


def report(owner_id=None, photo_id=None, reason=None):
    """
    Reports (submits a complaint about) a photo. 
    https://vk.com/dev/photos.report
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id,
        'reason': reason
    }
    result = call('photos.report', **params)
    return parse_response(result)


def reportComment(owner_id=None, comment_id=None, reason=None):
    """
    Reports (submits a complaint about) a comment on a photo.
    
    https://vk.com/dev/photos.reportComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id,
        'reason': reason
    }
    result = call('photos.reportComment', **params)
    return parse_response(result)


def restore(owner_id=None, photo_id=None):
    """
    Restores a deleted photo.
    https://vk.com/dev/photos.restore
    """
    params = {
        'owner_id': owner_id,
        'photo_id': photo_id
    }
    result = call('photos.restore', **params)
    return parse_response(result)


def restoreComment(owner_id=None, comment_id=None):
    """
    Restores a deleted comment on a photo.
    https://vk.com/dev/photos.restoreComment
    """
    params = {
        'owner_id': owner_id,
        'comment_id': comment_id
    }
    result = call('photos.restoreComment', **params)
    return parse_response(result)


def save(album_id=None, group_id=None, server=None, photos_list=None, hash=None,\
         latitude=None, longitude=None, caption=None):
    """
    Saves photos after successful uploading.
    https://vk.com/dev/photos.save
    """
    params = {
        'album_id': album_id,
        'group_id': group_id,
        'server': server,
        'photos_list': photos_list,
        'hash': hash,
        'latitude': latitude,
        'longitude': longitude,
        'caption': caption
    }
    result = call('photos.save', **params)
    return parse_response(result)


def saveMarketAlbumPhoto(group_id=None, photo=None, server=None, hash=None):
    """
    Saves market album photos after successful uploading.
    https://vk.com/dev/photos.saveMarketAlbumPhoto
    """
    params = {
        'group_id': group_id,
        'photo': photo,
        'server': server,
        'hash': hash
    }
    result = call('photos.saveMarketAlbumPhoto', **params)
    return parse_response(result)


def saveMarketPhoto(group_id=None, photo=None, server=None, hash=None, crop_data=None,\
                    crop_hash=None):
    """
    Saves market photos after successful uploading.
    https://vk.com/dev/photos.saveMarketPhoto
    """
    params = {
        'group_id': group_id,
        'photo': photo,
        'server': server,
        'hash': hash,
        'crop_data': crop_data,
        'crop_hash': crop_hash
    }
    result = call('photos.saveMarketPhoto', **params)
    return parse_response(result)


def saveMessagesPhoto(photo=None, server=None, hash=None):
    """
    Saves a photo after being successfully uploaded. URL
    obtained with photos.getMessagesUploadServer method.
    https://vk.com/dev/photos.saveMessagesPhoto
    """
    params = {
        'photo': photo,
        'server': server,
        'hash': hash
    }
    result = call('photos.saveMessagesPhoto', **params)
    return parse_response(result)


def saveOwnerPhoto(server=None, hash=None, photo=None):
    """
    Saves  a profile or community photo.
    https://vk.com/dev/photos.saveOwnerPhoto
    """
    params = {
        'server': server,
        'hash': hash,
        'photo': photo
    }
    result = call('photos.saveOwnerPhoto', **params)
    return parse_response(result)


def saveWallPhoto(user_id=None, group_id=None, photo=None, server=None,\
                  hash=None, latitude=None, longitude=None, caption=None):
    """
    Saves a photo to a user's or community's wall after
    being uploaded.
    https://vk.com/dev/photos.saveWallPhoto
    """
    params = {
        'user_id': user_id,
        'group_id': group_id,
        'photo': photo,
        'server': server,
        'hash': hash,
        'latitude': latitude,
        'longitude': longitude,
        'caption': caption
    }
    result = call('photos.saveWallPhoto', **params)
    return parse_response(result)


def search(q=None, lat=None, long=None, start_time=None, end_time=None,\
           sort=None, offset=None, count=None, radius=None):
    """
    Returns a list of photos.
    https://vk.com/dev/photos.search
    """
    params = {
        'q': q,
        'lat': lat,
        'long': long,
        'start_time': start_time,
        'end_time': end_time,
        'sort': sort,
        'offset': offset,
        'count': count,
        'radius': radius
    }
    result = call('photos.search', **params)
    return parse_response(result)


