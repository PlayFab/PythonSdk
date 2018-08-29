import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

"""
APIs which provide the full range of PlayFab features available to the client - authentication, account and data
management, inventory, friends, matchmaking, reporting, and platform-specific functionality
"""

def IsClientLoggedIn():
    """Determine if the client session ticket is set, without actually making it public"""
    return bool(PlayFabSettings._internalSettings.ClientSessionTicket)

def MultiStepClientLogin(settingsForUser):
    disabledAds = PlayFabSettings.DisableAdvertising
    adIdType = PlayFabSettings.AdvertisingIdType
    adIdVal = PlayFabSettings.AdvertisingIdValue

    if settingsForUser and settingsForUser["NeedsAttribution"] and not disabledAds and adIdType and adIdVal:
        request = {}
        if adIdType == PlayFabSettings.AD_TYPE_IDFA:
            request["Idfa"] = adIdVal
        elif adIdType == PlayFabSettings.AD_TYPE_ANDROID_ID:
            request["Adid"] = adIdVal
        AttributeInstall(request, None)

def AcceptTrade(request, callback, customData = None, extraHeaders = None):
    """
    Accepts an open trade (one that has not yet been accepted or cancelled), if the locally signed-in player is in the
    allowed player list for the trade, or it is open to all players. If the call is successful, the offered and accepted
    items will be swapped between the two players' inventories.
    https://api.playfab.com/documentation/client/method/AcceptTrade
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/AcceptTrade", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def AddFriend(request, callback, customData = None, extraHeaders = None):
    """
    Adds the PlayFab user, based upon a match against a supplied unique identifier, to the friend list of the local user. At
    least one of FriendPlayFabId,FriendUsername,FriendEmail, or FriendTitleDisplayName should be initialized.
    https://api.playfab.com/documentation/client/method/AddFriend
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/AddFriend", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def AddGenericID(request, callback, customData = None, extraHeaders = None):
    """
    Adds the specified generic service identifier to the player's PlayFab account. This is designed to allow for a PlayFab
    ID lookup of any arbitrary service identifier a title wants to add. This identifier should never be used as
    authentication credentials, as the intent is that it is easily accessible by other players.
    https://api.playfab.com/documentation/client/method/AddGenericID
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/AddGenericID", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def AddOrUpdateContactEmail(request, callback, customData = None, extraHeaders = None):
    """
    Adds or updates a contact email to the player's profile.
    https://api.playfab.com/documentation/client/method/AddOrUpdateContactEmail
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/AddOrUpdateContactEmail", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def AddSharedGroupMembers(request, callback, customData = None, extraHeaders = None):
    """
    Adds users to the set of those able to update both the shared data, as well as the set of users in the group. Only users
    in the group can add new members. Shared Groups are designed for sharing data between a very small number of players,
    please see our guide: https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/client/method/AddSharedGroupMembers
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/AddSharedGroupMembers", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def AddUsernamePassword(request, callback, customData = None, extraHeaders = None):
    """
    Adds playfab username/password auth to an existing account created via an anonymous auth method, e.g. automatic device
    ID login.
    https://api.playfab.com/documentation/client/method/AddUsernamePassword
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/AddUsernamePassword", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def AddUserVirtualCurrency(request, callback, customData = None, extraHeaders = None):
    """
    Increments the user's balance of the specified virtual currency by the stated amount
    https://api.playfab.com/documentation/client/method/AddUserVirtualCurrency
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/AddUserVirtualCurrency", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def AndroidDevicePushNotificationRegistration(request, callback, customData = None, extraHeaders = None):
    """
    Registers the Android device to receive push notifications
    https://api.playfab.com/documentation/client/method/AndroidDevicePushNotificationRegistration
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/AndroidDevicePushNotificationRegistration", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def AttributeInstall(request, callback, customData = None, extraHeaders = None):
    """
    Attributes an install for advertisment.
    https://api.playfab.com/documentation/client/method/AttributeInstall
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        # Modify AdvertisingIdType:  Prevents us from sending the id multiple times, and allows automated tests to determine id was sent successfully
        PlayFabSettings.AdvertisingIdType += "_Successful"
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/AttributeInstall", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def CancelTrade(request, callback, customData = None, extraHeaders = None):
    """
    Cancels an open trade (one that has not yet been accepted or cancelled). Note that only the player who created the trade
    can cancel it via this API call, to prevent griefing of the trade system (cancelling trades in order to prevent other
    players from accepting them, for trades that can be claimed by more than one player).
    https://api.playfab.com/documentation/client/method/CancelTrade
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/CancelTrade", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ConfirmPurchase(request, callback, customData = None, extraHeaders = None):
    """
    Confirms with the payment provider that the purchase was approved (if applicable) and adjusts inventory and virtual
    currency balances as appropriate
    https://api.playfab.com/documentation/client/method/ConfirmPurchase
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ConfirmPurchase", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ConsumeItem(request, callback, customData = None, extraHeaders = None):
    """
    Consume uses of a consumable item. When all uses are consumed, it will be removed from the player's inventory.
    https://api.playfab.com/documentation/client/method/ConsumeItem
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ConsumeItem", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ConsumeXboxEntitlements(request, callback, customData = None, extraHeaders = None):
    """
    Grants the player's current entitlements from Xbox Live, consuming all availble items in Xbox and granting them to the
    player's PlayFab inventory. This call is idempotent and will not grant previously granted items to the player.
    https://api.playfab.com/documentation/client/method/ConsumeXboxEntitlements
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ConsumeXboxEntitlements", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def CreateSharedGroup(request, callback, customData = None, extraHeaders = None):
    """
    Requests the creation of a shared group object, containing key/value pairs which may be updated by all members of the
    group. Upon creation, the current user will be the only member of the group. Shared Groups are designed for sharing data
    between a very small number of players, please see our guide:
    https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/client/method/CreateSharedGroup
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/CreateSharedGroup", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ExecuteCloudScript(request, callback, customData = None, extraHeaders = None):
    """
    Executes a CloudScript function, with the 'currentPlayerId' set to the PlayFab ID of the authenticated player.
    https://api.playfab.com/documentation/client/method/ExecuteCloudScript
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ExecuteCloudScript", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetAccountInfo(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the user's PlayFab account details
    https://api.playfab.com/documentation/client/method/GetAccountInfo
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetAccountInfo", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetAllUsersCharacters(request, callback, customData = None, extraHeaders = None):
    """
    Lists all of the characters that belong to a specific user. CharacterIds are not globally unique; characterId must be
    evaluated with the parent PlayFabId to guarantee uniqueness.
    https://api.playfab.com/documentation/client/method/GetAllUsersCharacters
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetAllUsersCharacters", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetCatalogItems(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the specified version of the title's catalog of virtual goods, including all defined properties
    https://api.playfab.com/documentation/client/method/GetCatalogItems
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetCatalogItems", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetCharacterData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the character which is readable and writable by the client
    https://api.playfab.com/documentation/client/method/GetCharacterData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetCharacterData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetCharacterInventory(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the specified character's current inventory of virtual goods
    https://api.playfab.com/documentation/client/method/GetCharacterInventory
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetCharacterInventory", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetCharacterLeaderboard(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked characters for the given statistic, starting from the indicated point in the leaderboard
    https://api.playfab.com/documentation/client/method/GetCharacterLeaderboard
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetCharacterLeaderboard", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetCharacterReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the character which can only be read by the client
    https://api.playfab.com/documentation/client/method/GetCharacterReadOnlyData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetCharacterReadOnlyData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetCharacterStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the details of all title-specific statistics for the user
    https://api.playfab.com/documentation/client/method/GetCharacterStatistics
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetCharacterStatistics", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetContentDownloadUrl(request, callback, customData = None, extraHeaders = None):
    """
    This API retrieves a pre-signed URL for accessing a content file for the title. A subsequent HTTP GET to the returned
    URL will attempt to download the content. A HEAD query to the returned URL will attempt to retrieve the metadata of the
    content. Note that a successful result does not guarantee the existence of this content - if it has not been uploaded,
    the query to retrieve the data will fail. See this post for more information:
    https://community.playfab.com/hc/en-us/community/posts/205469488-How-to-upload-files-to-PlayFab-s-Content-Service. Also,
    please be aware that the Content service is specifically PlayFab's CDN offering, for which standard CDN rates apply.
    https://api.playfab.com/documentation/client/method/GetContentDownloadUrl
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetContentDownloadUrl", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetCurrentGames(request, callback, customData = None, extraHeaders = None):
    """
    Get details about all current running game servers matching the given parameters.
    https://api.playfab.com/documentation/client/method/GetCurrentGames
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetCurrentGames", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetFriendLeaderboard(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked friends of the current player for the given statistic, starting from the indicated point in
    the leaderboard
    https://api.playfab.com/documentation/client/method/GetFriendLeaderboard
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetFriendLeaderboard", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetFriendLeaderboardAroundPlayer(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked friends of the current player for the given statistic, centered on the requested PlayFab
    user. If PlayFabId is empty or null will return currently logged in user.
    https://api.playfab.com/documentation/client/method/GetFriendLeaderboardAroundPlayer
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetFriendLeaderboardAroundPlayer", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetFriendsList(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the current friend list for the local user, constrained to users who have PlayFab accounts. Friends from
    linked accounts (Facebook, Steam) are also included. You may optionally exclude some linked services' friends.
    https://api.playfab.com/documentation/client/method/GetFriendsList
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetFriendsList", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetGameServerRegions(request, callback, customData = None, extraHeaders = None):
    """
    Get details about the regions hosting game servers matching the given parameters.
    https://api.playfab.com/documentation/client/method/GetGameServerRegions
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetGameServerRegions", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetLeaderboard(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked users for the given statistic, starting from the indicated point in the leaderboard
    https://api.playfab.com/documentation/client/method/GetLeaderboard
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetLeaderboard", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetLeaderboardAroundCharacter(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked characters for the given statistic, centered on the requested Character ID
    https://api.playfab.com/documentation/client/method/GetLeaderboardAroundCharacter
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetLeaderboardAroundCharacter", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetLeaderboardAroundPlayer(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of ranked users for the given statistic, centered on the requested player. If PlayFabId is empty or
    null will return currently logged in user.
    https://api.playfab.com/documentation/client/method/GetLeaderboardAroundPlayer
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetLeaderboardAroundPlayer", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetLeaderboardForUserCharacters(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a list of all of the user's characters for the given statistic.
    https://api.playfab.com/documentation/client/method/GetLeaderboardForUserCharacters
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetLeaderboardForUserCharacters", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPaymentToken(request, callback, customData = None, extraHeaders = None):
    """
    For payments flows where the provider requires playfab (the fulfiller) to initiate the transaction, but the client
    completes the rest of the flow. In the Xsolla case, the token returned here will be passed to Xsolla by the client to
    create a cart. Poll GetPurchase using the returned OrderId once you've completed the payment.
    https://api.playfab.com/documentation/client/method/GetPaymentToken
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPaymentToken", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPhotonAuthenticationToken(request, callback, customData = None, extraHeaders = None):
    """
    Gets a Photon custom authentication token that can be used to securely join the player into a Photon room. See
    https://api.playfab.com/docs/using-photon-with-playfab/ for more details.
    https://api.playfab.com/documentation/client/method/GetPhotonAuthenticationToken
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPhotonAuthenticationToken", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayerCombinedInfo(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves all of the user's different kinds of info.
    https://api.playfab.com/documentation/client/method/GetPlayerCombinedInfo
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayerCombinedInfo", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayerProfile(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the player's profile
    https://api.playfab.com/documentation/client/method/GetPlayerProfile
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayerProfile", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayerSegments(request, callback, customData = None, extraHeaders = None):
    """
    List all segments that a player currently belongs to at this moment in time.
    https://api.playfab.com/documentation/client/method/GetPlayerSegments
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayerSegments", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayerStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the indicated statistics (current version and values for all statistics, if none are specified), for the local
    player.
    https://api.playfab.com/documentation/client/method/GetPlayerStatistics
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayerStatistics", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayerStatisticVersions(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the information on the available versions of the specified statistic.
    https://api.playfab.com/documentation/client/method/GetPlayerStatisticVersions
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayerStatisticVersions", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayerTags(request, callback, customData = None, extraHeaders = None):
    """
    Get all tags with a given Namespace (optional) from a player profile.
    https://api.playfab.com/documentation/client/method/GetPlayerTags
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayerTags", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayerTrades(request, callback, customData = None, extraHeaders = None):
    """
    Gets all trades the player has either opened or accepted, optionally filtered by trade status.
    https://api.playfab.com/documentation/client/method/GetPlayerTrades
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayerTrades", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromFacebookIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Facebook identifiers.
    https://api.playfab.com/documentation/client/method/GetPlayFabIDsFromFacebookIDs
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromFacebookIDs", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromFacebookInstantGamesIds(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Facebook Instant Game identifiers.
    https://api.playfab.com/documentation/client/method/GetPlayFabIDsFromFacebookInstantGamesIds
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromFacebookInstantGamesIds", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromGameCenterIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Game Center identifiers (referenced in the Game Center
    Programming Guide as the Player Identifier).
    https://api.playfab.com/documentation/client/method/GetPlayFabIDsFromGameCenterIDs
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromGameCenterIDs", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromGenericIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of generic service identifiers. A generic identifier is the
    service name plus the service-specific ID for the player, as specified by the title when the generic identifier was
    added to the player account.
    https://api.playfab.com/documentation/client/method/GetPlayFabIDsFromGenericIDs
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromGenericIDs", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromGoogleIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Google identifiers. The Google identifiers are the IDs for
    the user accounts, available as "id" in the Google+ People API calls.
    https://api.playfab.com/documentation/client/method/GetPlayFabIDsFromGoogleIDs
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromGoogleIDs", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromKongregateIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Kongregate identifiers. The Kongregate identifiers are the
    IDs for the user accounts, available as "user_id" from the Kongregate API methods(ex:
    http://developers.kongregate.com/docs/client/getUserId).
    https://api.playfab.com/documentation/client/method/GetPlayFabIDsFromKongregateIDs
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromKongregateIDs", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromNintendoSwitchDeviceIds(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Nintendo Switch identifiers.
    https://api.playfab.com/documentation/client/method/GetPlayFabIDsFromNintendoSwitchDeviceIds
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromNintendoSwitchDeviceIds", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromSteamIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Steam identifiers. The Steam identifiers are the profile
    IDs for the user accounts, available as SteamId in the Steamworks Community API calls.
    https://api.playfab.com/documentation/client/method/GetPlayFabIDsFromSteamIDs
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromSteamIDs", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromTwitchIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Twitch identifiers. The Twitch identifiers are the IDs for
    the user accounts, available as "_id" from the Twitch API methods (ex:
    https://github.com/justintv/Twitch-API/blob/master/v3_resources/users.md#get-usersuser).
    https://api.playfab.com/documentation/client/method/GetPlayFabIDsFromTwitchIDs
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromTwitchIDs", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the key-value store of custom publisher settings
    https://api.playfab.com/documentation/client/method/GetPublisherData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPublisherData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPurchase(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a purchase along with its current PlayFab status. Returns inventory items from the purchase that are still
    active.
    https://api.playfab.com/documentation/client/method/GetPurchase
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPurchase", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetSharedGroupData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves data stored in a shared group object, as well as the list of members in the group. Non-members of the group
    may use this to retrieve group data, including membership, but they will not receive data for keys marked as private.
    Shared Groups are designed for sharing data between a very small number of players, please see our guide:
    https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/client/method/GetSharedGroupData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetSharedGroupData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetStoreItems(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the set of items defined for the specified store, including all prices defined
    https://api.playfab.com/documentation/client/method/GetStoreItems
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetStoreItems", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetTime(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the current server time
    https://api.playfab.com/documentation/client/method/GetTime
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetTime", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetTitleData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the key-value store of custom title settings
    https://api.playfab.com/documentation/client/method/GetTitleData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetTitleData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetTitleNews(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title news feed, as configured in the developer portal
    https://api.playfab.com/documentation/client/method/GetTitleNews
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetTitleNews", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetTitlePublicKey(request, callback, customData = None, extraHeaders = None):
    """
    Returns the title's base 64 encoded RSA CSP blob.
    https://api.playfab.com/documentation/client/method/GetTitlePublicKey
    """
    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetTitlePublicKey", request, None, None, wrappedCallback, customData, extraHeaders)

def GetTradeStatus(request, callback, customData = None, extraHeaders = None):
    """
    Gets the current status of an existing trade.
    https://api.playfab.com/documentation/client/method/GetTradeStatus
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetTradeStatus", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetUserData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user which is readable and writable by the client
    https://api.playfab.com/documentation/client/method/GetUserData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetUserData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetUserInventory(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the user's current inventory of virtual goods
    https://api.playfab.com/documentation/client/method/GetUserInventory
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetUserInventory", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetUserPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the publisher-specific custom data for the user which is readable and writable by the client
    https://api.playfab.com/documentation/client/method/GetUserPublisherData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetUserPublisherData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetUserPublisherReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the publisher-specific custom data for the user which can only be read by the client
    https://api.playfab.com/documentation/client/method/GetUserPublisherReadOnlyData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetUserPublisherReadOnlyData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetUserReadOnlyData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the title-specific custom data for the user which can only be read by the client
    https://api.playfab.com/documentation/client/method/GetUserReadOnlyData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetUserReadOnlyData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetWindowsHelloChallenge(request, callback, customData = None, extraHeaders = None):
    """
    Requests a challenge from the server to be signed by Windows Hello Passport service to authenticate.
    https://api.playfab.com/documentation/client/method/GetWindowsHelloChallenge
    """
    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetWindowsHelloChallenge", request, None, None, wrappedCallback, customData, extraHeaders)

def GrantCharacterToUser(request, callback, customData = None, extraHeaders = None):
    """
    Grants the specified character type to the user. CharacterIds are not globally unique; characterId must be evaluated
    with the parent PlayFabId to guarantee uniqueness.
    https://api.playfab.com/documentation/client/method/GrantCharacterToUser
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GrantCharacterToUser", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkAndroidDeviceID(request, callback, customData = None, extraHeaders = None):
    """
    Links the Android device identifier to the user's PlayFab account
    https://api.playfab.com/documentation/client/method/LinkAndroidDeviceID
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkAndroidDeviceID", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkCustomID(request, callback, customData = None, extraHeaders = None):
    """
    Links the custom identifier, generated by the title, to the user's PlayFab account
    https://api.playfab.com/documentation/client/method/LinkCustomID
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkCustomID", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkFacebookAccount(request, callback, customData = None, extraHeaders = None):
    """
    Links the Facebook account associated with the provided Facebook access token to the user's PlayFab account
    https://api.playfab.com/documentation/client/method/LinkFacebookAccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkFacebookAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkFacebookInstantGamesId(request, callback, customData = None, extraHeaders = None):
    """
    Links the Facebook Instant Games Id to the user's PlayFab account
    https://api.playfab.com/documentation/client/method/LinkFacebookInstantGamesId
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkFacebookInstantGamesId", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkGameCenterAccount(request, callback, customData = None, extraHeaders = None):
    """
    Links the Game Center account associated with the provided Game Center ID to the user's PlayFab account
    https://api.playfab.com/documentation/client/method/LinkGameCenterAccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkGameCenterAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkGoogleAccount(request, callback, customData = None, extraHeaders = None):
    """
    Links the currently signed-in user account to their Google account, using their Google account credentials
    https://api.playfab.com/documentation/client/method/LinkGoogleAccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkGoogleAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkIOSDeviceID(request, callback, customData = None, extraHeaders = None):
    """
    Links the vendor-specific iOS device identifier to the user's PlayFab account
    https://api.playfab.com/documentation/client/method/LinkIOSDeviceID
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkIOSDeviceID", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkKongregate(request, callback, customData = None, extraHeaders = None):
    """
    Links the Kongregate identifier to the user's PlayFab account
    https://api.playfab.com/documentation/client/method/LinkKongregate
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkKongregate", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkNintendoSwitchDeviceId(request, callback, customData = None, extraHeaders = None):
    """
    Links the NintendoSwitchDeviceId to the user's PlayFab account
    https://api.playfab.com/documentation/client/method/LinkNintendoSwitchDeviceId
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkNintendoSwitchDeviceId", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkSteamAccount(request, callback, customData = None, extraHeaders = None):
    """
    Links the Steam account associated with the provided Steam authentication ticket to the user's PlayFab account
    https://api.playfab.com/documentation/client/method/LinkSteamAccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkSteamAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkTwitch(request, callback, customData = None, extraHeaders = None):
    """
    Links the Twitch account associated with the token to the user's PlayFab account.
    https://api.playfab.com/documentation/client/method/LinkTwitch
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkTwitch", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkWindowsHello(request, callback, customData = None, extraHeaders = None):
    """
    Link Windows Hello authentication to the current PlayFab Account
    https://api.playfab.com/documentation/client/method/LinkWindowsHello
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkWindowsHello", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkXboxAccount(request, callback, customData = None, extraHeaders = None):
    """
    Links the Xbox Live account associated with the provided access code to the user's PlayFab account
    https://api.playfab.com/documentation/client/method/LinkXboxAccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkXboxAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LoginWithAndroidDeviceID(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using the Android device identifier, returning a session identifier that can subsequently be used for
    API calls which require an authenticated user
    https://api.playfab.com/documentation/client/method/LoginWithAndroidDeviceID
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithAndroidDeviceID", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithCustomID(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a custom unique identifier generated by the title, returning a session identifier that can
    subsequently be used for API calls which require an authenticated user
    https://api.playfab.com/documentation/client/method/LoginWithCustomID
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithCustomID", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithEmailAddress(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user into the PlayFab account, returning a session identifier that can subsequently be used for API calls
    which require an authenticated user. Unlike most other login API calls, LoginWithEmailAddress does not permit the
    creation of new accounts via the CreateAccountFlag. Email addresses may be used to create accounts via
    RegisterPlayFabUser.
    https://api.playfab.com/documentation/client/method/LoginWithEmailAddress
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithEmailAddress", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithFacebook(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a Facebook access token, returning a session identifier that can subsequently be used for API
    calls which require an authenticated user
    https://api.playfab.com/documentation/client/method/LoginWithFacebook
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithFacebook", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithFacebookInstantGamesId(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a Facebook Instant Games ID, returning a session identifier that can subsequently be used for
    API calls which require an authenticated user. Requires Facebook Instant Games to be configured.
    https://api.playfab.com/documentation/client/method/LoginWithFacebookInstantGamesId
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithFacebookInstantGamesId", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithGameCenter(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using an iOS Game Center player identifier, returning a session identifier that can subsequently be
    used for API calls which require an authenticated user
    https://api.playfab.com/documentation/client/method/LoginWithGameCenter
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithGameCenter", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithGoogleAccount(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using their Google account credentials
    https://api.playfab.com/documentation/client/method/LoginWithGoogleAccount
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithGoogleAccount", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithIOSDeviceID(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using the vendor-specific iOS device identifier, returning a session identifier that can subsequently
    be used for API calls which require an authenticated user
    https://api.playfab.com/documentation/client/method/LoginWithIOSDeviceID
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithIOSDeviceID", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithKongregate(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a Kongregate player account.
    https://api.playfab.com/documentation/client/method/LoginWithKongregate
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithKongregate", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithNintendoSwitchDeviceId(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a Nintendo Switch Device ID, returning a session identifier that can subsequently be used for
    API calls which require an authenticated user
    https://api.playfab.com/documentation/client/method/LoginWithNintendoSwitchDeviceId
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithNintendoSwitchDeviceId", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithPlayFab(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user into the PlayFab account, returning a session identifier that can subsequently be used for API calls
    which require an authenticated user. Unlike most other login API calls, LoginWithPlayFab does not permit the creation of
    new accounts via the CreateAccountFlag. Username/Password credentials may be used to create accounts via
    RegisterPlayFabUser, or added to existing accounts using AddUsernamePassword.
    https://api.playfab.com/documentation/client/method/LoginWithPlayFab
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithPlayFab", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithSteam(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a Steam authentication ticket, returning a session identifier that can subsequently be used for
    API calls which require an authenticated user
    https://api.playfab.com/documentation/client/method/LoginWithSteam
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithSteam", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithTwitch(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a Twitch access token.
    https://api.playfab.com/documentation/client/method/LoginWithTwitch
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithTwitch", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithWindowsHello(request, callback, customData = None, extraHeaders = None):
    """
    Completes the Windows Hello login flow by returning the signed value of the challange from GetWindowsHelloChallenge.
    Windows Hello has a 2 step client to server authentication scheme. Step one is to request from the server a challenge
    string. Step two is to request the user sign the string via Windows Hello and then send the signed value back to the
    server.
    https://api.playfab.com/documentation/client/method/LoginWithWindowsHello
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithWindowsHello", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithXbox(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a Xbox Live Token, returning a session identifier that can subsequently be used for API calls
    which require an authenticated user
    https://api.playfab.com/documentation/client/method/LoginWithXbox
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LoginWithXbox", request, None, None, wrappedCallback, customData, extraHeaders)

def Matchmake(request, callback, customData = None, extraHeaders = None):
    """
    Attempts to locate a game session matching the given parameters. If the goal is to match the player into a specific
    active session, only the LobbyId is required. Otherwise, the BuildVersion, GameMode, and Region are all required
    parameters. Note that parameters specified in the search are required (they are not weighting factors). If a slot is
    found in a server instance matching the parameters, the slot will be assigned to that player, removing it from the
    availabe set. In that case, the information on the game session will be returned, otherwise the Status returned will be
    GameNotFound.
    https://api.playfab.com/documentation/client/method/Matchmake
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/Matchmake", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def OpenTrade(request, callback, customData = None, extraHeaders = None):
    """
    Opens a new outstanding trade. Note that a given item instance may only be in one open trade at a time.
    https://api.playfab.com/documentation/client/method/OpenTrade
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/OpenTrade", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def PayForPurchase(request, callback, customData = None, extraHeaders = None):
    """
    Selects a payment option for purchase order created via StartPurchase
    https://api.playfab.com/documentation/client/method/PayForPurchase
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/PayForPurchase", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def PurchaseItem(request, callback, customData = None, extraHeaders = None):
    """
    Buys a single item with virtual currency. You must specify both the virtual currency to use to purchase, as well as what
    the client believes the price to be. This lets the server fail the purchase if the price has changed.
    https://api.playfab.com/documentation/client/method/PurchaseItem
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/PurchaseItem", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def RedeemCoupon(request, callback, customData = None, extraHeaders = None):
    """
    Adds the virtual goods associated with the coupon to the user's inventory. Coupons can be generated via the
    Economy->Catalogs tab in the PlayFab Game Manager.
    https://api.playfab.com/documentation/client/method/RedeemCoupon
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RedeemCoupon", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def RegisterForIOSPushNotification(request, callback, customData = None, extraHeaders = None):
    """
    Registers the iOS device to receive push notifications
    https://api.playfab.com/documentation/client/method/RegisterForIOSPushNotification
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RegisterForIOSPushNotification", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def RegisterPlayFabUser(request, callback, customData = None, extraHeaders = None):
    """
    Registers a new Playfab user account, returning a session identifier that can subsequently be used for API calls which
    require an authenticated user. You must supply either a username or an email address.
    https://api.playfab.com/documentation/client/method/RegisterPlayFabUser
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RegisterPlayFabUser", request, None, None, wrappedCallback, customData, extraHeaders)

def RegisterWithWindowsHello(request, callback, customData = None, extraHeaders = None):
    """
    Registers a new PlayFab user account using Windows Hello authentication, returning a session ticket that can
    subsequently be used for API calls which require an authenticated user
    https://api.playfab.com/documentation/client/method/RegisterWithWindowsHello
    """
    request["TitleId"] = PlayFabSettings.TitleId or request.TitleId
    if not request["TitleId"]:
        raise PlayFabErrors.PlayFabException("Must be have TitleId set to call this method")

    def wrappedCallback(playFabResult, error):
        if playFabResult:
            PlayFabSettings._internalSettings.ClientSessionTicket = playFabResult["SessionTicket"] if "SessionTicket" in playFabResult else PlayFabSettings._internalSettings.ClientSessionTicket
            PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"]["EntityToken"] if "EntityToken" in playFabResult else PlayFabSettings._internalSettings.EntityToken
            MultiStepClientLogin(playFabResult.get("SettingsForUser"))
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RegisterWithWindowsHello", request, None, None, wrappedCallback, customData, extraHeaders)

def RemoveContactEmail(request, callback, customData = None, extraHeaders = None):
    """
    Removes a contact email from the player's profile.
    https://api.playfab.com/documentation/client/method/RemoveContactEmail
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RemoveContactEmail", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def RemoveFriend(request, callback, customData = None, extraHeaders = None):
    """
    Removes a specified user from the friend list of the local user
    https://api.playfab.com/documentation/client/method/RemoveFriend
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RemoveFriend", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def RemoveGenericID(request, callback, customData = None, extraHeaders = None):
    """
    Removes the specified generic service identifier from the player's PlayFab account.
    https://api.playfab.com/documentation/client/method/RemoveGenericID
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RemoveGenericID", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def RemoveSharedGroupMembers(request, callback, customData = None, extraHeaders = None):
    """
    Removes users from the set of those able to update the shared data and the set of users in the group. Only users in the
    group can remove members. If as a result of the call, zero users remain with access, the group and its associated data
    will be deleted. Shared Groups are designed for sharing data between a very small number of players, please see our
    guide: https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/client/method/RemoveSharedGroupMembers
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RemoveSharedGroupMembers", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ReportDeviceInfo(request, callback, customData = None, extraHeaders = None):
    """
    Write a PlayStream event to describe the provided player device information. This API method is not designed to be
    called directly by developers. Each PlayFab client SDK will eventually report this information automatically.
    https://api.playfab.com/documentation/client/method/ReportDeviceInfo
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ReportDeviceInfo", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ReportPlayer(request, callback, customData = None, extraHeaders = None):
    """
    Submit a report for another player (due to bad bahavior, etc.), so that customer service representatives for the title
    can take action concerning potentially toxic players.
    https://api.playfab.com/documentation/client/method/ReportPlayer
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ReportPlayer", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def RestoreIOSPurchases(request, callback, customData = None, extraHeaders = None):
    """
    Restores all in-app purchases based on the given restore receipt
    https://api.playfab.com/documentation/client/method/RestoreIOSPurchases
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RestoreIOSPurchases", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def SendAccountRecoveryEmail(request, callback, customData = None, extraHeaders = None):
    """
    Forces an email to be sent to the registered email address for the user's account, with a link allowing the user to
    change the password.If an account recovery email template ID is provided, an email using the custom email template will
    be used.
    https://api.playfab.com/documentation/client/method/SendAccountRecoveryEmail
    """
    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/SendAccountRecoveryEmail", request, None, None, wrappedCallback, customData, extraHeaders)

def SetFriendTags(request, callback, customData = None, extraHeaders = None):
    """
    Updates the tag list for a specified user in the friend list of the local user
    https://api.playfab.com/documentation/client/method/SetFriendTags
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/SetFriendTags", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def SetPlayerSecret(request, callback, customData = None, extraHeaders = None):
    """
    Sets the player's secret if it is not already set. Player secrets are used to sign API requests. To reset a player's
    secret use the Admin or Server API method SetPlayerSecret.
    https://api.playfab.com/documentation/client/method/SetPlayerSecret
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/SetPlayerSecret", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def StartGame(request, callback, customData = None, extraHeaders = None):
    """
    Start a new game server with a given configuration, add the current player and return the connection information.
    https://api.playfab.com/documentation/client/method/StartGame
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/StartGame", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def StartPurchase(request, callback, customData = None, extraHeaders = None):
    """
    Creates an order for a list of items from the title catalog
    https://api.playfab.com/documentation/client/method/StartPurchase
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/StartPurchase", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def SubtractUserVirtualCurrency(request, callback, customData = None, extraHeaders = None):
    """
    Decrements the user's balance of the specified virtual currency by the stated amount. It is possible to make a VC
    balance negative with this API.
    https://api.playfab.com/documentation/client/method/SubtractUserVirtualCurrency
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/SubtractUserVirtualCurrency", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkAndroidDeviceID(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Android device identifier from the user's PlayFab account
    https://api.playfab.com/documentation/client/method/UnlinkAndroidDeviceID
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkAndroidDeviceID", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkCustomID(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related custom identifier from the user's PlayFab account
    https://api.playfab.com/documentation/client/method/UnlinkCustomID
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkCustomID", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkFacebookAccount(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Facebook account from the user's PlayFab account
    https://api.playfab.com/documentation/client/method/UnlinkFacebookAccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkFacebookAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkFacebookInstantGamesId(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Facebook Instant Game Ids from the user's PlayFab account
    https://api.playfab.com/documentation/client/method/UnlinkFacebookInstantGamesId
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkFacebookInstantGamesId", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkGameCenterAccount(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Game Center account from the user's PlayFab account
    https://api.playfab.com/documentation/client/method/UnlinkGameCenterAccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkGameCenterAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkGoogleAccount(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Google account from the user's PlayFab account
    (https://developers.google.com/android/reference/com/google/android/gms/auth/GoogleAuthUtil#public-methods).
    https://api.playfab.com/documentation/client/method/UnlinkGoogleAccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkGoogleAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkIOSDeviceID(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related iOS device identifier from the user's PlayFab account
    https://api.playfab.com/documentation/client/method/UnlinkIOSDeviceID
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkIOSDeviceID", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkKongregate(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Kongregate identifier from the user's PlayFab account
    https://api.playfab.com/documentation/client/method/UnlinkKongregate
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkKongregate", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkNintendoSwitchDeviceId(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related NintendoSwitchDeviceId from the user's PlayFab account
    https://api.playfab.com/documentation/client/method/UnlinkNintendoSwitchDeviceId
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkNintendoSwitchDeviceId", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkSteamAccount(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Steam account from the user's PlayFab account
    https://api.playfab.com/documentation/client/method/UnlinkSteamAccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkSteamAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkTwitch(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Twitch account from the user's PlayFab account.
    https://api.playfab.com/documentation/client/method/UnlinkTwitch
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkTwitch", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkWindowsHello(request, callback, customData = None, extraHeaders = None):
    """
    Unlink Windows Hello authentication from the current PlayFab Account
    https://api.playfab.com/documentation/client/method/UnlinkWindowsHello
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkWindowsHello", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkXboxAccount(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Xbox Live account from the user's PlayFab account
    https://api.playfab.com/documentation/client/method/UnlinkXboxAccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkXboxAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlockContainerInstance(request, callback, customData = None, extraHeaders = None):
    """
    Opens the specified container, with the specified key (when required), and returns the contents of the opened container.
    If the container (and key when relevant) are consumable (RemainingUses > 0), their RemainingUses will be decremented,
    consistent with the operation of ConsumeItem.
    https://api.playfab.com/documentation/client/method/UnlockContainerInstance
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlockContainerInstance", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlockContainerItem(request, callback, customData = None, extraHeaders = None):
    """
    Searches target inventory for an ItemInstance matching the given CatalogItemId, if necessary unlocks it using an
    appropriate key, and returns the contents of the opened container. If the container (and key when relevant) are
    consumable (RemainingUses > 0), their RemainingUses will be decremented, consistent with the operation of ConsumeItem.
    https://api.playfab.com/documentation/client/method/UnlockContainerItem
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlockContainerItem", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UpdateAvatarUrl(request, callback, customData = None, extraHeaders = None):
    """
    Update the avatar URL of the player
    https://api.playfab.com/documentation/client/method/UpdateAvatarUrl
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UpdateAvatarUrl", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UpdateCharacterData(request, callback, customData = None, extraHeaders = None):
    """
    Creates and updates the title-specific custom data for the user's character which is readable and writable by the client
    https://api.playfab.com/documentation/client/method/UpdateCharacterData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UpdateCharacterData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UpdateCharacterStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Updates the values of the specified title-specific statistics for the specific character. By default, clients are not
    permitted to update statistics. Developers may override this setting in the Game Manager > Settings > API Features.
    https://api.playfab.com/documentation/client/method/UpdateCharacterStatistics
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UpdateCharacterStatistics", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UpdatePlayerStatistics(request, callback, customData = None, extraHeaders = None):
    """
    Updates the values of the specified title-specific statistics for the user. By default, clients are not permitted to
    update statistics. Developers may override this setting in the Game Manager > Settings > API Features.
    https://api.playfab.com/documentation/client/method/UpdatePlayerStatistics
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UpdatePlayerStatistics", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UpdateSharedGroupData(request, callback, customData = None, extraHeaders = None):
    """
    Adds, updates, and removes data keys for a shared group object. If the permission is set to Public, all fields updated
    or added in this call will be readable by users not in the group. By default, data permissions are set to Private.
    Regardless of the permission setting, only members of the group can update the data. Shared Groups are designed for
    sharing data between a very small number of players, please see our guide:
    https://api.playfab.com/docs/tutorials/landing-players/shared-groups
    https://api.playfab.com/documentation/client/method/UpdateSharedGroupData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UpdateSharedGroupData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UpdateUserData(request, callback, customData = None, extraHeaders = None):
    """
    Creates and updates the title-specific custom data for the user which is readable and writable by the client
    https://api.playfab.com/documentation/client/method/UpdateUserData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UpdateUserData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UpdateUserPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Creates and updates the publisher-specific custom data for the user which is readable and writable by the client
    https://api.playfab.com/documentation/client/method/UpdateUserPublisherData
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UpdateUserPublisherData", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UpdateUserTitleDisplayName(request, callback, customData = None, extraHeaders = None):
    """
    Updates the title specific display name for the user
    https://api.playfab.com/documentation/client/method/UpdateUserTitleDisplayName
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UpdateUserTitleDisplayName", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ValidateAmazonIAPReceipt(request, callback, customData = None, extraHeaders = None):
    """
    Validates with Amazon that the receipt for an Amazon App Store in-app purchase is valid and that it matches the
    purchased catalog item
    https://api.playfab.com/documentation/client/method/ValidateAmazonIAPReceipt
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ValidateAmazonIAPReceipt", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ValidateGooglePlayPurchase(request, callback, customData = None, extraHeaders = None):
    """
    Validates a Google Play purchase and gives the corresponding item to the player.
    https://api.playfab.com/documentation/client/method/ValidateGooglePlayPurchase
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ValidateGooglePlayPurchase", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ValidateIOSReceipt(request, callback, customData = None, extraHeaders = None):
    """
    Validates with the Apple store that the receipt for an iOS in-app purchase is valid and that it matches the purchased
    catalog item
    https://api.playfab.com/documentation/client/method/ValidateIOSReceipt
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ValidateIOSReceipt", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ValidateWindowsStoreReceipt(request, callback, customData = None, extraHeaders = None):
    """
    Validates with Windows that the receipt for an Windows App Store in-app purchase is valid and that it matches the
    purchased catalog item
    https://api.playfab.com/documentation/client/method/ValidateWindowsStoreReceipt
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ValidateWindowsStoreReceipt", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def WriteCharacterEvent(request, callback, customData = None, extraHeaders = None):
    """
    Writes a character-based event into PlayStream.
    https://api.playfab.com/documentation/client/method/WriteCharacterEvent
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/WriteCharacterEvent", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def WritePlayerEvent(request, callback, customData = None, extraHeaders = None):
    """
    Writes a player-based event into PlayStream.
    https://api.playfab.com/documentation/client/method/WritePlayerEvent
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/WritePlayerEvent", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def WriteTitleEvent(request, callback, customData = None, extraHeaders = None):
    """
    Writes a title-based event into PlayStream.
    https://api.playfab.com/documentation/client/method/WriteTitleEvent
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/WriteTitleEvent", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)


