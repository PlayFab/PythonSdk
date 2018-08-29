import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

"""
Write custom PlayStream events for any PlayFab entity. PlayStream events can be used for analytics, reporting,
debugging, or to trigger custom actions in near real-time.
"""

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


