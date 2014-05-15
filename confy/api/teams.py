class Teams(object):

    """Every organization will have a default team named Owners. Owner of the organization will be a default member for every team.

    Args:
        org: Name of the organization
    """

    def __init__(self, org, client):
        self.org = org
        self.client = client

    def list(self, options={}):
        """List teams of the given organization authenticated user is a member of.

        '/orgs/:org/teams' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/teams', body, options)

        return response

    def create(self, name, description, options={}):
        """Create a team for the given organization. Authenticated user should be the owner of the organization.

        '/orgs/:org/teams' POST

        Args:
            name: Name of the team
            description: Description of the team
        """
        body = options['body'] if 'body' in options else {}
        body['name'] = name
        body['description'] = description

        response = self.client.post('/orgs/' + self.org + '/teams', body, options)

        return response

    def retrieve(self, team, options={}):
        """Get a team the user is member of.

        '/orgs/:org/teams/:team' GET

        Args:
            team: Name of the team
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/teams/' + team + '', body, options)

        return response

    def update(self, team, description, options={}):
        """Update a team. Authenticated user should be the owner of the organization.

        '/orgs/:org/teams/:team' PATCH

        Args:
            team: Name of the team
            description: Description of the team
        """
        body = options['body'] if 'body' in options else {}
        body['description'] = description

        response = self.client.patch('/orgs/' + self.org + '/teams/' + team + '', body, options)

        return response

    def destroy(self, team, options={}):
        """Delete the given team. Cannot delete the default team in the organization. Authenticated user should be the owner of the organization.

        '/orgs/:org/teams/:team' DELETE

        Args:
            team: Name of the team
        """
        body = options['body'] if 'body' in options else {}

        response = self.client.delete('/orgs/' + self.org + '/teams/' + team + '', body, options)

        return response

