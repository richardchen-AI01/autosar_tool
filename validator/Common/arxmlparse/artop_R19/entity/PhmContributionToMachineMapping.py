# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhmContributionToMachineMapping.py
from .ARElement import ARElement

class PhmContributionToMachineMapping(ARElement):

    def __init__(self):
        super().__init__()
        from .Machine import Machine
        from .PlatformHealthManagementContribution import PlatformHealthManagementContribution
        self._artop_machineRef = None
        self._artop_phmContributionRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_machineRef':"MACHINE", 
         '_artop_phmContributionRef':"PLATFORM-HEALTH-MANAGEMENT-CONTRIBUTION"})

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
    def ref_phmContributions_(self):
        return self._artop_phmContributionRef

    @property
    def phmContributions_(self):
        return self._artop_phmContributionRef
