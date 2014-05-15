class Access(object):

    """List of teams who has access to the project. Default team __Owners__ will have access to every project. Authenticated user should be the owner of the organization for the below endpoints.

    Args:
        org: Name of the organization
        project: Name of the project
    """

    def __init__(self, org, project, client):
        self.org = org
        self.project = project
        self.client = client

    def add(self, team, options={}):
        """Give the team access to the given project. The __team__ in the request needs to be a string.

        '/orgs/:org/projects/:project/access' POST

        Args:
            team: Name of the team
        """
        body = options['body'] if 'body' in options else {}
        body['team'] = team

        response = self.client.post('/orgs/' + self.org + '/projects/' + self.project + '/access', body, options)

        return response

    def remove(self, team, options={}):
        """Remove project access for the given team. The __team__ in the request needs to be a string. Can't delete default team's access.

        '/orgs/:org/projects/:project/access' DELETE

        Args:
            team: Name of the team
        """
        body = options['body'] if 'body' in options else {}
        body['team'] = team

        response = self.client.delete('/orgs/' + self.org + '/projects/' + self.project + '/access', body, options)

        return response

