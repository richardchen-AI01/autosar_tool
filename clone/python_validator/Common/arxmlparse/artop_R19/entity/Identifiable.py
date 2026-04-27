# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Identifiable.py
from .MultilanguageReferrable import MultilanguageReferrable

class Identifiable(MultilanguageReferrable):

    def __init__(self):
        super().__init__()
        from .MultiLanguageOverviewParagraph import MultiLanguageOverviewParagraph
        from .AdminData import AdminData
        from .DocumentationBlock import DocumentationBlock
        from .Annotation import Annotation
        from .IdentifiableAllExtensionsMapEntry import IdentifiableAllExtensionsMapEntry
        self._artop_category = None
        self.uuid = None
        self._artop_desc = None
        self._artop_adminData = None
        self._artop_introduction = None
        self._artop_annotation = []
        self._artop_allextensions = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_desc': '"MULTI-LANGUAGE-OVERVIEW-PARAGRAPH"', 
         '_artop_adminData': '"ADMIN-DATA"', 
         '_artop_introduction': '"DOCUMENTATION-BLOCK"', 
         '_artop_annotation': '"ANNOTATION"'})

    @property
    def category_(self):
        return self._artop_category

    @property
    def uuid_(self):
        return self.uuid

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
    def ref_adminData_(self):
        return self._artop_adminData

    @property
    def adminData_(self):
        if self._artop_adminData is not None:
            if hasattr(self._artop_adminData, "uuid"):
                return self._artop_adminData.uuid
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
    def annotations_Annotation(self):
        return self._artop_annotation

    @property
    def allExtensions_IdentifiableAllExtensionsMapEntry(self):
        return self._artop_allextensions
