import confy
from expects import *

with describe('Testing match function'):

    with context('with full url'):
        with before.all:
            url = 'https://user:pass@api.confy.io/orgs/org/projects/project/envs/env/config'
            self.result = confy.Config.match(url)

        with it('should return url object'):
            expect(self.result).to(be_a(object))
            expect(self.result['host']).to(equal('https://api.confy.io'))

        with it('should have auth info'):
            expect(self.result['user']).to(equal('user'))
            expect(self.result['pass']).to(equal('pass'))

        with it('should have org info'):
            expect(self.result['org']).to(equal('org'))

        with it('should have stage info'):
            expect(self.result['project']).to(equal('project'))
            expect(self.result['env']).to(equal('env'))

        with it('should not have heroku'):
            expect(self.result['heroku']).to(be_false)

        with it('should not have token'):
            expect(self.result['token']).to(be_none)

        with it('should have correct path'):
            expect(self.result['path']).to(equal('/orgs/org/projects/project/envs/env/config'))

    with context('with token url'):
        with before.all:
            url = 'https://api.confy.io/orgs/org/config/abcdefabcdefabcdefabcdefabcdef1234567890'
            self.result = confy.Config.match(url)

        with it('should return url object'):
            expect(self.result).to(be_a(object))
            expect(self.result['host']).to(equal('https://api.confy.io'))

        with it('should not have auth info'):
            expect(self.result['user']).to(be_none)
            expect(self.result['pass']).to(be_none)

        with it('should have org info'):
            expect(self.result['org']).to(equal('org'))

        with it('should not have stage info'):
            expect(self.result['project']).to(be_none)
            expect(self.result['env']).to(be_none)

        with it('should not have heroku'):
            expect(self.result['heroku']).to(be_false)

        with it('should have token'):
            expect(self.result['token']).to(equal('abcdefabcdefabcdefabcdefabcdef1234567890'))

        with it('should have correct path'):
            expect(self.result['path']).to(equal('/orgs/org/config/abcdefabcdefabcdefabcdefabcdef1234567890'))

    with context('with heroku url'):
        with before.all:
            url = 'https://user:pass@api.confy.io/heroku/config'
            self.result = confy.Config.match(url)

        with it('should return url object'):
            expect(self.result).to(be_a(object))
            expect(self.result['host']).to(equal('https://api.confy.io'))

        with it('should have auth info'):
            expect(self.result['user']).to(equal('user'))
            expect(self.result['pass']).to(equal('pass'))

        with it('should not have org info'):
            expect(self.result['org']).to(be_none)

        with it('should not have stage info'):
            expect(self.result['project']).to(be_none)
            expect(self.result['env']).to(be_none)

        with it('should have heroku'):
            expect(self.result['heroku']).to(be_true)

        with it('should not have token'):
            expect(self.result['token']).to(be_none)

        with it('should have correct path'):
            expect(self.result['path']).to(equal('/heroku/config'))

    with context('with non-string and non-object url'):
        with it('should raise error'):
            def callback():
                confy.Config.match(8)

            expect(callback).to(raise_error(Exception, 'Invalid URL'))

    with context('with bad url'):
        with it('should raise error'):
            def callback():
                confy.Config.match('http://api.confy.io/projects/config')

            expect(callback).to(raise_error(Exception, 'Invalid URL'))

    with context('with empty object'):
        with it('should raise error'):
            def callback():
                confy.Config.match({ 'user': 'user', 'pass': 'pass', 'heroku': True })

            expect(callback).to(raise_error(Exception, 'Invalid URL'))
