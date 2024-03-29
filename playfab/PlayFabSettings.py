import playfab.PlayFabErrors as PlayFabErrors
import sys
import traceback

ProductionEnvironmentURL = ".playfabapi.com"

"""
The name of a customer vertical. This is only for customers running a private cluster. Generally you shouldn't touch this
"""
VerticalName = None

"""
You must set this value for PlayFabSdk to work properly (Found in the Game
Manager for your title, at the PlayFab Website)
"""

TitleId = ""

"""
You must set this value for Admin/Server/Matchmaker to work properly (Found in the Game
Manager for your title, at the PlayFab Website)
"""

DeveloperSecretKey = None

class InternalSettings:
    pass

_internalSettings = InternalSettings()

"""
This is automatically populated by the PlayFabAuthenticationApi.GetEntityToken method.
"""
_internalSettings.EntityToken = None

"""
This is automatically populated by any PlayFabClientApi.Login method.
"""
_internalSettings.ClientSessionTicket = None
_internalSettings.SdkVersionString = "PythonSdk-0.0.220411"
_internalSettings.RequestGetParams = {
    "sdk": _internalSettings.SdkVersionString
}

def GetURL(methodUrl, getParams):
    if not TitleId:
        raise PlayFabErrors.PlayFabException("You must set PlayFabSettings.TitleId before making an API call")

    url = []
    if not ProductionEnvironmentURL.startswith("http"):
        if VerticalName:
            url.append("https://")
            url.append(VerticalName)
        else:
            url.append("https://")
            url.append(TitleId)

    url.append(ProductionEnvironmentURL)
    url.append(methodUrl)

    if getParams:
        for idx, (k, v) in enumerate(getParams.items()):
            if idx == 0:
                url.append("?")
            else:
                url.append("&")
            url.append(k)
            url.append("=")
            url.append(v)

    return "".join(url)

def DefaultExceptionLogger(exceptionObj):
    print("Unexpected error:", sys.exc_info()[0])
    traceback.print_exc()

GlobalErrorHandler = None
GlobalExceptionLogger = DefaultExceptionLogger
