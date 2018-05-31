from twisted.cred import credentials, error
from twisted.internet.defer import succeed, fail
from txweb2.auth.interfaces import ICredentialFactory

from zope.interface import implements


class BearerCredentialFactory(object):
    implements(ICredentialFactory)

    scheme = 'bearer'

    def __init__(self, realm):
        self.realm = realm

    def getChallenge(self, peer):
        """
        @see L{ICredentialFactory.getChallenge}
        """
        return succeed({'realm': self.realm})

    def decode(self, response, request):
        """
        Decode the credentials for basic auth.

        @see L{ICredentialFactory.decode}
        """
        try:
            creds = credentials.UsernamePassword(int(response), None)
        except:
            raise error.LoginFailed('Invalid credentials')

        return succeed(creds)
