# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticMasterToSlaveEventMapping.py
from .Identifiable import Identifiable

class DiagnosticMasterToSlaveEventMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .DiagnosticMasterToSlaveEventMappingSet import DiagnosticMasterToSlaveEventMappingSet
        from .DiagnosticEvent import DiagnosticEvent
        self._artop_diagnosticMasterToSlaveEventMappingSet = None
        self._artop_masterEventRef = None
        self._artop_slaveEventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticMasterToSlaveEventMappingSet':"DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING-SET", 
         '_artop_masterEventRef':"DIAGNOSTIC-EVENT", 
         '_artop_slaveEventRef':"DIAGNOSTIC-EVENT"})

    @property
    def ref_diagnosticMasterToSlaveEventMappingSet_(self):
        return self._artop_diagnosticMasterToSlaveEventMappingSet

    @property
    def diagnosticMasterToSlaveEventMappingSet_(self):
        if self._artop_diagnosticMasterToSlaveEventMappingSet is not None:
            if hasattr(self._artop_diagnosticMasterToSlaveEventMappingSet, "uuid"):
                return self._artop_diagnosticMasterToSlaveEventMappingSet.uuid
        return

    @property
    def ref_masterEvent_(self):
        return self._artop_masterEventRef

    @property
    def masterEvent_(self):
        if self._artop_masterEventRef is not None:
            if hasattr(self._artop_masterEventRef, "uuid"):
                return self._artop_masterEventRef.uuid
        return

    @property
    def ref_slaveEvent_(self):
        return self._artop_slaveEventRef

    @property
    def slaveEvent_(self):
        if self._artop_slaveEventRef is not None:
            if hasattr(self._artop_slaveEventRef, "uuid"):
                return self._artop_slaveEventRef.uuid
        return
