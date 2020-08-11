import logging

import tornado.web
import tornado.websocket

from abc import abstractmethod


class Request(tornado.web.RequestHandler):
    """ Base class for custom request handlers"""

    _logger = logging.getLogger(__name__)

    @abstractmethod
    def initialize(self):
        """
        Override RequestHandler.initialize
        """
        pass

    @abstractmethod
    def handle_request(self, host, port, **kwargs):
        """
        Handles HTTP request which will be forwarded to the given host:port
        :param host: remote host
        :param port: remote port
        """
        pass
