import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

"""
The Authentication APIs provide a convenient way to convert classic authentication responses into entity authentication
models. These APIs will provide you with the entity authentication token needed for subsequent Entity API calls. Manage
API keys for authenticating any entity.
"""

def ActivateKey(request, callback, customData = None, extraHeaders = None):
    """
    Activates the given API key. Active keys may be used for authentication.
    https://api.playfab.com/documentation/authentication/method/ActivateKey
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/APIKey/ActivateKey", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateKey(request, callback, customData = None, extraHeaders = None):
    """
    Creates an API key for the given entity.
    https://api.playfab.com/documentation/authentication/method/CreateKey
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/APIKey/CreateKey", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeactivateKey(request, callback, customData = None, extraHeaders = None):
    """
    Deactivates the given API key, causing subsequent authentication attempts with it to fail.Deactivating a key is a way to
    verify that the key is not in use before deleting it.
    https://api.playfab.com/documentation/authentication/method/DeactivateKey
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/APIKey/DeactivateKey", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteKey(request, callback, customData = None, extraHeaders = None):
    """
    Deletes the given API key.
    https://api.playfab.com/documentation/authentication/method/DeleteKey
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/APIKey/DeleteKey", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetEntityToken(request, callback, customData = None, extraHeaders = None):
    """
    Method to exchange a legacy AuthenticationTicket or title SecretKey for an Entity Token or to refresh a still valid
    Entity Token.
    https://api.playfab.com/documentation/authentication/method/GetEntityToken
    """
    authKey = None
    authValue = None
    if PlayFabSettings._internalSettings.EntityToken:
        authKey = "X-EntityToken"
        authValue = PlayFabSettings._internalSettings.EntityToken
    elif PlayFabSettings._internalSettings.ClientSessionTicket:
        authKey = "X-Authorization"
        authValue = PlayFabSettings._internalSettings.ClientSessionTicket 
    elif PlayFabSettings.DeveloperSecretKey:
        authKey = "X-SecretKey"
        authValue = PlayFabSettings.DeveloperSecretKey 

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Authentication/GetEntityToken", request, authKey, authValue, wrappedCallback, customData, extraHeaders)

def GetKeys(request, callback, customData = None, extraHeaders = None):
    """
    Gets the API keys associated with the given entity.
    https://api.playfab.com/documentation/authentication/method/GetKeys
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/APIKey/GetKeys", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


