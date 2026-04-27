# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ExecutionDependency.py
from .ARObject import ARObject

class ExecutionDependency(ARObject):

    def __init__(self):
        super().__init__()
        from .StateDependentStartupConfig import StateDependentStartupConfig
        from .ModeInProcessInstanceRef import ModeInProcessInstanceRef
        self._artop_stateDependentStartupConfig = None
        self._artop_processStateIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_stateDependentStartupConfig':"STATE-DEPENDENT-STARTUP-CONFIG", 
         '_artop_processStateIref':"MODE-IN-PROCESS-INSTANCE-REF-IREF"})

    @property
    def ref_stateDependentStartupConfig_(self):
        return self._artop_stateDependentStartupConfig

    @property
    def stateDependentStartupConfig_(self):
        if self._artop_stateDependentStartupConfig is not None:
            if hasattr(self._artop_stateDependentStartupConfig, "uuid"):
                return self._artop_stateDependentStartupConfig.uuid
        return

    @property
    def ref_processState_(self):
        return self._artop_processStateIref

    @property
    def processState_(self):
        if self._artop_processStateIref is not None:
            if hasattr(self._artop_processStateIref, "uuid"):
                return self._artop_processStateIref.uuid
        return
