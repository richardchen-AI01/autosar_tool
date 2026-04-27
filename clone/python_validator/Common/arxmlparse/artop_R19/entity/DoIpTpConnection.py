# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DoIpTpConnection.py
from .TpConnection import TpConnection

class DoIpTpConnection(TpConnection):

    def __init__(self):
        super().__init__()
        from .DoIpTpConfig import DoIpTpConfig
        from .DoIpLogicAddress import DoIpLogicAddress
        from .PduTriggering import PduTriggering
        self._artop_doIpTpConfig = None
        self._artop_doIpSourceAddressRef = None
        self._artop_doIpTargetAddressRef = None
        self._artop_tpSduRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_doIpTpConfig': '"DO-IP-TP-CONFIG"', 
         '_artop_doIpSourceAddressRef': '"DO-IP-LOGIC-ADDRESS"', 
         '_artop_doIpTargetAddressRef': '"DO-IP-LOGIC-ADDRESS"', 
         '_artop_tpSduRef': '"PDU-TRIGGERING"'})

    @property
    def ref_doIpTpConfig_(self):
        return self._artop_doIpTpConfig

    @property
    def doIpTpConfig_(self):
        if self._artop_doIpTpConfig is not None:
            if hasattr(self._artop_doIpTpConfig, "uuid"):
                return self._artop_doIpTpConfig.uuid
        return

    @property
    def ref_doIpSourceAddress_(self):
        return self._artop_doIpSourceAddressRef

    @property
    def doIpSourceAddress_(self):
        if self._artop_doIpSourceAddressRef is not None:
            if hasattr(self._artop_doIpSourceAddressRef, "uuid"):
                return self._artop_doIpSourceAddressRef.uuid
        return

    @property
    def ref_doIpTargetAddress_(self):
        return self._artop_doIpTargetAddressRef

    @property
    def doIpTargetAddress_(self):
        if self._artop_doIpTargetAddressRef is not None:
            if hasattr(self._artop_doIpTargetAddressRef, "uuid"):
                return self._artop_doIpTargetAddressRef.uuid
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
