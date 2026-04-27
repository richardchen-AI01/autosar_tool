# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinConfigurationEntry.py
from .ScheduleTableEntry import ScheduleTableEntry

class LinConfigurationEntry(ScheduleTableEntry):

    def __init__(self):
        super().__init__()
        from .LinSlave import LinSlave
        from .LinSlaveConfigIdent import LinSlaveConfigIdent
        self._artop_assignedControllerRef = None
        self._artop_assignedLinSlaveConfigRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_assignedControllerRef':"LIN-SLAVE", 
         '_artop_assignedLinSlaveConfigRef':"LIN-SLAVE-CONFIG-IDENT"})

    @property
    def ref_assignedController_(self):
        return self._artop_assignedControllerRef

    @property
    def assignedController_(self):
        if self._artop_assignedControllerRef is not None:
            if hasattr(self._artop_assignedControllerRef, "uuid"):
                return self._artop_assignedControllerRef.uuid
        return

    @property
    def ref_assignedLinSlaveConfig_(self):
        return self._artop_assignedLinSlaveConfigRef

    @property
    def assignedLinSlaveConfig_(self):
        if self._artop_assignedLinSlaveConfigRef is not None:
            if hasattr(self._artop_assignedLinSlaveConfigRef, "uuid"):
                return self._artop_assignedLinSlaveConfigRef.uuid
        return
