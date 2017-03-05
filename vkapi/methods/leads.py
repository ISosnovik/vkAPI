# Leads methods
from ..api import call, parse_response


def checkUser(lead_id=None, test_result=None, test_mode=None, auto_start=None,\
              age=None, country=None):
    """
    Checks if the user can start the lead.
    https://vk.com/dev/leads.checkUser
    """
    params = {
        'lead_id': lead_id,
        'test_result': test_result,
        'test_mode': test_mode,
        'auto_start': auto_start,
        'age': age,
        'country': country
    }
    result = call('leads.checkUser', **params)
    return parse_response(result)


def complete(vk_sid=None, secret=None, comment=None):
    """
    Completes the lead started by user.
    https://vk.com/dev/leads.complete
    """
    params = {
        'vk_sid': vk_sid,
        'secret': secret,
        'comment': comment
    }
    result = call('leads.complete', **params)
    return parse_response(result)


def getStats(lead_id=None, secret=None, date_start=None, date_end=None):
    """
    Returns lead stats data.
    https://vk.com/dev/leads.getStats
    """
    params = {
        'lead_id': lead_id,
        'secret': secret,
        'date_start': date_start,
        'date_end': date_end
    }
    result = call('leads.getStats', **params)
    return parse_response(result)


def getUsers(offer_id=None, secret=None, offset=None, count=None, status=None,\
             reverse=None):
    """
    Returns a list of last user actions for the offer.
    https://vk.com/dev/leads.getUsers
    """
    params = {
        'offer_id': offer_id,
        'secret': secret,
        'offset': offset,
        'count': count,
        'status': status,
        'reverse': reverse
    }
    result = call('leads.getUsers', **params)
    return parse_response(result)


def metricHit(data=None):
    """
    Counts the metric event.
    https://vk.com/dev/leads.metricHit
    """
    params = {
        'data': data
    }
    result = call('leads.metricHit', **params)
    return parse_response(result)


def start(lead_id=None, secret=None, uid=None, aid=None, test_mode=None,\
          force=None):
    """
    Creates new session for the user passing the offer.
    https://vk.com/dev/leads.start
    """
    params = {
        'lead_id': lead_id,
        'secret': secret,
        'uid': uid,
        'aid': aid,
        'test_mode': test_mode,
        'force': force
    }
    result = call('leads.start', **params)
    return parse_response(result)


