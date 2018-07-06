import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

# Enables the use of an external match-making service in conjunction with PlayFab hosted Game Server instances



# Validates a user with the PlayFab service
# https://api.playfab.com/documentation/matchmaker/method/AuthUser
def AuthUser(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Matchmaker/AuthUser", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Informs the PlayFab game server hosting service that the indicated user has joined the Game Server Instance specified
# https://api.playfab.com/documentation/matchmaker/method/PlayerJoined
def PlayerJoined(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Matchmaker/PlayerJoined", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Informs the PlayFab game server hosting service that the indicated user has left the Game Server Instance specified
# https://api.playfab.com/documentation/matchmaker/method/PlayerLeft
def PlayerLeft(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Matchmaker/PlayerLeft", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Instructs the PlayFab game server hosting service to instantiate a new Game Server Instance
# https://api.playfab.com/documentation/matchmaker/method/StartGame
def StartGame(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Matchmaker/StartGame", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

# Retrieves the relevant details for a specified user, which the external match-making service can then use to compute
# effective matches
# https://api.playfab.com/documentation/matchmaker/method/UserInfo
def UserInfo(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings.DeveloperSecretKey:
        raise PlayFabErrors.PlayFabException("Must have DeveloperSecretKey set to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Matchmaker/UserInfo", request, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, wrappedCallback, customData, extraHeaders)

