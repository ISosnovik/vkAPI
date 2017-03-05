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


def search(q=None, sort=None, offset=None, count=None, fields=None, city=None,\
           country=None, hometown=None, university_country=None, university=None,\
           university_year=None, university_faculty=None, university_chair=None,\
           sex=None, status=None, age_from=None, age_to=None, birth_day=None,\
           birth_month=None, birth_year=None, online=None, has_photo=None,\
           school_country=None, school_city=None, school_class=None, school=None,\
           school_year=None, religion=None, interests=None, company=None,\
           position=None, group_id=None, from_list=None):
    """
    Returns a list of users matching the search criteria.
    https://vk.com/dev/users.search
    """
    params = {
        'q': q,
        'sort': sort,
        'offset': offset,
        'count': count,
        'fields': fields,
        'city': city,
        'country': country,
        'hometown': hometown,
        'university_country': university_country,
        'university': university,
        'university_year': university_year,
        'university_faculty': university_faculty,
        'university_chair': university_chair,
        'sex': sex,
        'status': status,
        'age_from': age_from,
        'age_to': age_to,
        'birth_day': birth_day,
        'birth_month': birth_month,
        'birth_year': birth_year,
        'online': online,
        'has_photo': has_photo,
        'school_country': school_country,
        'school_city': school_city,
        'school_class': school_class,
        'school': school,
        'school_year': school_year,
        'religion': religion,
        'interests': interests,
        'company': company,
        'position': position,
        'group_id': group_id,
        'from_list': from_list
    }
    result = call('users.search', **params)
    return parse_response(result)


