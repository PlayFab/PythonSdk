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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/acceptgroupapplication
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/acceptgroupinvitation
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/addmembers
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/applytogroup
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/blockentity
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/changememberrole
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/creategroup
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/createrole
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/deletegroup
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/deleterole
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/getgroup
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/invitetogroup
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/ismember
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/listgroupapplications
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/listgroupblocks
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/listgroupinvitations
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/listgroupmembers
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/listmembership
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/listmembershipopportunities
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/removegroupapplication
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/removegroupinvitation
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/removemembers
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/unblockentity
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/updategroup
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
    https://docs.microsoft.com/rest/api/playfab/groups/groups/updaterole
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Group/UpdateRole", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


