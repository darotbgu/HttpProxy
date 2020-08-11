import asyncio
import logging
import sys

import tornado.ioloop
import tornado.web

from config.config import INIT_MIGRATE_PATH, RULES_FILE_PATH, DATABASE_FILE_PATH
from db.utils import execute_sql_script_sqlite
from policyEngine.engine import PolicyEngine
from server.consts import BASE_URL_PATH, EXECUTE_MIGRATIONS_LOG
from server.handlers.basic.get import GetRequestHandler
from server.handlers.basic.post import PostRequestHandler
from server.handlers.connect import ConnectRequestHandler


class ProxyServer(object):
    _logger = logging.getLogger(__name__)

    def __init__(self, port):
        self._port = port
        self._migrate_init()
        policy_engine = PolicyEngine()
        policy_engine.load_rules_from_json_file(RULES_FILE_PATH)

    def run(self):
        application = tornado.web.Application([
            (r"/get/{args}".format(args=BASE_URL_PATH), GetRequestHandler),
            (r"/post/{args}".format(args=BASE_URL_PATH), PostRequestHandler),
            (r'.*', ConnectRequestHandler),
            # (r"/connect/{args}".format(args=CONNECT_URL_PATH), ConnectRequestHandler),
        ])

        # Python 3.8 changed the default event loop on Windows (default is not compatible with Windows)
        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        self._logger.info("Listening on port {port}...".format(port=self._port))
        application.listen(self._port)

        self._logger.info("Starting proxy")
        try:
            tornado.ioloop.IOLoop.current().start()
        except KeyboardInterrupt:
            self._logger.critical('Shutting down...')

    def _migrate_init(self):
        """
        Execute DB Migrations
        """
        self._logger.info(EXECUTE_MIGRATIONS_LOG)
        execute_sql_script_sqlite(DATABASE_FILE_PATH, INIT_MIGRATE_PATH)



