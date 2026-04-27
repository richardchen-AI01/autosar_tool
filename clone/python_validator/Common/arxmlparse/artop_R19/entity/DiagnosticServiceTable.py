# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticServiceTable.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticServiceTable(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticConnectionRefConditional import DiagnosticConnectionRefConditional
        from .EcuInstance import EcuInstance
        from .DiagnosticServiceInstance import DiagnosticServiceInstance
        self._artop_protocolKind = None
        self._artop_diagnosticConnection = []
        self._artop_ecuInstanceRef = None
        self._artop_serviceInstanceRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticConnection':"DIAGNOSTIC-CONNECTION-REF-CONDITIONAL", 
         '_artop_ecuInstanceRef':"ECU-INSTANCE", 
         '_artop_serviceInstanceRef':"DIAGNOSTIC-SERVICE-INSTANCE"})

    @property
    def protocolKind_(self):
        return self._artop_protocolKind

    @property
    def diagnosticConnections_DiagnosticConnectionRefConditional(self):
        return self._artop_diagnosticConnection

    @property
    def ref_ecuInstance_(self):
        return self._artop_ecuInstanceRef

    @property
    def ecuInstance_(self):
        if self._artop_ecuInstanceRef is not None:
            if hasattr(self._artop_ecuInstanceRef, "uuid"):
                return self._artop_ecuInstanceRef.uuid
        return

    @property
    def ref_serviceInstances_(self):
        return self._artop_serviceInstanceRef

    @property
    def serviceInstances_(self):
        return self._artop_serviceInstanceRef
