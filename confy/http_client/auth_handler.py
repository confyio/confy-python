class AuthHandler(object):

    """AuthHandler takes care of devising the auth type and using it"""

    HTTP_PASSWORD = 0

    def __init__(self, auth):
        self.auth = auth

    def get_auth_type(self):
        """Calculating the Authentication Type"""

        if 'username' in self.auth and 'password' in self.auth:
            return self.HTTP_PASSWORD

        return -1

    def set(self, request):
        if len(self.auth.keys()) == 0:
            return request

        auth = self.get_auth_type()
        flag = False

        if auth == self.HTTP_PASSWORD:
            request = self.http_password(request)
            flag = True

        if not flag:
            raise StandardError("Unable to calculate authorization method. Please check")

        return request

    def http_password(self, request):
        """Basic Authorization with username and password"""
        request['auth'] = (self.auth['username'], self.auth['password'])
        return request

