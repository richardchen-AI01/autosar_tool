# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DocRevision.py
from .ARObject import ARObject

class DocRevision(ARObject):

    def __init__(self):
        super().__init__()
        from .AdminData import AdminData
        from .Modification import Modification
        self._artop_revisionLabel = None
        self._artop_revisionLabelP1 = None
        self._artop_revisionLabelP2 = None
        self._artop_state = None
        self._artop_issuedBy = None
        self._artop_date = None
        self._artop_adminData = None
        self._artop_modification = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_adminData':"ADMIN-DATA", 
         '_artop_modification':"MODIFICATION"})

    @property
    def revisionLabel_(self):
        return self._artop_revisionLabel

    @property
    def revisionLabelP1_(self):
        return self._artop_revisionLabelP1

    @property
    def revisionLabelP2_(self):
        return self._artop_revisionLabelP2

    @property
    def state_(self):
        return self._artop_state

    @property
    def issuedBy_(self):
        return self._artop_issuedBy

    @property
    def date_(self):
        return self._artop_date

    @property
    def ref_adminData_(self):
        return self._artop_adminData

    @property
    def adminData_(self):
        if self._artop_adminData is not None:
            if hasattr(self._artop_adminData, "uuid"):
                return self._artop_adminData.uuid
        return

    @property
    def modifications_Modification(self):
        return self._artop_modification
