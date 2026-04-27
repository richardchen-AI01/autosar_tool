# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswEntryRelationship.py
from .ARObject import ARObject

class BswEntryRelationship(ARObject):

    def __init__(self):
        super().__init__()
        from .BswEntryRelationshipSet import BswEntryRelationshipSet
        from .BswModuleEntry import BswModuleEntry
        self._artop_bswEntryRelationshipType = None
        self._artop_bswEntryRelationshipSet = None
        self._artop_fromRef = None
        self._artop_toRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_bswEntryRelationshipSet':"BSW-ENTRY-RELATIONSHIP-SET", 
         '_artop_fromRef':"BSW-MODULE-ENTRY", 
         '_artop_toRef':"BSW-MODULE-ENTRY"})

    @property
    def bswEntryRelationshipType_(self):
        return self._artop_bswEntryRelationshipType

    @property
    def ref_bswEntryRelationshipSet_(self):
        return self._artop_bswEntryRelationshipSet

    @property
    def bswEntryRelationshipSet_(self):
        if self._artop_bswEntryRelationshipSet is not None:
            if hasattr(self._artop_bswEntryRelationshipSet, "uuid"):
                return self._artop_bswEntryRelationshipSet.uuid
        return

    @property
    def ref_from_(self):
        return self._artop_fromRef

    @property
    def from_(self):
        if self._artop_fromRef is not None:
            if hasattr(self._artop_fromRef, "uuid"):
                return self._artop_fromRef.uuid
        return

    @property
    def ref_to_(self):
        return self._artop_toRef

    @property
    def to_(self):
        if self._artop_toRef is not None:
            if hasattr(self._artop_toRef, "uuid"):
                return self._artop_toRef.uuid
        return
