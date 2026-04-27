# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Describable.py
from .ARObject import ARObject

class Describable(ARObject):

    def __init__(self):
        super().__init__()
        from .MultiLanguageOverviewParagraph import MultiLanguageOverviewParagraph
        from .DocumentationBlock import DocumentationBlock
        from .AdminData import AdminData
        self._artop_category = None
        self._artop_desc = None
        self._artop_introduction = None
        self._artop_adminData = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_desc':"MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", 
         '_artop_introduction':"DOCUMENTATION-BLOCK", 
         '_artop_adminData':"ADMIN-DATA"})

    @property
    def category_(self):
        return self._artop_category

    @property
    def ref_desc_(self):
        return self._artop_desc

    @property
    def desc_(self):
        if self._artop_desc is not None:
            if hasattr(self._artop_desc, "uuid"):
                return self._artop_desc.uuid
        return

    @property
    def ref_introduction_(self):
        return self._artop_introduction

    @property
    def introduction_(self):
        if self._artop_introduction is not None:
            if hasattr(self._artop_introduction, "uuid"):
                return self._artop_introduction.uuid
        return

    @property
    def ref_adminData_(self):
        return self._artop_adminData

    @property
    def adminData_(self):
        if self._artop_adminData is not None:
            if hasattr(self._artop_adminData, "uuid"):
                return self._artop_adminData.uuid
        return
