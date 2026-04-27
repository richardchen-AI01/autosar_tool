# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoftwareClusterDesign.py
from .SoftwareActivationDependency import SoftwareActivationDependency
from .AtpClassifier import AtpClassifier

class SoftwareClusterDesign(AtpClassifier, SoftwareActivationDependency):

    def __init__(self):
        super().__init__()
        from .ProcessDesign import ProcessDesign
        from .SoftwareClusterDesignDependency import SoftwareClusterDesignDependency
        from .SoftwareClusterDiagnosticAddress import SoftwareClusterDiagnosticAddress
        from .DiagnosticContributionSet import DiagnosticContributionSet
        from .MachineDesign import MachineDesign
        from .ARElement import ARElement
        from .FibexElement import FibexElement
        from .UploadablePackageElement import UploadablePackageElement
        from .RootSwClusterDesignComponentPrototype import RootSwClusterDesignComponentPrototype
        self._artop_containedProcessRef = []
        self._artop_dependsOn = []
        self._artop_diagnosticAddress = []
        self._artop_diagnosticContributionRef = []
        self._artop_intendedTargetMachineRef = None
        self._artop_requiredArElementRef = []
        self._artop_requiredFibexElementRef = []
        self._artop_requiredPackageElementRef = []
        self._artop_rootComposition = None
        self._artop_subSoftwareClusterRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_containedProcessRef': '"PROCESS-DESIGN"', 
         '_artop_dependsOn': '"SOFTWARE-CLUSTER-DESIGN-DEPENDENCY"', 
         '_artop_diagnosticAddress': '"SOFTWARE-CLUSTER-DIAGNOSTIC-ADDRESS"', 
         '_artop_diagnosticContributionRef': '"DIAGNOSTIC-CONTRIBUTION-SET"', 
         '_artop_intendedTargetMachineRef': '"MACHINE-DESIGN"', 
         '_artop_requiredArElementRef': '"AR-ELEMENT"', 
         '_artop_requiredFibexElementRef': '"FIBEX-ELEMENT"', 
         '_artop_requiredPackageElementRef': '"UPLOADABLE-PACKAGE-ELEMENT"', 
         '_artop_rootComposition': '"ROOT-SW-CLUSTER-DESIGN-COMPONENT-PROTOTYPE"', 
         '_artop_subSoftwareClusterRef': '"SOFTWARE-CLUSTER-DESIGN"'})

    @property
    def ref_containedProcess_(self):
        return self._artop_containedProcessRef

    @property
    def containedProcess_(self):
        return self._artop_containedProcessRef

    @property
    def dependsOns_SoftwareClusterDesignDependency(self):
        return self._artop_dependsOn

    @property
    def diagnosticAddress_SoftwareClusterDiagnosticAddress(self):
        return self._artop_diagnosticAddress

    @property
    def ref_diagnosticContributions_(self):
        return self._artop_diagnosticContributionRef

    @property
    def diagnosticContributions_(self):
        return self._artop_diagnosticContributionRef

    @property
    def ref_intendedTargetMachine_(self):
        return self._artop_intendedTargetMachineRef

    @property
    def intendedTargetMachine_(self):
        if self._artop_intendedTargetMachineRef is not None:
            if hasattr(self._artop_intendedTargetMachineRef, "uuid"):
                return self._artop_intendedTargetMachineRef.uuid
        return

    @property
    def ref_requiredARElements_(self):
        return self._artop_requiredArElementRef

    @property
    def requiredARElements_(self):
        return self._artop_requiredArElementRef

    @property
    def ref_requiredFibexElements_(self):
        return self._artop_requiredFibexElementRef

    @property
    def requiredFibexElements_(self):
        return self._artop_requiredFibexElementRef

    @property
    def ref_requiredPackageElements_(self):
        return self._artop_requiredPackageElementRef

    @property
    def requiredPackageElements_(self):
        return self._artop_requiredPackageElementRef

    @property
    def ref_rootComposition_(self):
        return self._artop_rootComposition

    @property
    def rootComposition_(self):
        if self._artop_rootComposition is not None:
            if hasattr(self._artop_rootComposition, "uuid"):
                return self._artop_rootComposition.uuid
        return

    @property
    def ref_subSoftwareClusters_(self):
        return self._artop_subSoftwareClusterRef

    @property
    def subSoftwareClusters_(self):
        return self._artop_subSoftwareClusterRef
