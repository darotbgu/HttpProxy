import logging
from collections import  namedtuple
import tornado.httpclient

HttpRequest = namedtuple('Request', ['url', 'method', 'body', 'headers'])


class HttpClient(object):
    _logger = logging.getLogger(__name__)

    def __init__(self):
        self._client = tornado.httpclient.AsyncHTTPClient()

    def send_request(self, request):
        self._logger.info("Sending {method} request to url={url}".format(method=request.method, url=request.url))
        req = tornado.httpclient.HTTPRequest(request.url,
                                             method=request.method,
                                             body=request.body,
                                             headers=request.headers,
                                             follow_redirects=False,
                                             allow_nonstandard_methods=True)
        return self._client.fetch(req, raise_error=False)

    def close(self):
        self._client.close()