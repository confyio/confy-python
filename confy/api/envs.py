class Envs(object):

    """Every project has a default environment named Production. Each environment has __one__ configuration document which can have many keys and values.

    Args:
        org: Name of the organization
        project: Name of the project
    """

    def __init__(self, org, project, client):
        self.org = org
        self.project = project
        self.client = client

    def list(self, options={}):
        """List all the environmens of the project. The authenticated user should have access to the project.

        '/orgs/:org/projects/:project/envs' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/projects/' + self.project + '/envs', body, options)

        return response

    def create(self, name, description, options={}):
        """Create an environment. The authenticated user should have access to the project.

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
        """Get the given environment in the given project. The authenticated user should have access to the project.

        '/orgs/:org/projects/:project/envs/:env' GET

        Args:
            env: Name of the environment
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/projects/' + self.project + '/envs/' + env + '', body, options)

        return response

    def update(self, env, description, options={}):
        """Update the given environment. __Description__ is the only thing which can be updated. Authenticated user should have access to the project.

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
        """Delete the given environment. Authenticated user should have access to the project. Cannot delete the default environment.

        '/orgs/:org/projects/:project/envs/:env' DELETE

        Args:
            env: Name of the environment
        """
        body = options['body'] if 'body' in options else {}

        response = self.client.delete('/orgs/' + self.org + '/projects/' + self.project + '/envs/' + env + '', body, options)

        return response

