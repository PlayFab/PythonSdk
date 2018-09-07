import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

""" The Localization APIs give you the tools needed to manage language setup in your title. """


def GetLanguageList(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the list of allowed languages, only accessible by title entities
    https://api.playfab.com/documentation/localization/method/GetLanguageList
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Locale/GetLanguageList", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


