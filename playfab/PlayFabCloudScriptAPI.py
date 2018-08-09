import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

""" API methods for executing CloudScript using an Entity Profile """


def ExecuteEntityCloudScript(request, callback, customData = None, extraHeaders = None):
    """
    Executes CloudScript using the Entity Profile
    https://api.playfab.com/documentation/cloudscript/method/ExecuteEntityCloudScript
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/CloudScript/ExecuteEntityCloudScript", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


