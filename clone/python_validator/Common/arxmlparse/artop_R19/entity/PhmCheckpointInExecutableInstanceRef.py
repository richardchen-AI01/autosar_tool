# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhmCheckpointInExecutableInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class PhmCheckpointInExecutableInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .SupervisionCheckpoint import SupervisionCheckpoint
        from .Executable import Executable
        from .RootSwComponentPrototype import RootSwComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .RPortPrototype import RPortPrototype
        from .PhmCheckpoint import PhmCheckpoint
        self._artop_supervisionCheckpoint = None
        self._artop_executable = None
        self._artop_contextRootSwComponentPrototypeRef = None
        self._artop_contextComponentPrototypeRef = []
        self._artop_contextRPortPrototypeRef = None
        self._artop_targetPhmCheckpointRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_supervisionCheckpoint': '"SUPERVISION-CHECKPOINT"', 
         '_artop_executable': '"EXECUTABLE"', 
         '_artop_contextRootSwComponentPrototypeRef': '"ROOT-SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextRPortPrototypeRef': '"R-PORT-PROTOTYPE"', 
         '_artop_targetPhmCheckpointRef': '"PHM-CHECKPOINT"'})

    @property
    def ref_supervisionCheckpoint_(self):
        return self._artop_supervisionCheckpoint

    @property
    def supervisionCheckpoint_(self):
        if self._artop_supervisionCheckpoint is not None:
            if hasattr(self._artop_supervisionCheckpoint, "uuid"):
                return self._artop_supervisionCheckpoint.uuid
        return

    @property
    def ref_base_(self):
        return self._artop_executable

    @property
    def base_(self):
        if self._artop_executable is not None:
            if hasattr(self._artop_executable, "uuid"):
                return self._artop_executable.uuid
        return

    @property
    def ref_contextRootSwComponentPrototype_(self):
        return self._artop_contextRootSwComponentPrototypeRef

    @property
    def contextRootSwComponentPrototype_(self):
        if self._artop_contextRootSwComponentPrototypeRef is not None:
            if hasattr(self._artop_contextRootSwComponentPrototypeRef, "uuid"):
                return self._artop_contextRootSwComponentPrototypeRef.uuid
        return

    @property
    def ref_contextComponentPrototypes_(self):
        return self._artop_contextComponentPrototypeRef

    @property
    def contextComponentPrototypes_(self):
        return self._artop_contextComponentPrototypeRef

    @property
    def ref_contextRPortPrototype_(self):
        return self._artop_contextRPortPrototypeRef

    @property
    def contextRPortPrototype_(self):
        if self._artop_contextRPortPrototypeRef is not None:
            if hasattr(self._artop_contextRPortPrototypeRef, "uuid"):
                return self._artop_contextRPortPrototypeRef.uuid
        return

    @property
    def ref_targetPhmCheckpoint_(self):
        return self._artop_targetPhmCheckpointRef

    @property
    def targetPhmCheckpoint_(self):
        if self._artop_targetPhmCheckpointRef is not None:
            if hasattr(self._artop_targetPhmCheckpointRef, "uuid"):
                return self._artop_targetPhmCheckpointRef.uuid
        return
