# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticJ1939SpnMapping.py
from .DiagnosticMapping import DiagnosticMapping

class DiagnosticJ1939SpnMapping(DiagnosticMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticJ1939Node import DiagnosticJ1939Node
        from .DiagnosticJ1939Spn import DiagnosticJ1939Spn
        from .SystemSignal import SystemSignal
        self._artop_sendingNodeRef = []
        self._artop_spnRef = None
        self._artop_systemSignalRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_sendingNodeRef':"DIAGNOSTIC-J-1939-NODE", 
         '_artop_spnRef':"DIAGNOSTIC-J-1939-SPN", 
         '_artop_systemSignalRef':"SYSTEM-SIGNAL"})

    @property
    def ref_sendingNodes_(self):
        return self._artop_sendingNodeRef

    @property
    def sendingNodes_(self):
        return self._artop_sendingNodeRef

    @property
    def ref_spn_(self):
        return self._artop_spnRef

    @property
    def spn_(self):
        if self._artop_spnRef is not None:
            if hasattr(self._artop_spnRef, "uuid"):
                return self._artop_spnRef.uuid
        return

    @property
    def ref_systemSignal_(self):
        return self._artop_systemSignalRef

    @property
    def systemSignal_(self):
        if self._artop_systemSignalRef is not None:
            if hasattr(self._artop_systemSignalRef, "uuid"):
                return self._artop_systemSignalRef.uuid
        return
