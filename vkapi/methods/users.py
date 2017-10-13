# Users methods
from ..api import call, parse_response


def get(user_ids=None, fields=None, name_case=None):
    """
    Returns detailed information on users.
    https://vk.com/dev/users.get
    """
    params = {
        'user_ids': user_ids,
        'fields': fields,
        'name_case': name_case
    }
    result = call('users.get', **params)
    return parse_response(result)


def getFollowers(user_id=None, offset=None, count=None, fields=None, name_case=None):
    """
    Returns a list of IDs of followers of the user in question,
    sorted by date added, most recent first.
    https://vk.com/dev/users.getFollowers
    """
    params = {
        'user_id': user_id,
        'offset': offset,
        'count': count,
        'fields': fields,
        'name_case': name_case
    }
    result = call('users.getFollowers', **params)
    return parse_response(result)


def getNearby(latitude=None, longitude=None, accuracy=None, timeout=None,\
              radius=None, fields=None, name_case=None):
    """
    Indexes current user location and returns nearby users.
    https://vk.com/dev/users.getNearby
    """
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'accuracy': accuracy,
        'timeout': timeout,
        'radius': radius,
        'fields': fields,
        'name_case': name_case
    }
    result = call('users.getNearby', **params)
    return parse_response(result)


def getSubscriptions(user_id=None, extended=None, offset=None, count=None,\
                     fields=None):
    """
    Returns a list of IDs of users and communities followed
    by the user.
    https://vk.com/dev/users.getSubscriptions
    """
    params = {
        'user_id': user_id,
        'extended': extended,
        'offset': offset,
        'count': count,
        'fields': fields
    }
    result = call('users.getSubscriptions', **params)
    return parse_response(result)


def isAppUser(user_id=None):
    """
    Returns information whether a user installed the application.
    https://vk.com/dev/users.isAppUser
    """
    params = {
        'user_id': user_id
    }
    result = call('users.isAppUser', **params)
    return parse_response(result)


def report(user_id=None, type=None, comment=None):
    """
    Reports (submits a complain about) a user.
    https://vk.com/dev/users.report
    """
    params = {
        'user_id': user_id,
        'type': type,
        'comment': comment
    }
    result = call('users.report', **params)
    return parse_response(result)

    
 def search(**search_params):
    """
    Returns a list of users matching the search criteria.
    https://vk.com/dev/users.search
    """
	search_tags = (
		'q','sort','offset','count','fields',\
		'city','country','hometown','university_country', 'university',\
		'university_year', 'university_faculty', 'university_chair',\
		'sex', 'status', 'age_from', 'age_to', 'birth_day',\
	    'birth_month', 'birth_year', 'online', 'has_photo',\
	    'school_country', 'school_city', 'school_class', 'school',\
	    'school_year', 'religion', 'interests', 'company',\
		'position', 'group_id', 'from_list'
    )
    
	# checking if the param passed exists
	# using search_params.keys() gives runtime error
	for param in list(search_params):
		if param not in search_tags:
			del search_params[param]
			# remove the key-value from the passed args
            
	# not sure if search_params should be **search_params
	result = call('users.search', search_params)
	return parse_response(result)
