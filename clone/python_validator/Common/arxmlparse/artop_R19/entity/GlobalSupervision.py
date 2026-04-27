# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\GlobalSupervision.py
from .PhmSupervision import PhmSupervision

class GlobalSupervision(PhmSupervision):

    def __init__(self):
        super().__init__()
        from .PlatformHealthManagementContribution import PlatformHealthManagementContribution
        from .LocalSupervision import LocalSupervision
        self._artop_expiredSupervisionCyclesTolerance = None
        self._artop_supervisionCycle = None
        self._artop_platformHealthManagementContribution = None
        self._artop_localSupervisionRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_platformHealthManagementContribution':"PLATFORM-HEALTH-MANAGEMENT-CONTRIBUTION", 
         '_artop_localSupervisionRef':"LOCAL-SUPERVISION"})

    @property
    def expiredSupervisionCyclesTolerance_(self):
        return self._artop_expiredSupervisionCyclesTolerance

    @property
    def supervisionCycle_(self):
        return self._artop_supervisionCycle

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
    def ref_localSupervisions_(self):
        return self._artop_localSupervisionRef

    @property
    def localSupervisions_(self):
        return self._artop_localSupervisionRef
