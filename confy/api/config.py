class Config(object):

    """Any member of the team which has access to the project can retrieve any of it's environment's configuration document or edit it.

    Args:
        org: Name of the organization
        project: Name of the project
        env: Name of the environment
    """

    def __init__(self, org, project, env, client):
        self.org = org
        self.project = project
        self.env = env
        self.client = client

    def retrieve(self, options={}):
        """Get an environment config of the project.

        '/orgs/:org/projects/:project/envs/:env/config' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/orgs/' + self.org + '/projects/' + self.project + '/envs/' + self.env + '/config', body, options)

        return response

    def update(self, body, options={}):
        """Update the configuration document for the given environment of the project. We will patch the document recursively.

        '/orgs/:org/projects/:project/envs/:env/config' POST

        Args:
            body: Configuration to update
        """
        response = self.client.post('/orgs/' + self.org + '/projects/' + self.project + '/envs/' + self.env + '/config', body, options)

        return response

