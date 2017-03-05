# Pages methods
from ..api import call, parse_response


def clearCache(url=None):
    """
    Allows to clear the cache of particular 
    https://vk.com/dev/pages.clearCache
    """
    params = {
        'url': url
    }
    result = call('pages.clearCache', **params)
    return parse_response(result)


def get(owner_id=None, page_id=None, global_=None, site_preview=None, title=None,\
        need_source=None, need_html=None):
    """
    Returns information about a wiki page.
    https://vk.com/dev/pages.get
    """
    params = {
        'owner_id': owner_id,
        'page_id': page_id,
        'global_': global_,
        'site_preview': site_preview,
        'title': title,
        'need_source': need_source,
        'need_html': need_html
    }
    result = call('pages.get', **params)
    return parse_response(result)


def getHistory(page_id=None, group_id=None, user_id=None):
    """
    Returns a list of all previous versions of a wiki page.
    https://vk.com/dev/pages.getHistory
    """
    params = {
        'page_id': page_id,
        'group_id': group_id,
        'user_id': user_id
    }
    result = call('pages.getHistory', **params)
    return parse_response(result)


def getTitles(group_id=None):
    """
    Returns a list of wiki pages in a group.
    https://vk.com/dev/pages.getTitles
    """
    params = {
        'group_id': group_id
    }
    result = call('pages.getTitles', **params)
    return parse_response(result)


def getVersion(version_id=None, group_id=None, user_id=None, need_html=None):
    """
    Returns the text of one of the previous versions of
    a wiki page.
    https://vk.com/dev/pages.getVersion
    """
    params = {
        'version_id': version_id,
        'group_id': group_id,
        'user_id': user_id,
        'need_html': need_html
    }
    result = call('pages.getVersion', **params)
    return parse_response(result)


def parseWiki(text=None, group_id=None):
    """
    Returns HTML representation of the wiki markup.
    https://vk.com/dev/pages.parseWiki
    """
    params = {
        'text': text,
        'group_id': group_id
    }
    result = call('pages.parseWiki', **params)
    return parse_response(result)


def save(text=None, page_id=None, group_id=None, user_id=None, title=None):
    """
    Saves the text of a wiki page.
    https://vk.com/dev/pages.save
    """
    params = {
        'text': text,
        'page_id': page_id,
        'group_id': group_id,
        'user_id': user_id,
        'title': title
    }
    result = call('pages.save', **params)
    return parse_response(result)


def saveAccess(page_id=None, group_id=None, user_id=None, view=None, edit=None):
    """
    Saves modified read and edit access settings for a wiki
    page.
    https://vk.com/dev/pages.saveAccess
    """
    params = {
        'page_id': page_id,
        'group_id': group_id,
        'user_id': user_id,
        'view': view,
        'edit': edit
    }
    result = call('pages.saveAccess', **params)
    return parse_response(result)


