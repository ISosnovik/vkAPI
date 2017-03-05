# Places methods
from ..api import call, parse_response


def add(type=None, title=None, latitude=None, longitude=None, country=None,\
        city=None, address=None):
    """
    Adds a new location to the location database.
    https://vk.com/dev/places.add
    """
    params = {
        'type': type,
        'title': title,
        'latitude': latitude,
        'longitude': longitude,
        'country': country,
        'city': city,
        'address': address
    }
    result = call('places.add', **params)
    return parse_response(result)


def checkin(place_id=None, text=None, latitude=None, longitude=None, friends_only=None,\
            services=None):
    """
    Checks a user in at the specified location.
    https://vk.com/dev/places.checkin
    """
    params = {
        'place_id': place_id,
        'text': text,
        'latitude': latitude,
        'longitude': longitude,
        'friends_only': friends_only,
        'services': services
    }
    result = call('places.checkin', **params)
    return parse_response(result)


def getById(places=None):
    """
    Returns information about locations by their IDs.
    https://vk.com/dev/places.getById
    """
    params = {
        'places': places
    }
    result = call('places.getById', **params)
    return parse_response(result)


def getCheckins(latitude=None, longitude=None, place=None, user_id=None,\
                offset=None, count=None, timestamp=None, friends_only=None,\
                need_places=None):
    """
    Returns a list of user check-ins at locations according
    to the set parameters.
    https://vk.com/dev/places.getCheckins
    """
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'place': place,
        'user_id': user_id,
        'offset': offset,
        'count': count,
        'timestamp': timestamp,
        'friends_only': friends_only,
        'need_places': need_places
    }
    result = call('places.getCheckins', **params)
    return parse_response(result)


def getTypes():
    """
    Returns a list of all types of locations.
    https://vk.com/dev/places.getTypes
    """
    params = {
    }
    result = call('places.getTypes', **params)
    return parse_response(result)


def search(q=None, city=None, latitude=None, longitude=None, radius=None,\
           offset=None, count=None):
    """
    Returns a list of locations that match the search criteria.
    https://vk.com/dev/places.search
    """
    params = {
        'q': q,
        'city': city,
        'latitude': latitude,
        'longitude': longitude,
        'radius': radius,
        'offset': offset,
        'count': count
    }
    result = call('places.search', **params)
    return parse_response(result)


