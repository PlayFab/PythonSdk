import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

""" APIs for managing experiments. """


def CreateExperiment(request, callback, customData = None, extraHeaders = None):
    """
    Creates a new experiment for a title.
    https://docs.microsoft.com/rest/api/playfab/experimentation/experimentation/createexperiment
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Experimentation/CreateExperiment", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteExperiment(request, callback, customData = None, extraHeaders = None):
    """
    Deletes an existing experiment for a title.
    https://docs.microsoft.com/rest/api/playfab/experimentation/experimentation/deleteexperiment
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Experimentation/DeleteExperiment", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetExperiments(request, callback, customData = None, extraHeaders = None):
    """
    Gets the details of all experiments for a title.
    https://docs.microsoft.com/rest/api/playfab/experimentation/experimentation/getexperiments
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Experimentation/GetExperiments", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetLatestScorecard(request, callback, customData = None, extraHeaders = None):
    """
    Gets the latest scorecard of the experiment for the title.
    https://docs.microsoft.com/rest/api/playfab/experimentation/experimentation/getlatestscorecard
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Experimentation/GetLatestScorecard", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetTreatmentAssignment(request, callback, customData = None, extraHeaders = None):
    """
    Gets the treatment assignments for a player for every running experiment in the title.
    https://docs.microsoft.com/rest/api/playfab/experimentation/experimentation/gettreatmentassignment
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Experimentation/GetTreatmentAssignment", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def StartExperiment(request, callback, customData = None, extraHeaders = None):
    """
    Starts an existing experiment for a title.
    https://docs.microsoft.com/rest/api/playfab/experimentation/experimentation/startexperiment
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Experimentation/StartExperiment", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def StopExperiment(request, callback, customData = None, extraHeaders = None):
    """
    Stops an existing experiment for a title.
    https://docs.microsoft.com/rest/api/playfab/experimentation/experimentation/stopexperiment
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Experimentation/StopExperiment", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UpdateExperiment(request, callback, customData = None, extraHeaders = None):
    """
    Updates an existing experiment for a title.
    https://docs.microsoft.com/rest/api/playfab/experimentation/experimentation/updateexperiment
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Experimentation/UpdateExperiment", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


