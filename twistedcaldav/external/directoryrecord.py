from twext.who.directory import DirectoryRecord as BaseDirectoryRecord
from twisted.internet.defer import inlineCallbacks, returnValue, succeed


class DirectoryRecord(BaseDirectoryRecord):
    def __init__(self, service, fields):
        super(DirectoryRecord, self).__init__(service, fields)

        self.shortNames = ['user-' + self.uid]

    def isLoginEnabled(self):
        return True

    def verifyCredentials(self, credentials):
        yield True
