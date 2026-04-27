# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticProtocol.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticProtocol(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticConnectionRefConditional import DiagnosticConnectionRefConditional
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .BooleanValueVariationPoint import BooleanValueVariationPoint
        from .DiagnosticServiceTableRefConditional import DiagnosticServiceTableRefConditional
        self._artop_protocolKind = None
        self._artop_diagnosticConnection = []
        self._artop_priority = None
        self._artop_sendRespPendOnTransToBoot = None
        self._artop_serviceTable = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_diagnosticConnection': '"DIAGNOSTIC-CONNECTION-REF-CONDITIONAL"', 
         '_artop_priority': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_sendRespPendOnTransToBoot': '"BOOLEAN-VALUE-VARIATION-POINT"', 
         '_artop_serviceTable': '"DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL"'})

    @property
    def protocolKind_(self):
        return self._artop_protocolKind

    @property
    def diagnosticConnections_DiagnosticConnectionRefConditional(self):
        return self._artop_diagnosticConnection

    @property
    def ref_priority_(self):
        return self._artop_priority

    @property
    def priority_(self):
        if self._artop_priority is not None:
            if hasattr(self._artop_priority, "uuid"):
                return self._artop_priority.uuid
        return

    @property
    def ref_sendRespPendOnTransToBoot_(self):
        return self._artop_sendRespPendOnTransToBoot

    @property
    def sendRespPendOnTransToBoot_(self):
        if self._artop_sendRespPendOnTransToBoot is not None:
            if hasattr(self._artop_sendRespPendOnTransToBoot, "uuid"):
                return self._artop_sendRespPendOnTransToBoot.uuid
        return

    @property
    def serviceTables_DiagnosticServiceTableRefConditional(self):
        return self._artop_serviceTable
