class Projects(object):

    """An organization can contain any number of projects.

    Args:
        org: Name of the organization
    """

    def __init__(self, org, client):
        self.org = org
        self.client = client

    def list(self, options={}):
        """List all the projects of the organization which can be seen by the authenticated user.

        '/orgs/:org/projects' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/projects', body, options)

        return response

    def create(self, name, description, options={}):
        """Create a project for the given organization. Authenticated user should be the owner of the organization.

        '/orgs/:org/projects' POST

        Args:
            name: Name of the project
            description: Description of the project
        """
        body = options['body'] if 'body' in options else {}
        body['name'] = name
        body['description'] = description

        response = self.client.post('/orgs/' + self.org + '/projects', body, options)

        return response

    def retrieve(self, project, options={}):
        """Get a project the user has access to.

        '/orgs/:org/projects/:project' GET

        Args:
            project: Name of the project
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/projects/' + project + '', body, options)

        return response

    def update(self, project, description, options={}):
        """Update a project. Authenticated user should be the owner of the organization.

        '/orgs/:org/projects/:project' PATCH

        Args:
            project: Name of the project
            description: Description of the project
        """
        body = options['body'] if 'body' in options else {}
        body['description'] = description

        response = self.client.patch('/orgs/' + self.org + '/projects/' + project + '', body, options)

        return response

    def destroy(self, project, options={}):
        """Delete the given project. Cannot delete the default project in the organization. Authenticated user should be the owner of the organization.

        '/orgs/:org/projects/:project' DELETE

        Args:
            project: Name of the project
        """
        body = options['body'] if 'body' in options else {}

        response = self.client.delete('/orgs/' + self.org + '/projects/' + project + '', body, options)

        return response

