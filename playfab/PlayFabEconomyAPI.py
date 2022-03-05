import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabHTTP as PlayFabHTTP
import playfab.PlayFabSettings as PlayFabSettings

""" API methods for managing the catalog. Inventory manages in-game assets for any given entity. """


def CreateDraftItem(request, callback, customData = None, extraHeaders = None):
    """
    Creates a new item in the working catalog using provided metadata.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/createdraftitem
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/CreateDraftItem", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def CreateUploadUrls(request, callback, customData = None, extraHeaders = None):
    """
    Creates one or more upload URLs which can be used by the client to upload raw file data.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/createuploadurls
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/CreateUploadUrls", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteEntityItemReviews(request, callback, customData = None, extraHeaders = None):
    """
    Deletes all reviews, helpfulness votes, and ratings submitted by the entity specified.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/deleteentityitemreviews
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/DeleteEntityItemReviews", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def DeleteItem(request, callback, customData = None, extraHeaders = None):
    """
    Removes an item from working catalog and all published versions from the public catalog.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/deleteitem
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/DeleteItem", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetCatalogConfig(request, callback, customData = None, extraHeaders = None):
    """
    Gets the configuration for the catalog.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getcatalogconfig
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetCatalogConfig", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetDraftItem(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves an item from the working catalog. This item represents the current working state of the item.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getdraftitem
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetDraftItem", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetDraftItems(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a paginated list of the items from the draft catalog.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getdraftitems
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetDraftItems", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetEntityDraftItems(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves a paginated list of the items from the draft catalog created by the Entity.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getentitydraftitems
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetEntityDraftItems", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetEntityItemReview(request, callback, customData = None, extraHeaders = None):
    """
    Gets the submitted review for the specified item by the authenticated entity.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getentityitemreview
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetEntityItemReview", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetItem(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves an item from the public catalog.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getitem
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetItem", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetItemModerationState(request, callback, customData = None, extraHeaders = None):
    """
    Gets the moderation state for an item, including the concern category and string reason.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getitemmoderationstate
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetItemModerationState", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetItemPublishStatus(request, callback, customData = None, extraHeaders = None):
    """
    Gets the status of a publish of an item.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getitempublishstatus
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetItemPublishStatus", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetItemReviews(request, callback, customData = None, extraHeaders = None):
    """
    Get a paginated set of reviews associated with the specified item.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getitemreviews
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetItemReviews", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetItemReviewSummary(request, callback, customData = None, extraHeaders = None):
    """
    Get a summary of all reviews associated with the specified item.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getitemreviewsummary
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetItemReviewSummary", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def GetItems(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves items from the public catalog.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/getitems
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/GetItems", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def PublishDraftItem(request, callback, customData = None, extraHeaders = None):
    """
    Initiates a publish of an item from the working catalog to the public catalog.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/publishdraftitem
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/PublishDraftItem", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ReportItem(request, callback, customData = None, extraHeaders = None):
    """
    Submit a report for an item, indicating in what way the item is inappropriate.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/reportitem
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/ReportItem", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ReportItemReview(request, callback, customData = None, extraHeaders = None):
    """
    Submit a report for a review
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/reportitemreview
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/ReportItemReview", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def ReviewItem(request, callback, customData = None, extraHeaders = None):
    """
    Creates or updates a review for the specified item.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/reviewitem
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/ReviewItem", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SearchItems(request, callback, customData = None, extraHeaders = None):
    """
    Executes a search against the public catalog using the provided search parameters and returns a set of paginated
    results.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/searchitems
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/SearchItems", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SetItemModerationState(request, callback, customData = None, extraHeaders = None):
    """
    Sets the moderation state for an item, including the concern category and string reason.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/setitemmoderationstate
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/SetItemModerationState", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def SubmitItemReviewVote(request, callback, customData = None, extraHeaders = None):
    """
    Submit a vote for a review, indicating whether the review was helpful or unhelpful.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/submititemreviewvote
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/SubmitItemReviewVote", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def TakedownItemReviews(request, callback, customData = None, extraHeaders = None):
    """
    Submit a request to takedown one or more reviews.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/takedownitemreviews
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/TakedownItemReviews", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UpdateCatalogConfig(request, callback, customData = None, extraHeaders = None):
    """
    Updates the configuration for the catalog.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/updatecatalogconfig
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/UpdateCatalogConfig", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)

def UpdateDraftItem(request, callback, customData = None, extraHeaders = None):
    """
    Update the metadata for an item in the working catalog.
    https://docs.microsoft.com/rest/api/playfab/economy/catalog/updatedraftitem
    """
    if not PlayFabSettings._internalSettings.EntityToken:
        raise PlayFabErrors.PlayFabException("Must call GetEntityToken before calling this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    PlayFabHTTP.DoPost("/Catalog/UpdateDraftItem", request, "X-EntityToken", PlayFabSettings._internalSettings.EntityToken, wrappedCallback, customData, extraHeaders)


