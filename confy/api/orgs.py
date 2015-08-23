class Orgs(object):

    """Organizations are owned by users and only (s)he can add/remove teams and projects for that organization. A default organization will be created for every user.
    """

    def __init__(self, client):
        self.client = client

    def list(self, options={}):
        """List all organizations the authenticated user is a member of.

        '/orgs' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs', body, options)

        return response

    def retrieve(self, org, options={}):
        """Get the given organization if the authenticated user is a member.

        '/orgs/:org' GET

        Args:
            org: Name of the organization
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + org + '', body, options)

        return response

    def update(self, org, email, options={}):
        """Update the given organization if the authenticated user is the owner. __Email__ is the only thing which can be updated.

        '/orgs/:org' PATCH

        Args:
            org: Name of the organization
            email: Billing email of the organization
        """
        body = options['body'] if 'body' in options else {}
        body['email'] = email

        response = self.client.patch('/orgs/' + org + '', body, options)

        return response

