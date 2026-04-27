# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ReferenceTailoring.py
from .AttributeTailoring import AttributeTailoring

class ReferenceTailoring(AttributeTailoring):

    def __init__(self):
        super().__init__()
        from .ClassTailoring import ClassTailoring
        from .UnresolvedReferenceRestrictionWithSeverity import UnresolvedReferenceRestrictionWithSeverity
        self._artop_typeTailoring = []
        self._artop_unresolvedReferenceRestriction = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_typeTailoring':"CLASS-TAILORING", 
         '_artop_unresolvedReferenceRestriction':"UNRESOLVED-REFERENCE-RESTRICTION-WITH-SEVERITY"})

    @property
    def typeTailorings_ClassTailoring(self):
        return self._artop_typeTailoring

    @property
    def ref_unresolvedReferenceRestriction_(self):
        return self._artop_unresolvedReferenceRestriction

    @property
    def unresolvedReferenceRestriction_(self):
        if self._artop_unresolvedReferenceRestriction is not None:
            if hasattr(self._artop_unresolvedReferenceRestriction, "uuid"):
                return self._artop_unresolvedReferenceRestriction.uuid
        return
