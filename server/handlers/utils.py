from server.consts import FORWARD_URL_QUERY, FORWARD_URL, FORWARD_URL_NO_PATH


def create_remote_url(host, port, path=None, query=None):
    if path:
        if query:
            url = FORWARD_URL_QUERY.format(host=host, port=port, path=path, query=query)
        else:
            url = FORWARD_URL.format(host=host, port=port, path=path)
    else:
        url = FORWARD_URL_NO_PATH.format(host=host, port=port)
    return url
