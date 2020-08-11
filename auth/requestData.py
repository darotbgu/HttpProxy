class RequestData(object):
    SOURCE_USER_KEY = 'username'

    def __init__(self, request,  host, port):
        self._request = request
        self._host = host
        self._port = port

    @property
    def source_ip(self):
        return self._request.remote_ip

    @property
    def source_user(self):
        user = self._request.body_arguments.get(self.SOURCE_USER_KEY)
        if user:
            user = user[0]
        return user

    @property
    def destination_host(self):
        return self._host

    @property
    def destination_port(self):
        return self._port

    @property
    def method(self):
        return self._request.method

