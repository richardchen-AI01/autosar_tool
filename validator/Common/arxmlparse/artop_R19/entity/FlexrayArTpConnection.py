# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayArTpConnection.py
from .TpConnection import TpConnection

class FlexrayArTpConnection(TpConnection):

    def __init__(self):
        super().__init__()
        from .FlexrayArTpChannel import FlexrayArTpChannel
        from .IPdu import IPdu
        from .NPdu import NPdu
        from .TpAddress import TpAddress
        from .FlexrayArTpNode import FlexrayArTpNode
        self._artop_connectionPrioPdus = None
        self._artop_flexrayArTpChannel = None
        self._artop_directTpSduRef = None
        self._artop_flowControlPduRef = None
        self._artop_multicastRef = None
        self._artop_reversedTpSduRef = None
        self._artop_sourceRef = None
        self._artop_targetRef = []
        self._artop_transmitPduRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_flexrayArTpChannel': '"FLEXRAY-AR-TP-CHANNEL"', 
         '_artop_directTpSduRef': '"I-PDU"', 
         '_artop_flowControlPduRef': '"N-PDU"', 
         '_artop_multicastRef': '"TP-ADDRESS"', 
         '_artop_reversedTpSduRef': '"I-PDU"', 
         '_artop_sourceRef': '"FLEXRAY-AR-TP-NODE"', 
         '_artop_targetRef': '"FLEXRAY-AR-TP-NODE"', 
         '_artop_transmitPduRef': '"N-PDU"'})

    @property
    def connectionPrioPdus_(self):
        if self._artop_connectionPrioPdus:
            return int(self._artop_connectionPrioPdus)
        return self._artop_connectionPrioPdus

    @property
    def ref_flexrayArTpChannel_(self):
        return self._artop_flexrayArTpChannel

    @property
    def flexrayArTpChannel_(self):
        if self._artop_flexrayArTpChannel is not None:
            if hasattr(self._artop_flexrayArTpChannel, "uuid"):
                return self._artop_flexrayArTpChannel.uuid
        return

    @property
    def ref_directTpSdu_(self):
        return self._artop_directTpSduRef

    @property
    def directTpSdu_(self):
        if self._artop_directTpSduRef is not None:
            if hasattr(self._artop_directTpSduRef, "uuid"):
                return self._artop_directTpSduRef.uuid
        return

    @property
    def ref_flowControlPdu_(self):
        return self._artop_flowControlPduRef

    @property
    def flowControlPdu_(self):
        if self._artop_flowControlPduRef is not None:
            if hasattr(self._artop_flowControlPduRef, "uuid"):
                return self._artop_flowControlPduRef.uuid
        return

    @property
    def ref_multicast_(self):
        return self._artop_multicastRef

    @property
    def multicast_(self):
        if self._artop_multicastRef is not None:
            if hasattr(self._artop_multicastRef, "uuid"):
                return self._artop_multicastRef.uuid
        return

    @property
    def ref_reversedTpSdu_(self):
        return self._artop_reversedTpSduRef

    @property
    def reversedTpSdu_(self):
        if self._artop_reversedTpSduRef is not None:
            if hasattr(self._artop_reversedTpSduRef, "uuid"):
                return self._artop_reversedTpSduRef.uuid
        return

    @property
    def ref_source_(self):
        return self._artop_sourceRef

    @property
    def source_(self):
        if self._artop_sourceRef is not None:
            if hasattr(self._artop_sourceRef, "uuid"):
                return self._artop_sourceRef.uuid
        return

    @property
    def ref_targets_(self):
        return self._artop_targetRef

    @property
    def targets_(self):
        return self._artop_targetRef

    @property
    def ref_transmitPdus_(self):
        return self._artop_transmitPduRef

    @property
    def transmitPdus_(self):
        return self._artop_transmitPduRef
