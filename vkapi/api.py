import requests

__all__ = ['VKError', 'call', 'parse_response', 'Config']


# Public utils and helpers
class VKError(Exception):
    pass

def parse_response(response):
    try:
        return response['response']
    except KeyError:
        print(VKError(response['error']['error_msg']))

class Config:
    token = None
    version = '5.74'


def call(method, **params):
    url = __prefix + method
    params = {k: __str(v) for k,v in params.items() if v != None}
    if Config.token:
        params['access_token'] = Config.token
    if Config.version:
        params['v'] = Config.version 
    request = requests.get(url, params=params)
    return request.json()


# Private utils and helpers
__prefix = 'https://api.vk.com/method/'


def __str(obj):
    if isinstance(obj, list or tuple):
        str_values = (str(val) for val in obj)
        return (',').join(str_values)
    return str(obj)





