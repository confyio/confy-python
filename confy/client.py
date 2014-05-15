from .http_client import HttpClient

# Assign all the api classes
from .api.user import User
from .api.orgs import Orgs
from .api.teams import Teams
from .api.members import Members
from .api.projects import Projects
from .api.access import Access
from .api.envs import Envs
from .api.config import Config


class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def user(self):
        """User who is authenticated currently.
        """
        return User(self.http_client)

    def orgs(self):
        """Organizations are owned by users and only (s)he can add/remove teams and projects for that organization. A default organization will be created for every user.
        """
        return Orgs(self.http_client)

    def teams(self, org):
        """Every organization will have a default team named Owners. Owner of the organization will be a default member for every team.

        Args:
            org: Name of the organization
        """
        return Teams(org, self.http_client)

    def members(self, org, team):
        """Teams contain a list of users. The Authenticated user should be the owner of the organization.

        Args:
            org: Name of the organization
            team: Name of the team
        """
        return Members(org, team, self.http_client)

    def projects(self, org):
        """An organization can contain any number of projects.

        Args:
            org: Name of the organization
        """
        return Projects(org, self.http_client)

    def access(self, org, project):
        """List of teams who has access to the project. Default team __Owners__ will have access to every project. Authenticated user should be the owner of the organization for the below endpoints.

        Args:
            org: Name of the organization
            project: Name of the project
        """
        return Access(org, project, self.http_client)

    def envs(self, org, project):
        """Every project has a default environment named Production. Each environment has one configuration document which can have many keys and values.

        Args:
            org: Name of the organization
            project: Name of the project
        """
        return Envs(org, project, self.http_client)

    def config(self, org, project, env):
        """Any member of the team which has access to the project can retrieve any of it's environment's configuration document or edit it.

        Args:
            org: Name of the organization
            project: Name of the project
            env: Name of the environment
        """
        return Config(org, project, env, self.http_client)

