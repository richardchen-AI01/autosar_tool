# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwAxisType.py
from .ARElement import ARElement

class SwAxisType(ARElement):

    def __init__(self):
        super().__init__()
        from .DocumentationBlock import DocumentationBlock
        from .SwGenericAxisParamType import SwGenericAxisParamType
        self._artop_swGenericAxisDesc = None
        self._artop_swGenericAxisParamType = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swGenericAxisDesc':"DOCUMENTATION-BLOCK", 
         '_artop_swGenericAxisParamType':"SW-GENERIC-AXIS-PARAM-TYPE"})

    @property
    def ref_swGenericAxisDesc_(self):
        return self._artop_swGenericAxisDesc

    @property
    def swGenericAxisDesc_(self):
        if self._artop_swGenericAxisDesc is not None:
            if hasattr(self._artop_swGenericAxisDesc, "uuid"):
                return self._artop_swGenericAxisDesc.uuid
        return

    @property
    def swGenericAxisParamTypes_SwGenericAxisParamType(self):
        return self._artop_swGenericAxisParamType
