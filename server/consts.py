SUPPORTED_REQUESTS = ['GET', 'POST', 'CONNECT']


# URL
HOST_REGEX = "([^:/ ]+)"
PORT_REGEX = "([0-9]*)"
PATH_REGEX = "(.*[^:/])"

BASE_URL_PATH = r"{host}/{port}/{path}".format(host=HOST_REGEX, port=PORT_REGEX, path=PATH_REGEX)
CONNECT_URL_PATH = r"{host}/{port}".format(host=HOST_REGEX, port=PORT_REGEX)

# LOGS
EXECUTE_MIGRATIONS_LOG = "Executing DB initial migration"

NEW_REQUEST_LOG = "Got a {method} request for host={host}, port={port}, path={path}"
NEW_CONNECTION_LOG = "Got a CONNECT request for host={host}, port={port}"

# RESPONSE
FORWARD_URL = "http://{host}:{port}/{path}"
FORWARD_URL_QUERY = "http://{host}:{port}/{path}?{query}"
FORWARD_URL_NO_PATH = "http://{host}:{port}"

EXCLUDE_HEADERS = [
    # Hop By Hop headers
    'Connection',
    'Keep-Alive',
    'Public',
    'Proxy-Authenticate',
    'Proxy-Authorization',
    'Te',
    'Trailer',
    'Transfer-Encoding',
    'Upgrade',
    # Will be set automatically
    'Content-Encoding',
    'Content-Length']

CONTENT_ENCODING_HEADER = 'Content-Encoding'
HOST_HEADER = 'Host'
CONTENT_LENGTH_HEADER = 'Content-Length'
