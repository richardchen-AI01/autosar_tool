# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswImplementation.py
from .Implementation import Implementation

class BswImplementation(Implementation):

    def __init__(self):
        super().__init__()
        from .BswInternalBehavior import BswInternalBehavior
        from .BswDebugInfo import BswDebugInfo
        from .EcucModuleConfigurationValues import EcucModuleConfigurationValues
        from .EcucModuleDef import EcucModuleDef
        self._artop_arReleaseVersion = None
        self._artop_vendorApiInfix = None
        self._artop_behaviorRef = None
        self._artop_debugInfo = []
        self._artop_preconfiguredConfigurationRef = []
        self._artop_recommendedConfigurationRef = []
        self._artop_vendorSpecificModuleDefRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_behaviorRef': '"BSW-INTERNAL-BEHAVIOR"', 
         '_artop_debugInfo': '"BSW-DEBUG-INFO"', 
         '_artop_preconfiguredConfigurationRef': '"ECUC-MODULE-CONFIGURATION-VALUES"', 
         '_artop_recommendedConfigurationRef': '"ECUC-MODULE-CONFIGURATION-VALUES"', 
         '_artop_vendorSpecificModuleDefRef': '"ECUC-MODULE-DEF"'})

    @property
    def arReleaseVersion_(self):
        return self._artop_arReleaseVersion

    @property
    def vendorApiInfix_(self):
        return self._artop_vendorApiInfix

    @property
    def ref_behavior_(self):
        return self._artop_behaviorRef

    @property
    def behavior_(self):
        if self._artop_behaviorRef is not None:
            if hasattr(self._artop_behaviorRef, "uuid"):
                return self._artop_behaviorRef.uuid
        return

    @property
    def debugInfos_BswDebugInfo(self):
        return self._artop_debugInfo

    @property
    def ref_preconfiguredConfigurations_(self):
        return self._artop_preconfiguredConfigurationRef

    @property
    def preconfiguredConfigurations_(self):
        return self._artop_preconfiguredConfigurationRef

    @property
    def ref_recommendedConfigurations_(self):
        return self._artop_recommendedConfigurationRef

    @property
    def recommendedConfigurations_(self):
        return self._artop_recommendedConfigurationRef

    @property
    def ref_vendorSpecificModuleDefs_(self):
        return self._artop_vendorSpecificModuleDefRef

    @property
    def vendorSpecificModuleDefs_(self):
        return self._artop_vendorSpecificModuleDefRef
