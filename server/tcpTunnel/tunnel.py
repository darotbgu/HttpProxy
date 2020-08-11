import logging
import socket
import ssl

import tornado.iostream
import tornado.tcpclient


class TCPTunnel(object):
    _logger = logging.getLogger(__name__)

    def __init__(self, client_stream):
        self._client_stream = client_stream
        _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self._server_stream = tornado.iostream.IOStream(_socket)

    async def connect(self, host, port):
        await self._server_stream.connect((host, int(port)))
        self._logger.info("Connected tunnel to host={host},port={port}".format(host=host, port=port))
        await self._client_stream.write(b'HTTP/1.1 200 OK\r\n\r\n')
        await self._start_tunnel()

    async def _start_tunnel(self):
        server_stream = self._server_stream
        client_stream = self._client_stream

        def _on_client_stream_close():
            if server_stream.closed():
                return
            server_stream.close()

        def _on_server_stream_close():
            if client_stream.closed():
                return
            client_stream.close()

        self._client_stream.set_close_callback(_on_client_stream_close)
        self._server_stream.set_close_callback(_on_server_stream_close)
        await self._server_stream.read_until_close()
        await self.read_from_upstream()
        await self.read_from_client()

    async def read_from_client(self):
        data = await self._client_stream.read_until(b"\r\n")
        await self._server_stream.write(data)

    async def read_from_upstream(self):
        data = await self._server_stream.read_until(b"\r\n")
        await self._client_stream.write(data)



