import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

"""
The Authentication API group is currently in-progress. The current GetEntityToken method is a stop-gap to convert
another authentication into an Entity Authentication. See https://api.playfab.com/documentation/client#Authentication
for the other authentication methods.
"""

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


