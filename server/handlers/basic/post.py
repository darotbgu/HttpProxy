import tornado.gen

from auth.authorization import authorized
from server.handlers.basic.basicRequest import BasicRequestHandler


class PostRequestHandler(BasicRequestHandler):
    SUPPORTED_METHODS = ['POST']

    @tornado.gen.coroutine
    @authorized
    def post(self, host, port, path):
        return self.handle_request(host, port, path)
