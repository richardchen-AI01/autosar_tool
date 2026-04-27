# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwBitRepresentation.py
from .ARObject import ARObject

class SwBitRepresentation(ARObject):

    def __init__(self):
        super().__init__()
        from .SwDataDefPropsContent import SwDataDefPropsContent
        self._artop_bitPosition = None
        self._artop_numberOfBits = None
        self._artop_swDataDefPropsContent = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_swDataDefPropsContent": "SW-DATA-DEF-PROPS-CONTENT"})

    @property
    def bitPosition_(self):
        if self._artop_bitPosition:
            return int(self._artop_bitPosition)
        return self._artop_bitPosition

    @property
    def numberOfBits_(self):
        if self._artop_numberOfBits:
            return int(self._artop_numberOfBits)
        return self._artop_numberOfBits

    @property
    def ref_swDataDefPropsContent_(self):
        return self._artop_swDataDefPropsContent

    @property
    def swDataDefPropsContent_(self):
        if self._artop_swDataDefPropsContent is not None:
            if hasattr(self._artop_swDataDefPropsContent, "uuid"):
                return self._artop_swDataDefPropsContent.uuid
        return
