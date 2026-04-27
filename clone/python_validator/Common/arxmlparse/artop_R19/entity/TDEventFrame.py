# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventFrame.py
from .TDEventCom import TDEventCom

class TDEventFrame(TDEventCom):

    def __init__(self):
        super().__init__()
        from .Frame import Frame
        from .PhysicalChannel import PhysicalChannel
        self._artop_tdEventType = None
        self._artop_frameRef = None
        self._artop_physicalChannelRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_frameRef':"FRAME", 
         '_artop_physicalChannelRef':"PHYSICAL-CHANNEL"})

    @property
    def tdEventType_(self):
        return self._artop_tdEventType

    @property
    def ref_frame_(self):
        return self._artop_frameRef

    @property
    def frame_(self):
        if self._artop_frameRef is not None:
            if hasattr(self._artop_frameRef, "uuid"):
                return self._artop_frameRef.uuid
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
