import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

"""
The Authentication APIs provide a convenient way to convert classic authentication responses into entity authentication
models. These APIs will provide you with the entity authentication token needed for subsequent Entity API calls. Manage
API keys for authenticating any entity.
"""

def GetEntityToken(request, callback, customData = None, extraHeaders = None):
    """
    Method to exchange a legacy AuthenticationTicket or title SecretKey for an Entity Token or to refresh a still valid
    Entity Token.
    https://docs.microsoft.com/rest/api/playfab/authentication/authentication/getentitytoken
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

def ValidateEntityToken(request, callback, customData = None, extraHeaders = None):
    """
    Method for a server to validate a client provided EntityToken. Only callable by the title entity.
    https://docs.microsoft.com/rest/api/playfab/authentication/authentication/validateentitytoken
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Authentication/ValidateEntityToken", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


