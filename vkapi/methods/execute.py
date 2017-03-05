from ..api import call, parse_response


def execute(code=None):
    """
    A universal method for calling a sequence of other methods
    while saving and filtering interim results.
    https://vk.com/dev/execute
    """
    params = {
        'code': code
    }
    result = call('execute', **params)
    return parse_response(result)


