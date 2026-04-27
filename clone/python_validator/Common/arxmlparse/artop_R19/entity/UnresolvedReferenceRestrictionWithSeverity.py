# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UnresolvedReferenceRestrictionWithSeverity.py
from .RestrictionWithSeverity import RestrictionWithSeverity

class UnresolvedReferenceRestrictionWithSeverity(RestrictionWithSeverity):

    def __init__(self):
        super().__init__()
        from .ReferenceTailoring import ReferenceTailoring
        self._artop_referenceTailoring = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_referenceTailoring": "REFERENCE-TAILORING"})

    @property
    def ref_referenceTailoring_(self):
        return self._artop_referenceTailoring

    @property
    def referenceTailoring_(self):
        if self._artop_referenceTailoring is not None:
            if hasattr(self._artop_referenceTailoring, "uuid"):
                return self._artop_referenceTailoring.uuid
        return
