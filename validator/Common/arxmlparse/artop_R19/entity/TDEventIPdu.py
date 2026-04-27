# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventIPdu.py
from .TDEventCom import TDEventCom

class TDEventIPdu(TDEventCom):

    def __init__(self):
        super().__init__()
        from .IPdu import IPdu
        from .PhysicalChannel import PhysicalChannel
        self._artop_tdEventType = None
        self._artop_iPduRef = None
        self._artop_physicalChannelRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_iPduRef':"I-PDU", 
         '_artop_physicalChannelRef':"PHYSICAL-CHANNEL"})

    @property
    def tdEventType_(self):
        return self._artop_tdEventType

    @property
    def ref_iPdu_(self):
        return self._artop_iPduRef

    @property
    def iPdu_(self):
        if self._artop_iPduRef is not None:
            if hasattr(self._artop_iPduRef, "uuid"):
                return self._artop_iPduRef.uuid
        return

    @property
    def ref_physicalChannel_(self):
        return self._artop_physicalChannelRef

    @property
    def physicalChannel_(self):
        if self._artop_physicalChannelRef is not None:
            if hasattr(self._artop_physicalChannelRef, "uuid"):
                return self._artop_physicalChannelRef.uuid
        return
