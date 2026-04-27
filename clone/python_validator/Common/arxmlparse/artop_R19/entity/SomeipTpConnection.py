# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipTpConnection.py
from .ARObject import ARObject

class SomeipTpConnection(ARObject):

    def __init__(self):
        super().__init__()
        from .SomeipTpConfig import SomeipTpConfig
        from .SomeipTpChannel import SomeipTpChannel
        from .PduTriggering import PduTriggering
        self._artop_separationTime = None
        self._artop_someipTpConfig = None
        self._artop_tpChannelRef = None
        self._artop_tpSduRef = None
        self._artop_transportPduRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_someipTpConfig': '"SOMEIP-TP-CONFIG"', 
         '_artop_tpChannelRef': '"SOMEIP-TP-CHANNEL"', 
         '_artop_tpSduRef': '"PDU-TRIGGERING"', 
         '_artop_transportPduRef': '"PDU-TRIGGERING"'})

    @property
    def separationTime_(self):
        return self._artop_separationTime

    @property
    def ref_someipTpConfig_(self):
        return self._artop_someipTpConfig

    @property
    def someipTpConfig_(self):
        if self._artop_someipTpConfig is not None:
            if hasattr(self._artop_someipTpConfig, "uuid"):
                return self._artop_someipTpConfig.uuid
        return

    @property
    def ref_tpChannel_(self):
        return self._artop_tpChannelRef

    @property
    def tpChannel_(self):
        if self._artop_tpChannelRef is not None:
            if hasattr(self._artop_tpChannelRef, "uuid"):
                return self._artop_tpChannelRef.uuid
        return

    @property
    def ref_tpSdu_(self):
        return self._artop_tpSduRef

    @property
    def tpSdu_(self):
        if self._artop_tpSduRef is not None:
            if hasattr(self._artop_tpSduRef, "uuid"):
                return self._artop_tpSduRef.uuid
        return

    @property
    def ref_transportPdu_(self):
        return self._artop_transportPduRef

    @property
    def transportPdu_(self):
        if self._artop_transportPduRef is not None:
            if hasattr(self._artop_transportPduRef, "uuid"):
                return self._artop_transportPduRef.uuid
        return
