# confy-python

Official Confy API library client for python

__This library is generated by [alpaca](https://github.com/pksunkara/alpaca)__

## Installation

Make sure you have [pip](https://pypi.python.org/pypi/pip) installed

```bash
$ pip install confyio
```

#### Versions

Works with [ 2.6 / 2.7 / 3.2 / 3.3 ]

## Usage

```python
import confy

# Retrieve the config using URL
config = confy.Config.load('https://user:pass@api.confy.io/orgs/company/project/app/envs/production')

# or using options hash
config = confy.Config.load({
  'host': 'https://api.confy.io', 'user': 'user', 'pass': 'pass',
  'org': 'company', 'project': 'app', 'env': 'production'
})

# => { 'port': 6000, 'db': { 'pass': 'sun' } }

config['port'] # => 6000
config['db']['pass'] # => 'sun'

# Or you could instantiate a client to work with other api (as shown below)
```

You can also load the config directly into environment variables by doing as shown below. All the values will be stored in the key formed by concatenizing their keys with underscores.

```python
# Using URL
confy.Config.env("https://user:pass@api.confy.io/orgs/company/project/app/envs/production")

# or using options hash
confy.Config.env({
  'host': 'https://api.confy.io', 'user': 'user', 'pass': 'pass',
  'org': 'company', 'project': 'app', 'env': 'production'
});

# ['port']
os.environ['PORT'] # => 6000

# ['db']['pass']
os.environ['DB_PASS'] # => 'sun'
```

### Build a client

__Using this api without authentication gives an error__

##### Basic authentication

```python
auth = { 'username': 'pksunkara', 'password': 'password' }

client = confy.Client(auth, client_options)
```

### Client Options

The following options are available while instantiating a client:

 * __base__: Base url for the api
 * __api_version__: Default version of the api (to be used in url)
 * __user_agent__: Default user-agent for all requests
 * __headers__: Default headers for all requests
 * __request_type__: Default format of the request body

### Response information

__All the callbacks provided to an api call will recieve the response as shown below__

```python
response = client.klass('args').method('args', method_options)

response.code
# >>> 200

response.headers
# >>> {'x-server': 'apache'}
```

##### JSON response

When the response sent by server is __json__, it is decoded into a dict

```python
response.body
# >>> {'user': 'pksunkara'}
```

### Method Options

The following options are available while calling a method of an api:

 * __api_version__: Version of the api (to be used in url)
 * __headers__: Headers for the request
 * __query__: Query parameters for the url
 * __body__: Body of the request
 * __request_type__: Format of the request body

### Request body information

Set __request_type__ in options to modify the body accordingly

##### RAW request

When the value is set to __raw__, don't modify the body at all.

```python
body = 'username=pksunkara'
# >>> 'username=pksunkara'
```

##### JSON request

When the value is set to __json__, JSON encode the body.

```python
body = {'user': 'pksunkara'}
# >>> '{"user": "pksunkara"}'
```

### Authenticated User api

User who is authenticated currently.

```python
user = client.user()
```

##### Retrieve authenticated user (GET /user)

Get the authenticated user's profile.

```python
response = user.retrieve(options)
```

##### Update authenticated user (PATCH /user)

Update the authenticated user's profile

The following arguments are required:

 * __email__: Profile email of the user

```python
response = user.update("john@smith.com", options)
```

### Organizations api

Organizations are owned by users and only (s)he can add/remove teams and projects for that organization. A default organization will be created for every user.

```python
orgs = client.orgs()
```

##### List Organizations (GET /orgs)

List all organizations the authenticated user is a member of.

```python
response = orgs.list(options)
```

##### Create an organization (POST /orgs)

Create an organization with a name and the email for billing.

The following arguments are required:

 * __name__: Name of the organization
 * __email__: Billing email of the organization

```python
response = orgs.create("OpenSourceProject", "admin@osp.com", options)
```

##### Retrieve an organization (GET /orgs/:org)

Get an organization the user has access to.

The following arguments are required:

 * __org__: Name of the organization

```python
response = orgs.retrieve("bigcompany", options)
```

##### Update an organization (PATCH /orgs/:org)

Update an organization the user is owner of.

The following arguments are required:

 * __org__: Name of the organization
 * __email__: Billing email of the organization

```python
response = orgs.update("bigcompany", "admin@bigcompany.com", options)
```

### Teams api

Every organization will have a default team named Owners. Owner of the organization will be a default member for every team.

The following arguments are required:

 * __org__: Name of the organization

```python
teams = client.teams("bigcompany")
```

##### List Teams (GET /orgs/:org/teams)

List teams of the given organization authenticated user is a member of.

```python
response = teams.list(options)
```

##### Create a team (POST /orgs/:org/teams)

Create a team for the given organization. Authenticated user should be the owner of the organization.

The following arguments are required:

 * __name__: Name of the team
 * __description__: Description of the team

```python
response = teams.create("Consultants", "Guys who are contractors", options)
```

##### Retrieve a team (GET /orgs/:org/teams/:team)

Get a team the user is member of.

The following arguments are required:

 * __team__: Name of the team

```python
response = teams.retrieve("consultants", options)
```

##### Update a team (PATCH /orgs/:org/teams/:team)

Update a team. Authenticated user should be the owner of the organization.

The following arguments are required:

 * __team__: Name of the team
 * __description__: Description of the team

```python
response = teams.update("consultants", "Guys who are contractors", options)
```

##### Delete a team (DELETE /orgs/:org/teams/:team)

Delete the given team. Cannot delete the default team in the organization. Authenticated user should be the owner of the organization.

The following arguments are required:

 * __team__: Name of the team

```python
response = teams.destroy("consultants", options)
```

### Members api

Teams contain a list of users. The Authenticated user should be the owner of the organization.

The following arguments are required:

 * __org__: Name of the organization
 * __team__: Name of the team

```python
members = client.members("bigcompany", "consultants")
```

##### Add a member (POST /orgs/:org/teams/:team/member)

Add the user to the given team. The __user__ in the request needs to be a string.

The following arguments are required:

 * __user__: Username of the user

```python
response = members.add("johnsmith", options)
```

##### Remove a member (DELETE /orgs/:org/teams/:team/member)

Remove users from the given team. The __user__ in the request needs to be a string. Cannot delete the default member in a team.

The following arguments are required:

 * __user__: Username of the user

```python
response = members.remove("johnsmith", options)
```

### Projects api

An organization can contain any number of projects.

The following arguments are required:

 * __org__: Name of the organization

```python
projects = client.projects("bigcompany")
```

##### List projects (GET /orgs/:org/projects)

List all the projects of the organization which can be seen by the authenticated user.

```python
response = projects.list(options)
```

##### Create a project (POST /orgs/:org/projects)

Create a project for the given organization. Authenticated user should be the owner of the organization.

The following arguments are required:

 * __name__: Name of the project
 * __description__: Description of the project

```python
response = projects.create("KnowledgeBase", "Support FAQ & Wiki", options)
```

##### Retrieve a project (GET /orgs/:org/projects/:project)

Get a project the user has access to.

The following arguments are required:

 * __project__: Name of the project

```python
response = projects.retrieve("knowledgebase", options)
```

##### Update a project (PATCH /orgs/:org/projects/:project)

Update a project. Authenticated user should be the owner of the organization.

The following arguments are required:

 * __project__: Name of the project
 * __description__: Description of the project

```python
response = projects.update("knowledgebase", "Support FAQ and Wiki", options)
```

##### Delete a project (DELETE /orgs/:org/projects/:project)

Delete the given project. Cannot delete the default project in the organization. Authenticated user should be the owner of the organization.

The following arguments are required:

 * __project__: Name of the project

```python
response = projects.destroy("knowledgebase", options)
```

### Access api

List of teams who has access to the project. Default team __Owners__ will have access to every project. Authenticated user should be the owner of the organization for the below endpoints.

The following arguments are required:

 * __org__: Name of the organization
 * __project__: Name of the project

```python
access = client.access("bigcompany", "knowledgebase")
```

##### Add a team (POST /orgs/:org/projects/:project/access)

Give the team access to the given project. The __team__ in the request needs to be a string.

The following arguments are required:

 * __team__: Name of the team

```python
response = access.add("consultants", options)
```

##### Remove a team (DELETE /orgs/:org/projects/:project/access)

Remove project access for the given team. The __team__ in the request needs to be a string. Can't delete default team's access.

The following arguments are required:

 * __team__: Name of the team

```python
response = access.remove("consultants", options)
```

### Environments api

Every project has a default environment named Production. Each environment has one configuration document which can have many keys and values.

The following arguments are required:

 * __org__: Name of the organization
 * __project__: Name of the project

```python
envs = client.envs("bigcompany", "knowledgebase")
```

##### List all environments (GET /orgs/:org/projects/:project/envs)

List all the environmens of the project which can be seen by the authenticated user.

```python
response = envs.list(options)
```

##### Create an environment (POST /orgs/:org/projects/:project/envs)

Create an environment for the given project. Authenticated user should have access to the project.

The following arguments are required:

 * __name__: Name of the environment
 * __description__: Description of the environment

```python
response = envs.create("QA", "Quality assurance guys server", options)
```

##### Retrieve an environment (GET /orgs/:org/projects/:project/envs/:env)

Get an environment of the project the user has access to.

The following arguments are required:

 * __env__: Name of the environment

```python
response = envs.retrieve("qa", options)
```

##### Update an environment (PATCH /orgs/:org/projects/:project/envs/:env)

Update an environment. Authenticated user should have access to the project.

The following arguments are required:

 * __env__: Name of the environment
 * __description__: Description of the environment

```python
response = envs.update("qa", "Testing server for QA guys", options)
```

##### Delete an environment (DELETE /orgs/:org/projects/:project/envs/:env)

Delete the given environment of the project. Authenticated user should have access to the project. Cannot delete the default environment.

The following arguments are required:

 * __env__: Name of the environment

```python
response = envs.destroy("knowledgebase", options)
```

### configuration api

Any member of the team which has access to the project can retrieve any of it's environment's configuration document or edit it.

The following arguments are required:

 * __org__: Name of the organization
 * __project__: Name of the project
 * __env__: Name of the environment

```python
config = client.config("bigcompany", "knowledgebase", "production")
```

##### Retrieve an config (GET /orgs/:org/projects/:project/envs/:env/config)

Get an environment config of the project.

```python
response = config.retrieve(options)
```

##### Update the configuration (POST /orgs/:org/projects/:project/envs/:env/config)

Update the configuration document for the given environment of the project. We will patch the document recursively.

The following arguments are required:

 * __config__: Configuration to update

```python
response = config.update({
    'database': {
        'port': 6984
    },
    'random': "wow"
}, options)
```

## Contributors
Here is a list of [Contributors](https://github.com/asm-products/confy-python/contributors)

### TODO

## License
BSD

## Bug Reports
Report [here](https://github.com/asm-products/confy-python/issues).

## Contact
Pavan Kumar Sunkara (pavan.sss1991@gmail.com)
