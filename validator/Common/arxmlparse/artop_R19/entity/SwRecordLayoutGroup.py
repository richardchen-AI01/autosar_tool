# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwRecordLayoutGroup.py
from .ARObject import ARObject

class SwRecordLayoutGroup(ARObject):

    def __init__(self):
        super().__init__()
        from .MultiLanguageOverviewParagraph import MultiLanguageOverviewParagraph
        from .SwGenericAxisParamType import SwGenericAxisParamType
        from .SwRecordLayoutGroupContent import SwRecordLayoutGroupContent
        self._artop_shortLabel = None
        self._artop_category = None
        self._artop_swRecordLayoutGroupAxis = None
        self._artop_swRecordLayoutGroupIndex = None
        self._artop_swRecordLayoutGroupFrom = None
        self._artop_swRecordLayoutGroupTo = None
        self._artop_swRecordLayoutGroupStep = None
        self._artop_swRecordLayoutComponent = None
        self._artop_desc = None
        self._artop_swGenericAxisParamTypeRef = None
        self._artop_swRecordLayoutGroupContentType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_desc':"MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", 
         '_artop_swGenericAxisParamTypeRef':"SW-GENERIC-AXIS-PARAM-TYPE", 
         '_artop_swRecordLayoutGroupContentType':"SW-RECORD-LAYOUT-GROUP-CONTENT"})

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def category_(self):
        return self._artop_category

    @property
    def swRecordLayoutGroupAxis_(self):
        return self._artop_swRecordLayoutGroupAxis

    @property
    def swRecordLayoutGroupIndex_(self):
        return self._artop_swRecordLayoutGroupIndex

    @property
    def swRecordLayoutGroupFrom_(self):
        return self._artop_swRecordLayoutGroupFrom

    @property
    def swRecordLayoutGroupTo_(self):
        return self._artop_swRecordLayoutGroupTo

    @property
    def swRecordLayoutGroupStep_(self):
        if self._artop_swRecordLayoutGroupStep:
            return int(self._artop_swRecordLayoutGroupStep)
        return self._artop_swRecordLayoutGroupStep

    @property
    def swRecordLayoutComponent_(self):
        return self._artop_swRecordLayoutComponent

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
    def ref_swGenericAxisParamType_(self):
        return self._artop_swGenericAxisParamTypeRef

    @property
    def swGenericAxisParamType_(self):
        if self._artop_swGenericAxisParamTypeRef is not None:
            if hasattr(self._artop_swGenericAxisParamTypeRef, "uuid"):
                return self._artop_swGenericAxisParamTypeRef.uuid
        return

    @property
    def ref_swRecordLayoutGroupContentType_(self):
        return self._artop_swRecordLayoutGroupContentType

    @property
    def swRecordLayoutGroupContentType_(self):
        if self._artop_swRecordLayoutGroupContentType is not None:
            if hasattr(self._artop_swRecordLayoutGroupContentType, "uuid"):
                return self._artop_swRecordLayoutGroupContentType.uuid
        return
