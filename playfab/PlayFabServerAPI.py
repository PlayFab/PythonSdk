import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

"""
Provides functionality to allow external (developer-controlled) servers to interact with user inventories and data in a
trusted manner, and to handle matchmaking and client connection orchestration
"""

def AddCharacterVirtualCurrency(request, callback, customData = None, extraHeaders = None):
    """
    Increments the character's balance of the specified virtual currency by the stated amount
    https://api.playfab.com/documentation/server/method/AddCharacterVirtualCurrency
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/AddCharacterVirtualCurrency", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AddFriend(request, callback, customData = None, extraHeaders = None):
    """
    Adds the Friend user to the friendlist of the user with PlayFabId. At least one of
    FriendPlayFabId,FriendUsername,FriendEmail, or FriendTitleDisplayName should be initialized.
    https://api.playfab.com/documentation/server/method/AddFriend
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/AddFriend", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AddPlayerTag(request, callback, customData = None, extraHeaders = None):
    """
    Adds a given tag to a player profile. The tag's namespace is automatically generated based on the source of the tag.
    https://api.playfab.com/documentation/server/method/AddPlayerTag
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/AddPlayerTag", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AddSharedGroupMembers(request, callback, customData = None, extraHeaders = None):
    """
    Adds users to the set of those able to update both the shared data, as well as the set of users in the group. Only users
    in the group (and the server) can add new members. Shared Groups are designed for sharing data between a very small
    number of players, please see our guide: https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/server/method/AddSharedGroupMembers
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/AddSharedGroupMembers", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AddUserVirtualCurrency(request, callback, customData = None, extraHeaders = None):
    """
    Increments the user's balance of the specified virtual currency by the stated amount
    https://api.playfab.com/documentation/server/method/AddUserVirtualCurrency
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/AddUserVirtualCurrency", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AuthenticateSessionTicket(request, callback, customData = None, extraHeaders = None):
    """
    Validated a client's session ticket, and if successful, returns details for that user
    https://api.playfab.com/documentation/server/method/AuthenticateSessionTicket
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/AuthenticateSessionTicket", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def AwardSteamAchievement(request, callback, customData = None, extraHeaders = None):
    """
    Awards the specified users the specified Steam achievements
    https://api.playfab.com/documentation/server/method/AwardSteamAchievement
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/AwardSteamAchievement", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def BanUsers(request, callback, customData = None, extraHeaders = None):
    """
    Bans users by PlayFab ID with optional IP address, or MAC address for the provided game.
    https://api.playfab.com/documentation/server/method/BanUsers
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/BanUsers", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ConsumeItem(request, callback, customData = None, extraHeaders = None):
    """
    Consume uses of a consumable item. When all uses are consumed, it will be removed from the player's inventory.
    https://api.playfab.com/documentation/server/method/ConsumeItem
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/ConsumeItem", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def CreateSharedGroup(request, callback, customData = None, extraHeaders = None):
    """
    Requests the creation of a shared group object, containing key/value pairs which may be updated by all members of the
    group. When created by a server, the group will initially have no members. Shared Groups are designed for sharing data
    between a very small number of players, please see our guide:
    https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/server/method/CreateSharedGroup
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/CreateSharedGroup", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeleteCharacterFromUser(request, callback, customData = None, extraHeaders = None):
    """
    Deletes the specific character ID from the specified user.
    https://api.playfab.com/documentation/server/method/DeleteCharacterFromUser
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/DeleteCharacterFromUser", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeletePlayer(request, callback, customData = None, extraHeaders = None):
    """
    Removes a user's player account from a title and deletes all associated data
    https://api.playfab.com/documentation/server/method/DeletePlayer
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/DeletePlayer", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeleteSharedGroup(request, callback, customData = None, extraHeaders = None):
    """
    Deletes a shared group, freeing up the shared group ID to be reused for a new group. Shared Groups are designed for
    sharing data between a very small number of players, please see our guide:
    https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/server/method/DeleteSharedGroup
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/DeleteSharedGroup", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# [Obsolete("Use 'DeletePlayer' instead", false)]
def DeleteUsers(request, callback, customData = None, extraHeaders = None):
    """
    Deletes custom data, all account linkages, and statistics.
    https://api.playfab.com/documentation/server/method/DeleteUsers
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/DeleteUsers", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def DeregisterGame(request, callback, customData = None, extraHeaders = None):
    """
    Inform the matchmaker that a Game Server Instance is removed.
    https://api.playfab.com/documentation/server/method/DeregisterGame
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/DeregisterGame", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def EvaluateRandomResultTable(request, callback, customData = None, extraHeaders = None):
    """
    Returns the result of an evaluation of a Random Result Table - the ItemId from the game Catalog which would have been
    added to the player inventory, if the Random Result Table were added via a Bundle or a call to UnlockContainer.
    https://api.playfab.com/documentation/server/method/EvaluateRandomResultTable
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/EvaluateRandomResultTable", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ExecuteCloudScript(request, callback, customData = None, extraHeaders = None):
    """
    Executes a CloudScript function, with the 'currentPlayerId' variable set to the specified PlayFabId parameter value.
    https://api.playfab.com/documentation/server/method/ExecuteCloudScript
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/ExecuteCloudScript", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetAllSegments(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves an array of player segment definitions. Results from this can be used in subsequent API calls such as
    GetPlayersInSegment which requires a Segment ID. While segment names can change the ID for that segment will not change.
    https://api.playfab.com/documentation/server/method/GetAllSegments
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetAllSegments", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetAllUsersCharacters(request, callback, customData = None, extraHeaders = None):
    """
    Lists all of the characters that belong to a specific user. CharacterIds are not globally unique; characterId must be
    evaluated with the parent PlayFabId to guarantee uniqueness.
    https://api.playfab.com/documentation/server/method/GetAllUsersCharacters
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetAllUsersCharacters", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCatalogItems(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the specified version of the title's catalog of virtual goods, including all defined properties
    https://api.playfab.com/documentation/server/method/GetCatalogItems
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetCatalogItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCharacterData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user which is readable and writable by the client
    https://api.playfab.com/documentation/server/method/GetCharacterData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetCharacterData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCharacterInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user's character which cannot be accessed by the client
    https://api.playfab.com/documentation/server/method/GetCharacterInternalData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetCharacterInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCharacterInventory(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the specified character's current inventory of virtual goods
    https://api.playfab.com/documentation/server/method/GetCharacterInventory
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetCharacterInventory", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCharacterLeaderboard(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked characters for the given statistic, starting from the indicated point in the leaderboard
    https://api.playfab.com/documentation/server/method/GetCharacterLeaderboard
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetCharacterLeaderboard", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCharacterReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user's character which can only be read by the client
    https://api.playfab.com/documentation/server/method/GetCharacterReadOnlyData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetCharacterReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetCharacterStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the details of all title-specific statistics for the specific character
    https://api.playfab.com/documentation/server/method/GetCharacterStatistics
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetCharacterStatistics", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetContentDownloadUrl(request, callback, customData = None, extraHeaders = None):
    """
    This API retrieves a pre-signed URL for accessing a content file for the title. A subsequent HTTP GET to the returned
    URL will attempt to download the content. A HEAD query to the returned URL will attempt to retrieve the metadata of the
    content. Note that a successful result does not guarantee the existence of this content - if it has not been uploaded,
    the query to retrieve the data will fail. See this post for more information:
    https://community.playfab.com/hc/en-us/community/posts/205469488-How-to-upload-files-to-PlayFab-s-Content-Service. Also,
    please be aware that the Content service is specifically PlayFab's CDN offering, for which standard CDN rates apply.
    https://api.playfab.com/documentation/server/method/GetContentDownloadUrl
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetContentDownloadUrl", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetFriendLeaderboard(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked friends of the given player for the given statistic, starting from the indicated point in the
    leaderboard
    https://api.playfab.com/documentation/server/method/GetFriendLeaderboard
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetFriendLeaderboard", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetFriendsList(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the current friends for the user with PlayFabId, constrained to users who have PlayFab accounts. Friends from
    linked accounts (Facebook, Steam) are also included. You may optionally exclude some linked services' friends.
    https://api.playfab.com/documentation/server/method/GetFriendsList
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetFriendsList", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetLeaderboard(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked users for the given statistic, starting from the indicated point in the leaderboard
    https://api.playfab.com/documentation/server/method/GetLeaderboard
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetLeaderboard", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetLeaderboardAroundCharacter(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked characters for the given statistic, centered on the requested user
    https://api.playfab.com/documentation/server/method/GetLeaderboardAroundCharacter
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetLeaderboardAroundCharacter", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetLeaderboardAroundUser(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked users for the given statistic, centered on the currently signed-in user
    https://api.playfab.com/documentation/server/method/GetLeaderboardAroundUser
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetLeaderboardAroundUser", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetLeaderboardForUserCharacters(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of all of the user's characters for the given statistic.
    https://api.playfab.com/documentation/server/method/GetLeaderboardForUserCharacters
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetLeaderboardForUserCharacters", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerCombinedInfo(request, callback, customData = None, extraHeaders = None):
    """
    Returns whatever info is requested in the response for the user. Note that PII (like email address, facebook id) may be
    returned. All parameters default to false.
    https://api.playfab.com/documentation/server/method/GetPlayerCombinedInfo
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayerCombinedInfo", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerProfile(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the player's profile
    https://api.playfab.com/documentation/server/method/GetPlayerProfile
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayerProfile", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerSegments(request, callback, customData = None, extraHeaders = None):
    """
    List all segments that a player currently belongs to at this moment in time.
    https://api.playfab.com/documentation/server/method/GetPlayerSegments
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayerSegments", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayersInSegment(request, callback, customData = None, extraHeaders = None):
    """
    Allows for paging through all players in a given segment. This API creates a snapshot of all player profiles that match
    the segment definition at the time of its creation and lives through the Total Seconds to Live, refreshing its life span
    on each subsequent use of the Continuation Token. Profiles that change during the course of paging will not be reflected
    in the results. AB Test segments are currently not supported by this operation.
    https://api.playfab.com/documentation/server/method/GetPlayersInSegment
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayersInSegment", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the current version and values for the indicated statistics, for the local player.
    https://api.playfab.com/documentation/server/method/GetPlayerStatistics
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayerStatistics", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerStatisticVersions(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the information on the available versions of the specified statistic.
    https://api.playfab.com/documentation/server/method/GetPlayerStatisticVersions
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayerStatisticVersions", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayerTags(request, callback, customData = None, extraHeaders = None):
    """
    Get all tags with a given Namespace (optional) from a player profile.
    https://api.playfab.com/documentation/server/method/GetPlayerTags
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayerTags", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromFacebookIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Facebook identifiers.
    https://api.playfab.com/documentation/server/method/GetPlayFabIDsFromFacebookIDs
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayFabIDsFromFacebookIDs", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromFacebookInstantGamesIds(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Facebook Instant Games identifiers.
    https://api.playfab.com/documentation/server/method/GetPlayFabIDsFromFacebookInstantGamesIds
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayFabIDsFromFacebookInstantGamesIds", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromNintendoSwitchDeviceIds(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Nintendo Switch Device identifiers.
    https://api.playfab.com/documentation/server/method/GetPlayFabIDsFromNintendoSwitchDeviceIds
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayFabIDsFromNintendoSwitchDeviceIds", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromSteamIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Steam identifiers. The Steam identifiers are the profile
    IDs for the user accounts, available as SteamId in the Steamworks Community API calls.
    https://api.playfab.com/documentation/server/method/GetPlayFabIDsFromSteamIDs
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPlayFabIDsFromSteamIDs", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the key-value store of custom publisher settings
    https://api.playfab.com/documentation/server/method/GetPublisherData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetRandomResultTables(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the configuration information for the specified random results tables for the title, including all ItemId
    values and weights
    https://api.playfab.com/documentation/server/method/GetRandomResultTables
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetRandomResultTables", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetSharedGroupData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves data stored in a shared group object, as well as the list of members in the group. The server can access all
    public and private group data. Shared Groups are designed for sharing data between a very small number of players,
    please see our guide: https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/server/method/GetSharedGroupData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetSharedGroupData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetTime(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the current server time
    https://api.playfab.com/documentation/server/method/GetTime
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetTime", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetTitleData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the key-value store of custom title settings
    https://api.playfab.com/documentation/server/method/GetTitleData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetTitleData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetTitleInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the key-value store of custom internal title settings
    https://api.playfab.com/documentation/server/method/GetTitleInternalData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetTitleInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetTitleNews(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title news feed, as configured in the developer portal
    https://api.playfab.com/documentation/server/method/GetTitleNews
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetTitleNews", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserAccountInfo(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the relevant details for a specified user
    https://api.playfab.com/documentation/server/method/GetUserAccountInfo
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetUserAccountInfo", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserBans(request, callback, customData = None, extraHeaders = None):
    """
    Gets all bans for a user.
    https://api.playfab.com/documentation/server/method/GetUserBans
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetUserBans", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user which is readable and writable by the client
    https://api.playfab.com/documentation/server/method/GetUserData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetUserData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user which cannot be accessed by the client
    https://api.playfab.com/documentation/server/method/GetUserInternalData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetUserInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserInventory(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the specified user's current inventory of virtual goods
    https://api.playfab.com/documentation/server/method/GetUserInventory
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetUserInventory", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the publisher-specific custom data for the user which is readable and writable by the client
    https://api.playfab.com/documentation/server/method/GetUserPublisherData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetUserPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserPublisherInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the publisher-specific custom data for the user which cannot be accessed by the client
    https://api.playfab.com/documentation/server/method/GetUserPublisherInternalData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetUserPublisherInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserPublisherReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the publisher-specific custom data for the user which can only be read by the client
    https://api.playfab.com/documentation/server/method/GetUserPublisherReadOnlyData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetUserPublisherReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GetUserReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user which can only be read by the client
    https://api.playfab.com/documentation/server/method/GetUserReadOnlyData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GetUserReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GrantCharacterToUser(request, callback, customData = None, extraHeaders = None):
    """
    Grants the specified character type to the user. CharacterIds are not globally unique; characterId must be evaluated
    with the parent PlayFabId to guarantee uniqueness.
    https://api.playfab.com/documentation/server/method/GrantCharacterToUser
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GrantCharacterToUser", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GrantItemsToCharacter(request, callback, customData = None, extraHeaders = None):
    """
    Adds the specified items to the specified character's inventory
    https://api.playfab.com/documentation/server/method/GrantItemsToCharacter
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GrantItemsToCharacter", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GrantItemsToUser(request, callback, customData = None, extraHeaders = None):
    """
    Adds the specified items to the specified user's inventory
    https://api.playfab.com/documentation/server/method/GrantItemsToUser
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GrantItemsToUser", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def GrantItemsToUsers(request, callback, customData = None, extraHeaders = None):
    """
    Adds the specified items to the specified user inventories
    https://api.playfab.com/documentation/server/method/GrantItemsToUsers
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/GrantItemsToUsers", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ModifyItemUses(request, callback, customData = None, extraHeaders = None):
    """
    Modifies the number of remaining uses of a player's inventory item
    https://api.playfab.com/documentation/server/method/ModifyItemUses
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/ModifyItemUses", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def MoveItemToCharacterFromCharacter(request, callback, customData = None, extraHeaders = None):
    """
    Moves an item from a character's inventory into another of the users's character's inventory.
    https://api.playfab.com/documentation/server/method/MoveItemToCharacterFromCharacter
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/MoveItemToCharacterFromCharacter", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def MoveItemToCharacterFromUser(request, callback, customData = None, extraHeaders = None):
    """
    Moves an item from a user's inventory into their character's inventory.
    https://api.playfab.com/documentation/server/method/MoveItemToCharacterFromUser
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/MoveItemToCharacterFromUser", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def MoveItemToUserFromCharacter(request, callback, customData = None, extraHeaders = None):
    """
    Moves an item from a character's inventory into the owning user's inventory.
    https://api.playfab.com/documentation/server/method/MoveItemToUserFromCharacter
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/MoveItemToUserFromCharacter", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def NotifyMatchmakerPlayerLeft(request, callback, customData = None, extraHeaders = None):
    """
    Informs the PlayFab match-making service that the user specified has left the Game Server Instance
    https://api.playfab.com/documentation/server/method/NotifyMatchmakerPlayerLeft
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/NotifyMatchmakerPlayerLeft", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RedeemCoupon(request, callback, customData = None, extraHeaders = None):
    """
    Adds the virtual goods associated with the coupon to the user's inventory. Coupons can be generated via the
    Economy->Catalogs tab in the PlayFab Game Manager.
    https://api.playfab.com/documentation/server/method/RedeemCoupon
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RedeemCoupon", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RedeemMatchmakerTicket(request, callback, customData = None, extraHeaders = None):
    """
    Validates a Game Server session ticket and returns details about the user
    https://api.playfab.com/documentation/server/method/RedeemMatchmakerTicket
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RedeemMatchmakerTicket", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RefreshGameServerInstanceHeartbeat(request, callback, customData = None, extraHeaders = None):
    """
    Set the state of the indicated Game Server Instance. Also update the heartbeat for the instance.
    https://api.playfab.com/documentation/server/method/RefreshGameServerInstanceHeartbeat
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RefreshGameServerInstanceHeartbeat", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RegisterGame(request, callback, customData = None, extraHeaders = None):
    """
    Inform the matchmaker that a new Game Server Instance is added.
    https://api.playfab.com/documentation/server/method/RegisterGame
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RegisterGame", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RemoveFriend(request, callback, customData = None, extraHeaders = None):
    """
    Removes the specified friend from the the user's friend list
    https://api.playfab.com/documentation/server/method/RemoveFriend
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RemoveFriend", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RemovePlayerTag(request, callback, customData = None, extraHeaders = None):
    """
    Remove a given tag from a player profile. The tag's namespace is automatically generated based on the source of the tag.
    https://api.playfab.com/documentation/server/method/RemovePlayerTag
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RemovePlayerTag", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RemoveSharedGroupMembers(request, callback, customData = None, extraHeaders = None):
    """
    Removes users from the set of those able to update the shared data and the set of users in the group. Only users in the
    group can remove members. If as a result of the call, zero users remain with access, the group and its associated data
    will be deleted. Shared Groups are designed for sharing data between a very small number of players, please see our
    guide: https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/server/method/RemoveSharedGroupMembers
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RemoveSharedGroupMembers", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def ReportPlayer(request, callback, customData = None, extraHeaders = None):
    """
    Submit a report about a player (due to bad bahavior, etc.) on behalf of another player, so that customer service
    representatives for the title can take action concerning potentially toxic players.
    https://api.playfab.com/documentation/server/method/ReportPlayer
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/ReportPlayer", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RevokeAllBansForUser(request, callback, customData = None, extraHeaders = None):
    """
    Revoke all active bans for a user.
    https://api.playfab.com/documentation/server/method/RevokeAllBansForUser
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RevokeAllBansForUser", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RevokeBans(request, callback, customData = None, extraHeaders = None):
    """
    Revoke all active bans specified with BanId.
    https://api.playfab.com/documentation/server/method/RevokeBans
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RevokeBans", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RevokeInventoryItem(request, callback, customData = None, extraHeaders = None):
    """
    Revokes access to an item in a user's inventory
    https://api.playfab.com/documentation/server/method/RevokeInventoryItem
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RevokeInventoryItem", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def RevokeInventoryItems(request, callback, customData = None, extraHeaders = None):
    """
    Revokes access for up to 25 items across multiple users and characters.
    https://api.playfab.com/documentation/server/method/RevokeInventoryItems
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/RevokeInventoryItems", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SendCustomAccountRecoveryEmail(request, callback, customData = None, extraHeaders = None):
    """
    Forces an email to be sent to the registered contact email address for the user's account based on an account recovery
    email template
    https://api.playfab.com/documentation/server/method/SendCustomAccountRecoveryEmail
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SendCustomAccountRecoveryEmail", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SendEmailFromTemplate(request, callback, customData = None, extraHeaders = None):
    """
    Sends an email based on an email template to a player's contact email
    https://api.playfab.com/documentation/server/method/SendEmailFromTemplate
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SendEmailFromTemplate", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SendPushNotification(request, callback, customData = None, extraHeaders = None):
    """
    Sends an iOS/Android Push Notification to a specific user, if that user's device has been configured for Push
    Notifications in PlayFab. If a user has linked both Android and iOS devices, both will be notified.
    https://api.playfab.com/documentation/server/method/SendPushNotification
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SendPushNotification", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetFriendTags(request, callback, customData = None, extraHeaders = None):
    """
    Updates the tag list for a specified user in the friend list of another user
    https://api.playfab.com/documentation/server/method/SetFriendTags
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SetFriendTags", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetGameServerInstanceData(request, callback, customData = None, extraHeaders = None):
    """
    Sets the custom data of the indicated Game Server Instance
    https://api.playfab.com/documentation/server/method/SetGameServerInstanceData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SetGameServerInstanceData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetGameServerInstanceState(request, callback, customData = None, extraHeaders = None):
    """
    Set the state of the indicated Game Server Instance.
    https://api.playfab.com/documentation/server/method/SetGameServerInstanceState
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SetGameServerInstanceState", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetGameServerInstanceTags(request, callback, customData = None, extraHeaders = None):
    """
    Set custom tags for the specified Game Server Instance
    https://api.playfab.com/documentation/server/method/SetGameServerInstanceTags
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SetGameServerInstanceTags", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetPlayerSecret(request, callback, customData = None, extraHeaders = None):
    """
    Sets the player's secret if it is not already set. Player secrets are used to sign API requests. To reset a player's
    secret use the Admin or Server API method SetPlayerSecret.
    https://api.playfab.com/documentation/server/method/SetPlayerSecret
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SetPlayerSecret", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the key-value store of custom publisher settings
    https://api.playfab.com/documentation/server/method/SetPublisherData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SetPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetTitleData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the key-value store of custom title settings
    https://api.playfab.com/documentation/server/method/SetTitleData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SetTitleData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SetTitleInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the key-value store of custom title settings
    https://api.playfab.com/documentation/server/method/SetTitleInternalData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SetTitleInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SubtractCharacterVirtualCurrency(request, callback, customData = None, extraHeaders = None):
    """
    Decrements the character's balance of the specified virtual currency by the stated amount. It is possible to make a VC
    balance negative with this API.
    https://api.playfab.com/documentation/server/method/SubtractCharacterVirtualCurrency
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SubtractCharacterVirtualCurrency", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def SubtractUserVirtualCurrency(request, callback, customData = None, extraHeaders = None):
    """
    Decrements the user's balance of the specified virtual currency by the stated amount. It is possible to make a VC
    balance negative with this API.
    https://api.playfab.com/documentation/server/method/SubtractUserVirtualCurrency
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/SubtractUserVirtualCurrency", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UnlockContainerInstance(request, callback, customData = None, extraHeaders = None):
    """
    Opens a specific container (ContainerItemInstanceId), with a specific key (KeyItemInstanceId, when required), and
    returns the contents of the opened container. If the container (and key when relevant) are consumable (RemainingUses >
    0), their RemainingUses will be decremented, consistent with the operation of ConsumeItem.
    https://api.playfab.com/documentation/server/method/UnlockContainerInstance
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UnlockContainerInstance", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UnlockContainerItem(request, callback, customData = None, extraHeaders = None):
    """
    Searches Player or Character inventory for any ItemInstance matching the given CatalogItemId, if necessary unlocks it
    using any appropriate key, and returns the contents of the opened container. If the container (and key when relevant)
    are consumable (RemainingUses > 0), their RemainingUses will be decremented, consistent with the operation of
    ConsumeItem.
    https://api.playfab.com/documentation/server/method/UnlockContainerItem
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UnlockContainerItem", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateAvatarUrl(request, callback, customData = None, extraHeaders = None):
    """
    Update the avatar URL of the specified player
    https://api.playfab.com/documentation/server/method/UpdateAvatarUrl
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateAvatarUrl", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateBans(request, callback, customData = None, extraHeaders = None):
    """
    Updates information of a list of existing bans specified with Ban Ids.
    https://api.playfab.com/documentation/server/method/UpdateBans
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateBans", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateCharacterData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title-specific custom data for the user's character which is readable and writable by the client
    https://api.playfab.com/documentation/server/method/UpdateCharacterData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateCharacterData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateCharacterInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title-specific custom data for the user's character which cannot be accessed by the client
    https://api.playfab.com/documentation/server/method/UpdateCharacterInternalData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateCharacterInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateCharacterReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title-specific custom data for the user's character which can only be read by the client
    https://api.playfab.com/documentation/server/method/UpdateCharacterReadOnlyData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateCharacterReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateCharacterStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Updates the values of the specified title-specific statistics for the specific character
    https://api.playfab.com/documentation/server/method/UpdateCharacterStatistics
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateCharacterStatistics", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdatePlayerStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Updates the values of the specified title-specific statistics for the user
    https://api.playfab.com/documentation/server/method/UpdatePlayerStatistics
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdatePlayerStatistics", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateSharedGroupData(request, callback, customData = None, extraHeaders = None):
    """
    Adds, updates, and removes data keys for a shared group object. If the permission is set to Public, all fields updated
    or added in this call will be readable by users not in the group. By default, data permissions are set to Private.
    Regardless of the permission setting, only members of the group (and the server) can update the data. Shared Groups are
    designed for sharing data between a very small number of players, please see our guide:
    https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/server/method/UpdateSharedGroupData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateSharedGroupData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title-specific custom data for the user which is readable and writable by the client
    https://api.playfab.com/documentation/server/method/UpdateUserData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateUserData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title-specific custom data for the user which cannot be accessed by the client
    https://api.playfab.com/documentation/server/method/UpdateUserInternalData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateUserInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserInventoryItemCustomData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the key-value pair data tagged to the specified item, which is read-only from the client.
    https://api.playfab.com/documentation/server/method/UpdateUserInventoryItemCustomData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateUserInventoryItemCustomData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the publisher-specific custom data for the user which is readable and writable by the client
    https://api.playfab.com/documentation/server/method/UpdateUserPublisherData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateUserPublisherData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserPublisherInternalData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the publisher-specific custom data for the user which cannot be accessed by the client
    https://api.playfab.com/documentation/server/method/UpdateUserPublisherInternalData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateUserPublisherInternalData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserPublisherReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the publisher-specific custom data for the user which can only be read by the client
    https://api.playfab.com/documentation/server/method/UpdateUserPublisherReadOnlyData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateUserPublisherReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def UpdateUserReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title-specific custom data for the user which can only be read by the client
    https://api.playfab.com/documentation/server/method/UpdateUserReadOnlyData
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/UpdateUserReadOnlyData", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def WriteCharacterEvent(request, callback, customData = None, extraHeaders = None):
    """
    Writes a character-based event into PlayStream.
    https://api.playfab.com/documentation/server/method/WriteCharacterEvent
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/WriteCharacterEvent", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def WritePlayerEvent(request, callback, customData = None, extraHeaders = None):
    """
    Writes a player-based event into PlayStream.
    https://api.playfab.com/documentation/server/method/WritePlayerEvent
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/WritePlayerEvent", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

def WriteTitleEvent(request, callback, customData = None, extraHeaders = None):
    """
    Writes a title-based event into PlayStream.
    https://api.playfab.com/documentation/server/method/WriteTitleEvent
    """
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Server/WriteTitleEvent", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)


