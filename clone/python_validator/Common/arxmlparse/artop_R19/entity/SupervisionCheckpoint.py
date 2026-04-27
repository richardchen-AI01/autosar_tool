# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SupervisionCheckpoint.py
from .Identifiable import Identifiable

class SupervisionCheckpoint(Identifiable):

    def __init__(self):
        super().__init__()
        from .PlatformHealthManagementContribution import PlatformHealthManagementContribution
        from .PhmCheckpointInExecutableInstanceRef import PhmCheckpointInExecutableInstanceRef
        from .Process import Process
        self._artop_platformHealthManagementContribution = None
        self._artop_phmCheckpointIref = None
        self._artop_processRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_platformHealthManagementContribution':"PLATFORM-HEALTH-MANAGEMENT-CONTRIBUTION", 
         '_artop_phmCheckpointIref':"PHM-CHECKPOINT-IN-EXECUTABLE-INSTANCE-REF-IREF", 
         '_artop_processRef':"PROCESS"})

    @property
    def ref_platformHealthManagementContribution_(self):
        return self._artop_platformHealthManagementContribution

    @property
    def platformHealthManagementContribution_(self):
        if self._artop_platformHealthManagementContribution is not None:
            if hasattr(self._artop_platformHealthManagementContribution, "uuid"):
                return self._artop_platformHealthManagementContribution.uuid
        return

    @property
    def ref_phmCheckpoint_(self):
        return self._artop_phmCheckpointIref

    @property
    def phmCheckpoint_(self):
        if self._artop_phmCheckpointIref is not None:
            if hasattr(self._artop_phmCheckpointIref, "uuid"):
                return self._artop_phmCheckpointIref.uuid
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
