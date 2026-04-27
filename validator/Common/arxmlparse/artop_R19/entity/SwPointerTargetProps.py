# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwPointerTargetProps.py
from .ARObject import ARObject

class SwPointerTargetProps(ARObject):

    def __init__(self):
        super().__init__()
        from .SwDataDefPropsContent import SwDataDefPropsContent
        from .SwDataDefProps import SwDataDefProps
        from .BswModuleEntry import BswModuleEntry
        self._artop_targetCategory = None
        self._artop_swDataDefPropsContent = None
        self._artop_swDataDefProps = None
        self._artop_functionPointerSignatureRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swDataDefPropsContent':"SW-DATA-DEF-PROPS-CONTENT", 
         '_artop_swDataDefProps':"SW-DATA-DEF-PROPS", 
         '_artop_functionPointerSignatureRef':"BSW-MODULE-ENTRY"})

    @property
    def targetCategory_(self):
        return self._artop_targetCategory

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
    def ref_swDataDefProps_(self):
        return self._artop_swDataDefProps

    @property
    def swDataDefProps_(self):
        if self._artop_swDataDefProps is not None:
            if hasattr(self._artop_swDataDefProps, "uuid"):
                return self._artop_swDataDefProps.uuid
        return

    @property
    def ref_functionPointerSignature_(self):
        return self._artop_functionPointerSignatureRef

    @property
    def functionPointerSignature_(self):
        if self._artop_functionPointerSignatureRef is not None:
            if hasattr(self._artop_functionPointerSignatureRef, "uuid"):
                return self._artop_functionPointerSignatureRef.uuid
        return
