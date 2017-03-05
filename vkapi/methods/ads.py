# Ads methods
from ..api import call, parse_response


def addOfficeUsers(account_id=None, data=None):
    """
    Adds managers and/or supervisors to advertising account.
    https://vk.com/dev/ads.addOfficeUsers
    """
    params = {
        'account_id': account_id,
        'data': data
    }
    result = call('ads.addOfficeUsers', **params)
    return parse_response(result)


def checkLink(account_id=None, link_type=None, link_url=None, campaign_id=None):
    """
    Allows to check the ad link.
    https://vk.com/dev/ads.checkLink
    """
    params = {
        'account_id': account_id,
        'link_type': link_type,
        'link_url': link_url,
        'campaign_id': campaign_id
    }
    result = call('ads.checkLink', **params)
    return parse_response(result)


def createAds(account_id=None, data=None):
    """
    Creates ads.
    https://vk.com/dev/ads.createAds
    """
    params = {
        'account_id': account_id,
        'data': data
    }
    result = call('ads.createAds', **params)
    return parse_response(result)


def createCampaigns(account_id=None, data=None):
    """
    Creates advertising campaigns.
    https://vk.com/dev/ads.createCampaigns
    """
    params = {
        'account_id': account_id,
        'data': data
    }
    result = call('ads.createCampaigns', **params)
    return parse_response(result)


def createClients(account_id=None, data=None):
    """
    Creates clients of an advertising agency.
    https://vk.com/dev/ads.createClients
    """
    params = {
        'account_id': account_id,
        'data': data
    }
    result = call('ads.createClients', **params)
    return parse_response(result)


def createTargetGroup(account_id=None, client_id=None, name=None, domain=None,\
                      lifetime=None):
    """
    Creates a group to re-target ads for users who visited
    advertiser's site (viewed information about the
    product, registered, etc.).
    https://vk.com/dev/ads.createTargetGroup
    """
    params = {
        'account_id': account_id,
        'client_id': client_id,
        'name': name,
        'domain': domain,
        'lifetime': lifetime
    }
    result = call('ads.createTargetGroup', **params)
    return parse_response(result)


def deleteAds(account_id=None, ids=None):
    """
    Archives ads.
    https://vk.com/dev/ads.deleteAds
    """
    params = {
        'account_id': account_id,
        'ids': ids
    }
    result = call('ads.deleteAds', **params)
    return parse_response(result)


def deleteCampaigns(account_id=None, ids=None):
    """
    Archives advertising campaigns.
    https://vk.com/dev/ads.deleteCampaigns
    """
    params = {
        'account_id': account_id,
        'ids': ids
    }
    result = call('ads.deleteCampaigns', **params)
    return parse_response(result)


def deleteClients(account_id=None, ids=None):
    """
    Archives clients of an advertising agency.
    https://vk.com/dev/ads.deleteClients
    """
    params = {
        'account_id': account_id,
        'ids': ids
    }
    result = call('ads.deleteClients', **params)
    return parse_response(result)


def deleteTargetGroup(account_id=None, client_id=None, target_group_id=None):
    """
    Deletes a retarget group.
    https://vk.com/dev/ads.deleteTargetGroup
    """
    params = {
        'account_id': account_id,
        'client_id': client_id,
        'target_group_id': target_group_id
    }
    result = call('ads.deleteTargetGroup', **params)
    return parse_response(result)


def getAccounts():
    """
    Returns a list of advertising accounts.
    https://vk.com/dev/ads.getAccounts
    """
    params = {
    }
    result = call('ads.getAccounts', **params)
    return parse_response(result)


def getAds(account_id=None, client_id=None, include_deleted=None, campaign_ids=None,\
           ad_ids=None, limit=None, offset=None):
    """
    Returns number of ads.
    https://vk.com/dev/ads.getAds
    """
    params = {
        'account_id': account_id,
        'client_id': client_id,
        'include_deleted': include_deleted,
        'campaign_ids': campaign_ids,
        'ad_ids': ad_ids,
        'limit': limit,
        'offset': offset
    }
    result = call('ads.getAds', **params)
    return parse_response(result)


def getAdsLayout(account_id=None, client_id=None, include_deleted=None,\
                 campaign_ids=None, ad_ids=None, limit=None, offset=None):
    """
    Returns descriptions of ad layouts.
    https://vk.com/dev/ads.getAdsLayout
    """
    params = {
        'account_id': account_id,
        'client_id': client_id,
        'include_deleted': include_deleted,
        'campaign_ids': campaign_ids,
        'ad_ids': ad_ids,
        'limit': limit,
        'offset': offset
    }
    result = call('ads.getAdsLayout', **params)
    return parse_response(result)


def getAdsPostsReach(account_id=None, ads_ids=None):
    """
    Allows to get detailed information about the ad post
    reach.
    https://vk.com/dev/ads.getAdsPostsReach
    """
    params = {
        'account_id': account_id,
        'ads_ids': ads_ids
    }
    result = call('ads.getAdsPostsReach', **params)
    return parse_response(result)


def getAdsTargeting(account_id=None, client_id=None, include_deleted=None,\
                    campaign_ids=None, ad_ids=None, limit=None, offset=None):
    """
    Retuns ad targeting parameters.
    https://vk.com/dev/ads.getAdsTargeting
    """
    params = {
        'account_id': account_id,
        'client_id': client_id,
        'include_deleted': include_deleted,
        'campaign_ids': campaign_ids,
        'ad_ids': ad_ids,
        'limit': limit,
        'offset': offset
    }
    result = call('ads.getAdsTargeting', **params)
    return parse_response(result)


def getBudget(account_id=None):
    """
    Returns current budget of the advertising account.
    https://vk.com/dev/ads.getBudget
    """
    params = {
        'account_id': account_id
    }
    result = call('ads.getBudget', **params)
    return parse_response(result)


def getCampaigns(account_id=None, client_id=None, include_deleted=None,\
                 campaign_ids=None):
    """
    Returns a list of campaigns in an advertising account.
    https://vk.com/dev/ads.getCampaigns
    """
    params = {
        'account_id': account_id,
        'client_id': client_id,
        'include_deleted': include_deleted,
        'campaign_ids': campaign_ids
    }
    result = call('ads.getCampaigns', **params)
    return parse_response(result)


def getCategories(lang=None):
    """
    Returns a list of possible ad categories.
    https://vk.com/dev/ads.getCategories
    """
    params = {
        'lang': lang
    }
    result = call('ads.getCategories', **params)
    return parse_response(result)


def getClients(account_id=None):
    """
    Returns a list of advertising agency's clients.
    https://vk.com/dev/ads.getClients
    """
    params = {
        'account_id': account_id
    }
    result = call('ads.getClients', **params)
    return parse_response(result)


def getDemographics(account_id=None, ids_type=None, ids=None, period=None,\
                    date_from=None, date_to=None):
    """
    Returns demographics for ads or campaigns.
    https://vk.com/dev/ads.getDemographics
    """
    params = {
        'account_id': account_id,
        'ids_type': ids_type,
        'ids': ids,
        'period': period,
        'date_from': date_from,
        'date_to': date_to
    }
    result = call('ads.getDemographics', **params)
    return parse_response(result)


def getFloodStats(account_id=None):
    """
    Returns information about current state of a counter
     number of remaining runs of methods and time to
    the next counter nulling in seconds.
    https://vk.com/dev/ads.getFloodStats
    """
    params = {
        'account_id': account_id
    }
    result = call('ads.getFloodStats', **params)
    return parse_response(result)


def getOfficeUsers(account_id=None):
    """
    Returns a list of managers and supervisors of advertising
    account.
    https://vk.com/dev/ads.getOfficeUsers
    """
    params = {
        'account_id': account_id
    }
    result = call('ads.getOfficeUsers', **params)
    return parse_response(result)


def getRejectionReason(account_id=None, ad_id=None):
    """
    Returns a reason of ad rejection for pre-moderation.
    https://vk.com/dev/ads.getRejectionReason
    """
    params = {
        'account_id': account_id,
        'ad_id': ad_id
    }
    result = call('ads.getRejectionReason', **params)
    return parse_response(result)


def getStatistics(account_id=None, ids_type=None, ids=None, period=None,\
                  date_from=None, date_to=None):
    """
    Returns statistics of performance indicators for ads,
    campaigns, clients or the whole account.
    https://vk.com/dev/ads.getStatistics
    """
    params = {
        'account_id': account_id,
        'ids_type': ids_type,
        'ids': ids,
        'period': period,
        'date_from': date_from,
        'date_to': date_to
    }
    result = call('ads.getStatistics', **params)
    return parse_response(result)


def getSuggestions(section=None, ids=None, q=None, country=None, cities=None,\
                   lang=None):
    """
    Returns a set of auto-suggestions for various targeting
    parameters.
    https://vk.com/dev/ads.getSuggestions
    """
    params = {
        'section': section,
        'ids': ids,
        'q': q,
        'country': country,
        'cities': cities,
        'lang': lang
    }
    result = call('ads.getSuggestions', **params)
    return parse_response(result)


def getTargetGroups(account_id=None, client_id=None, extended=None):
    """
    Returns a list of target groups.
    https://vk.com/dev/ads.getTargetGroups
    """
    params = {
        'account_id': account_id,
        'client_id': client_id,
        'extended': extended
    }
    result = call('ads.getTargetGroups', **params)
    return parse_response(result)


def getTargetingStats(account_id=None, criteria=None, ad_id=None, ad_format=None,\
                      ad_platform=None, link_url=None, link_domain=None):
    """
    Returns the size of targeting audience, and also recommended
    values for CPC and CPM.
    https://vk.com/dev/ads.getTargetingStats
    """
    params = {
        'account_id': account_id,
        'criteria': criteria,
        'ad_id': ad_id,
        'ad_format': ad_format,
        'ad_platform': ad_platform,
        'link_url': link_url,
        'link_domain': link_domain
    }
    result = call('ads.getTargetingStats', **params)
    return parse_response(result)


def getUploadURL(ad_format=None):
    """
    Returns URL to upload an ad photo to.
    https://vk.com/dev/ads.getUploadURL
    """
    params = {
        'ad_format': ad_format
    }
    result = call('ads.getUploadURL', **params)
    return parse_response(result)


def getVideoUploadURL():
    """
    Returns URL to upload an ad video to.
    https://vk.com/dev/ads.getVideoUploadURL
    """
    params = {
    }
    result = call('ads.getVideoUploadURL', **params)
    return parse_response(result)


def importTargetContacts(account_id=None, client_id=None, target_group_id=None,\
                         contacts=None):
    """
    Imports a list of advertiser's contacts to count VK
    registered users against the target group.
    https://vk.com/dev/ads.importTargetContacts
    """
    params = {
        'account_id': account_id,
        'client_id': client_id,
        'target_group_id': target_group_id,
        'contacts': contacts
    }
    result = call('ads.importTargetContacts', **params)
    return parse_response(result)


def removeOfficeUsers(account_id=None, ids=None):
    """
    Removes managers and/or supervisors from advertising
    account.
    https://vk.com/dev/ads.removeOfficeUsers
    """
    params = {
        'account_id': account_id,
        'ids': ids
    }
    result = call('ads.removeOfficeUsers', **params)
    return parse_response(result)


def updateAds(account_id=None, data=None):
    """
    Edits ads.
    https://vk.com/dev/ads.updateAds
    """
    params = {
        'account_id': account_id,
        'data': data
    }
    result = call('ads.updateAds', **params)
    return parse_response(result)


def updateCampaigns(account_id=None, data=None):
    """
    Edits advertising campaigns.
    https://vk.com/dev/ads.updateCampaigns
    """
    params = {
        'account_id': account_id,
        'data': data
    }
    result = call('ads.updateCampaigns', **params)
    return parse_response(result)


def updateClients(account_id=None, data=None):
    """
    Edits clients of an advertising agency.
    https://vk.com/dev/ads.updateClients
    """
    params = {
        'account_id': account_id,
        'data': data
    }
    result = call('ads.updateClients', **params)
    return parse_response(result)


def updateTargetGroup(account_id=None, client_id=None, target_group_id=None,\
                      name=None, domain=None, lifetime=None):
    """
    Edits a retarget group.
    https://vk.com/dev/ads.updateTargetGroup
    """
    params = {
        'account_id': account_id,
        'client_id': client_id,
        'target_group_id': target_group_id,
        'name': name,
        'domain': domain,
        'lifetime': lifetime
    }
    result = call('ads.updateTargetGroup', **params)
    return parse_response(result)


