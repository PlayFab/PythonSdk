import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

"""
All PlayFab entities have profiles, which hold top-level properties about the entity. These APIs give you the tools
needed to manage entity profiles.
"""

def GetGlobalPolicy(request, callback, customData = None, extraHeaders = None):
    """
    Gets the global title access policy
    https://docs.microsoft.com/rest/api/playfab/profiles/account-management/getglobalpolicy
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/GetGlobalPolicy", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetProfile(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the entity's profile.
    https://docs.microsoft.com/rest/api/playfab/profiles/account-management/getprofile
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/GetProfile", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetProfiles(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the entity's profile.
    https://docs.microsoft.com/rest/api/playfab/profiles/account-management/getprofiles
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/GetProfiles", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetTitlePlayersFromMasterPlayerAccountIds(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title player accounts associated with the given master player account.
    https://docs.microsoft.com/rest/api/playfab/profiles/account-management/gettitleplayersfrommasterplayeraccountids
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/GetTitlePlayersFromMasterPlayerAccountIds", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetGlobalPolicy(request, callback, customData = None, extraHeaders = None):
    """
    Sets the global title access policy
    https://docs.microsoft.com/rest/api/playfab/profiles/account-management/setglobalpolicy
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/SetGlobalPolicy", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetProfileLanguage(request, callback, customData = None, extraHeaders = None):
    """
    Updates the entity's language. The precedence hierarchy for communication to the player is Title Player Account
    language, Master Player Account language, and then title default language if the first two aren't set or supported.
    https://docs.microsoft.com/rest/api/playfab/profiles/account-management/setprofilelanguage
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/SetProfileLanguage", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetProfilePolicy(request, callback, customData = None, extraHeaders = None):
    """
    Sets the profiles access policy
    https://docs.microsoft.com/rest/api/playfab/profiles/account-management/setprofilepolicy
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/SetProfilePolicy", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


