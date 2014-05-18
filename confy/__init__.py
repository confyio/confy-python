import os, re

from .client import Client

class Config(object):

    @classmethod
    def load(cls, url={}):
        if type(url) is str:
            regex = re.compile('(https?:\/\/)(.*):(.*)@(.*)\/orgs\/([a-z0-9]*)\/projects\/([a-z0-9]*)\/envs\/([a-z0-9]*)\/config', re.I)
            matches = regex.match(url)

            if matches is None:
                raise Exception('Invalid url')

            url = {
                'host': matches.group(1) + matches.group(4), 'user': matches.group(2), 'pass': matches.group(3),
                'org': matches.group(5), 'project': matches.group(6), 'env': matches.group(7)
            }

        client = Client({
            'username': url['user'], 'password': url['pass']
        }, { 'base': url['host'] })

        return client.config(url['org'], url['project'], url['env']).retrieve().body

    @classmethod
    def env(cls, url={}):
        cls.path(cls.load(url))

    @classmethod
    def path(cls, config, string=''):
        typ = type(config)

        if typ is list:
            for (key, value) in enumerate(config):
                cls.path(value, string + '_' + key)
        elif typ is dict:
            for (key, value) in config.items():
                cls.path(value, string + '_' + key.upper())
        elif typ is bool:
            if typ:
                os.environ[string[1:]] = '1'
            else:
                os.environ[string[1:]] = '0'
        elif typ is not NoneType:
            os.environ[string[1:]] = str(config)
