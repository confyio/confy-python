from .http_client import HttpClient

# Assign all the api classes
from .api.user import User
from .api.orgs import Orgs


class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def user(self):
        """User who is authenticated currently.
        """
        return User(self.http_client)

    def orgs(self):
        """Organizations are owned by users and only (s)he can add/remove teams and projects for that organization. A default organization will be created for every user.
        """
        return Orgs(self.http_client)

