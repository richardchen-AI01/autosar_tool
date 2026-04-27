# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VehicleRolloutStep.py
from .Identifiable import Identifiable

class VehicleRolloutStep(Identifiable):

    def __init__(self):
        super().__init__()
        from .VehiclePackage import VehiclePackage
        from .UcmStep import UcmStep
        self._artop_safetyPolicy = None
        self._artop_vehiclePackage = None
        self._artop_ucmProcessing = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_vehiclePackage':"VEHICLE-PACKAGE", 
         '_artop_ucmProcessing':"UCM-STEP"})

    @property
    def safetyPolicy_(self):
        return self._artop_safetyPolicy

    @property
    def ref_vehiclePackage_(self):
        return self._artop_vehiclePackage

    @property
    def vehiclePackage_(self):
        if self._artop_vehiclePackage is not None:
            if hasattr(self._artop_vehiclePackage, "uuid"):
                return self._artop_vehiclePackage.uuid
        return

    @property
    def ucmProcessings_UcmStep(self):
        return self._artop_ucmProcessing
