import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

""" Manage the Insights performance level and data storage retention settings. """


def GetDetails(request, callback, customData = None, extraHeaders = None):
    """
    Gets the current values for the Insights performance and data storage retention, list of pending operations, and the
    performance and data storage retention limits.
    https://docs.microsoft.com/rest/api/playfab/insights/analytics/getdetails
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Insights/GetDetails", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetLimits(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the range of allowed values for performance and data storage retention values as well as the submeter details
    for each performance level.
    https://docs.microsoft.com/rest/api/playfab/insights/analytics/getlimits
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Insights/GetLimits", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetOperationStatus(request, callback, customData = None, extraHeaders = None):
    """
    Gets the status of a SetPerformance or SetStorageRetention operation.
    https://docs.microsoft.com/rest/api/playfab/insights/analytics/getoperationstatus
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Insights/GetOperationStatus", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetPendingOperations(request, callback, customData = None, extraHeaders = None):
    """
    Gets a list of pending SetPerformance and/or SetStorageRetention operations for the title.
    https://docs.microsoft.com/rest/api/playfab/insights/analytics/getpendingoperations
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Insights/GetPendingOperations", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetPerformance(request, callback, customData = None, extraHeaders = None):
    """
    Sets the Insights performance level value for the title.
    https://docs.microsoft.com/rest/api/playfab/insights/analytics/setperformance
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Insights/SetPerformance", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetStorageRetention(request, callback, customData = None, extraHeaders = None):
    """
    Sets the Insights data storage retention days value for the title.
    https://docs.microsoft.com/rest/api/playfab/insights/analytics/setstorageretention
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Insights/SetStorageRetention", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


