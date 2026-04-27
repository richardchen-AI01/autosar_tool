# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LocalSupervision.py
from .PhmSupervision import PhmSupervision

class LocalSupervision(PhmSupervision):

    def __init__(self):
        super().__init__()
        from .PlatformHealthManagementContribution import PlatformHealthManagementContribution
        from .AliveSupervision import AliveSupervision
        from .DeadlineSupervision import DeadlineSupervision
        from .LogicalSupervision import LogicalSupervision
        from .CheckpointTransition import CheckpointTransition
        self._artop_failedSupervisionCyclesTolerance = None
        self._artop_platformHealthManagementContribution = None
        self._artop_aliveSupervision = []
        self._artop_deadlineSupervision = []
        self._artop_logicalSupervision = []
        self._artop_transition = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_platformHealthManagementContribution': '"PLATFORM-HEALTH-MANAGEMENT-CONTRIBUTION"', 
         '_artop_aliveSupervision': '"ALIVE-SUPERVISION"', 
         '_artop_deadlineSupervision': '"DEADLINE-SUPERVISION"', 
         '_artop_logicalSupervision': '"LOGICAL-SUPERVISION"', 
         '_artop_transition': '"CHECKPOINT-TRANSITION"'})

    @property
    def failedSupervisionCyclesTolerance_(self):
        return self._artop_failedSupervisionCyclesTolerance

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
    def aliveSupervisions_AliveSupervision(self):
        return self._artop_aliveSupervision

    @property
    def deadlineSupervisions_DeadlineSupervision(self):
        return self._artop_deadlineSupervision

    @property
    def logicalSupervisions_LogicalSupervision(self):
        return self._artop_logicalSupervision

    @property
    def transitions_CheckpointTransition(self):
        return self._artop_transition
