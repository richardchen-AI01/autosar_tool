# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Modification.py
from .ARObject import ARObject

class Modification(ARObject):

    def __init__(self):
        super().__init__()
        from .DocRevision import DocRevision
        from .MultiLanguageOverviewParagraph import MultiLanguageOverviewParagraph
        self._artop_docRevision = None
        self._artop_change = None
        self._artop_reason = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_docRevision':"DOC-REVISION", 
         '_artop_change':"MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", 
         '_artop_reason':"MULTI-LANGUAGE-OVERVIEW-PARAGRAPH"})

    @property
    def ref_docRevision_(self):
        return self._artop_docRevision

    @property
    def docRevision_(self):
        if self._artop_docRevision is not None:
            if hasattr(self._artop_docRevision, "uuid"):
                return self._artop_docRevision.uuid
        return

    @property
    def ref_change_(self):
        return self._artop_change

    @property
    def change_(self):
        if self._artop_change is not None:
            if hasattr(self._artop_change, "uuid"):
                return self._artop_change.uuid
        return

    @property
    def ref_reason_(self):
        return self._artop_reason

    @property
    def reason_(self):
        if self._artop_reason is not None:
            if hasattr(self._artop_reason, "uuid"):
                return self._artop_reason.uuid
        return
