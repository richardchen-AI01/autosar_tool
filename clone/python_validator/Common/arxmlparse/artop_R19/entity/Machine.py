# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Machine.py
from .AtpStructureElement import AtpStructureElement
from .ARElement import ARElement

class Machine(ARElement, AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .EnterExitTimeout import EnterExitTimeout
        from .TagWithOptionalValue import TagWithOptionalValue
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .HwElement import HwElement
        from .MachineDesign import MachineDesign
        from .AdaptiveModuleInstantiation import AdaptiveModuleInstantiation
        from .Processor import Processor
        from .SecureCommunicationDeployment import SecureCommunicationDeployment
        self._artop_trustedPlatformExecutableLaunchBehavior = None
        self._artop_defaultApplicationTimeout = None
        self._artop_environmentVariable = []
        self._artop_functionGroup = []
        self._artop_hwElementRef = []
        self._artop_machineDesignRef = None
        self._artop_moduleInstantiation = []
        self._artop_processor = []
        self._artop_secureCommunicationDeployment = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_defaultApplicationTimeout': '"ENTER-EXIT-TIMEOUT"', 
         '_artop_environmentVariable': '"TAG-WITH-OPTIONAL-VALUE"', 
         '_artop_functionGroup': '"MODE-DECLARATION-GROUP-PROTOTYPE"', 
         '_artop_hwElementRef': '"HW-ELEMENT"', 
         '_artop_machineDesignRef': '"MACHINE-DESIGN"', 
         '_artop_moduleInstantiation': '"ADAPTIVE-MODULE-INSTANTIATION"', 
         '_artop_processor': '"PROCESSOR"', 
         '_artop_secureCommunicationDeployment': '"SECURE-COMMUNICATION-DEPLOYMENT"'})

    @property
    def trustedPlatformExecutableLaunchBehavior_(self):
        return self._artop_trustedPlatformExecutableLaunchBehavior

    @property
    def ref_defaultApplicationTimeout_(self):
        return self._artop_defaultApplicationTimeout

    @property
    def defaultApplicationTimeout_(self):
        if self._artop_defaultApplicationTimeout is not None:
            if hasattr(self._artop_defaultApplicationTimeout, "uuid"):
                return self._artop_defaultApplicationTimeout.uuid
        return

    @property
    def environmentVariables_TagWithOptionalValue(self):
        return self._artop_environmentVariable

    @property
    def functionGroups_ModeDeclarationGroupPrototype(self):
        return self._artop_functionGroup

    @property
    def ref_hwElements_(self):
        return self._artop_hwElementRef

    @property
    def hwElements_(self):
        return self._artop_hwElementRef

    @property
    def ref_machineDesign_(self):
        return self._artop_machineDesignRef

    @property
    def machineDesign_(self):
        if self._artop_machineDesignRef is not None:
            if hasattr(self._artop_machineDesignRef, "uuid"):
                return self._artop_machineDesignRef.uuid
        return

    @property
    def moduleInstantiations_AdaptiveModuleInstantiation(self):
        return self._artop_moduleInstantiation

    @property
    def processors_Processor(self):
        return self._artop_processor

    @property
    def secureCommunicationDeployments_SecureCommunicationDeployment(self):
        return self._artop_secureCommunicationDeployment
