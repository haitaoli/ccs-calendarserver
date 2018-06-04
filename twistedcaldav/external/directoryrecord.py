from twext.who.directory import DirectoryRecord as BaseDirectoryRecord
from twext.who.idirectory import FieldName, RecordType
from txdav.who.idirectory import FieldName as BaseFieldName
from twisted.internet.defer import inlineCallbacks, returnValue, succeed

from uuid import UUID


class DirectoryRecord(BaseDirectoryRecord):
    def __init__(self, service, uid):

        super(DirectoryRecord, self).__init__(service, {
            FieldName.recordType: RecordType.user,
            FieldName.uid: uid,
            FieldName.shortNames: [uid],
            # FieldName.fullNames: [u'userFullName'],
            BaseFieldName.hasCalendars: True,
            BaseFieldName.hasContacts: False,
            BaseFieldName.loginAllowed: True,
        })

    def verifyCredentials(self, credentials):
        yield True

    def verifyPlaintextPassword(self, password):
        return succeed(True)
