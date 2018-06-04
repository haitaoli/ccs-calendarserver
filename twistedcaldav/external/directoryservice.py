from twext.who.idirectory import RecordType, FieldName
from twext.who.directory import DirectoryRecord, DirectoryService as BaseDirectoryService
from twext.who.util import ConstantsContainer
from twisted.internet.defer import inlineCallbacks, returnValue, succeed
from directoryrecord import DirectoryRecord


"""
External directory service implementation.
"""


class DirectoryService(BaseDirectoryService):
    recordType = ConstantsContainer(
        (BaseDirectoryService.recordType, RecordType)
    )

    def __init__(self):
        BaseDirectoryService.__init__(self, realmName="no realm")

    def recordWithUID(self, uid, timeoutSeconds=None):
        return DirectoryRecord(self, uid)

    def recordWithShortName(self, recordType, shortName, timeoutSeconds=None):
        return DirectoryRecord(self, shortName)

