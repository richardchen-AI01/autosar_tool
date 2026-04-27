# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MultiplexedIPdu.py
from .IPdu import IPdu

class MultiplexedIPdu(IPdu):

    def __init__(self):
        super().__init__()
        from .DynamicPart import DynamicPart
        from .StaticPart import StaticPart
        self._artop_selectorFieldByteOrder = None
        self._artop_selectorFieldLength = None
        self._artop_selectorFieldStartPosition = None
        self._artop_triggerMode = None
        self._artop_unusedBitPattern = None
        self._artop_dynamicPart = []
        self._artop_staticPart = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dynamicPart':"DYNAMIC-PART", 
         '_artop_staticPart':"STATIC-PART"})

    @property
    def selectorFieldByteOrder_(self):
        return self._artop_selectorFieldByteOrder

    @property
    def selectorFieldLength_(self):
        if self._artop_selectorFieldLength:
            return int(self._artop_selectorFieldLength)
        return self._artop_selectorFieldLength

    @property
    def selectorFieldStartPosition_(self):
        if self._artop_selectorFieldStartPosition:
            return int(self._artop_selectorFieldStartPosition)
        return self._artop_selectorFieldStartPosition

    @property
    def triggerMode_(self):
        return self._artop_triggerMode

    @property
    def unusedBitPattern_(self):
        if self._artop_unusedBitPattern:
            return int(self._artop_unusedBitPattern)
        return self._artop_unusedBitPattern

    @property
    def dynamicParts_DynamicPart(self):
        return self._artop_dynamicPart

    @property
    def staticParts_StaticPart(self):
        return self._artop_staticPart
