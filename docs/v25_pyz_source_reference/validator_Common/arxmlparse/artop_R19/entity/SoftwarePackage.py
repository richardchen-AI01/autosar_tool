# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoftwarePackage.py
from .ARElement import ARElement

class SoftwarePackage(ARElement):

    def __init__(self):
        super().__init__()
        from .CryptoServiceCertificate import CryptoServiceCertificate
        from .ModeInMachineInstanceRef import ModeInMachineInstanceRef
        from .SoftwareCluster import SoftwareCluster
        self._artop_actionType = None
        self._artop_activationAction = None
        self._artop_compressedSoftwarePackageSize = None
        self._artop_isDeltaPackage = None
        self._artop_maximumSupportedUcmVersion = None
        self._artop_minimumSupportedUcmVersion = None
        self._artop_packagerId = None
        self._artop_postVerificationReboot = None
        self._artop_preActivationReboot = None
        self._artop_uncompressedSoftwareClusterSize = None
        self._artop_packagerSignatureRef = None
        self._artop_preActivateIref = []
        self._artop_softwareClusterRef = None
        self._artop_verifyIref = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_packagerSignatureRef': '"CRYPTO-SERVICE-CERTIFICATE"', 
         '_artop_preActivateIref': '"MODE-IN-MACHINE-INSTANCE-REF-IREF"', 
         '_artop_softwareClusterRef': '"SOFTWARE-CLUSTER"', 
         '_artop_verifyIref': '"MODE-IN-MACHINE-INSTANCE-REF-IREF"'})

    @property
    def actionType_(self):
        return self._artop_actionType

    @property
    def activationAction_(self):
        return self._artop_activationAction

    @property
    def compressedSoftwarePackageSize_(self):
        return self._artop_compressedSoftwarePackageSize

    @property
    def isDeltaPackage_(self):
        if self._artop_isDeltaPackage:
            if self._artop_isDeltaPackage == "true":
                return True
            return False
        else:
            return self._artop_isDeltaPackage

    @property
    def maximumSupportedUcmVersion_(self):
        return self._artop_maximumSupportedUcmVersion

    @property
    def minimumSupportedUcmVersion_(self):
        return self._artop_minimumSupportedUcmVersion

    @property
    def packagerId_(self):
        return self._artop_packagerId

    @property
    def postVerificationReboot_(self):
        if self._artop_postVerificationReboot:
            if self._artop_postVerificationReboot == "true":
                return True
            return False
        else:
            return self._artop_postVerificationReboot

    @property
    def preActivationReboot_(self):
        if self._artop_preActivationReboot:
            if self._artop_preActivationReboot == "true":
                return True
            return False
        else:
            return self._artop_preActivationReboot

    @property
    def uncompressedSoftwareClusterSize_(self):
        return self._artop_uncompressedSoftwareClusterSize

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
    def preActivates_ModeInMachineInstanceRef(self):
        return self._artop_preActivateIref

    @property
    def ref_softwareCluster_(self):
        return self._artop_softwareClusterRef

    @property
    def softwareCluster_(self):
        if self._artop_softwareClusterRef is not None:
            if hasattr(self._artop_softwareClusterRef, "uuid"):
                return self._artop_softwareClusterRef.uuid
        return

    @property
    def verifies_ModeInMachineInstanceRef(self):
        return self._artop_verifyIref
