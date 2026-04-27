# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UcmStep.py
from .Identifiable import Identifiable

class UcmStep(Identifiable):

    def __init__(self):
        super().__init__()
        from .VehicleRolloutStep import VehicleRolloutStep
        from .SoftwarePackageStep import SoftwarePackageStep
        from .UcmDescription import UcmDescription
        self._artop_vehicleRolloutStep = None
        self._artop_softwarePackageStep = []
        self._artop_ucmRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_vehicleRolloutStep':"VEHICLE-ROLLOUT-STEP", 
         '_artop_softwarePackageStep':"SOFTWARE-PACKAGE-STEP", 
         '_artop_ucmRef':"UCM-DESCRIPTION"})

    @property
    def ref_vehicleRolloutStep_(self):
        return self._artop_vehicleRolloutStep

    @property
    def vehicleRolloutStep_(self):
        if self._artop_vehicleRolloutStep is not None:
            if hasattr(self._artop_vehicleRolloutStep, "uuid"):
                return self._artop_vehicleRolloutStep.uuid
        return

    @property
    def softwarePackageSteps_SoftwarePackageStep(self):
        return self._artop_softwarePackageStep

    @property
    def ref_ucm_(self):
        return self._artop_ucmRef

    @property
    def ucm_(self):
        if self._artop_ucmRef is not None:
            if hasattr(self._artop_ucmRef, "uuid"):
                return self._artop_ucmRef.uuid
        return
