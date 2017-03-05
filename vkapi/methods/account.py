# Account methods
from ..api import call, parse_response


def banUser(user_id=None):
    """
    Adds user to the banlist.
    https://vk.com/dev/account.banUser
    """
    params = {
        'user_id': user_id
    }
    result = call('account.banUser', **params)
    return parse_response(result)


def changePassword(restore_sid=None, change_password_hash=None, old_password=None,\
                   new_password=None):
    """
    Changes a user password after access is successfully
    restored with the auth.restore method.
    https://vk.com/dev/account.changePassword
    """
    params = {
        'restore_sid': restore_sid,
        'change_password_hash': change_password_hash,
        'old_password': old_password,
        'new_password': new_password
    }
    result = call('account.changePassword', **params)
    return parse_response(result)


def getActiveOffers(offset=None, count=None):
    """
    Returns a list of active ads (offers) which executed
    by the user will bring him/her respective number
    of votes to his balance in the application.
    https://vk.com/dev/account.getActiveOffers
    """
    params = {
        'offset': offset,
        'count': count
    }
    result = call('account.getActiveOffers', **params)
    return parse_response(result)


def getAppPermissions(user_id=None):
    """
    Gets settings of the user in this application.
    https://vk.com/dev/account.getAppPermissions
    """
    params = {
        'user_id': user_id
    }
    result = call('account.getAppPermissions', **params)
    return parse_response(result)


def getBanned(offset=None, count=None):
    """
    Returns a user's blacklist.
    https://vk.com/dev/account.getBanned
    """
    params = {
        'offset': offset,
        'count': count
    }
    result = call('account.getBanned', **params)
    return parse_response(result)


def getCounters(filter=None):
    """
    Returns non-null values of user counters.
    https://vk.com/dev/account.getCounters
    """
    params = {
        'filter': filter
    }
    result = call('account.getCounters', **params)
    return parse_response(result)


def getInfo(fields=None):
    """
    Returns current account info.
    https://vk.com/dev/account.getInfo
    """
    params = {
        'fields': fields
    }
    result = call('account.getInfo', **params)
    return parse_response(result)


def getProfileInfo():
    """
    Returns the current account info.
    https://vk.com/dev/account.getProfileInfo
    """
    params = {
    }
    result = call('account.getProfileInfo', **params)
    return parse_response(result)


def getPushSettings(device_id=None, token=None):
    """
    Gets settings of push notifications.
    https://vk.com/dev/account.getPushSettings
    """
    params = {
        'device_id': device_id,
        'token': token
    }
    result = call('account.getPushSettings', **params)
    return parse_response(result)


def lookupContacts(contacts=None, service=None, mycontact=None, return_all=None,\
                   fields=None):
    """
    Allows to search the VK users using phone numbers, e-mail
    addresses and user IDs on other services.
    https://vk.com/dev/account.lookupContacts
    """
    params = {
        'contacts': contacts,
        'service': service,
        'mycontact': mycontact,
        'return_all': return_all,
        'fields': fields
    }
    result = call('account.lookupContacts', **params)
    return parse_response(result)


def registerDevice(token=None, device_model=None, device_year=None, device_id=None,\
                   system_version=None, settings=None, sandbox=None, no_text=None,\
                   subscribe=None):
    """
    Subscribes an iOS/Android/Windows Phone-based device
    to receive push notifications
    https://vk.com/dev/account.registerDevice
    """
    params = {
        'token': token,
        'device_model': device_model,
        'device_year': device_year,
        'device_id': device_id,
        'system_version': system_version,
        'settings': settings,
        'sandbox': sandbox,
        'no_text': no_text,
        'subscribe': subscribe
    }
    result = call('account.registerDevice', **params)
    return parse_response(result)


def saveProfileInfo(first_name=None, last_name=None, maiden_name=None, screen_name=None,\
                    cancel_request_id=None, sex=None, relation=None, relation_partner_id=None,\
                    bdate=None, bdate_visibility=None, home_town=None, country_id=None,\
                    city_id=None, status=None):
    """
    Edits current profile info.
    https://vk.com/dev/account.saveProfileInfo
    """
    params = {
        'first_name': first_name,
        'last_name': last_name,
        'maiden_name': maiden_name,
        'screen_name': screen_name,
        'cancel_request_id': cancel_request_id,
        'sex': sex,
        'relation': relation,
        'relation_partner_id': relation_partner_id,
        'bdate': bdate,
        'bdate_visibility': bdate_visibility,
        'home_town': home_town,
        'country_id': country_id,
        'city_id': city_id,
        'status': status
    }
    result = call('account.saveProfileInfo', **params)
    return parse_response(result)


def setInfo(name=None, value=None, intro=None, own_posts_default=None, no_wall_replies=None):
    """
    Allows to edit the current account info.
    https://vk.com/dev/account.setInfo
    """
    params = {
        'name': name,
        'value': value,
        'intro': intro,
        'own_posts_default': own_posts_default,
        'no_wall_replies': no_wall_replies
    }
    result = call('account.setInfo', **params)
    return parse_response(result)


def setNameInMenu(user_id=None, name=None):
    """
    Sets an application screen name (up to 17 characters),
    that is shown to the user in the left menu.
    https://vk.com/dev/account.setNameInMenu
    """
    params = {
        'user_id': user_id,
        'name': name
    }
    result = call('account.setNameInMenu', **params)
    return parse_response(result)


def setOffline():
    """
    Marks a current user as offline.
    https://vk.com/dev/account.setOffline
    """
    params = {
    }
    result = call('account.setOffline', **params)
    return parse_response(result)


def setOnline(voip=None):
    """
    Marks the current user as online for 15 minutes.
    https://vk.com/dev/account.setOnline
    """
    params = {
        'voip': voip
    }
    result = call('account.setOnline', **params)
    return parse_response(result)


def setPushSettings(device_id=None, settings=None, key=None, value=None):
    """
    Change push settings.
    https://vk.com/dev/account.setPushSettings
    """
    params = {
        'device_id': device_id,
        'settings': settings,
        'key': key,
        'value': value
    }
    result = call('account.setPushSettings', **params)
    return parse_response(result)


def setSilenceMode(device_id=None, time=None, peer_id=None, sound=None,\
                   token=None, chat_id=None, user_id=None):
    """
    Mutes push notifications for the set period of time.
    https://vk.com/dev/account.setSilenceMode
    """
    params = {
        'device_id': device_id,
        'time': time,
        'peer_id': peer_id,
        'sound': sound,
        'token': token,
        'chat_id': chat_id,
        'user_id': user_id
    }
    result = call('account.setSilenceMode', **params)
    return parse_response(result)


def unbanUser(user_id=None):
    """
    Deletes user from the blacklist.
    https://vk.com/dev/account.unbanUser
    """
    params = {
        'user_id': user_id
    }
    result = call('account.unbanUser', **params)
    return parse_response(result)


def unregisterDevice(device_id=None, sandbox=None, token=None):
    """
    Unsubscribes a device from push notifications.
    https://vk.com/dev/account.unregisterDevice
    """
    params = {
        'device_id': device_id,
        'sandbox': sandbox,
        'token': token
    }
    result = call('account.unregisterDevice', **params)
    return parse_response(result)


