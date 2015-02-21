class Projects(object):

    """An organization can contain any number of projects.

    Args:
        org: Name of the organization
    """

    def __init__(self, org, client):
        self.org = org
        self.client = client

    def list(self, options={}):
        """List all the projects of the given organization which can be accessed by the authenticated user.

        '/orgs/:org/projects' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/projects', body, options)

        return response

    def create(self, name, description, options={}):
        """Create a project if the authenticated user is the owner of the given organization. Only the __owners__ team will be able to see the project initially.

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
        """Get the given project in the given organization. Works only if the authenticated user has access to the project.

        '/orgs/:org/projects/:project' GET

        Args:
            project: Name of the project
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/projects/' + project + '', body, options)

        return response

    def update(self, project, description, options={}):
        """Update the given project. __Description__ is the only thing which can be updated. Authenticated user should be the owner of the organization.

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
        """Delete the given project. Authenticated user should be the owner of the organization.

        '/orgs/:org/projects/:project' DELETE

        Args:
            project: Name of the project
        """
        body = options['body'] if 'body' in options else {}

        response = self.client.delete('/orgs/' + self.org + '/projects/' + project + '', body, options)

        return response

