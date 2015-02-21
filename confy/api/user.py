class User(object):

    """User who is authenticated currently.
    """

    def __init__(self, client):
        self.client = client

    def retrieve(self, options={}):
        """Get the authenticated user's profile.

        '/user' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/user', body, options)

        return response

    def update(self, options={}):
        """Update the authenticated user's profile. Should use basic authentication.

        '/user' PATCH

        Args:
        """
        body = options['body'] if 'body' in options else {}

        response = self.client.patch('/user', body, options)

        return response

