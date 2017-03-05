# Widgets methods
from ..api import call, parse_response


def getComments(widget_api_id=None, url=None, page_id=None, order=None,\
                fields=None, offset=None, count=None):
    """
    Gets a list of comments for the page added through the
    Comments widget.
    https://vk.com/dev/widgets.getComments
    """
    params = {
        'widget_api_id': widget_api_id,
        'url': url,
        'page_id': page_id,
        'order': order,
        'fields': fields,
        'offset': offset,
        'count': count
    }
    result = call('widgets.getComments', **params)
    return parse_response(result)


def getPages(widget_api_id=None, order=None, period=None, offset=None, count=None):
    """
    Gets a list of application/site pages where the Comments
    widget or Like widget is installed.
    https://vk.com/dev/widgets.getPages
    """
    params = {
        'widget_api_id': widget_api_id,
        'order': order,
        'period': period,
        'offset': offset,
        'count': count
    }
    result = call('widgets.getPages', **params)
    return parse_response(result)


