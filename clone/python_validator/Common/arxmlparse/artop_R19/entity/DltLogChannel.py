# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DltLogChannel.py
from .Identifiable import Identifiable

class DltLogChannel(Identifiable):

    def __init__(self):
        super().__init__()
        from .DltConfig import DltConfig
        from .DltMessage import DltMessage
        from .PduTriggering import PduTriggering
        self._artop_applicationDescription = None
        self._artop_applicationId = None
        self._artop_contextDescription = None
        self._artop_contextId = None
        self._artop_sessionId = None
        self._artop_dltConfig = None
        self._artop_dltMessageRef = []
        self._artop_rxPduTriggeringRef = None
        self._artop_txPduTriggeringRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dltConfig': '"DLT-CONFIG"', 
         '_artop_dltMessageRef': '"DLT-MESSAGE"', 
         '_artop_rxPduTriggeringRef': '"PDU-TRIGGERING"', 
         '_artop_txPduTriggeringRef': '"PDU-TRIGGERING"'})

    @property
    def applicationDescription_(self):
        return self._artop_applicationDescription

    @property
    def applicationId_(self):
        return self._artop_applicationId

    @property
    def contextDescription_(self):
        return self._artop_contextDescription

    @property
    def contextId_(self):
        return self._artop_contextId

    @property
    def sessionId_(self):
        return self._artop_sessionId

    @property
    def ref_dltConfig_(self):
        return self._artop_dltConfig

    @property
    def dltConfig_(self):
        if self._artop_dltConfig is not None:
            if hasattr(self._artop_dltConfig, "uuid"):
                return self._artop_dltConfig.uuid
        return

    @property
    def ref_dltMessages_(self):
        return self._artop_dltMessageRef

    @property
    def dltMessages_(self):
        return self._artop_dltMessageRef

    @property
    def ref_rxPduTriggering_(self):
        return self._artop_rxPduTriggeringRef

    @property
    def rxPduTriggering_(self):
        if self._artop_rxPduTriggeringRef is not None:
            if hasattr(self._artop_rxPduTriggeringRef, "uuid"):
                return self._artop_rxPduTriggeringRef.uuid
        return

    @property
    def ref_txPduTriggering_(self):
        return self._artop_txPduTriggeringRef

    @property
    def txPduTriggering_(self):
        if self._artop_txPduTriggeringRef is not None:
            if hasattr(self._artop_txPduTriggeringRef, "uuid"):
                return self._artop_txPduTriggeringRef.uuid
        return
