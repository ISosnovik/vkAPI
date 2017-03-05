# Database methods
from ..api import call, parse_response


def getChairs(faculty_id=None, offset=None, count=None):
    """
    Returns list of chairs on a specified faculty.
    https://vk.com/dev/database.getChairs
    """
    params = {
        'faculty_id': faculty_id,
        'offset': offset,
        'count': count
    }
    result = call('database.getChairs', **params)
    return parse_response(result)


def getCities(country_id=None, region_id=None, q=None, need_all=None, offset=None,\
              count=None):
    """
    Returns a list of cities.
    https://vk.com/dev/database.getCities
    """
    params = {
        'country_id': country_id,
        'region_id': region_id,
        'q': q,
        'need_all': need_all,
        'offset': offset,
        'count': count
    }
    result = call('database.getCities', **params)
    return parse_response(result)


def getCitiesById(city_ids=None):
    """
    Returns information about cities by their IDs.
    https://vk.com/dev/database.getCitiesById
    """
    params = {
        'city_ids': city_ids
    }
    result = call('database.getCitiesById', **params)
    return parse_response(result)


def getCountries(need_all=None, code=None, offset=None, count=None):
    """
    Returns a list of countries.
    https://vk.com/dev/database.getCountries
    """
    params = {
        'need_all': need_all,
        'code': code,
        'offset': offset,
        'count': count
    }
    result = call('database.getCountries', **params)
    return parse_response(result)


def getCountriesById(country_ids=None):
    """
    Returns information about countries by their IDs.
    https://vk.com/dev/database.getCountriesById
    """
    params = {
        'country_ids': country_ids
    }
    result = call('database.getCountriesById', **params)
    return parse_response(result)


def getFaculties(university_id=None, offset=None, count=None):
    """
    Returns a list of faculties (i.e., university departments).
    https://vk.com/dev/database.getFaculties
    """
    params = {
        'university_id': university_id,
        'offset': offset,
        'count': count
    }
    result = call('database.getFaculties', **params)
    return parse_response(result)


def getRegions(country_id=None, q=None, offset=None, count=None):
    """
    Returns a list of regions.
    https://vk.com/dev/database.getRegions
    """
    params = {
        'country_id': country_id,
        'q': q,
        'offset': offset,
        'count': count
    }
    result = call('database.getRegions', **params)
    return parse_response(result)


def getSchoolClasses(country_id=None):
    """
    Returns a list of school classes specified for the country.
    https://vk.com/dev/database.getSchoolClasses
    """
    params = {
        'country_id': country_id
    }
    result = call('database.getSchoolClasses', **params)
    return parse_response(result)


def getSchools(q=None, city_id=None, offset=None, count=None):
    """
    Returns a list of schools.
    https://vk.com/dev/database.getSchools
    """
    params = {
        'q': q,
        'city_id': city_id,
        'offset': offset,
        'count': count
    }
    result = call('database.getSchools', **params)
    return parse_response(result)


def getStreetsById(street_ids=None):
    """
    Returns information about streets by their IDs.
    https://vk.com/dev/database.getStreetsById
    """
    params = {
        'street_ids': street_ids
    }
    result = call('database.getStreetsById', **params)
    return parse_response(result)


def getUniversities(q=None, country_id=None, city_id=None, offset=None,\
                    count=None):
    """
    Returns a list of higher education institutions.
    https://vk.com/dev/database.getUniversities
    """
    params = {
        'q': q,
        'country_id': country_id,
        'city_id': city_id,
        'offset': offset,
        'count': count
    }
    result = call('database.getUniversities', **params)
    return parse_response(result)


