# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwTextProps.py
from .ARObject import ARObject

class SwTextProps(ARObject):

    def __init__(self):
        super().__init__()
        from .SwDataDefPropsContent import SwDataDefPropsContent
        from .IntegerValueVariationPoint import IntegerValueVariationPoint
        from .SwBaseType import SwBaseType
        self._artop_arraySizeSemantics = None
        self._artop_swFillCharacter = None
        self._artop_swDataDefPropsContent = None
        self._artop_swMaxTextSize = None
        self._artop_baseTypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swDataDefPropsContent':"SW-DATA-DEF-PROPS-CONTENT", 
         '_artop_swMaxTextSize':"INTEGER-VALUE-VARIATION-POINT", 
         '_artop_baseTypeRef':"SW-BASE-TYPE"})

    @property
    def arraySizeSemantics_(self):
        return self._artop_arraySizeSemantics

    @property
    def swFillCharacter_(self):
        if self._artop_swFillCharacter:
            return int(self._artop_swFillCharacter)
        return self._artop_swFillCharacter

    @property
    def ref_swDataDefPropsContent_(self):
        return self._artop_swDataDefPropsContent

    @property
    def swDataDefPropsContent_(self):
        if self._artop_swDataDefPropsContent is not None:
            if hasattr(self._artop_swDataDefPropsContent, "uuid"):
                return self._artop_swDataDefPropsContent.uuid
        return

    @property
    def ref_swMaxTextSize_(self):
        return self._artop_swMaxTextSize

    @property
    def swMaxTextSize_(self):
        if self._artop_swMaxTextSize is not None:
            if hasattr(self._artop_swMaxTextSize, "uuid"):
                return self._artop_swMaxTextSize.uuid
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
