# Secure methods
from ..api import call, parse_response


def addAppEvent(user_id=None, activity_id=None, value=None):
    """
    Adds user activity information to an application
    https://vk.com/dev/secure.addAppEvent
    """
    params = {
        'user_id': user_id,
        'activity_id': activity_id,
        'value': value
    }
    result = call('secure.addAppEvent', **params)
    return parse_response(result)


def checkToken(token=None, ip=None):
    """
    Checks the user authentification in 
    https://vk.com/dev/secure.checkToken
    """
    params = {
        'token': token,
        'ip': ip
    }
    result = call('secure.checkToken', **params)
    return parse_response(result)


def getAppBalance():
    """
    Returns payment balance of the application in hundredth
    of a vote.
    https://vk.com/dev/secure.getAppBalance
    """
    params = {
    }
    result = call('secure.getAppBalance', **params)
    return parse_response(result)


def getSMSHistory(user_id=None, date_from=None, date_to=None, limit=None):
    """
    Shows a list of SMS notifications sent by the application
    using secure.sendSMSNotification method.
    https://vk.com/dev/secure.getSMSHistory
    """
    params = {
        'user_id': user_id,
        'date_from': date_from,
        'date_to': date_to,
        'limit': limit
    }
    result = call('secure.getSMSHistory', **params)
    return parse_response(result)


def getTransactionsHistory():
    """
    Shows history of votes transaction between users and
    the application.
    https://vk.com/dev/secure.getTransactionsHistory
    """
    params = {
    }
    result = call('secure.getTransactionsHistory', **params)
    return parse_response(result)


def getUserLevel(user_ids=None):
    """
    Returns one of the previously set game levels of one
    or more users in the application.
    https://vk.com/dev/secure.getUserLevel
    """
    params = {
        'user_ids': user_ids
    }
    result = call('secure.getUserLevel', **params)
    return parse_response(result)


def sendNotification(user_ids=None, user_id=None, message=None):
    """
    Sends notification to the user.
    https://vk.com/dev/secure.sendNotification
    """
    params = {
        'user_ids': user_ids,
        'user_id': user_id,
        'message': message
    }
    result = call('secure.sendNotification', **params)
    return parse_response(result)


def sendSMSNotification(user_id=None, message=None):
    """
    Sends 
    https://vk.com/dev/secure.sendSMSNotification
    """
    params = {
        'user_id': user_id,
        'message': message
    }
    result = call('secure.sendSMSNotification', **params)
    return parse_response(result)


def setCounter(counters=None, user_id=None, counter=None):
    """
    Sets a counter which is shown to the user in bold in
    the left menu.
    https://vk.com/dev/secure.setCounter
    """
    params = {
        'counters': counters,
        'user_id': user_id,
        'counter': counter
    }
    result = call('secure.setCounter', **params)
    return parse_response(result)


def setUserLevel(levels=None, user_id=None, level=None):
    """
    Sets user game level in the application which can be
    seen by his/her friends.
    https://vk.com/dev/secure.setUserLevel
    """
    params = {
        'levels': levels,
        'user_id': user_id,
        'level': level
    }
    result = call('secure.setUserLevel', **params)
    return parse_response(result)


