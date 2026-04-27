# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VehiclePackage.py
from .SoftwareActivationDependency import SoftwareActivationDependency

class VehiclePackage(SoftwareActivationDependency):

    def __init__(self):
        super().__init__()
        from .VehicleDriverNotification import VehicleDriverNotification
        from .CryptoServiceCertificate import CryptoServiceCertificate
        from .VehicleRolloutStep import VehicleRolloutStep
        from .UcmDescription import UcmDescription
        from .Documentation import Documentation
        self._artop_repository = None
        self._artop_driverNotification = []
        self._artop_packagerSignatureRef = None
        self._artop_rolloutQualification = []
        self._artop_ucm = []
        self._artop_ucmMasterFallbackRef = []
        self._artop_vehicleDescriptionRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_driverNotification': '"VEHICLE-DRIVER-NOTIFICATION"', 
         '_artop_packagerSignatureRef': '"CRYPTO-SERVICE-CERTIFICATE"', 
         '_artop_rolloutQualification': '"VEHICLE-ROLLOUT-STEP"', 
         '_artop_ucm': '"UCM-DESCRIPTION"', 
         '_artop_ucmMasterFallbackRef': '"UCM-DESCRIPTION"', 
         '_artop_vehicleDescriptionRef': '"DOCUMENTATION"'})

    @property
    def repository_(self):
        return self._artop_repository

    @property
    def driverNotifications_VehicleDriverNotification(self):
        return self._artop_driverNotification

    @property
    def ref_packagerSignature_(self):
        return self._artop_packagerSignatureRef

    @property
    def packagerSignature_(self):
        if self._artop_packagerSignatureRef is not None:
            if hasattr(self._artop_packagerSignatureRef, "uuid"):
                return self._artop_packagerSignatureRef.uuid
        return

    @property
    def rolloutQualifications_VehicleRolloutStep(self):
        return self._artop_rolloutQualification

    @property
    def ucms_UcmDescription(self):
        return self._artop_ucm

    @property
    def ref_ucmMasterFallbacks_(self):
        return self._artop_ucmMasterFallbackRef

    @property
    def ucmMasterFallbacks_(self):
        return self._artop_ucmMasterFallbackRef

    @property
    def ref_vehicleDescription_(self):
        return self._artop_vehicleDescriptionRef

    @property
    def vehicleDescription_(self):
        if self._artop_vehicleDescriptionRef is not None:
            if hasattr(self._artop_vehicleDescriptionRef, "uuid"):
                return self._artop_vehicleDescriptionRef.uuid
        return
