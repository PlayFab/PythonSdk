import py_compile

files = [
"PlayFabAdminAPI.py",
"PlayFabClientAPI.py",
"PlayFabMatchmakerAPI.py",
"PlayFabServerAPI.py",
"PlayFabAuthenticationAPI.py",
"PlayFabCloudScriptAPI.py",
"PlayFabDataAPI.py",
"PlayFabEventsAPI.py",
"PlayFabGroupsAPI.py",
"PlayFabProfilesAPI.py",

"__init__.py",
"PlayFabErrors.py",
"PlayFabPlayStreamEventsAPI.py",
"PlayFabHTTP.py",
"PlayFabSettings.py",
"PlayFabManualTest.py"
]

for eachFile in files:
    py_compile.compile(eachFile)
