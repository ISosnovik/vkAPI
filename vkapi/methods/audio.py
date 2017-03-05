# Audio methods
from ..api import call, parse_response


def add(audio_id=None, owner_id=None, group_id=None, album_id=None):
    """
    Copies an audio file to a user page or community page.
    https://vk.com/dev/audio.add
    """
    params = {
        'audio_id': audio_id,
        'owner_id': owner_id,
        'group_id': group_id,
        'album_id': album_id
    }
    result = call('audio.add', **params)
    return parse_response(result)


def addAlbum(group_id=None, title=None):
    """
    Creates an empty audio album.
    https://vk.com/dev/audio.addAlbum
    """
    params = {
        'group_id': group_id,
        'title': title
    }
    result = call('audio.addAlbum', **params)
    return parse_response(result)


def delete(audio_id=None, owner_id=None):
    """
    Deletes an audio file from a user page or community
    page.
    https://vk.com/dev/audio.delete
    """
    params = {
        'audio_id': audio_id,
        'owner_id': owner_id
    }
    result = call('audio.delete', **params)
    return parse_response(result)


def deleteAlbum(group_id=None, album_id=None):
    """
    Deletes an audio album.
    https://vk.com/dev/audio.deleteAlbum
    """
    params = {
        'group_id': group_id,
        'album_id': album_id
    }
    result = call('audio.deleteAlbum', **params)
    return parse_response(result)


def edit(owner_id=None, audio_id=None, artist=None, title=None, text=None,\
         genre_id=None, no_search=None):
    """
    Edits an audio file on a user or community page.
    https://vk.com/dev/audio.edit
    """
    params = {
        'owner_id': owner_id,
        'audio_id': audio_id,
        'artist': artist,
        'title': title,
        'text': text,
        'genre_id': genre_id,
        'no_search': no_search
    }
    result = call('audio.edit', **params)
    return parse_response(result)


def editAlbum(group_id=None, album_id=None, title=None):
    """
    Edits the title of an audio album.
    https://vk.com/dev/audio.editAlbum
    """
    params = {
        'group_id': group_id,
        'album_id': album_id,
        'title': title
    }
    result = call('audio.editAlbum', **params)
    return parse_response(result)


def get(owner_id=None, album_id=None, audio_ids=None, need_user=None, offset=None,\
        count=None):
    """
    Returns a list of audio files of a user or community.
    https://vk.com/dev/audio.get
    """
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'audio_ids': audio_ids,
        'need_user': need_user,
        'offset': offset,
        'count': count
    }
    result = call('audio.get', **params)
    return parse_response(result)


def getAlbums(owner_id=None, offset=None, count=None):
    """
    Returns a list of audio albums of a user or community.
    https://vk.com/dev/audio.getAlbums
    """
    params = {
        'owner_id': owner_id,
        'offset': offset,
        'count': count
    }
    result = call('audio.getAlbums', **params)
    return parse_response(result)


def getBroadcastList(filter=None, active=None):
    """
    Returns a list of the user's friends and communities
    that are broadcasting music in their statuses.
    https://vk.com/dev/audio.getBroadcastList
    """
    params = {
        'filter': filter,
        'active': active
    }
    result = call('audio.getBroadcastList', **params)
    return parse_response(result)


def getById(audios=None):
    """
    Returns information about audio files by their IDs.
    https://vk.com/dev/audio.getById
    """
    params = {
        'audios': audios
    }
    result = call('audio.getById', **params)
    return parse_response(result)


def getCount(owner_id=None):
    """
    Returns the total number of audio files on a user or
    community page.
    https://vk.com/dev/audio.getCount
    """
    params = {
        'owner_id': owner_id
    }
    result = call('audio.getCount', **params)
    return parse_response(result)


def getLyrics(lyrics_id=None):
    """
    Returns lyrics associated with an audio file.
    https://vk.com/dev/audio.getLyrics
    """
    params = {
        'lyrics_id': lyrics_id
    }
    result = call('audio.getLyrics', **params)
    return parse_response(result)


def getPopular(only_eng=None, genre_id=None, offset=None, count=None):
    """
    Returns a list of audio files from the "Popular".
    https://vk.com/dev/audio.getPopular
    """
    params = {
        'only_eng': only_eng,
        'genre_id': genre_id,
        'offset': offset,
        'count': count
    }
    result = call('audio.getPopular', **params)
    return parse_response(result)


def getRecommendations(target_audio=None, user_id=None, offset=None, count=None,\
                       shuffle=None):
    """
    Returns a list of suggested audio files based on a user's
    playlist or a particular audio file.
    https://vk.com/dev/audio.getRecommendations
    """
    params = {
        'target_audio': target_audio,
        'user_id': user_id,
        'offset': offset,
        'count': count,
        'shuffle': shuffle
    }
    result = call('audio.getRecommendations', **params)
    return parse_response(result)


def getUploadServer():
    """
    Returns the server address to upload audio files.
    https://vk.com/dev/audio.getUploadServer
    """
    params = {
    }
    result = call('audio.getUploadServer', **params)
    return parse_response(result)


def moveToAlbum(group_id=None, album_id=None, audio_ids=None):
    """
    Moves audio files to an album.
    https://vk.com/dev/audio.moveToAlbum
    """
    params = {
        'group_id': group_id,
        'album_id': album_id,
        'audio_ids': audio_ids
    }
    result = call('audio.moveToAlbum', **params)
    return parse_response(result)


def reorder(audio_id=None, owner_id=None, before=None, after=None):
    """
    Reorders an audio file, placing it between other specified
    audio files.
    https://vk.com/dev/audio.reorder
    """
    params = {
        'audio_id': audio_id,
        'owner_id': owner_id,
        'before': before,
        'after': after
    }
    result = call('audio.reorder', **params)
    return parse_response(result)


def restore(audio_id=None, owner_id=None):
    """
    Restores a deleted audio file.
    https://vk.com/dev/audio.restore
    """
    params = {
        'audio_id': audio_id,
        'owner_id': owner_id
    }
    result = call('audio.restore', **params)
    return parse_response(result)


def save(server=None, audio=None, hash=None, artist=None, title=None):
    """
    Saves audio files after successful uploading.
    https://vk.com/dev/audio.save
    """
    params = {
        'server': server,
        'audio': audio,
        'hash': hash,
        'artist': artist,
        'title': title
    }
    result = call('audio.save', **params)
    return parse_response(result)


def search(q=None, auto_complete=None, lyrics=None, performer_only=None,\
           sort=None, search_own=None, offset=None, count=None):
    """
    Returns a list of audio matching the search criteria.
    https://vk.com/dev/audio.search
    """
    params = {
        'q': q,
        'auto_complete': auto_complete,
        'lyrics': lyrics,
        'performer_only': performer_only,
        'sort': sort,
        'search_own': search_own,
        'offset': offset,
        'count': count
    }
    result = call('audio.search', **params)
    return parse_response(result)


def setBroadcast(audio=None, target_ids=None):
    """
    Activates an audio broadcast to the status of a user
    or community.
    https://vk.com/dev/audio.setBroadcast
    """
    params = {
        'audio': audio,
        'target_ids': target_ids
    }
    result = call('audio.setBroadcast', **params)
    return parse_response(result)


