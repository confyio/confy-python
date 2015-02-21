class Members(object):

    """Teams contain a list of users. The Authenticated user should be the owner of the organization.

    Args:
        org: Name of the organization
        team: Name of the team
    """

    def __init__(self, org, team, client):
        self.org = org
        self.team = team
        self.client = client

    def list(self, options={}):
        """List all the members in the given team. Authenticated user should be a member of the team or the owner of the org.

        '/orgs/:org/teams/:team/member' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/teams/' + self.team + '/member', body, options)

        return response

    def add(self, user, options={}):
        """Add the user to the given team. The __user__ in the request needs to be a string and be the username of a valid user.  The Authenticated user should be the owner of the organization.

        '/orgs/:org/teams/:team/member' POST

        Args:
            user: Username of the user
        """
        body = options['body'] if 'body' in options else {}
        body['user'] = user

        response = self.client.post('/orgs/' + self.org + '/teams/' + self.team + '/member', body, options)

        return response

    def remove(self, user, options={}):
        """Remove users from the given team. The __user__ in the request needs to be a string and be the username of a valid user. Cannot delete the default member in a team.  The Authenticated user should be the owner of the organization.

        '/orgs/:org/teams/:team/member' DELETE

        Args:
            user: Username of the user
        """
        body = options['body'] if 'body' in options else {}
        body['user'] = user

        response = self.client.delete('/orgs/' + self.org + '/teams/' + self.team + '/member', body, options)

        return response

