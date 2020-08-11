import os
import socket
from urllib.parse import urlparse

import tornado.websocket
import tornado.gen
import tornado.tcpclient

from auth.authorization import authorized
from server.consts import NEW_CONNECTION_LOG
from server.handlers.request import Request
from server.tcpTunnel.tunnel import TCPTunnel


class ConnectRequestHandler(Request):
    SUPPORTED_METHODS = ['CONNECT']

    def initialize(self):
        pass

    # @tornado.gen.coroutine
    # @authorized
    async def connect(self):
        host, port = self.request.uri.split(':')
        self._logger.debug(NEW_CONNECTION_LOG.format(host=host, port=port))
        return await self.handle_request(host, port)

    async def handle_request(self, host, port, **kwargs):
        client_stream = self.request.connection.stream
        tcp_tunnel = TCPTunnel(client_stream)
        return await tcp_tunnel.connect(host, port)

