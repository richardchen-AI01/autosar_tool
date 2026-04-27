# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoftwareCluster.py
from .SoftwareActivationDependency import SoftwareActivationDependency

class SoftwareCluster(SoftwareActivationDependency):

    def __init__(self):
        super().__init__()
        from .ARElement import ARElement
        from .FibexElement import FibexElement
        from .UploadablePackageElement import UploadablePackageElement
        from .Process import Process
        from .SoftwareClusterDesign import SoftwareClusterDesign
        from .SoftwareClusterDiagnosticAddress import SoftwareClusterDiagnosticAddress
        from .DiagnosticContributionSet import DiagnosticContributionSet
        from .Documentation import Documentation
        from .AdaptiveModuleInstantiation import AdaptiveModuleInstantiation
        from .CryptoServiceCertificate import CryptoServiceCertificate
        self._artop_typeApproval = None
        self._artop_vendorId = None
        self._artop_version = None
        self._artop_containedArElementRef = []
        self._artop_containedFibexElementRef = []
        self._artop_containedPackageElementRef = []
        self._artop_containedProcessRef = []
        self._artop_designRef = []
        self._artop_diagnosticAddress = []
        self._artop_diagnosticExtractRef = None
        self._artop_licenseRef = []
        self._artop_moduleInstantiationRef = []
        self._artop_releaseNotesRef = None
        self._artop_subSoftwareClusterRef = []
        self._artop_vendorSignatureRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_containedArElementRef': '"AR-ELEMENT"', 
         '_artop_containedFibexElementRef': '"FIBEX-ELEMENT"', 
         '_artop_containedPackageElementRef': '"UPLOADABLE-PACKAGE-ELEMENT"', 
         '_artop_containedProcessRef': '"PROCESS"', 
         '_artop_designRef': '"SOFTWARE-CLUSTER-DESIGN"', 
         '_artop_diagnosticAddress': '"SOFTWARE-CLUSTER-DIAGNOSTIC-ADDRESS"', 
         '_artop_diagnosticExtractRef': '"DIAGNOSTIC-CONTRIBUTION-SET"', 
         '_artop_licenseRef': '"DOCUMENTATION"', 
         '_artop_moduleInstantiationRef': '"ADAPTIVE-MODULE-INSTANTIATION"', 
         '_artop_releaseNotesRef': '"DOCUMENTATION"', 
         '_artop_subSoftwareClusterRef': '"SOFTWARE-CLUSTER"', 
         '_artop_vendorSignatureRef': '"CRYPTO-SERVICE-CERTIFICATE"'})

    @property
    def typeApproval_(self):
        return self._artop_typeApproval

    @property
    def vendorId_(self):
        return self._artop_vendorId

    @property
    def version_(self):
        return self._artop_version

    @property
    def ref_containedARElements_(self):
        return self._artop_containedArElementRef

    @property
    def containedARElements_(self):
        return self._artop_containedArElementRef

    @property
    def ref_containedFibexElements_(self):
        return self._artop_containedFibexElementRef

    @property
    def containedFibexElements_(self):
        return self._artop_containedFibexElementRef

    @property
    def ref_containedPackageElements_(self):
        return self._artop_containedPackageElementRef

    @property
    def containedPackageElements_(self):
        return self._artop_containedPackageElementRef

    @property
    def ref_containedProcess_(self):
        return self._artop_containedProcessRef

    @property
    def containedProcess_(self):
        return self._artop_containedProcessRef

    @property
    def ref_designs_(self):
        return self._artop_designRef

    @property
    def designs_(self):
        return self._artop_designRef

    @property
    def diagnosticAddress_SoftwareClusterDiagnosticAddress(self):
        return self._artop_diagnosticAddress

    @property
    def ref_diagnosticExtract_(self):
        return self._artop_diagnosticExtractRef

    @property
    def diagnosticExtract_(self):
        if self._artop_diagnosticExtractRef is not None:
            if hasattr(self._artop_diagnosticExtractRef, "uuid"):
                return self._artop_diagnosticExtractRef.uuid
        return

    @property
    def ref_licenses_(self):
        return self._artop_licenseRef

    @property
    def licenses_(self):
        return self._artop_licenseRef

    @property
    def ref_moduleInstantiations_(self):
        return self._artop_moduleInstantiationRef

    @property
    def moduleInstantiations_(self):
        return self._artop_moduleInstantiationRef

    @property
    def ref_releaseNotes_(self):
        return self._artop_releaseNotesRef

    @property
    def releaseNotes_(self):
        if self._artop_releaseNotesRef is not None:
            if hasattr(self._artop_releaseNotesRef, "uuid"):
                return self._artop_releaseNotesRef.uuid
        return

    @property
    def ref_subSoftwareClusters_(self):
        return self._artop_subSoftwareClusterRef

    @property
    def subSoftwareClusters_(self):
        return self._artop_subSoftwareClusterRef

    @property
    def ref_vendorSignature_(self):
        return self._artop_vendorSignatureRef

    @property
    def vendorSignature_(self):
        if self._artop_vendorSignatureRef is not None:
            if hasattr(self._artop_vendorSignatureRef, "uuid"):
                return self._artop_vendorSignatureRef.uuid
        return
