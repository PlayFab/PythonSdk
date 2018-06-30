import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

# APIs for managing title configurations, uploaded Game Server code executables, and user data



# Abort an ongoing task instance.
# https://api.playfab.com/documentation/admin/method/AbortTaskInstance
def AbortTaskInstance(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AbortTaskInstance", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Adds a new news item to the title's news feed
# https://api.playfab.com/documentation/admin/method/AddNews
def AddNews(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddNews", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Adds a given tag to a player profile. The tag's namespace is automatically generated based on the source of the tag.
# https://api.playfab.com/documentation/admin/method/AddPlayerTag
def AddPlayerTag(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddPlayerTag", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Adds the game server executable specified (previously uploaded - see GetServerBuildUploadUrl) to the set of those a
# client is permitted to request in a call to StartGame
# https://api.playfab.com/documentation/admin/method/AddServerBuild
def AddServerBuild(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddServerBuild", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Increments the specified virtual currency by the stated amount
# https://api.playfab.com/documentation/admin/method/AddUserVirtualCurrency
def AddUserVirtualCurrency(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddUserVirtualCurrency", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Adds one or more virtual currencies to the set defined for the title. Virtual Currencies have a maximum value of
# 2,147,483,647 when granted to a player. Any value over that will be discarded.
# https://api.playfab.com/documentation/admin/method/AddVirtualCurrencyTypes
def AddVirtualCurrencyTypes(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/AddVirtualCurrencyTypes", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Bans users by PlayFab ID with optional IP address, or MAC address for the provided game.
# https://api.playfab.com/documentation/admin/method/BanUsers
def BanUsers(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/BanUsers", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Checks the global count for the limited edition item.
# https://api.playfab.com/documentation/admin/method/CheckLimitedEditionItemAvailability
def CheckLimitedEditionItemAvailability(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CheckLimitedEditionItemAvailability", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Create an ActionsOnPlayersInSegment task, which iterates through all players in a segment to execute action.
# https://api.playfab.com/documentation/admin/method/CreateActionsOnPlayersInSegmentTask
def CreateActionsOnPlayersInSegmentTask(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CreateActionsOnPlayersInSegmentTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Create a CloudScript task, which can run a CloudScript on a schedule.
# https://api.playfab.com/documentation/admin/method/CreateCloudScriptTask
def CreateCloudScriptTask(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CreateCloudScriptTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Creates a new Player Shared Secret Key. It may take up to 5 minutes for this key to become generally available after
# this API returns.
# https://api.playfab.com/documentation/admin/method/CreatePlayerSharedSecret
def CreatePlayerSharedSecret(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CreatePlayerSharedSecret", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Adds a new player statistic configuration to the title, optionally allowing the developer to specify a reset interval
# and an aggregation method.
# https://api.playfab.com/documentation/admin/method/CreatePlayerStatisticDefinition
def CreatePlayerStatisticDefinition(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/CreatePlayerStatisticDefinition", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Delete a content file from the title. When deleting a file that does not exist, it returns success.
# https://api.playfab.com/documentation/admin/method/DeleteContent
def DeleteContent(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteContent", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Removes a master player account entirely from all titles and deletes all associated data
# https://api.playfab.com/documentation/admin/method/DeleteMasterPlayerAccount
def DeleteMasterPlayerAccount(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteMasterPlayerAccount", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Removes a user's player account from a title and deletes all associated data
# https://api.playfab.com/documentation/admin/method/DeletePlayer
def DeletePlayer(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeletePlayer", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Deletes an existing Player Shared Secret Key. It may take up to 5 minutes for this delete to be reflected after this API
# returns.
# https://api.playfab.com/documentation/admin/method/DeletePlayerSharedSecret
def DeletePlayerSharedSecret(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeletePlayerSharedSecret", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Deletes an existing virtual item store
# https://api.playfab.com/documentation/admin/method/DeleteStore
def DeleteStore(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteStore", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Delete a task.
# https://api.playfab.com/documentation/admin/method/DeleteTask
def DeleteTask(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Permanently deletes a title and all associated configuration
# https://api.playfab.com/documentation/admin/method/DeleteTitle
def DeleteTitle(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/DeleteTitle", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Exports all associated data of a master player account
# https://api.playfab.com/documentation/admin/method/ExportMasterPlayerData
def ExportMasterPlayerData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ExportMasterPlayerData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Get information about a ActionsOnPlayersInSegment task instance.
# https://api.playfab.com/documentation/admin/method/GetActionsOnPlayersInSegmentTaskInstance
def GetActionsOnPlayersInSegmentTaskInstance(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetActionsOnPlayersInSegmentTaskInstance", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves an array of player segment definitions. Results from this can be used in subsequent API calls such as
# GetPlayersInSegment which requires a Segment ID. While segment names can change the ID for that segment will not change.
# https://api.playfab.com/documentation/admin/method/GetAllSegments
def GetAllSegments(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetAllSegments", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the specified version of the title's catalog of virtual goods, including all defined properties
# https://api.playfab.com/documentation/admin/method/GetCatalogItems
def GetCatalogItems(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetCatalogItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Gets the contents and information of a specific Cloud Script revision.
# https://api.playfab.com/documentation/admin/method/GetCloudScriptRevision
def GetCloudScriptRevision(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetCloudScriptRevision", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Get detail information about a CloudScript task instance.
# https://api.playfab.com/documentation/admin/method/GetCloudScriptTaskInstance
def GetCloudScriptTaskInstance(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetCloudScriptTaskInstance", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Lists all the current cloud script versions. For each version, information about the current published and latest
# revisions is also listed.
# https://api.playfab.com/documentation/admin/method/GetCloudScriptVersions
def GetCloudScriptVersions(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetCloudScriptVersions", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# List all contents of the title and get statistics such as size
# https://api.playfab.com/documentation/admin/method/GetContentList
def GetContentList(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetContentList", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the pre-signed URL for uploading a content file. A subsequent HTTP PUT to the returned URL uploads the
# content. Also, please be aware that the Content service is specifically PlayFab's CDN offering, for which standard CDN
# rates apply.
# https://api.playfab.com/documentation/admin/method/GetContentUploadUrl
def GetContentUploadUrl(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetContentUploadUrl", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves a download URL for the requested report
# https://api.playfab.com/documentation/admin/method/GetDataReport
def GetDataReport(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetDataReport", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the details for a specific completed session, including links to standard out and standard error logs
# https://api.playfab.com/documentation/admin/method/GetMatchmakerGameInfo
def GetMatchmakerGameInfo(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetMatchmakerGameInfo", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the details of defined game modes for the specified game server executable
# https://api.playfab.com/documentation/admin/method/GetMatchmakerGameModes
def GetMatchmakerGameModes(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetMatchmakerGameModes", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Get the list of titles that the player has played
# https://api.playfab.com/documentation/admin/method/GetPlayedTitleList
def GetPlayedTitleList(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayedTitleList", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Gets a player's ID from an auth token.
# https://api.playfab.com/documentation/admin/method/GetPlayerIdFromAuthToken
def GetPlayerIdFromAuthToken(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerIdFromAuthToken", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the player's profile
# https://api.playfab.com/documentation/admin/method/GetPlayerProfile
def GetPlayerProfile(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerProfile", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# List all segments that a player currently belongs to at this moment in time.
# https://api.playfab.com/documentation/admin/method/GetPlayerSegments
def GetPlayerSegments(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerSegments", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Returns all Player Shared Secret Keys including disabled and expired.
# https://api.playfab.com/documentation/admin/method/GetPlayerSharedSecrets
def GetPlayerSharedSecrets(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerSharedSecrets", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Allows for paging through all players in a given segment. This API creates a snapshot of all player profiles that match
# the segment definition at the time of its creation and lives through the Total Seconds to Live, refreshing its life span
# on each subsequent use of the Continuation Token. Profiles that change during the course of paging will not be reflected
# in the results. AB Test segments are currently not supported by this operation.
# https://api.playfab.com/documentation/admin/method/GetPlayersInSegment
def GetPlayersInSegment(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayersInSegment", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the configuration information for all player statistics defined in the title, regardless of whether they have
# a reset interval.
# https://api.playfab.com/documentation/admin/method/GetPlayerStatisticDefinitions
def GetPlayerStatisticDefinitions(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerStatisticDefinitions", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the information on the available versions of the specified statistic.
# https://api.playfab.com/documentation/admin/method/GetPlayerStatisticVersions
def GetPlayerStatisticVersions(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerStatisticVersions", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Get all tags with a given Namespace (optional) from a player profile.
# https://api.playfab.com/documentation/admin/method/GetPlayerTags
def GetPlayerTags(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPlayerTags", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Gets the requested policy.
# https://api.playfab.com/documentation/admin/method/GetPolicy
def GetPolicy(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPolicy", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the key-value store of custom publisher settings
# https://api.playfab.com/documentation/admin/method/GetPublisherData
def GetPublisherData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the random drop table configuration for the title
# https://api.playfab.com/documentation/admin/method/GetRandomResultTables
def GetRandomResultTables(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetRandomResultTables", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the build details for the specified game server executable
# https://api.playfab.com/documentation/admin/method/GetServerBuildInfo
def GetServerBuildInfo(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetServerBuildInfo", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the pre-authorized URL for uploading a game server package containing a build (does not enable the build for
# use - see AddServerBuild)
# https://api.playfab.com/documentation/admin/method/GetServerBuildUploadUrl
def GetServerBuildUploadUrl(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetServerBuildUploadUrl", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the set of items defined for the specified store, including all prices defined
# https://api.playfab.com/documentation/admin/method/GetStoreItems
def GetStoreItems(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetStoreItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Query for task instances by task, status, or time range.
# https://api.playfab.com/documentation/admin/method/GetTaskInstances
def GetTaskInstances(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetTaskInstances", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Get definition information on a specified task or all tasks within a title.
# https://api.playfab.com/documentation/admin/method/GetTasks
def GetTasks(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetTasks", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the key-value store of custom title settings which can be read by the client
# https://api.playfab.com/documentation/admin/method/GetTitleData
def GetTitleData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetTitleData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the key-value store of custom title settings which cannot be read by the client
# https://api.playfab.com/documentation/admin/method/GetTitleInternalData
def GetTitleInternalData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetTitleInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the relevant details for a specified user, based upon a match against a supplied unique identifier
# https://api.playfab.com/documentation/admin/method/GetUserAccountInfo
def GetUserAccountInfo(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserAccountInfo", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Gets all bans for a user.
# https://api.playfab.com/documentation/admin/method/GetUserBans
def GetUserBans(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserBans", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the title-specific custom data for the user which is readable and writable by the client
# https://api.playfab.com/documentation/admin/method/GetUserData
def GetUserData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the title-specific custom data for the user which cannot be accessed by the client
# https://api.playfab.com/documentation/admin/method/GetUserInternalData
def GetUserInternalData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the specified user's current inventory of virtual goods
# https://api.playfab.com/documentation/admin/method/GetUserInventory
def GetUserInventory(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserInventory", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the publisher-specific custom data for the user which is readable and writable by the client
# https://api.playfab.com/documentation/admin/method/GetUserPublisherData
def GetUserPublisherData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the publisher-specific custom data for the user which cannot be accessed by the client
# https://api.playfab.com/documentation/admin/method/GetUserPublisherInternalData
def GetUserPublisherInternalData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserPublisherInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the publisher-specific custom data for the user which can only be read by the client
# https://api.playfab.com/documentation/admin/method/GetUserPublisherReadOnlyData
def GetUserPublisherReadOnlyData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserPublisherReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the title-specific custom data for the user which can only be read by the client
# https://api.playfab.com/documentation/admin/method/GetUserReadOnlyData
def GetUserReadOnlyData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GetUserReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Adds the specified items to the specified user inventories
# https://api.playfab.com/documentation/admin/method/GrantItemsToUsers
def GrantItemsToUsers(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/GrantItemsToUsers", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Increases the global count for the given scarce resource.
# https://api.playfab.com/documentation/admin/method/IncrementLimitedEditionItemAvailability
def IncrementLimitedEditionItemAvailability(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/IncrementLimitedEditionItemAvailability", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Resets the indicated statistic, removing all player entries for it and backing up the old values.
# https://api.playfab.com/documentation/admin/method/IncrementPlayerStatisticVersion
def IncrementPlayerStatisticVersion(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/IncrementPlayerStatisticVersion", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the build details for all game server executables which are currently defined for the title
# https://api.playfab.com/documentation/admin/method/ListServerBuilds
def ListServerBuilds(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ListServerBuilds", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retuns the list of all defined virtual currencies for the title
# https://api.playfab.com/documentation/admin/method/ListVirtualCurrencyTypes
def ListVirtualCurrencyTypes(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ListVirtualCurrencyTypes", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the game server mode details for the specified game server executable
# https://api.playfab.com/documentation/admin/method/ModifyMatchmakerGameModes
def ModifyMatchmakerGameModes(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ModifyMatchmakerGameModes", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the build details for the specified game server executable
# https://api.playfab.com/documentation/admin/method/ModifyServerBuild
def ModifyServerBuild(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ModifyServerBuild", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Attempts to process an order refund through the original real money payment provider.
# https://api.playfab.com/documentation/admin/method/RefundPurchase
def RefundPurchase(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RefundPurchase", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Remove a given tag from a player profile. The tag's namespace is automatically generated based on the source of the tag.
# https://api.playfab.com/documentation/admin/method/RemovePlayerTag
def RemovePlayerTag(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RemovePlayerTag", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Removes the game server executable specified from the set of those a client is permitted to request in a call to
# StartGame
# https://api.playfab.com/documentation/admin/method/RemoveServerBuild
def RemoveServerBuild(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RemoveServerBuild", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Removes one or more virtual currencies from the set defined for the title.
# https://api.playfab.com/documentation/admin/method/RemoveVirtualCurrencyTypes
def RemoveVirtualCurrencyTypes(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RemoveVirtualCurrencyTypes", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Completely removes all statistics for the specified character, for the current game
# https://api.playfab.com/documentation/admin/method/ResetCharacterStatistics
def ResetCharacterStatistics(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ResetCharacterStatistics", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Reset a player's password for a given title.
# https://api.playfab.com/documentation/admin/method/ResetPassword
def ResetPassword(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ResetPassword", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Completely removes all statistics for the specified user, for the current game
# https://api.playfab.com/documentation/admin/method/ResetUserStatistics
def ResetUserStatistics(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ResetUserStatistics", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Attempts to resolve a dispute with the original order's payment provider.
# https://api.playfab.com/documentation/admin/method/ResolvePurchaseDispute
def ResolvePurchaseDispute(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/ResolvePurchaseDispute", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Revoke all active bans for a user.
# https://api.playfab.com/documentation/admin/method/RevokeAllBansForUser
def RevokeAllBansForUser(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RevokeAllBansForUser", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Revoke all active bans specified with BanId.
# https://api.playfab.com/documentation/admin/method/RevokeBans
def RevokeBans(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RevokeBans", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Revokes access to an item in a user's inventory
# https://api.playfab.com/documentation/admin/method/RevokeInventoryItem
def RevokeInventoryItem(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RevokeInventoryItem", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Revokes access for up to 25 items across multiple users and characters.
# https://api.playfab.com/documentation/admin/method/RevokeInventoryItems
def RevokeInventoryItems(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RevokeInventoryItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Run a task immediately regardless of its schedule.
# https://api.playfab.com/documentation/admin/method/RunTask
def RunTask(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/RunTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Forces an email to be sent to the registered email address for the user's account, with a link allowing the user to
# change the password.If an account recovery email template ID is provided, an email using the custom email template will
# be used.
# https://api.playfab.com/documentation/admin/method/SendAccountRecoveryEmail
def SendAccountRecoveryEmail(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SendAccountRecoveryEmail", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Creates the catalog configuration of all virtual goods for the specified catalog version
# https://api.playfab.com/documentation/admin/method/SetCatalogItems
def SetCatalogItems(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetCatalogItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Sets or resets the player's secret. Player secrets are used to sign API requests.
# https://api.playfab.com/documentation/admin/method/SetPlayerSecret
def SetPlayerSecret(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetPlayerSecret", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Sets the currently published revision of a title Cloud Script
# https://api.playfab.com/documentation/admin/method/SetPublishedRevision
def SetPublishedRevision(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetPublishedRevision", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the key-value store of custom publisher settings
# https://api.playfab.com/documentation/admin/method/SetPublisherData
def SetPublisherData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Sets all the items in one virtual store
# https://api.playfab.com/documentation/admin/method/SetStoreItems
def SetStoreItems(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetStoreItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Creates and updates the key-value store of custom title settings which can be read by the client
# https://api.playfab.com/documentation/admin/method/SetTitleData
def SetTitleData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetTitleData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the key-value store of custom title settings which cannot be read by the client
# https://api.playfab.com/documentation/admin/method/SetTitleInternalData
def SetTitleInternalData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetTitleInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Sets the Amazon Resource Name (ARN) for iOS and Android push notifications. Documentation on the exact restrictions can
# be found at: http://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformApplication.html. Currently, Amazon device
# Messaging is not supported.
# https://api.playfab.com/documentation/admin/method/SetupPushNotification
def SetupPushNotification(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SetupPushNotification", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Decrements the specified virtual currency by the stated amount
# https://api.playfab.com/documentation/admin/method/SubtractUserVirtualCurrency
def SubtractUserVirtualCurrency(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/SubtractUserVirtualCurrency", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates information of a list of existing bans specified with Ban Ids.
# https://api.playfab.com/documentation/admin/method/UpdateBans
def UpdateBans(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateBans", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the catalog configuration for virtual goods in the specified catalog version
# https://api.playfab.com/documentation/admin/method/UpdateCatalogItems
def UpdateCatalogItems(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateCatalogItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Creates a new Cloud Script revision and uploads source code to it. Note that at this time, only one file should be
# submitted in the revision.
# https://api.playfab.com/documentation/admin/method/UpdateCloudScript
def UpdateCloudScript(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateCloudScript", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates a existing Player Shared Secret Key. It may take up to 5 minutes for this update to become generally available
# after this API returns.
# https://api.playfab.com/documentation/admin/method/UpdatePlayerSharedSecret
def UpdatePlayerSharedSecret(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdatePlayerSharedSecret", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates a player statistic configuration for the title, optionally allowing the developer to specify a reset interval.
# https://api.playfab.com/documentation/admin/method/UpdatePlayerStatisticDefinition
def UpdatePlayerStatisticDefinition(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdatePlayerStatisticDefinition", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Changes a policy for a title
# https://api.playfab.com/documentation/admin/method/UpdatePolicy
def UpdatePolicy(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdatePolicy", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the random drop table configuration for the title
# https://api.playfab.com/documentation/admin/method/UpdateRandomResultTables
def UpdateRandomResultTables(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateRandomResultTables", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates an existing virtual item store with new or modified items
# https://api.playfab.com/documentation/admin/method/UpdateStoreItems
def UpdateStoreItems(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateStoreItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Update an existing task.
# https://api.playfab.com/documentation/admin/method/UpdateTask
def UpdateTask(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateTask", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the title-specific custom data for the user which is readable and writable by the client
# https://api.playfab.com/documentation/admin/method/UpdateUserData
def UpdateUserData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the title-specific custom data for the user which cannot be accessed by the client
# https://api.playfab.com/documentation/admin/method/UpdateUserInternalData
def UpdateUserInternalData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the publisher-specific custom data for the user which is readable and writable by the client
# https://api.playfab.com/documentation/admin/method/UpdateUserPublisherData
def UpdateUserPublisherData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the publisher-specific custom data for the user which cannot be accessed by the client
# https://api.playfab.com/documentation/admin/method/UpdateUserPublisherInternalData
def UpdateUserPublisherInternalData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserPublisherInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the publisher-specific custom data for the user which can only be read by the client
# https://api.playfab.com/documentation/admin/method/UpdateUserPublisherReadOnlyData
def UpdateUserPublisherReadOnlyData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserPublisherReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the title-specific custom data for the user which can only be read by the client
# https://api.playfab.com/documentation/admin/method/UpdateUserReadOnlyData
def UpdateUserReadOnlyData(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Updates the title specific display name for a user
# https://api.playfab.com/documentation/admin/method/UpdateUserTitleDisplayName
def UpdateUserTitleDisplayName(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Admin/UpdateUserTitleDisplayName", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

