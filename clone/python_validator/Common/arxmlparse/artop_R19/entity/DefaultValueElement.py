# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DefaultValueElement.py
from .ARObject import ARObject

class DefaultValueElement(ARObject):

    def __init__(self):
        super().__init__()
        from .PduMappingDefaultValue import PduMappingDefaultValue
        self._artop_elementByteValue = None
        self._artop_elementPosition = None
        self._artop_pduMappingDefaultValue = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_pduMappingDefaultValue": "PDU-MAPPING-DEFAULT-VALUE"})

    @property
    def elementByteValue_(self):
        if self._artop_elementByteValue:
            return int(self._artop_elementByteValue)
        return self._artop_elementByteValue

    @property
    def elementPosition_(self):
        if self._artop_elementPosition:
            return int(self._artop_elementPosition)
        return self._artop_elementPosition

    @property
    def ref_pduMappingDefaultValue_(self):
        return self._artop_pduMappingDefaultValue

    @property
    def pduMappingDefaultValue_(self):
        if self._artop_pduMappingDefaultValue is not None:
            if hasattr(self._artop_pduMappingDefaultValue, "uuid"):
                return self._artop_pduMappingDefaultValue.uuid
        return
