import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

"""
Store arbitrary data associated with an entity. Objects are small (~1KB) JSON-compatible objects which are stored
directly on the entity profile. Objects are made available for use in other PlayFab contexts, such as PlayStream events
and CloudScript functions. Files can efficiently store data of any size or format. Both objects and files support a
flexible permissions system to control read and write access by other entities.
"""

def AbortFileUploads(request, callback, customData = None, extraHeaders = None):
    """
    Abort pending file uploads to an entity's profile.
    https://api.playfab.com/documentation/data/method/AbortFileUploads
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/File/AbortFileUploads", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteFiles(request, callback, customData = None, extraHeaders = None):
    """
    Delete files on an entity's profile.
    https://api.playfab.com/documentation/data/method/DeleteFiles
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/File/DeleteFiles", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def FinalizeFileUploads(request, callback, customData = None, extraHeaders = None):
    """
    Finalize file uploads to an entity's profile.
    https://api.playfab.com/documentation/data/method/FinalizeFileUploads
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/File/FinalizeFileUploads", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetFiles(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves file metadata from an entity's profile.
    https://api.playfab.com/documentation/data/method/GetFiles
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/File/GetFiles", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetObjects(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves objects from an entity's profile.
    https://api.playfab.com/documentation/data/method/GetObjects
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Object/GetObjects", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def InitiateFileUploads(request, callback, customData = None, extraHeaders = None):
    """
    Initiates file uploads to an entity's profile.
    https://api.playfab.com/documentation/data/method/InitiateFileUploads
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/File/InitiateFileUploads", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetObjects(request, callback, customData = None, extraHeaders = None):
    """
    Sets objects on an entity's profile.
    https://api.playfab.com/documentation/data/method/SetObjects
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Object/SetObjects", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


