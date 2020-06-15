import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

""" API methods for managing multiplayer servers. API methods for managing parties. """


def CancelAllMatchmakingTicketsForPlayer(request, callback, customData = None, extraHeaders = None):
    """
    Cancel all active tickets the player is a member of in a given queue.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/cancelallmatchmakingticketsforplayer
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/CancelAllMatchmakingTicketsForPlayer", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CancelAllServerBackfillTicketsForPlayer(request, callback, customData = None, extraHeaders = None):
    """
    Cancel all active backfill tickets the player is a member of in a given queue.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/cancelallserverbackfillticketsforplayer
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/CancelAllServerBackfillTicketsForPlayer", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CancelMatchmakingTicket(request, callback, customData = None, extraHeaders = None):
    """
    Cancel a matchmaking ticket.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/cancelmatchmakingticket
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/CancelMatchmakingTicket", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CancelServerBackfillTicket(request, callback, customData = None, extraHeaders = None):
    """
    Cancel a server backfill ticket.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/cancelserverbackfillticket
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/CancelServerBackfillTicket", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateBuildAlias(request, callback, customData = None, extraHeaders = None):
    """
    Creates a multiplayer server build alias.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/createbuildalias
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/CreateBuildAlias", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateBuildWithCustomContainer(request, callback, customData = None, extraHeaders = None):
    """
    Creates a multiplayer server build with a custom container.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/createbuildwithcustomcontainer
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/createbuildwithmanagedcontainer
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/creatematchmakingticket
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/createremoteuser
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/CreateRemoteUser", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateServerBackfillTicket(request, callback, customData = None, extraHeaders = None):
    """
    Create a backfill matchmaking ticket as a server. A backfill ticket represents an ongoing game. The matchmaking service
    automatically starts matching the backfill ticket against other matchmaking tickets. Backfill tickets cannot match with
    other backfill tickets.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/createserverbackfillticket
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/CreateServerBackfillTicket", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateServerMatchmakingTicket(request, callback, customData = None, extraHeaders = None):
    """
    Create a matchmaking ticket as a server. The matchmaking service automatically starts matching the ticket against other
    matchmaking tickets.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/createservermatchmakingticket
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/deleteasset
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/deletebuild
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/DeleteBuild", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteBuildAlias(request, callback, customData = None, extraHeaders = None):
    """
    Deletes a multiplayer server build alias.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/deletebuildalias
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/DeleteBuildAlias", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteBuildRegion(request, callback, customData = None, extraHeaders = None):
    """
    Removes a multiplayer server build's region.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/deletebuildregion
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/DeleteBuildRegion", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteCertificate(request, callback, customData = None, extraHeaders = None):
    """
    Deletes a multiplayer server game certificate.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/deletecertificate
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/DeleteCertificate", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteContainerImageRepository(request, callback, customData = None, extraHeaders = None):
    """
    Deletes a container image repository.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/deletecontainerimagerepository
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/DeleteContainerImageRepository", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteRemoteUser(request, callback, customData = None, extraHeaders = None):
    """
    Deletes a remote user to log on to a VM for a multiplayer server build.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/deleteremoteuser
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/enablemultiplayerserversfortitle
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/getassetuploadurl
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/getbuild
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetBuild", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetBuildAlias(request, callback, customData = None, extraHeaders = None):
    """
    Gets a multiplayer server build alias.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/getbuildalias
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetBuildAlias", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetContainerRegistryCredentials(request, callback, customData = None, extraHeaders = None):
    """
    Gets the credentials to the container registry.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/getcontainerregistrycredentials
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/getmatch
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/GetMatch", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetMatchmakingQueue(request, callback, customData = None, extraHeaders = None):
    """
    SDK support is limited to C# and Java for this API. Get a matchmaking queue configuration.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking-admin/getmatchmakingqueue
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/getmatchmakingticket
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/getmultiplayerserverdetails
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetMultiplayerServerDetails", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetMultiplayerServerLogs(request, callback, customData = None, extraHeaders = None):
    """
    Gets multiplayer server logs after a server has terminated.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/getmultiplayerserverlogs
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetMultiplayerServerLogs", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetMultiplayerSessionLogsBySessionId(request, callback, customData = None, extraHeaders = None):
    """
    Gets multiplayer server logs after a server has terminated.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/getmultiplayersessionlogsbysessionid
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetMultiplayerSessionLogsBySessionId", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetQueueStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Get the statistics for a queue.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/getqueuestatistics
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/getremoteloginendpoint
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetRemoteLoginEndpoint", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetServerBackfillTicket(request, callback, customData = None, extraHeaders = None):
    """
    Get a matchmaking backfill ticket by ticket Id.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/getserverbackfillticket
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/GetServerBackfillTicket", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetTitleEnabledForMultiplayerServersStatus(request, callback, customData = None, extraHeaders = None):
    """
    Gets the status of whether a title is enabled for the multiplayer server feature.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/gettitleenabledformultiplayerserversstatus
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetTitleEnabledForMultiplayerServersStatus", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetTitleMultiplayerServersQuotas(request, callback, customData = None, extraHeaders = None):
    """
    Gets the quotas for a title in relation to multiplayer servers.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/gettitlemultiplayerserversquotas
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/GetTitleMultiplayerServersQuotas", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def JoinMatchmakingTicket(request, callback, customData = None, extraHeaders = None):
    """
    Join a matchmaking ticket.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/joinmatchmakingticket
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listarchivedmultiplayerservers
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listassetsummaries
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListAssetSummaries", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListBuildAliases(request, callback, customData = None, extraHeaders = None):
    """
    Lists details of all build aliases for a title. Accepts tokens for title and if game client access is enabled, allows
    game client to request list of builds with player entity token.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listbuildaliases
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListBuildAliases", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListBuildSummaries(request, callback, customData = None, extraHeaders = None):
    """
    Lists summarized details of all multiplayer server builds for a title. Accepts tokens for title and if game client
    access is enabled, allows game client to request list of builds with player entity token.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listbuildsummaries
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listcertificatesummaries
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listcontainerimages
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listcontainerimagetags
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListContainerImageTags", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListMatchmakingQueues(request, callback, customData = None, extraHeaders = None):
    """
    SDK support is limited to C# and Java for this API. List all matchmaking queue configs.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking-admin/listmatchmakingqueues
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/listmatchmakingticketsforplayer
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listmultiplayerservers
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListMultiplayerServers", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListPartyQosServers(request, callback, customData = None, extraHeaders = None):
    """
    Lists quality of service servers for party.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listpartyqosservers
    """
    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListPartyQosServers", request, None, None, wrappedCallback, customData, extraHeaders)

# [Obsolete("Use 'ListQosServersForTitle' instead", true)]
def ListQosServers(request, callback, customData = None, extraHeaders = None):
    """
    Lists quality of service servers.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listqosservers
    """
    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListQosServers", request, None, None, wrappedCallback, customData, extraHeaders)

def ListQosServersForTitle(request, callback, customData = None, extraHeaders = None):
    """
    Lists quality of service servers.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listqosserversfortitle
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListQosServersForTitle", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListServerBackfillTicketsForPlayer(request, callback, customData = None, extraHeaders = None):
    """
    List all server backfill ticket Ids the user is a member of.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking/listserverbackfillticketsforplayer
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/ListServerBackfillTicketsForPlayer", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListVirtualMachineSummaries(request, callback, customData = None, extraHeaders = None):
    """
    Lists virtual machines for a title.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/listvirtualmachinesummaries
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ListVirtualMachineSummaries", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def RemoveMatchmakingQueue(request, callback, customData = None, extraHeaders = None):
    """
    SDK support is limited to C# and Java for this API. Remove a matchmaking queue config.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking-admin/removematchmakingqueue
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Match/RemoveMatchmakingQueue", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def RequestMultiplayerServer(request, callback, customData = None, extraHeaders = None):
    """
    Request a multiplayer server session. Accepts tokens for title and if game client access is enabled, allows game client
    to request a server with player entity token.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/requestmultiplayerserver
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/rollovercontainerregistrycredentials
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/RolloverContainerRegistryCredentials", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetMatchmakingQueue(request, callback, customData = None, extraHeaders = None):
    """
    SDK support is limited to C# and Java for this API. Create or update a matchmaking queue configuration.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/matchmaking-admin/setmatchmakingqueue
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/shutdownmultiplayerserver
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/ShutdownMultiplayerServer", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UntagContainerImage(request, callback, customData = None, extraHeaders = None):
    """
    Untags a container image.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/untagcontainerimage
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/UntagContainerImage", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UpdateBuildAlias(request, callback, customData = None, extraHeaders = None):
    """
    Creates a multiplayer server build alias.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/updatebuildalias
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/UpdateBuildAlias", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UpdateBuildRegion(request, callback, customData = None, extraHeaders = None):
    """
    Updates a multiplayer server build's region. If the region is not yet created, it will be created
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/updatebuildregion
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/UpdateBuildRegion", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UpdateBuildRegions(request, callback, customData = None, extraHeaders = None):
    """
    Updates a multiplayer server build's regions.
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/updatebuildregions
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
    https://docs.microsoft.com/rest/api/playfab/multiplayer/multiplayerserver/uploadcertificate
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/MultiplayerServer/UploadCertificate", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


