# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ProcessToMachineMapping.py
from .Identifiable import Identifiable

class ProcessToMachineMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .ProcessToMachineMappingSet import ProcessToMachineMappingSet
        from .ProcessDesignToMachineDesignMapping import ProcessDesignToMachineDesignMapping
        from .Machine import Machine
        from .NonOsModuleInstantiation import NonOsModuleInstantiation
        from .Process import Process
        from .ProcessorCore import ProcessorCore
        self._artop_processToMachineMappingSet = None
        self._artop_designRef = None
        self._artop_machineRef = None
        self._artop_nonOsModuleInstantiationRef = None
        self._artop_processRef = None
        self._artop_shallNotRunOnRef = []
        self._artop_shallRunOnRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_processToMachineMappingSet': '"PROCESS-TO-MACHINE-MAPPING-SET"', 
         '_artop_designRef': '"PROCESS-DESIGN-TO-MACHINE-DESIGN-MAPPING"', 
         '_artop_machineRef': '"MACHINE"', 
         '_artop_nonOsModuleInstantiationRef': '"NON-OS-MODULE-INSTANTIATION"', 
         '_artop_processRef': '"PROCESS"', 
         '_artop_shallNotRunOnRef': '"PROCESSOR-CORE"', 
         '_artop_shallRunOnRef': '"PROCESSOR-CORE"'})

    @property
    def ref_processToMachineMappingSet_(self):
        return self._artop_processToMachineMappingSet

    @property
    def processToMachineMappingSet_(self):
        if self._artop_processToMachineMappingSet is not None:
            if hasattr(self._artop_processToMachineMappingSet, "uuid"):
                return self._artop_processToMachineMappingSet.uuid
        return

    @property
    def ref_design_(self):
        return self._artop_designRef

    @property
    def design_(self):
        if self._artop_designRef is not None:
            if hasattr(self._artop_designRef, "uuid"):
                return self._artop_designRef.uuid
        return

    @property
    def ref_machine_(self):
        return self._artop_machineRef

    @property
    def machine_(self):
        if self._artop_machineRef is not None:
            if hasattr(self._artop_machineRef, "uuid"):
                return self._artop_machineRef.uuid
        return

    @property
    def ref_nonOsModuleInstantiation_(self):
        return self._artop_nonOsModuleInstantiationRef

    @property
    def nonOsModuleInstantiation_(self):
        if self._artop_nonOsModuleInstantiationRef is not None:
            if hasattr(self._artop_nonOsModuleInstantiationRef, "uuid"):
                return self._artop_nonOsModuleInstantiationRef.uuid
        return

    @property
    def ref_process_(self):
        return self._artop_processRef

    @property
    def process_(self):
        if self._artop_processRef is not None:
            if hasattr(self._artop_processRef, "uuid"):
                return self._artop_processRef.uuid
        return

    @property
    def ref_shallNotRunOns_(self):
        return self._artop_shallNotRunOnRef

    @property
    def shallNotRunOns_(self):
        return self._artop_shallNotRunOnRef

    @property
    def ref_shallRunOns_(self):
        return self._artop_shallRunOnRef

    @property
    def shallRunOns_(self):
        return self._artop_shallRunOnRef
