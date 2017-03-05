# Auth methods
from ..api import call, parse_response


def checkPhone(phone=None, client_id=None, client_secret=None, auth_by_phone=None):
    """
    Checks a user's phone number for correctness.
    https://vk.com/dev/auth.checkPhone
    """
    params = {
        'phone': phone,
        'client_id': client_id,
        'client_secret': client_secret,
        'auth_by_phone': auth_by_phone
    }
    result = call('auth.checkPhone', **params)
    return parse_response(result)


def confirm(client_id=None, client_secret=None, phone=None, code=None, password=None,\
            test_mode=None, intro=None):
    """
    Completes a user's registration (begun with theauth.signup
    method) using an authorization code.
    https://vk.com/dev/auth.confirm
    """
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'phone': phone,
        'code': code,
        'password': password,
        'test_mode': test_mode,
        'intro': intro
    }
    result = call('auth.confirm', **params)
    return parse_response(result)


def restore(phone=None):
    """
    Allows to restore account access using a code received
    via SMS. 
    https://vk.com/dev/auth.restore
    """
    params = {
        'phone': phone
    }
    result = call('auth.restore', **params)
    return parse_response(result)


def signup(first_name=None, last_name=None, client_id=None, client_secret=None,\
           phone=None, password=None, test_mode=None, voice=None, sex=None,\
           sid=None):
    """
    Registers a new user by phone number.
    https://vk.com/dev/auth.signup
    """
    params = {
        'first_name': first_name,
        'last_name': last_name,
        'client_id': client_id,
        'client_secret': client_secret,
        'phone': phone,
        'password': password,
        'test_mode': test_mode,
        'voice': voice,
        'sex': sex,
        'sid': sid
    }
    result = call('auth.signup', **params)
    return parse_response(result)


