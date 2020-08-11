import tornado.gen
import tornado.httpclient

from auth.authorization import authorized
from server.handlers.basic.basicRequest import BasicRequestHandler


class GetRequestHandler(BasicRequestHandler):
    SUPPORTED_METHODS = ['GET']

    @tornado.gen.coroutine
    @authorized
    def get(self, host, port, path):
        return self.handle_request(host, port, path)
