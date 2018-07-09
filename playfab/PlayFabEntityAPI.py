import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

# PlayFab Entity APIs provide a variety of core PlayFab features and work consistently across a broad set of entities,
# such as titles, players, characters, and more. API methods for executing CloudScript with an Entity Profile



# Abort pending file uploads to an entity's profile.
# https://api.playfab.com/documentation/entity/method/AbortFileUploads
def AbortFileUploads(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/File/AbortFileUploads", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Accepts an outstanding invitation to to join a group
# https://api.playfab.com/documentation/entity/method/AcceptGroupApplication
def AcceptGroupApplication(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/AcceptGroupApplication", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Accepts an invitation to join a group
# https://api.playfab.com/documentation/entity/method/AcceptGroupInvitation
def AcceptGroupInvitation(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/AcceptGroupInvitation", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Adds members to a group or role.
# https://api.playfab.com/documentation/entity/method/AddMembers
def AddMembers(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/AddMembers", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Applies to join a group
# https://api.playfab.com/documentation/entity/method/ApplyToGroup
def ApplyToGroup(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ApplyToGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Blocks a list of entities from joining a group.
# https://api.playfab.com/documentation/entity/method/BlockEntity
def BlockEntity(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/BlockEntity", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Changes the role membership of a list of entities from one role to another.
# https://api.playfab.com/documentation/entity/method/ChangeMemberRole
def ChangeMemberRole(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ChangeMemberRole", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Creates a new group.
# https://api.playfab.com/documentation/entity/method/CreateGroup
def CreateGroup(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/CreateGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Creates a new group role.
# https://api.playfab.com/documentation/entity/method/CreateRole
def CreateRole(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/CreateRole", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Delete files on an entity's profile.
# https://api.playfab.com/documentation/entity/method/DeleteFiles
def DeleteFiles(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/File/DeleteFiles", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Deletes a group and all roles, invitations, join requests, and blocks associated with it.
# https://api.playfab.com/documentation/entity/method/DeleteGroup
def DeleteGroup(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/DeleteGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Deletes an existing role in a group.
# https://api.playfab.com/documentation/entity/method/DeleteRole
def DeleteRole(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/DeleteRole", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Executes CloudScript using the Entity Profile
# https://api.playfab.com/documentation/entity/method/ExecuteEntityCloudScript
def ExecuteEntityCloudScript(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/CloudScript/ExecuteEntityCloudScript", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Finalize file uploads to an entity's profile.
# https://api.playfab.com/documentation/entity/method/FinalizeFileUploads
def FinalizeFileUploads(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/File/FinalizeFileUploads", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Method to exchange a legacy AuthenticationTicket or title SecretKey for an Entity Token or to refresh a still valid
# Entity Token.
# https://api.playfab.com/documentation/entity/method/GetEntityToken
def GetEntityToken(request, callback, customData = None, extraHeaders = None):
    authKey = None
    authValue = None
    if PlayFabSettings._internalSettings.EntityToken:
        authKey = "X-EntityToken"
        authValue = PlayFabSettings._internalSettings.EntityToken
    elif PlayFabSettings._internalSettings.ClientSessionTicket:
        authKey = "X-Authorization"
        authValue = PlayFabSettings._internalSettings.ClientSessionTicket 
    elif PlayFabSettings.DeveloperSecretKey:
        authKey = "X-SecretKey"
        authValue = PlayFabSettings.DeveloperSecretKey 

    def wrappedCallback(playFabResult, error):
        PlayFabSettings._internalSettings.EntityToken = playFabResult["EntityToken"] or PlayFabSettings._internalSettings.EntityToken
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Authentication/GetEntityToken", request, authKey, authValue, wrappedCallback, customData, extraHeaders)

# Retrieves file metadata from an entity's profile.
# https://api.playfab.com/documentation/entity/method/GetFiles
def GetFiles(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/File/GetFiles", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Gets the global title access policy
# https://api.playfab.com/documentation/entity/method/GetGlobalPolicy
def GetGlobalPolicy(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/GetGlobalPolicy", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Gets information about a group and its roles
# https://api.playfab.com/documentation/entity/method/GetGroup
def GetGroup(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/GetGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Retrieves objects from an entity's profile.
# https://api.playfab.com/documentation/entity/method/GetObjects
def GetObjects(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Object/GetObjects", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Retrieves the entity's profile.
# https://api.playfab.com/documentation/entity/method/GetProfile
def GetProfile(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/GetProfile", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Retrieves the entity's profile.
# https://api.playfab.com/documentation/entity/method/GetProfiles
def GetProfiles(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/GetProfiles", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Initiates file uploads to an entity's profile.
# https://api.playfab.com/documentation/entity/method/InitiateFileUploads
def InitiateFileUploads(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/File/InitiateFileUploads", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Invites a player to join a group
# https://api.playfab.com/documentation/entity/method/InviteToGroup
def InviteToGroup(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/InviteToGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Checks to see if an entity is a member of a group or role within the group
# https://api.playfab.com/documentation/entity/method/IsMember
def IsMember(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/IsMember", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Lists all outstanding requests to join a group
# https://api.playfab.com/documentation/entity/method/ListGroupApplications
def ListGroupApplications(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListGroupApplications", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Lists all entities blocked from joining a group
# https://api.playfab.com/documentation/entity/method/ListGroupBlocks
def ListGroupBlocks(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListGroupBlocks", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Lists all outstanding invitations for a group
# https://api.playfab.com/documentation/entity/method/ListGroupInvitations
def ListGroupInvitations(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListGroupInvitations", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Lists all members for a group
# https://api.playfab.com/documentation/entity/method/ListGroupMembers
def ListGroupMembers(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListGroupMembers", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Lists all groups and roles for an entity
# https://api.playfab.com/documentation/entity/method/ListMembership
def ListMembership(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListMembership", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Lists all outstanding invitations and group applications for an entity
# https://api.playfab.com/documentation/entity/method/ListMembershipOpportunities
def ListMembershipOpportunities(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListMembershipOpportunities", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Removes an application to join a group
# https://api.playfab.com/documentation/entity/method/RemoveGroupApplication
def RemoveGroupApplication(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/RemoveGroupApplication", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Removes an invitation join a group
# https://api.playfab.com/documentation/entity/method/RemoveGroupInvitation
def RemoveGroupInvitation(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/RemoveGroupInvitation", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Removes members from a group.
# https://api.playfab.com/documentation/entity/method/RemoveMembers
def RemoveMembers(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/RemoveMembers", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Sets the global title access policy
# https://api.playfab.com/documentation/entity/method/SetGlobalPolicy
def SetGlobalPolicy(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/SetGlobalPolicy", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Sets objects on an entity's profile.
# https://api.playfab.com/documentation/entity/method/SetObjects
def SetObjects(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Object/SetObjects", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Sets the profiles access policy
# https://api.playfab.com/documentation/entity/method/SetProfilePolicy
def SetProfilePolicy(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Profile/SetProfilePolicy", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Unblocks a list of entities from joining a group
# https://api.playfab.com/documentation/entity/method/UnblockEntity
def UnblockEntity(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/UnblockEntity", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Updates non-membership data about a group.
# https://api.playfab.com/documentation/entity/method/UpdateGroup
def UpdateGroup(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/UpdateGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Updates metadata about a role.
# https://api.playfab.com/documentation/entity/method/UpdateRole
def UpdateRole(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/UpdateRole", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

# Write batches of entity based events to PlayStream.
# https://api.playfab.com/documentation/entity/method/WriteEvents
def WriteEvents(request, callback, customData = None, extraHeaders = None):
    if not PlayFabSettings._internalSettings.EntityToken:
         raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Event/WriteEvents", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

