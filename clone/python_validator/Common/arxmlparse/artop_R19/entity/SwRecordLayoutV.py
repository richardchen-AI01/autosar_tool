# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwRecordLayoutV.py
from .ARObject import ARObject

class SwRecordLayoutV(ARObject):

    def __init__(self):
        super().__init__()
        from .SwRecordLayoutGroupContent import SwRecordLayoutGroupContent
        from .MultiLanguageOverviewParagraph import MultiLanguageOverviewParagraph
        from .SwBaseType import SwBaseType
        from .SwGenericAxisParamType import SwGenericAxisParamType
        self._artop_shortLabel = None
        self._artop_category = None
        self._artop_swRecordLayoutVAxis = None
        self._artop_swRecordLayoutVProp = None
        self._artop_swRecordLayoutVIndex = None
        self._artop_swRecordLayoutVFixValue = None
        self._artop_swRecordLayoutGroupContent = None
        self._artop_desc = None
        self._artop_baseTypeRef = None
        self._artop_swGenericAxisParamTypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swRecordLayoutGroupContent': '"SW-RECORD-LAYOUT-GROUP-CONTENT"', 
         '_artop_desc': '"MULTI-LANGUAGE-OVERVIEW-PARAGRAPH"', 
         '_artop_baseTypeRef': '"SW-BASE-TYPE"', 
         '_artop_swGenericAxisParamTypeRef': '"SW-GENERIC-AXIS-PARAM-TYPE"'})

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def category_(self):
        return self._artop_category

    @property
    def swRecordLayoutVAxis_(self):
        return self._artop_swRecordLayoutVAxis

    @property
    def swRecordLayoutVProp_(self):
        return self._artop_swRecordLayoutVProp

    @property
    def swRecordLayoutVIndex_(self):
        return self._artop_swRecordLayoutVIndex

    @property
    def swRecordLayoutVFixValue_(self):
        if self._artop_swRecordLayoutVFixValue:
            return int(self._artop_swRecordLayoutVFixValue)
        return self._artop_swRecordLayoutVFixValue

    @property
    def ref_swRecordLayoutGroupContent_(self):
        return self._artop_swRecordLayoutGroupContent

    @property
    def swRecordLayoutGroupContent_(self):
        if self._artop_swRecordLayoutGroupContent is not None:
            if hasattr(self._artop_swRecordLayoutGroupContent, "uuid"):
                return self._artop_swRecordLayoutGroupContent.uuid
        return

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
    def ref_baseType_(self):
        return self._artop_baseTypeRef

    @property
    def baseType_(self):
        if self._artop_baseTypeRef is not None:
            if hasattr(self._artop_baseTypeRef, "uuid"):
                return self._artop_baseTypeRef.uuid
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
