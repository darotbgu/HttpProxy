import logging

from config.config import PORT
from server.proxy import ProxyServer


def main():
    logging.basicConfig(level=logging.INFO)
    proxy_server = ProxyServer(PORT)
    proxy_server.run()


if __name__ == '__main__':
    main()
