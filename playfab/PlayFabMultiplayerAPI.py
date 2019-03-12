import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

""" API methods for managing multiplayer servers. API methods for managing parties. """


def CancelAllMatchmakingTicketsForPlayer(request, callback, customData = None, extraHeaders = None):
    """
    Cancel all active tickets the player is a member of in a given queue.
    https://api.playfab.com/documentation/multiplayer/method/CancelAllMatchmakingTicketsForPlayer
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/CancelAllMatchmakingTicketsForPlayer", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CancelMatchmakingTicket(request, callback, customData = None, extraHeaders = None):
    """
    Cancel a matchmaking ticket.
    https://api.playfab.com/documentation/multiplayer/method/CancelMatchmakingTicket
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/CancelMatchmakingTicket", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateBuildWithCustomContainer(request, callback, customData = None, extraHeaders = None):
    """
    Creates a multiplayer server build with a custom container.
    https://api.playfab.com/documentation/multiplayer/method/CreateBuildWithCustomContainer
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/CreateBuildWithCustomContainer", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateBuildWithManagedContainer(request, callback, customData = None, extraHeaders = None):
    """
    Creates a multiplayer server build with a managed container.
    https://api.playfab.com/documentation/multiplayer/method/CreateBuildWithManagedContainer
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/CreateBuildWithManagedContainer", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateMatchmakingTicket(request, callback, customData = None, extraHeaders = None):
    """
    Create a matchmaking ticket as a client.
    https://api.playfab.com/documentation/multiplayer/method/CreateMatchmakingTicket
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/CreateMatchmakingTicket", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateRemoteUser(request, callback, customData = None, extraHeaders = None):
    """
    Creates a remote user to log on to a VM for a multiplayer server build.
    https://api.playfab.com/documentation/multiplayer/method/CreateRemoteUser
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/CreateRemoteUser", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateServerMatchmakingTicket(request, callback, customData = None, extraHeaders = None):
    """
    Create a matchmaking ticket as a server. The matchmaking service automatically starts matching the ticket against other
    matchmaking tickets.
    https://api.playfab.com/documentation/multiplayer/method/CreateServerMatchmakingTicket
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/CreateServerMatchmakingTicket", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteAsset(request, callback, customData = None, extraHeaders = None):
    """
    Deletes a multiplayer server game asset for a title.
    https://api.playfab.com/documentation/multiplayer/method/DeleteAsset
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/DeleteAsset", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteBuild(request, callback, customData = None, extraHeaders = None):
    """
    Deletes a multiplayer server build.
    https://api.playfab.com/documentation/multiplayer/method/DeleteBuild
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/DeleteBuild", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteCertificate(request, callback, customData = None, extraHeaders = None):
    """
    Deletes a multiplayer server game certificate.
    https://api.playfab.com/documentation/multiplayer/method/DeleteCertificate
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/DeleteCertificate", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteRemoteUser(request, callback, customData = None, extraHeaders = None):
    """
    Deletes a remote user to log on to a VM for a multiplayer server build.
    https://api.playfab.com/documentation/multiplayer/method/DeleteRemoteUser
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/DeleteRemoteUser", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def EnableMultiplayerServersForTitle(request, callback, customData = None, extraHeaders = None):
    """
    Enables the multiplayer server feature for a title.
    https://api.playfab.com/documentation/multiplayer/method/EnableMultiplayerServersForTitle
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/EnableMultiplayerServersForTitle", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetAssetUploadUrl(request, callback, customData = None, extraHeaders = None):
    """
    Gets the URL to upload assets to.
    https://api.playfab.com/documentation/multiplayer/method/GetAssetUploadUrl
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetAssetUploadUrl", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetBuild(request, callback, customData = None, extraHeaders = None):
    """
    Gets a multiplayer server build.
    https://api.playfab.com/documentation/multiplayer/method/GetBuild
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetBuild", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetContainerRegistryCredentials(request, callback, customData = None, extraHeaders = None):
    """
    Gets the credentials to the container registry.
    https://api.playfab.com/documentation/multiplayer/method/GetContainerRegistryCredentials
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetContainerRegistryCredentials", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetMatch(request, callback, customData = None, extraHeaders = None):
    """
    Get a match.
    https://api.playfab.com/documentation/multiplayer/method/GetMatch
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/GetMatch", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetMatchmakingQueue(request, callback, customData = None, extraHeaders = None):
    """
    Get a matchmaking queue configuration.
    https://api.playfab.com/documentation/multiplayer/method/GetMatchmakingQueue
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/GetMatchmakingQueue", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetMatchmakingTicket(request, callback, customData = None, extraHeaders = None):
    """
    Get a matchmaking ticket by ticket Id.
    https://api.playfab.com/documentation/multiplayer/method/GetMatchmakingTicket
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/GetMatchmakingTicket", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetMultiplayerServerDetails(request, callback, customData = None, extraHeaders = None):
    """
    Gets multiplayer server session details for a build.
    https://api.playfab.com/documentation/multiplayer/method/GetMultiplayerServerDetails
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetMultiplayerServerDetails", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetQueueStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Get the statistics for a queue.
    https://api.playfab.com/documentation/multiplayer/method/GetQueueStatistics
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/GetQueueStatistics", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetRemoteLoginEndpoint(request, callback, customData = None, extraHeaders = None):
    """
    Gets a remote login endpoint to a VM that is hosting a multiplayer server build.
    https://api.playfab.com/documentation/multiplayer/method/GetRemoteLoginEndpoint
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetRemoteLoginEndpoint", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetTitleEnabledForMultiplayerServersStatus(request, callback, customData = None, extraHeaders = None):
    """
    Gets the status of whether a title is enabled for the multiplayer server feature.
    https://api.playfab.com/documentation/multiplayer/method/GetTitleEnabledForMultiplayerServersStatus
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetTitleEnabledForMultiplayerServersStatus", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def JoinMatchmakingTicket(request, callback, customData = None, extraHeaders = None):
    """
    Join a matchmaking ticket.
    https://api.playfab.com/documentation/multiplayer/method/JoinMatchmakingTicket
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/JoinMatchmakingTicket", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListArchivedMultiplayerServers(request, callback, customData = None, extraHeaders = None):
    """
    Lists archived multiplayer server sessions for a build.
    https://api.playfab.com/documentation/multiplayer/method/ListArchivedMultiplayerServers
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListArchivedMultiplayerServers", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListAssetSummaries(request, callback, customData = None, extraHeaders = None):
    """
    Lists multiplayer server game assets for a title.
    https://api.playfab.com/documentation/multiplayer/method/ListAssetSummaries
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListAssetSummaries", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListBuildSummaries(request, callback, customData = None, extraHeaders = None):
    """
    Lists summarized details of all multiplayer server builds for a title.
    https://api.playfab.com/documentation/multiplayer/method/ListBuildSummaries
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListBuildSummaries", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListCertificateSummaries(request, callback, customData = None, extraHeaders = None):
    """
    Lists multiplayer server game certificates for a title.
    https://api.playfab.com/documentation/multiplayer/method/ListCertificateSummaries
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListCertificateSummaries", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListContainerImages(request, callback, customData = None, extraHeaders = None):
    """
    Lists custom container images for a title.
    https://api.playfab.com/documentation/multiplayer/method/ListContainerImages
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListContainerImages", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListContainerImageTags(request, callback, customData = None, extraHeaders = None):
    """
    Lists the tags for a custom container image.
    https://api.playfab.com/documentation/multiplayer/method/ListContainerImageTags
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListContainerImageTags", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListMatchmakingQueues(request, callback, customData = None, extraHeaders = None):
    """
    List all matchmaking queue configs.
    https://api.playfab.com/documentation/multiplayer/method/ListMatchmakingQueues
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/ListMatchmakingQueues", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListMatchmakingTicketsForPlayer(request, callback, customData = None, extraHeaders = None):
    """
    List all matchmaking ticket Ids the user is a member of.
    https://api.playfab.com/documentation/multiplayer/method/ListMatchmakingTicketsForPlayer
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/ListMatchmakingTicketsForPlayer", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListMultiplayerServers(request, callback, customData = None, extraHeaders = None):
    """
    Lists multiplayer server sessions for a build.
    https://api.playfab.com/documentation/multiplayer/method/ListMultiplayerServers
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListMultiplayerServers", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListQosServers(request, callback, customData = None, extraHeaders = None):
    """
    Lists quality of service servers.
    https://api.playfab.com/documentation/multiplayer/method/ListQosServers
    """
    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListQosServers", request, None, None, wrappedCallback, customData, extraHeaders)

def ListVirtualMachineSummaries(request, callback, customData = None, extraHeaders = None):
    """
    Lists virtual machines for a title.
    https://api.playfab.com/documentation/multiplayer/method/ListVirtualMachineSummaries
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListVirtualMachineSummaries", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def RemoveMatchmakingQueue(request, callback, customData = None, extraHeaders = None):
    """
    Remove a matchmaking queue config.
    https://api.playfab.com/documentation/multiplayer/method/RemoveMatchmakingQueue
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/RemoveMatchmakingQueue", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def RequestMultiplayerServer(request, callback, customData = None, extraHeaders = None):
    """
    Request a multiplayer server session. Accepts tokens for title and if game client accesss is enabled, allows game client
    to request a server with player entity token.
    https://api.playfab.com/documentation/multiplayer/method/RequestMultiplayerServer
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/RequestMultiplayerServer", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def RolloverContainerRegistryCredentials(request, callback, customData = None, extraHeaders = None):
    """
    Rolls over the credentials to the container registry.
    https://api.playfab.com/documentation/multiplayer/method/RolloverContainerRegistryCredentials
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/RolloverContainerRegistryCredentials", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetMatchmakingQueue(request, callback, customData = None, extraHeaders = None):
    """
    Create or update a matchmaking queue configuration.
    https://api.playfab.com/documentation/multiplayer/method/SetMatchmakingQueue
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/SetMatchmakingQueue", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ShutdownMultiplayerServer(request, callback, customData = None, extraHeaders = None):
    """
    Shuts down a multiplayer server session.
    https://api.playfab.com/documentation/multiplayer/method/ShutdownMultiplayerServer
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ShutdownMultiplayerServer", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UpdateBuildRegions(request, callback, customData = None, extraHeaders = None):
    """
    Updates a multiplayer server build's regions.
    https://api.playfab.com/documentation/multiplayer/method/UpdateBuildRegions
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/UpdateBuildRegions", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UploadCertificate(request, callback, customData = None, extraHeaders = None):
    """
    Uploads a multiplayer server game certificate.
    https://api.playfab.com/documentation/multiplayer/method/UploadCertificate
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/UploadCertificate", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


