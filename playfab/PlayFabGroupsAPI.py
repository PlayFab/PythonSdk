import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

"""
The Groups API is designed for any permanent or semi-permanent collections of Entities (players, or non-players). If you
want to make Guilds/Clans/Corporations/etc., then you should use groups. Groups can also be used to make chatrooms,
parties, or any other persistent collection of entities.
"""

def AcceptGroupApplication(request, callback, customData = None, extraHeaders = None):
    """
    Accepts an outstanding invitation to to join a group
    https://api.playfab.com/documentation/groups/method/AcceptGroupApplication
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/AcceptGroupApplication", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def AcceptGroupInvitation(request, callback, customData = None, extraHeaders = None):
    """
    Accepts an invitation to join a group
    https://api.playfab.com/documentation/groups/method/AcceptGroupInvitation
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/AcceptGroupInvitation", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def AddMembers(request, callback, customData = None, extraHeaders = None):
    """
    Adds members to a group or role.
    https://api.playfab.com/documentation/groups/method/AddMembers
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/AddMembers", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ApplyToGroup(request, callback, customData = None, extraHeaders = None):
    """
    Applies to join a group
    https://api.playfab.com/documentation/groups/method/ApplyToGroup
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ApplyToGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def BlockEntity(request, callback, customData = None, extraHeaders = None):
    """
    Blocks a list of entities from joining a group.
    https://api.playfab.com/documentation/groups/method/BlockEntity
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/BlockEntity", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ChangeMemberRole(request, callback, customData = None, extraHeaders = None):
    """
    Changes the role membership of a list of entities from one role to another.
    https://api.playfab.com/documentation/groups/method/ChangeMemberRole
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ChangeMemberRole", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateGroup(request, callback, customData = None, extraHeaders = None):
    """
    Creates a new group.
    https://api.playfab.com/documentation/groups/method/CreateGroup
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/CreateGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateRole(request, callback, customData = None, extraHeaders = None):
    """
    Creates a new group role.
    https://api.playfab.com/documentation/groups/method/CreateRole
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/CreateRole", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteGroup(request, callback, customData = None, extraHeaders = None):
    """
    Deletes a group and all roles, invitations, join requests, and blocks associated with it.
    https://api.playfab.com/documentation/groups/method/DeleteGroup
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/DeleteGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteRole(request, callback, customData = None, extraHeaders = None):
    """
    Deletes an existing role in a group.
    https://api.playfab.com/documentation/groups/method/DeleteRole
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/DeleteRole", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetGroup(request, callback, customData = None, extraHeaders = None):
    """
    Gets information about a group and its roles
    https://api.playfab.com/documentation/groups/method/GetGroup
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/GetGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def InviteToGroup(request, callback, customData = None, extraHeaders = None):
    """
    Invites a player to join a group
    https://api.playfab.com/documentation/groups/method/InviteToGroup
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/InviteToGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def IsMember(request, callback, customData = None, extraHeaders = None):
    """
    Checks to see if an entity is a member of a group or role within the group
    https://api.playfab.com/documentation/groups/method/IsMember
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/IsMember", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListGroupApplications(request, callback, customData = None, extraHeaders = None):
    """
    Lists all outstanding requests to join a group
    https://api.playfab.com/documentation/groups/method/ListGroupApplications
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListGroupApplications", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListGroupBlocks(request, callback, customData = None, extraHeaders = None):
    """
    Lists all entities blocked from joining a group
    https://api.playfab.com/documentation/groups/method/ListGroupBlocks
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListGroupBlocks", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListGroupInvitations(request, callback, customData = None, extraHeaders = None):
    """
    Lists all outstanding invitations for a group
    https://api.playfab.com/documentation/groups/method/ListGroupInvitations
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListGroupInvitations", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListGroupMembers(request, callback, customData = None, extraHeaders = None):
    """
    Lists all members for a group
    https://api.playfab.com/documentation/groups/method/ListGroupMembers
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListGroupMembers", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListMembership(request, callback, customData = None, extraHeaders = None):
    """
    Lists all groups and roles for an entity
    https://api.playfab.com/documentation/groups/method/ListMembership
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListMembership", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ListMembershipOpportunities(request, callback, customData = None, extraHeaders = None):
    """
    Lists all outstanding invitations and group applications for an entity
    https://api.playfab.com/documentation/groups/method/ListMembershipOpportunities
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/ListMembershipOpportunities", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def RemoveGroupApplication(request, callback, customData = None, extraHeaders = None):
    """
    Removes an application to join a group
    https://api.playfab.com/documentation/groups/method/RemoveGroupApplication
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/RemoveGroupApplication", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def RemoveGroupInvitation(request, callback, customData = None, extraHeaders = None):
    """
    Removes an invitation join a group
    https://api.playfab.com/documentation/groups/method/RemoveGroupInvitation
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/RemoveGroupInvitation", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def RemoveMembers(request, callback, customData = None, extraHeaders = None):
    """
    Removes members from a group.
    https://api.playfab.com/documentation/groups/method/RemoveMembers
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/RemoveMembers", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UnblockEntity(request, callback, customData = None, extraHeaders = None):
    """
    Unblocks a list of entities from joining a group
    https://api.playfab.com/documentation/groups/method/UnblockEntity
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/UnblockEntity", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UpdateGroup(request, callback, customData = None, extraHeaders = None):
    """
    Updates non-membership data about a group.
    https://api.playfab.com/documentation/groups/method/UpdateGroup
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/UpdateGroup", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UpdateRole(request, callback, customData = None, extraHeaders = None):
    """
    Updates metadata about a role.
    https://api.playfab.com/documentation/groups/method/UpdateRole
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/UpdateRole", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


