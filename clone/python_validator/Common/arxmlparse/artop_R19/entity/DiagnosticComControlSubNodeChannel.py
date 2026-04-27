# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticComControlSubNodeChannel.py
from .ARObject import ARObject

class DiagnosticComControlSubNodeChannel(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticComControlClass import DiagnosticComControlClass
        from .CommunicationCluster import CommunicationCluster
        self._artop_subNodeNumber = None
        self._artop_diagnosticComControlClass = None
        self._artop_subNodeChannelRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticComControlClass':"DIAGNOSTIC-COM-CONTROL-CLASS", 
         '_artop_subNodeChannelRef':"COMMUNICATION-CLUSTER"})

    @property
    def subNodeNumber_(self):
        return self._artop_subNodeNumber

    @property
    def ref_diagnosticComControlClass_(self):
        return self._artop_diagnosticComControlClass

    @property
    def diagnosticComControlClass_(self):
        if self._artop_diagnosticComControlClass is not None:
            if hasattr(self._artop_diagnosticComControlClass, "uuid"):
                return self._artop_diagnosticComControlClass.uuid
        return

    @property
    def ref_subNodeChannel_(self):
        return self._artop_subNodeChannelRef

    @property
    def subNodeChannel_(self):
        if self._artop_subNodeChannelRef is not None:
            if hasattr(self._artop_subNodeChannelRef, "uuid"):
                return self._artop_subNodeChannelRef.uuid
        return
