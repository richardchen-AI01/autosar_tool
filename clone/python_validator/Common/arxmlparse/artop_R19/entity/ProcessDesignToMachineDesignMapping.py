# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ProcessDesignToMachineDesignMapping.py
from .Identifiable import Identifiable

class ProcessDesignToMachineDesignMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .ProcessDesignToMachineDesignMappingSet import ProcessDesignToMachineDesignMappingSet
        from .MachineDesign import MachineDesign
        from .ProcessDesign import ProcessDesign
        self._artop_processDesignToMachineDesignMappingSet = None
        self._artop_machineDesignRef = None
        self._artop_processDesignRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_processDesignToMachineDesignMappingSet':"PROCESS-DESIGN-TO-MACHINE-DESIGN-MAPPING-SET", 
         '_artop_machineDesignRef':"MACHINE-DESIGN", 
         '_artop_processDesignRef':"PROCESS-DESIGN"})

    @property
    def ref_processDesignToMachineDesignMappingSet_(self):
        return self._artop_processDesignToMachineDesignMappingSet

    @property
    def processDesignToMachineDesignMappingSet_(self):
        if self._artop_processDesignToMachineDesignMappingSet is not None:
            if hasattr(self._artop_processDesignToMachineDesignMappingSet, "uuid"):
                return self._artop_processDesignToMachineDesignMappingSet.uuid
        return

    @property
    def ref_machineDesign_(self):
        return self._artop_machineDesignRef

    @property
    def machineDesign_(self):
        if self._artop_machineDesignRef is not None:
            if hasattr(self._artop_machineDesignRef, "uuid"):
                return self._artop_machineDesignRef.uuid
        return

    @property
    def ref_processDesign_(self):
        return self._artop_processDesignRef

    @property
    def processDesign_(self):
        if self._artop_processDesignRef is not None:
            if hasattr(self._artop_processDesignRef, "uuid"):
                return self._artop_processDesignRef.uuid
        return
