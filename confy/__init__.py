import os, re, base64, binascii, hashlib, json
from Crypto.Cipher import AES

from .client import Client

class Config(object):

    @classmethod
    def load(cls, url={}):
        if type(url) is str:
            name_regex = '([a-z0-9][a-z0-9-]*[a-z0-9])'
            path_regex = 'orgs\\/' + name_regex + '\\/projects\\/' + name_regex + '\\/envs\\/' + name_regex
            url_regex = re.compile('(https?:\\/\\/)(.*):(.*)@(.*)\\/(' + path_regex + '|heroku)\\/config', re.I)

            matches = url_regex.match(url)

            if matches is None:
                raise Exception('Invalid url')

            url = {
                'host': matches.group(1) + matches.group(4), 'path': '/' + matches.group(5) + '/config',
                'user': matches.group(2), 'pass': matches.group(3)
            }

        if type(url) is not dict:
            raise Exception('Invalid url')

        client = Client({
            'username': url['user'], 'password': url['pass']
        }, { 'base': url['host'] })

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
