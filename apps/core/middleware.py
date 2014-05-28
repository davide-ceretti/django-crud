from django.utils.cache import add_never_cache_headers

class DisableClientSideCachingMiddleware(object):
    """ A middleware object that prevent django to use
    any kind of cache when processing a request.
    This is quite important because, for example, when adding
    a new item in the database the item list must NOT be cached and
    it needs to be updated with the last insert """
    def process_response(self, request, response):
        add_never_cache_headers(response)
        return response