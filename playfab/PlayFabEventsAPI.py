import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

""" Entity profiles are the top level containers for essentially all information about an entity. """


def WriteEvents(request, callback, customData = None, extraHeaders = None):
    """
    Write batches of entity based events to PlayStream.
    https://api.playfab.com/documentation/events/method/WriteEvents
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Event/WriteEvents", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


