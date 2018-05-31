from twext.who.idirectory import RecordType, FieldName
from twext.who.directory import DirectoryRecord, DirectoryService as BaseDirectoryService
from twext.who.util import ConstantsContainer


"""
External directory service implementation.
"""

__all__ = [
    "DirectoryService",
]

##
# Directory Service
##

class DirectoryService(BaseDirectoryService):
    recordType = ConstantsContainer(
        (BaseDirectoryService.recordType, RecordType)
    )

    def __init__(self):
        BaseDirectoryService.__init__(self, realmName="no realm")


