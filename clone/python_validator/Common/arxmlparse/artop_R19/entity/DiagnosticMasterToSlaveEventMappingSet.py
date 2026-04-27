# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticMasterToSlaveEventMappingSet.py
from .ARElement import ARElement

class DiagnosticMasterToSlaveEventMappingSet(ARElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticMasterToSlaveEventMapping import DiagnosticMasterToSlaveEventMapping
        self._artop_masterToSlaveEventMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_masterToSlaveEventMapping": "DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING"})

    @property
    def masterToSlaveEventMappings_DiagnosticMasterToSlaveEventMapping(self):
        return self._artop_masterToSlaveEventMapping
