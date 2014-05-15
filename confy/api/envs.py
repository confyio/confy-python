class Envs(object):

    """Every project has a default environment named Production. Each environment has one configuration document which can have many keys and values.

    Args:
        org: Name of the organization
        project: Name of the project
    """

    def __init__(self, org, project, client):
        self.org = org
        self.project = project
        self.client = client

    def list(self, options={}):
        """List all the environmens of the project which can be seen by the authenticated user.

        '/orgs/:org/projects/:project/envs' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/projects/' + self.project + '/envs', body, options)

        return response

    def create(self, name, description, options={}):
        """Create an environment for the given project. Authenticated user should have access to the project.

        '/orgs/:org/projects/:project/envs' POST

        Args:
            name: Name of the environment
            description: Description of the environment
        """
        body = options['body'] if 'body' in options else {}
        body['name'] = name
        body['description'] = description

        response = self.client.post('/orgs/' + self.org + '/projects/' + self.project + '/envs', body, options)

        return response

    def retrieve(self, env, options={}):
        """Get an environment of the project the user has access to.

        '/orgs/:org/projects/:project/envs/:env' GET

        Args:
            env: Name of the environment
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/projects/' + self.project + '/envs/' + env + '', body, options)

        return response

    def update(self, env, description, options={}):
        """Update an environment. Authenticated user should have access to the project.

        '/orgs/:org/projects/:project/envs/:env' PATCH

        Args:
            env: Name of the environment
            description: Description of the environment
        """
        body = options['body'] if 'body' in options else {}
        body['description'] = description

        response = self.client.patch('/orgs/' + self.org + '/projects/' + self.project + '/envs/' + env + '', body, options)

        return response

    def destroy(self, env, options={}):
        """Delete the given environment of the project. Authenticated user should have access to the project. Cannot delete the default environment.

        '/orgs/:org/projects/:project/envs/:env' DELETE

        Args:
            env: Name of the environment
        """
        body = options['body'] if 'body' in options else {}

        response = self.client.delete('/orgs/' + self.org + '/projects/' + self.project + '/envs/' + env + '', body, options)

        return response

