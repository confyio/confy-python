import os, re, base64, binascii, hashlib, json
from Crypto.Cipher import AES

from .client import Client

class Config(object):

    @classmethod
    def match(clas, url):
        if type(url) is str:
            name_regex = '([a-z0-9][a-z0-9-]*[a-z0-9])'
            token_regex = '([a-f0-9]{40})'
            path_regex = 'orgs\\/' + name_regex + '(\\/projects\\/' + name_regex + '\\/envs\\/' + name_regex + '\\/config|\\/config\\/' + token_regex + ')'
            url_regex = re.compile('(https?:\\/\\/)((.*):(.*)@)?(.*)\\/(' + path_regex + '|heroku\\/config)', re.I)

            matches = url_regex.match(url)

            if matches is None:
                raise Exception('Invalid URL')

            url = {
                'host': matches.group(1) + matches.group(5),
                'user': matches.group(3), 'pass': matches.group(4),
                'org': matches.group(7), 'project': matches.group(9), 'env': matches.group(10),
                'token': matches.group(11),
                'heroku': (matches.group(6) == 'heroku/config')
            }

        if type(url) is not dict:
            raise Exception('Invalid URL')

        def exists(key):
            return key in url and url[key]

        if exists('host') and exists('user') and exists('pass') and exists('heroku'):
            url['path'] = '/heroku/config'
        elif exists('host') and exists('token') and exists('org'):
            url['path'] = '/orgs/' + url['org'] + '/config/' + url['token']
        elif exists('host') and exists('user') and exists('pass') and exists('org') and exists('project') and exists('env'):
            url['path'] = '/orgs/' + url['org'] + '/projects/' + url['project'] + '/envs/' + url['env'] + '/config'
        else:
            raise Exception('Invalid URL')

        return url

    @classmethod
    def load(cls, url={}):
        url = cls.match(url)

        auth = {}

        if url['user'] and url['pass']:
            auth['username'] = url['user']
            auth['password'] = url['pass']

        client = Client(auth, { 'base': url['host'] })

        body = client.http_client.get(url['path']).body

        if type(body) is dict:
            return body

        decryptPass = os.getenv('CONFY_DECRYPT_PASS')

        if type(body) is not str and type(body) is not unicode:
            raise Exception('Invalid credential document')

        if decryptPass is None:
            raise Exception('No decryption password found. Fill env var CONFY_DECRYPT_PASS')

        try:
            iv = base64.b64decode(body[:24])
        except TypeError:
            iv = base64.b64decode(bytes(body[:24], 'ascii'))

        key = hashlib.md5(decryptPass.encode('utf-8')).hexdigest()
        cipher = AES.new(key, AES.MODE_CBC, iv)

        try:
            decrypted = cipher.decrypt(base64.b64decode(body[24:]))
        except TypeError:
            decrypted = cipher.decrypt(base64.b64decode(bytes(body[24:], 'ascii')))

        try:
            padding_size = int(binascii.hexlify(decrypted[-1]), 16)
        except TypeError:
            padding_size = decrypted[-1]

        decrypted = decrypted[:(len(decrypted) - padding_size)]

        if type(decrypted) is not str:
            decrypted = str(decrypted, 'utf-8')

        try:
            body = json.loads(decrypted)
        except ValueError:
            raise Exception('Decryption password is wrong')

        return body

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
