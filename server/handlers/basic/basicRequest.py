from server.consts import *
from server.handlers.request import Request
from server.httpClient.client import HttpClient, HttpRequest
from server.handlers.utils import create_remote_url


class BasicRequestHandler(Request):
    _http_client = None

    def initialize(self):
        self._http_client = HttpClient()

    def handle_request(self, host, port, path=None):
        self._logger.debug(NEW_REQUEST_LOG.format(method=self.request.method, host=host, port=port, path=path))

        request = self._create_forwarding_request(host, port, path)
        response = yield self._http_client.send_request(request)

        self.set_status(response.code)

        for header in response.headers:
            if header == CONTENT_LENGTH_HEADER:
                self.set_header(header, str(max(len(response.body), int(response.headers.get(header)))))
            if header not in EXCLUDE_HEADERS:
                self.set_header(header, response.headers.get(header))

        self.write(response.body)
        self.flush()

    def _create_forwarding_request(self, host, port, path):
        """
        Create Http request for the HttpClient,
        creates the url and adjust the headers for the request forwarding
        :param host: remote host
        :param port: remote port
        :param path: url path
        :return: HttpRequest
        """
        url = create_remote_url(host, port, path, self.request.query)
        method = self.request.method
        body = self.request.body if self.request.body else None

        headers = self.request.headers
        del headers[HOST_HEADER]

        return HttpRequest(url, method, body, headers)

    def on_finish(self):
        """
        Overriding tornado.web.RequestHandler.on_finish, making sure the http client is closed.
        """
        self._http_client.close()
