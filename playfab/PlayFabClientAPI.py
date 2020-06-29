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
    https://docs.microsoft.com/rest/api/playfab/client/trading/accepttrade
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
    https://docs.microsoft.com/rest/api/playfab/client/friend-list-management/addfriend
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/addgenericid
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/addorupdatecontactemail
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
    please see our guide: https://docs.microsoft.com/gaming/playfab/features/social/groups/using-shared-group-data
    https://docs.microsoft.com/rest/api/playfab/client/shared-group-data/addsharedgroupmembers
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/addusernamepassword
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/adduservirtualcurrency
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
    https://docs.microsoft.com/rest/api/playfab/client/platform-specific-methods/androiddevicepushnotificationregistration
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
    https://docs.microsoft.com/rest/api/playfab/client/advertising/attributeinstall
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
    https://docs.microsoft.com/rest/api/playfab/client/trading/canceltrade
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/confirmpurchase
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/consumeitem
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ConsumeItem", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ConsumePSNEntitlements(request, callback, customData = None, extraHeaders = None):
    """
    Checks for any new consumable entitlements. If any are found, they are consumed and added as PlayFab items
    https://docs.microsoft.com/rest/api/playfab/client/platform-specific-methods/consumepsnentitlements
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ConsumePSNEntitlements", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ConsumeXboxEntitlements(request, callback, customData = None, extraHeaders = None):
    """
    Grants the player's current entitlements from Xbox Live, consuming all availble items in Xbox and granting them to the
    player's PlayFab inventory. This call is idempotent and will not grant previously granted items to the player.
    https://docs.microsoft.com/rest/api/playfab/client/platform-specific-methods/consumexboxentitlements
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
    https://docs.microsoft.com/gaming/playfab/features/social/groups/using-shared-group-data
    https://docs.microsoft.com/rest/api/playfab/client/shared-group-data/createsharedgroup
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
    https://docs.microsoft.com/rest/api/playfab/client/server-side-cloud-script/executecloudscript
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getaccountinfo
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetAccountInfo", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetAdPlacements(request, callback, customData = None, extraHeaders = None):
    """
    Returns a list of ad placements and a reward for each
    https://docs.microsoft.com/rest/api/playfab/client/advertising/getadplacements
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetAdPlacements", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetAllUsersCharacters(request, callback, customData = None, extraHeaders = None):
    """
    Lists all of the characters that belong to a specific user. CharacterIds are not globally unique; characterId must be
    evaluated with the parent PlayFabId to guarantee uniqueness.
    https://docs.microsoft.com/rest/api/playfab/client/characters/getalluserscharacters
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
    https://docs.microsoft.com/rest/api/playfab/client/title-wide-data-management/getcatalogitems
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
    https://docs.microsoft.com/rest/api/playfab/client/character-data/getcharacterdata
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/getcharacterinventory
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
    https://docs.microsoft.com/rest/api/playfab/client/characters/getcharacterleaderboard
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
    https://docs.microsoft.com/rest/api/playfab/client/character-data/getcharacterreadonlydata
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
    https://docs.microsoft.com/rest/api/playfab/client/characters/getcharacterstatistics
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
    https://community.playfab.com/hc/community/posts/205469488-How-to-upload-files-to-PlayFab-s-Content-Service. Also,
    please be aware that the Content service is specifically PlayFab's CDN offering, for which standard CDN rates apply.
    https://docs.microsoft.com/rest/api/playfab/client/content/getcontentdownloadurl
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
    https://docs.microsoft.com/rest/api/playfab/client/matchmaking/getcurrentgames
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getfriendleaderboard
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getfriendleaderboardaroundplayer
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
    https://docs.microsoft.com/rest/api/playfab/client/friend-list-management/getfriendslist
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
    https://docs.microsoft.com/rest/api/playfab/client/matchmaking/getgameserverregions
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getleaderboard
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
    https://docs.microsoft.com/rest/api/playfab/client/characters/getleaderboardaroundcharacter
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getleaderboardaroundplayer
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
    https://docs.microsoft.com/rest/api/playfab/client/characters/getleaderboardforusercharacters
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/getpaymenttoken
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
    https://docs.microsoft.com/gaming/playfab/features/multiplayer/photon/quickstart for more details.
    https://docs.microsoft.com/rest/api/playfab/client/authentication/getphotonauthenticationtoken
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayercombinedinfo
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayerprofile
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
    https://docs.microsoft.com/rest/api/playfab/client/playstream/getplayersegments
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getplayerstatistics
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getplayerstatisticversions
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
    https://docs.microsoft.com/rest/api/playfab/client/playstream/getplayertags
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
    https://docs.microsoft.com/rest/api/playfab/client/trading/getplayertrades
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfromfacebookids
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfromfacebookinstantgamesids
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfromgamecenterids
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfromgenericids
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfromgoogleids
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfromkongregateids
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfromnintendoswitchdeviceids
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromNintendoSwitchDeviceIds", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromPSNAccountIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of PlayStation Network identifiers.
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfrompsnaccountids
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromPSNAccountIDs", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromSteamIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of Steam identifiers. The Steam identifiers are the profile
    IDs for the user accounts, available as SteamId in the Steamworks Community API calls.
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfromsteamids
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfromtwitchids
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromTwitchIDs", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPlayFabIDsFromXboxLiveIDs(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the unique PlayFab identifiers for the given set of XboxLive identifiers.
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getplayfabidsfromxboxliveids
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetPlayFabIDsFromXboxLiveIDs", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def GetPublisherData(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the key-value store of custom publisher settings
    https://docs.microsoft.com/rest/api/playfab/client/title-wide-data-management/getpublisherdata
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/getpurchase
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
    https://docs.microsoft.com/gaming/playfab/features/social/groups/using-shared-group-data
    https://docs.microsoft.com/rest/api/playfab/client/shared-group-data/getsharedgroupdata
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
    https://docs.microsoft.com/rest/api/playfab/client/title-wide-data-management/getstoreitems
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
    https://docs.microsoft.com/rest/api/playfab/client/title-wide-data-management/gettime
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
    https://docs.microsoft.com/rest/api/playfab/client/title-wide-data-management/gettitledata
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
    https://docs.microsoft.com/rest/api/playfab/client/title-wide-data-management/gettitlenews
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/gettitlepublickey
    """
    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetTitlePublicKey", request, None, None, wrappedCallback, customData, extraHeaders)

def GetTradeStatus(request, callback, customData = None, extraHeaders = None):
    """
    Gets the current status of an existing trade.
    https://docs.microsoft.com/rest/api/playfab/client/trading/gettradestatus
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getuserdata
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/getuserinventory
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getuserpublisherdata
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getuserpublisherreadonlydata
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getuserreadonlydata
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/getwindowshellochallenge
    """
    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/GetWindowsHelloChallenge", request, None, None, wrappedCallback, customData, extraHeaders)

def GrantCharacterToUser(request, callback, customData = None, extraHeaders = None):
    """
    Grants the specified character type to the user. CharacterIds are not globally unique; characterId must be evaluated
    with the parent PlayFabId to guarantee uniqueness.
    https://docs.microsoft.com/rest/api/playfab/client/characters/grantcharactertouser
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkandroiddeviceid
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkAndroidDeviceID", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkApple(request, callback, customData = None, extraHeaders = None):
    """
    Links the Apple account associated with the token to the user's PlayFab account.
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkapple
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkApple", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkCustomID(request, callback, customData = None, extraHeaders = None):
    """
    Links the custom identifier, generated by the title, to the user's PlayFab account
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkcustomid
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkfacebookaccount
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkfacebookinstantgamesid
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkgamecenteraccount
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkgoogleaccount
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkiosdeviceid
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkkongregate
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkKongregate", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkNintendoServiceAccount(request, callback, customData = None, extraHeaders = None):
    """
    Links the Nintendo account associated with the token to the user's PlayFab account.
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linknintendoserviceaccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkNintendoServiceAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkNintendoSwitchDeviceId(request, callback, customData = None, extraHeaders = None):
    """
    Links the NintendoSwitchDeviceId to the user's PlayFab account
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linknintendoswitchdeviceid
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkNintendoSwitchDeviceId", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkOpenIdConnect(request, callback, customData = None, extraHeaders = None):
    """
    Links an OpenID Connect account to a user's PlayFab account, based on an existing relationship between a title and an
    Open ID Connect provider and the OpenId Connect JWT from that provider.
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkopenidconnect
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkOpenIdConnect", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkPSNAccount(request, callback, customData = None, extraHeaders = None):
    """
    Links the PlayStation Network account associated with the provided access code to the user's PlayFab account
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkpsnaccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/LinkPSNAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def LinkSteamAccount(request, callback, customData = None, extraHeaders = None):
    """
    Links the Steam account associated with the provided Steam authentication ticket to the user's PlayFab account
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linksteamaccount
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linktwitch
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkwindowshello
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/linkxboxaccount
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithandroiddeviceid
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

def LoginWithApple(request, callback, customData = None, extraHeaders = None):
    """
    Signs in the user with a Sign in with Apple identity token.
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithapple
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

    PlayFabHTTP.DoPost("/Client/LoginWithApple", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithCustomID(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a custom unique identifier generated by the title, returning a session identifier that can
    subsequently be used for API calls which require an authenticated user
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithcustomid
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithemailaddress
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithfacebook
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithfacebookinstantgamesid
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithgamecenter
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithgoogleaccount
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithiosdeviceid
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithkongregate
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

def LoginWithNintendoServiceAccount(request, callback, customData = None, extraHeaders = None):
    """
    Signs in the user with a Nintendo service account token.
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithnintendoserviceaccount
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

    PlayFabHTTP.DoPost("/Client/LoginWithNintendoServiceAccount", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithNintendoSwitchDeviceId(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a Nintendo Switch Device ID, returning a session identifier that can subsequently be used for
    API calls which require an authenticated user
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithnintendoswitchdeviceid
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

def LoginWithOpenIdConnect(request, callback, customData = None, extraHeaders = None):
    """
    Logs in a user with an Open ID Connect JWT created by an existing relationship between a title and an Open ID Connect
    provider.
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithopenidconnect
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

    PlayFabHTTP.DoPost("/Client/LoginWithOpenIdConnect", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithPlayFab(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user into the PlayFab account, returning a session identifier that can subsequently be used for API calls
    which require an authenticated user. Unlike most other login API calls, LoginWithPlayFab does not permit the creation of
    new accounts via the CreateAccountFlag. Username/Password credentials may be used to create accounts via
    RegisterPlayFabUser, or added to existing accounts using AddUsernamePassword.
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithplayfab
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

def LoginWithPSN(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a PlayStation Network authentication code, returning a session identifier that can subsequently
    be used for API calls which require an authenticated user
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithpsn
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

    PlayFabHTTP.DoPost("/Client/LoginWithPSN", request, None, None, wrappedCallback, customData, extraHeaders)

def LoginWithSteam(request, callback, customData = None, extraHeaders = None):
    """
    Signs the user in using a Steam authentication ticket, returning a session identifier that can subsequently be used for
    API calls which require an authenticated user
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithsteam
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithtwitch
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithwindowshello
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/loginwithxbox
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
    https://docs.microsoft.com/rest/api/playfab/client/matchmaking/matchmake
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
    https://docs.microsoft.com/rest/api/playfab/client/trading/opentrade
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/payforpurchase
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/purchaseitem
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/redeemcoupon
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RedeemCoupon", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def RefreshPSNAuthToken(request, callback, customData = None, extraHeaders = None):
    """
    Uses the supplied OAuth code to refresh the internally cached player PSN auth token
    https://docs.microsoft.com/rest/api/playfab/client/platform-specific-methods/refreshpsnauthtoken
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RefreshPSNAuthToken", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def RegisterForIOSPushNotification(request, callback, customData = None, extraHeaders = None):
    """
    Registers the iOS device to receive push notifications
    https://docs.microsoft.com/rest/api/playfab/client/platform-specific-methods/registerforiospushnotification
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/registerplayfabuser
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/registerwithwindowshello
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/removecontactemail
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
    https://docs.microsoft.com/rest/api/playfab/client/friend-list-management/removefriend
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/removegenericid
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
    guide: https://docs.microsoft.com/gaming/playfab/features/social/groups/using-shared-group-data
    https://docs.microsoft.com/rest/api/playfab/client/shared-group-data/removesharedgroupmembers
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RemoveSharedGroupMembers", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ReportAdActivity(request, callback, customData = None, extraHeaders = None):
    """
    Report player's ad activity
    https://docs.microsoft.com/rest/api/playfab/client/advertising/reportadactivity
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/ReportAdActivity", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def ReportDeviceInfo(request, callback, customData = None, extraHeaders = None):
    """
    Write a PlayStream event to describe the provided player device information. This API method is not designed to be
    called directly by developers. Each PlayFab client SDK will eventually report this information automatically.
    https://docs.microsoft.com/rest/api/playfab/client/analytics/reportdeviceinfo
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/reportplayer
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
    https://docs.microsoft.com/rest/api/playfab/client/platform-specific-methods/restoreiospurchases
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RestoreIOSPurchases", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def RewardAdActivity(request, callback, customData = None, extraHeaders = None):
    """
    Reward player's ad activity
    https://docs.microsoft.com/rest/api/playfab/client/advertising/rewardadactivity
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/RewardAdActivity", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def SendAccountRecoveryEmail(request, callback, customData = None, extraHeaders = None):
    """
    Forces an email to be sent to the registered email address for the user's account, with a link allowing the user to
    change the password.If an account recovery email template ID is provided, an email using the custom email template will
    be used.
    https://docs.microsoft.com/rest/api/playfab/client/account-management/sendaccountrecoveryemail
    """
    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/SendAccountRecoveryEmail", request, None, None, wrappedCallback, customData, extraHeaders)

def SetFriendTags(request, callback, customData = None, extraHeaders = None):
    """
    Updates the tag list for a specified user in the friend list of the local user
    https://docs.microsoft.com/rest/api/playfab/client/friend-list-management/setfriendtags
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
    https://docs.microsoft.com/rest/api/playfab/client/authentication/setplayersecret
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
    https://docs.microsoft.com/rest/api/playfab/client/matchmaking/startgame
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/startpurchase
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/subtractuservirtualcurrency
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkandroiddeviceid
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkAndroidDeviceID", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkApple(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Apple account from the user's PlayFab account.
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkapple
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkApple", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkCustomID(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related custom identifier from the user's PlayFab account
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkcustomid
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkfacebookaccount
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkfacebookinstantgamesid
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkgamecenteraccount
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkgoogleaccount
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkiosdeviceid
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkkongregate
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkKongregate", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkNintendoServiceAccount(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Nintendo account from the user's PlayFab account.
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinknintendoserviceaccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkNintendoServiceAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkNintendoSwitchDeviceId(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related NintendoSwitchDeviceId from the user's PlayFab account
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinknintendoswitchdeviceid
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkNintendoSwitchDeviceId", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkOpenIdConnect(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks an OpenID Connect account from a user's PlayFab account, based on the connection ID of an existing relationship
    between a title and an Open ID Connect provider.
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkopenidconnect
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkOpenIdConnect", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkPSNAccount(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related PSN account from the user's PlayFab account
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkpsnaccount
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/UnlinkPSNAccount", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)

def UnlinkSteamAccount(request, callback, customData = None, extraHeaders = None):
    """
    Unlinks the related Steam account from the user's PlayFab account
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinksteamaccount
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinktwitch
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkwindowshello
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/unlinkxboxaccount
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/unlockcontainerinstance
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
    https://docs.microsoft.com/rest/api/playfab/client/player-item-management/unlockcontaineritem
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/updateavatarurl
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
    https://docs.microsoft.com/rest/api/playfab/client/character-data/updatecharacterdata
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
    https://docs.microsoft.com/rest/api/playfab/client/characters/updatecharacterstatistics
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/updateplayerstatistics
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
    https://docs.microsoft.com/gaming/playfab/features/social/groups/using-shared-group-data
    https://docs.microsoft.com/rest/api/playfab/client/shared-group-data/updatesharedgroupdata
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/updateuserdata
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
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/updateuserpublisherdata
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
    https://docs.microsoft.com/rest/api/playfab/client/account-management/updateusertitledisplayname
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
    https://docs.microsoft.com/rest/api/playfab/client/platform-specific-methods/validateamazoniapreceipt
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
    https://docs.microsoft.com/rest/api/playfab/client/platform-specific-methods/validategoogleplaypurchase
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
    https://docs.microsoft.com/rest/api/playfab/client/platform-specific-methods/validateiosreceipt
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
    https://docs.microsoft.com/rest/api/playfab/client/platform-specific-methods/validatewindowsstorereceipt
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
    https://docs.microsoft.com/rest/api/playfab/client/analytics/writecharacterevent
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
    https://docs.microsoft.com/rest/api/playfab/client/analytics/writeplayerevent
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
    https://docs.microsoft.com/rest/api/playfab/client/analytics/writetitleevent
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Client/WriteTitleEvent", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)


