import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

""" Entity profiles are the top level containers for essentially all information about an entity. """


def GetGlobalPolicy(request, callback, customData = None, extraHeaders = None):
    """
    Gets the global title access policy
    https://api.playfab.com/documentation/profiles/method/GetGlobalPolicy
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
    https://api.playfab.com/documentation/profiles/method/GetProfile
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
    https://api.playfab.com/documentation/profiles/method/GetProfiles
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/GetProfiles", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetGlobalPolicy(request, callback, customData = None, extraHeaders = None):
    """
    Sets the global title access policy
    https://api.playfab.com/documentation/profiles/method/SetGlobalPolicy
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/SetGlobalPolicy", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetProfileLanguage(request, callback, customData = None, extraHeaders = None):
    """
    Updates the entity's language
    https://api.playfab.com/documentation/profiles/method/SetProfileLanguage
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
    https://api.playfab.com/documentation/profiles/method/SetProfilePolicy
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/SetProfilePolicy", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

