import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

""" APIs for managing title configurations, uploaded Game Server code executables, and user data """


def AbortTaskInstance(request, callback, customData = None, extraHeaders = None):
    """
    Abort an ongoing task instance.
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/aborttaskinstance
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AbortTaskInstance", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AddLocalizedNews(request, callback, customData = None, extraHeaders = None):
    """
    Update news item to include localized version
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/addlocalizednews
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddLocalizedNews", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AddNews(request, callback, customData = None, extraHeaders = None):
    """
    Adds a new news item to the title's news feed
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/addnews
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddNews", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AddPlayerTag(request, callback, customData = None, extraHeaders = None):
    """
    Adds a given tag to a player profile. The tag's namespace is automatically generated based on the source of the tag.
    https://docs.microsoft.com/rest/api/playfab/admin/playstream/addplayertag
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddPlayerTag", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AddServerBuild(request, callback, customData = None, extraHeaders = None):
    """
    Adds the game server executable specified (previously uploaded - see GetServerBuildUploadUrl) to the set of those a
    client is permitted to request in a call to StartGame
    https://docs.microsoft.com/rest/api/playfab/admin/custom-server-management/addserverbuild
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddServerBuild", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AddUserVirtualCurrency(request, callback, customData = None, extraHeaders = None):
    """
    Increments the specified virtual currency by the stated amount
    https://docs.microsoft.com/rest/api/playfab/admin/player-item-management/adduservirtualcurrency
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddUserVirtualCurrency", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AddVirtualCurrencyTypes(request, callback, customData = None, extraHeaders = None):
    """
    Adds one or more virtual currencies to the set defined for the title. Virtual Currencies have a maximum value of
    2,147,483,647 when granted to a player. Any value over that will be discarded.
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/addvirtualcurrencytypes
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddVirtualCurrencyTypes", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def BanUsers(request, callback, customData = None, extraHeaders = None):
    """
    Bans users by PlayFab ID with optional IP address, or MAC address for the provided game.
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/banusers
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/BanUsers", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def CheckLimitedEditionItemAvailability(request, callback, customData = None, extraHeaders = None):
    """
    Checks the global count for the limited edition item.
    https://docs.microsoft.com/rest/api/playfab/admin/player-item-management/checklimitededitionitemavailability
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CheckLimitedEditionItemAvailability", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def CreateActionsOnPlayersInSegmentTask(request, callback, customData = None, extraHeaders = None):
    """
    Create an ActionsOnPlayersInSegment task, which iterates through all players in a segment to execute action.
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/createactionsonplayersinsegmenttask
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CreateActionsOnPlayersInSegmentTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def CreateCloudScriptTask(request, callback, customData = None, extraHeaders = None):
    """
    Create a CloudScript task, which can run a CloudScript on a schedule.
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/createcloudscripttask
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CreateCloudScriptTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def CreateInsightsScheduledScalingTask(request, callback, customData = None, extraHeaders = None):
    """
    Create a Insights Scheduled Scaling task, which can scale Insights Performance Units on a schedule
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/createinsightsscheduledscalingtask
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CreateInsightsScheduledScalingTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def CreateOpenIdConnection(request, callback, customData = None, extraHeaders = None):
    """
    Registers a relationship between a title and an Open ID Connect provider.
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/createopenidconnection
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CreateOpenIdConnection", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def CreatePlayerSharedSecret(request, callback, customData = None, extraHeaders = None):
    """
    Creates a new Player Shared Secret Key. It may take up to 5 minutes for this key to become generally available after
    this API returns.
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/createplayersharedsecret
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CreatePlayerSharedSecret", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def CreatePlayerStatisticDefinition(request, callback, customData = None, extraHeaders = None):
    """
    Adds a new player statistic configuration to the title, optionally allowing the developer to specify a reset interval
    and an aggregation method.
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/createplayerstatisticdefinition
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CreatePlayerStatisticDefinition", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeleteContent(request, callback, customData = None, extraHeaders = None):
    """
    Delete a content file from the title. When deleting a file that does not exist, it returns success.
    https://docs.microsoft.com/rest/api/playfab/admin/content/deletecontent
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteContent", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeleteMasterPlayerAccount(request, callback, customData = None, extraHeaders = None):
    """
    Removes a master player account entirely from all titles and deletes all associated data
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/deletemasterplayeraccount
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteMasterPlayerAccount", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeleteOpenIdConnection(request, callback, customData = None, extraHeaders = None):
    """
    Removes a relationship between a title and an OpenID Connect provider.
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/deleteopenidconnection
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteOpenIdConnection", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeletePlayer(request, callback, customData = None, extraHeaders = None):
    """
    Removes a user's player account from a title and deletes all associated data
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/deleteplayer
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeletePlayer", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeletePlayerSharedSecret(request, callback, customData = None, extraHeaders = None):
    """
    Deletes an existing Player Shared Secret Key. It may take up to 5 minutes for this delete to be reflected after this API
    returns.
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/deleteplayersharedsecret
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeletePlayerSharedSecret", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeleteStore(request, callback, customData = None, extraHeaders = None):
    """
    Deletes an existing virtual item store
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/deletestore
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteStore", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeleteTask(request, callback, customData = None, extraHeaders = None):
    """
    Delete a task.
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/deletetask
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeleteTitle(request, callback, customData = None, extraHeaders = None):
    """
    Permanently deletes a title and all associated configuration
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/deletetitle
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteTitle", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ExportMasterPlayerData(request, callback, customData = None, extraHeaders = None):
    """
    Exports all associated data of a master player account
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/exportmasterplayerdata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ExportMasterPlayerData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetActionsOnPlayersInSegmentTaskInstance(request, callback, customData = None, extraHeaders = None):
    """
    Get information about a ActionsOnPlayersInSegment task instance.
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/getactionsonplayersinsegmenttaskinstance
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetActionsOnPlayersInSegmentTaskInstance", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetAllSegments(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves an array of player segment definitions. Results from this can be used in subsequent API calls such as
    GetPlayersInSegment which requires a Segment ID. While segment names can change the ID for that segment will not change.
    https://docs.microsoft.com/rest/api/playfab/admin/playstream/getallsegments
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetAllSegments", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCatalogItems(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the specified version of the title's catalog of virtual goods, including all defined properties
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/getcatalogitems
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetCatalogItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCloudScriptRevision(request, callback, customData = None, extraHeaders = None):
    """
    Gets the contents and information of a specific Cloud Script revision.
    https://docs.microsoft.com/rest/api/playfab/admin/server-side-cloud-script/getcloudscriptrevision
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetCloudScriptRevision", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCloudScriptTaskInstance(request, callback, customData = None, extraHeaders = None):
    """
    Get detail information about a CloudScript task instance.
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/getcloudscripttaskinstance
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetCloudScriptTaskInstance", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCloudScriptVersions(request, callback, customData = None, extraHeaders = None):
    """
    Lists all the current cloud script versions. For each version, information about the current published and latest
    revisions is also listed.
    https://docs.microsoft.com/rest/api/playfab/admin/server-side-cloud-script/getcloudscriptversions
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetCloudScriptVersions", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetContentList(request, callback, customData = None, extraHeaders = None):
    """
    List all contents of the title and get statistics such as size
    https://docs.microsoft.com/rest/api/playfab/admin/content/getcontentlist
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetContentList", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetContentUploadUrl(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the pre-signed URL for uploading a content file. A subsequent HTTP PUT to the returned URL uploads the
    content. Also, please be aware that the Content service is specifically PlayFab's CDN offering, for which standard CDN
    rates apply.
    https://docs.microsoft.com/rest/api/playfab/admin/content/getcontentuploadurl
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetContentUploadUrl", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetDataReport(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a download URL for the requested report
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/getdatareport
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetDataReport", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetMatchmakerGameInfo(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the details for a specific completed session, including links to standard out and standard error logs
    https://docs.microsoft.com/rest/api/playfab/admin/matchmaking/getmatchmakergameinfo
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetMatchmakerGameInfo", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetMatchmakerGameModes(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the details of defined game modes for the specified game server executable
    https://docs.microsoft.com/rest/api/playfab/admin/matchmaking/getmatchmakergamemodes
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetMatchmakerGameModes", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayedTitleList(request, callback, customData = None, extraHeaders = None):
    """
    Get the list of titles that the player has played
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/getplayedtitlelist
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayedTitleList", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerIdFromAuthToken(request, callback, customData = None, extraHeaders = None):
    """
    Gets a player's ID from an auth token.
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/getplayeridfromauthtoken
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerIdFromAuthToken", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerProfile(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the player's profile
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/getplayerprofile
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerProfile", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerSegments(request, callback, customData = None, extraHeaders = None):
    """
    List all segments that a player currently belongs to at this moment in time.
    https://docs.microsoft.com/rest/api/playfab/admin/playstream/getplayersegments
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerSegments", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerSharedSecrets(request, callback, customData = None, extraHeaders = None):
    """
    Returns all Player Shared Secret Keys including disabled and expired.
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/getplayersharedsecrets
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerSharedSecrets", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayersInSegment(request, callback, customData = None, extraHeaders = None):
    """
    Allows for paging through all players in a given segment. This API creates a snapshot of all player profiles that match
    the segment definition at the time of its creation and lives through the Total Seconds to Live, refreshing its life span
    on each subsequent use of the Continuation Token. Profiles that change during the course of paging will not be reflected
    in the results. AB Test segments are currently not supported by this operation. NOTE: This API is limited to being
    called 30 times in one minute. You will be returned an error if you exceed this threshold.
    https://docs.microsoft.com/rest/api/playfab/admin/playstream/getplayersinsegment
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayersInSegment", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerStatisticDefinitions(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the configuration information for all player statistics defined in the title, regardless of whether they have
    a reset interval.
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/getplayerstatisticdefinitions
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerStatisticDefinitions", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerStatisticVersions(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the information on the available versions of the specified statistic.
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/getplayerstatisticversions
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerStatisticVersions", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerTags(request, callback, customData = None, extraHeaders = None):
    """
    Get all tags with a given Namespace (optional) from a player profile.
    https://docs.microsoft.com/rest/api/playfab/admin/playstream/getplayertags
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerTags", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPolicy(request, callback, customData = None, extraHeaders = None):
    """
    Gets the requested policy.
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/getpolicy
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPolicy", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the key-value store of custom publisher settings
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/getpublisherdata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetRandomResultTables(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the random drop table configuration for the title
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/getrandomresulttables
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetRandomResultTables", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetServerBuildInfo(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the build details for the specified game server executable
    https://docs.microsoft.com/rest/api/playfab/admin/custom-server-management/getserverbuildinfo
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetServerBuildInfo", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetServerBuildUploadUrl(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the pre-authorized URL for uploading a game server package containing a build (does not enable the build for
    use - see AddServerBuild)
    https://docs.microsoft.com/rest/api/playfab/admin/custom-server-management/getserverbuilduploadurl
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetServerBuildUploadUrl", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetStoreItems(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the set of items defined for the specified store, including all prices defined
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/getstoreitems
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetStoreItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetTaskInstances(request, callback, customData = None, extraHeaders = None):
    """
    Query for task instances by task, status, or time range.
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/gettaskinstances
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetTaskInstances", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetTasks(request, callback, customData = None, extraHeaders = None):
    """
    Get definition information on a specified task or all tasks within a title.
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/gettasks
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetTasks", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetTitleData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the key-value store of custom title settings which can be read by the client
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/gettitledata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetTitleData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetTitleInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the key-value store of custom title settings which cannot be read by the client
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/gettitleinternaldata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetTitleInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserAccountInfo(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the relevant details for a specified user, based upon a match against a supplied unique identifier
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/getuseraccountinfo
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserAccountInfo", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserBans(request, callback, customData = None, extraHeaders = None):
    """
    Gets all bans for a user.
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/getuserbans
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserBans", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user which is readable and writable by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/getuserdata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user which cannot be accessed by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/getuserinternaldata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserInventory(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the specified user's current inventory of virtual goods
    https://docs.microsoft.com/rest/api/playfab/admin/player-item-management/getuserinventory
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserInventory", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the publisher-specific custom data for the user which is readable and writable by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/getuserpublisherdata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserPublisherInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the publisher-specific custom data for the user which cannot be accessed by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/getuserpublisherinternaldata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserPublisherInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserPublisherReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the publisher-specific custom data for the user which can only be read by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/getuserpublisherreadonlydata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserPublisherReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user which can only be read by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/getuserreadonlydata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GrantItemsToUsers(request, callback, customData = None, extraHeaders = None):
    """
    Adds the specified items to the specified user inventories
    https://docs.microsoft.com/rest/api/playfab/admin/player-item-management/grantitemstousers
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GrantItemsToUsers", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def IncrementLimitedEditionItemAvailability(request, callback, customData = None, extraHeaders = None):
    """
    Increases the global count for the given scarce resource.
    https://docs.microsoft.com/rest/api/playfab/admin/player-item-management/incrementlimitededitionitemavailability
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/IncrementLimitedEditionItemAvailability", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def IncrementPlayerStatisticVersion(request, callback, customData = None, extraHeaders = None):
    """
    Resets the indicated statistic, removing all player entries for it and backing up the old values.
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/incrementplayerstatisticversion
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/IncrementPlayerStatisticVersion", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ListOpenIdConnection(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of all Open ID Connect providers registered to a title.
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/listopenidconnection
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ListOpenIdConnection", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ListServerBuilds(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the build details for all game server executables which are currently defined for the title
    https://docs.microsoft.com/rest/api/playfab/admin/custom-server-management/listserverbuilds
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ListServerBuilds", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ListVirtualCurrencyTypes(request, callback, customData = None, extraHeaders = None):
    """
    Retuns the list of all defined virtual currencies for the title
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/listvirtualcurrencytypes
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ListVirtualCurrencyTypes", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ModifyMatchmakerGameModes(request, callback, customData = None, extraHeaders = None):
    """
    Updates the game server mode details for the specified game server executable
    https://docs.microsoft.com/rest/api/playfab/admin/matchmaking/modifymatchmakergamemodes
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ModifyMatchmakerGameModes", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ModifyServerBuild(request, callback, customData = None, extraHeaders = None):
    """
    Updates the build details for the specified game server executable
    https://docs.microsoft.com/rest/api/playfab/admin/custom-server-management/modifyserverbuild
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ModifyServerBuild", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RefundPurchase(request, callback, customData = None, extraHeaders = None):
    """
    Attempts to process an order refund through the original real money payment provider.
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/refundpurchase
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RefundPurchase", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RemovePlayerTag(request, callback, customData = None, extraHeaders = None):
    """
    Remove a given tag from a player profile. The tag's namespace is automatically generated based on the source of the tag.
    https://docs.microsoft.com/rest/api/playfab/admin/playstream/removeplayertag
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RemovePlayerTag", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RemoveServerBuild(request, callback, customData = None, extraHeaders = None):
    """
    Removes the game server executable specified from the set of those a client is permitted to request in a call to
    StartGame
    https://docs.microsoft.com/rest/api/playfab/admin/custom-server-management/removeserverbuild
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RemoveServerBuild", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RemoveVirtualCurrencyTypes(request, callback, customData = None, extraHeaders = None):
    """
    Removes one or more virtual currencies from the set defined for the title.
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/removevirtualcurrencytypes
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RemoveVirtualCurrencyTypes", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ResetCharacterStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Completely removes all statistics for the specified character, for the current game
    https://docs.microsoft.com/rest/api/playfab/admin/characters/resetcharacterstatistics
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ResetCharacterStatistics", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ResetPassword(request, callback, customData = None, extraHeaders = None):
    """
    Reset a player's password for a given title.
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/resetpassword
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ResetPassword", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ResetUserStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Completely removes all statistics for the specified user, for the current game
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/resetuserstatistics
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ResetUserStatistics", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ResolvePurchaseDispute(request, callback, customData = None, extraHeaders = None):
    """
    Attempts to resolve a dispute with the original order's payment provider.
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/resolvepurchasedispute
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ResolvePurchaseDispute", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RevokeAllBansForUser(request, callback, customData = None, extraHeaders = None):
    """
    Revoke all active bans for a user.
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/revokeallbansforuser
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RevokeAllBansForUser", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RevokeBans(request, callback, customData = None, extraHeaders = None):
    """
    Revoke all active bans specified with BanId.
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/revokebans
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RevokeBans", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RevokeInventoryItem(request, callback, customData = None, extraHeaders = None):
    """
    Revokes access to an item in a user's inventory
    https://docs.microsoft.com/rest/api/playfab/admin/player-item-management/revokeinventoryitem
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RevokeInventoryItem", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RevokeInventoryItems(request, callback, customData = None, extraHeaders = None):
    """
    Revokes access for up to 25 items across multiple users and characters.
    https://docs.microsoft.com/rest/api/playfab/admin/player-item-management/revokeinventoryitems
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RevokeInventoryItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RunTask(request, callback, customData = None, extraHeaders = None):
    """
    Run a task immediately regardless of its schedule.
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/runtask
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RunTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SendAccountRecoveryEmail(request, callback, customData = None, extraHeaders = None):
    """
    Forces an email to be sent to the registered email address for the user's account, with a link allowing the user to
    change the password.If an account recovery email template ID is provided, an email using the custom email template will
    be used.
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/sendaccountrecoveryemail
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SendAccountRecoveryEmail", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetCatalogItems(request, callback, customData = None, extraHeaders = None):
    """
    Creates the catalog configuration of all virtual goods for the specified catalog version
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/setcatalogitems
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetCatalogItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetPlayerSecret(request, callback, customData = None, extraHeaders = None):
    """
    Sets or resets the player's secret. Player secrets are used to sign API requests.
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/setplayersecret
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetPlayerSecret", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetPublishedRevision(request, callback, customData = None, extraHeaders = None):
    """
    Sets the currently published revision of a title Cloud Script
    https://docs.microsoft.com/rest/api/playfab/admin/server-side-cloud-script/setpublishedrevision
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetPublishedRevision", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the key-value store of custom publisher settings
    https://docs.microsoft.com/rest/api/playfab/admin/shared-group-data/setpublisherdata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetStoreItems(request, callback, customData = None, extraHeaders = None):
    """
    Sets all the items in one virtual store
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/setstoreitems
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetStoreItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetTitleData(request, callback, customData = None, extraHeaders = None):
    """
    Creates and updates the key-value store of custom title settings which can be read by the client
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/settitledata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetTitleData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetTitleInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the key-value store of custom title settings which cannot be read by the client
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/settitleinternaldata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetTitleInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetupPushNotification(request, callback, customData = None, extraHeaders = None):
    """
    Sets the Amazon Resource Name (ARN) for iOS and Android push notifications. Documentation on the exact restrictions can
    be found at: http://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformApplication.html. Currently, Amazon device
    Messaging is not supported.
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/setuppushnotification
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetupPushNotification", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SubtractUserVirtualCurrency(request, callback, customData = None, extraHeaders = None):
    """
    Decrements the specified virtual currency by the stated amount
    https://docs.microsoft.com/rest/api/playfab/admin/player-item-management/subtractuservirtualcurrency
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SubtractUserVirtualCurrency", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateBans(request, callback, customData = None, extraHeaders = None):
    """
    Updates information of a list of existing bans specified with Ban Ids.
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/updatebans
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateBans", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateCatalogItems(request, callback, customData = None, extraHeaders = None):
    """
    Updates the catalog configuration for virtual goods in the specified catalog version
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/updatecatalogitems
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateCatalogItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateCloudScript(request, callback, customData = None, extraHeaders = None):
    """
    Creates a new Cloud Script revision and uploads source code to it. Note that at this time, only one file should be
    submitted in the revision.
    https://docs.microsoft.com/rest/api/playfab/admin/server-side-cloud-script/updatecloudscript
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateCloudScript", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateOpenIdConnection(request, callback, customData = None, extraHeaders = None):
    """
    Modifies data and credentials for an existing relationship between a title and an Open ID Connect provider
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/updateopenidconnection
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateOpenIdConnection", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdatePlayerSharedSecret(request, callback, customData = None, extraHeaders = None):
    """
    Updates a existing Player Shared Secret Key. It may take up to 5 minutes for this update to become generally available
    after this API returns.
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/updateplayersharedsecret
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdatePlayerSharedSecret", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdatePlayerStatisticDefinition(request, callback, customData = None, extraHeaders = None):
    """
    Updates a player statistic configuration for the title, optionally allowing the developer to specify a reset interval.
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/updateplayerstatisticdefinition
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdatePlayerStatisticDefinition", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdatePolicy(request, callback, customData = None, extraHeaders = None):
    """
    Changes a policy for a title
    https://docs.microsoft.com/rest/api/playfab/admin/authentication/updatepolicy
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdatePolicy", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateRandomResultTables(request, callback, customData = None, extraHeaders = None):
    """
    Updates the random drop table configuration for the title
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/updaterandomresulttables
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateRandomResultTables", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateStoreItems(request, callback, customData = None, extraHeaders = None):
    """
    Updates an existing virtual item store with new or modified items
    https://docs.microsoft.com/rest/api/playfab/admin/title-wide-data-management/updatestoreitems
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateStoreItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateTask(request, callback, customData = None, extraHeaders = None):
    """
    Update an existing task.
    https://docs.microsoft.com/rest/api/playfab/admin/scheduledtask/updatetask
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title-specific custom data for the user which is readable and writable by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/updateuserdata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title-specific custom data for the user which cannot be accessed by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/updateuserinternaldata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the publisher-specific custom data for the user which is readable and writable by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/updateuserpublisherdata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserPublisherInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the publisher-specific custom data for the user which cannot be accessed by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/updateuserpublisherinternaldata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserPublisherInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserPublisherReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the publisher-specific custom data for the user which can only be read by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/updateuserpublisherreadonlydata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserPublisherReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title-specific custom data for the user which can only be read by the client
    https://docs.microsoft.com/rest/api/playfab/admin/player-data-management/updateuserreadonlydata
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserTitleDisplayName(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title specific display name for a user
    https://docs.microsoft.com/rest/api/playfab/admin/account-management/updateusertitledisplayname
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserTitleDisplayName", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)


