# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventISignal.py
from .TDEventCom import TDEventCom

class TDEventISignal(TDEventCom):

    def __init__(self):
        super().__init__()
        from .ISignal import ISignal
        from .PhysicalChannel import PhysicalChannel
        self._artop_tdEventType = None
        self._artop_iSignalRef = None
        self._artop_physicalChannelRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_iSignalRef':"I-SIGNAL", 
         '_artop_physicalChannelRef':"PHYSICAL-CHANNEL"})

    @property
    def tdEventType_(self):
        return self._artop_tdEventType

    @property
    def ref_iSignal_(self):
        return self._artop_iSignalRef

    @property
    def iSignal_(self):
        if self._artop_iSignalRef is not None:
            if hasattr(self._artop_iSignalRef, "uuid"):
                return self._artop_iSignalRef.uuid
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
