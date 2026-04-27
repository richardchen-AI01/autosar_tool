# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\StateDependentStartupConfig.py
from .ARObject import ARObject

class StateDependentStartupConfig(ARObject):

    def __init__(self):
        super().__init__()
        from .Process import Process
        from .ExecutionDependency import ExecutionDependency
        from .ModeInMachineInstanceRef import ModeInMachineInstanceRef
        from .ResourceConsumption import ResourceConsumption
        from .ResourceGroup import ResourceGroup
        from .StartupConfig import StartupConfig
        self._artop_process = None
        self._artop_executionDependency = []
        self._artop_functionGroupStateIref = []
        self._artop_resourceConsumption = None
        self._artop_resourceGroupRef = None
        self._artop_startupConfigRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_process': '"PROCESS"', 
         '_artop_executionDependency': '"EXECUTION-DEPENDENCY"', 
         '_artop_functionGroupStateIref': '"MODE-IN-MACHINE-INSTANCE-REF-IREF"', 
         '_artop_resourceConsumption': '"RESOURCE-CONSUMPTION"', 
         '_artop_resourceGroupRef': '"RESOURCE-GROUP"', 
         '_artop_startupConfigRef': '"STARTUP-CONFIG"'})

    @property
    def ref_process_(self):
        return self._artop_process

    @property
    def process_(self):
        if self._artop_process is not None:
            if hasattr(self._artop_process, "uuid"):
                return self._artop_process.uuid
        return

    @property
    def executionDependencies_ExecutionDependency(self):
        return self._artop_executionDependency

    @property
    def functionGroupStates_ModeInMachineInstanceRef(self):
        return self._artop_functionGroupStateIref

    @property
    def ref_resourceConsumption_(self):
        return self._artop_resourceConsumption

    @property
    def resourceConsumption_(self):
        if self._artop_resourceConsumption is not None:
            if hasattr(self._artop_resourceConsumption, "uuid"):
                return self._artop_resourceConsumption.uuid
        return

    @property
    def ref_resourceGroup_(self):
        return self._artop_resourceGroupRef

    @property
    def resourceGroup_(self):
        if self._artop_resourceGroupRef is not None:
            if hasattr(self._artop_resourceGroupRef, "uuid"):
                return self._artop_resourceGroupRef.uuid
        return

    @property
    def ref_startupConfig_(self):
        return self._artop_startupConfigRef

    @property
    def startupConfig_(self):
        if self._artop_startupConfigRef is not None:
            if hasattr(self._artop_startupConfigRef, "uuid"):
                return self._artop_startupConfigRef.uuid
        return
