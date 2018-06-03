from twext.who.idirectory import RecordType, FieldName
from twisted.internet.defer import inlineCallbacks, returnValue, succeed
from twistedcaldav.directory.principal import DirectoryCalendarPrincipalResource
from txweb2.dav.resource import DAVPrincipalCollectionResource
from directoryservice import DirectoryService
from directoryrecord import DirectoryRecord

class ExternalPrincipalProvisioningResource(DAVPrincipalCollectionResource):
    """
    Collection resource which provisions principals as its children.
    """

    def __init__(self, url):
        #
        # Create children
        #
        DAVPrincipalCollectionResource.__init__(self, url)
        self.service = DirectoryService()

    def principalForUser(self, user):
        record = DirectoryRecord(self.service, {
          FieldName.uid: unicode(user),
          FieldName.recordType: RecordType.user,
        })

        returnValue(self.principalForRecord(record))

    def principalForRecord(self, record):
        return DirectoryCalendarPrincipalResource(self, record)

    def principalCollections(self):
        return (self,)

