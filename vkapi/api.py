import requests

__all__ = ['VKError', 'call', 'parse_response', 'AccessToken']


# Public utils and helpers
class VKError(Exception):
    pass

def parse_response(response):
    try:
        return response['response']
    except KeyError:
        print(VKError(response['error']['error_msg']))

class AccessToken:
    token = None


# Public general methods
ACCESS_TOKEN = None

def call(method, **params):
    url = __prefix + method
    params = {k: __str(v) for k,v in params.items()}
    if AccessToken.token:
        # print("here is the token")
        params['access_token'] = AccessToken.token
    # print(params)
    request = requests.get(url, params=params)
    return request.json()


# Private utils and helpers
__prefix = 'https://api.vk.com/method/'


def __str(obj):
    if isinstance(obj, list or tuple):
        str_values = (str(val) for val in obj)
        return (',').join(str_values)
    return str(obj)





