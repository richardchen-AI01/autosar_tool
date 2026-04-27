# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucCommonAttributes.py
from .EcucDefinitionElement import EcucDefinitionElement

class EcucCommonAttributes(EcucDefinitionElement):

    def __init__(self):
        super().__init__()
        from .EcucConfigurationClassAffection import EcucConfigurationClassAffection
        from .EcucImplementationConfigurationClass import EcucImplementationConfigurationClass
        from .EcucMultiplicityConfigurationClass import EcucMultiplicityConfigurationClass
        from .EcucValueConfigurationClass import EcucValueConfigurationClass
        self._artop_origin = None
        self._artop_postBuildVariantMultiplicity = None
        self._artop_postBuildVariantValue = None
        self._artop_requiresIndex = None
        self._artop_configurationClassAffection = None
        self._artop_implementationConfigClass = []
        self._artop_multiplicityConfigClass = []
        self._artop_valueConfigClass = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_configurationClassAffection': '"ECUC-CONFIGURATION-CLASS-AFFECTION"', 
         '_artop_implementationConfigClass': '"ECUC-IMPLEMENTATION-CONFIGURATION-CLASS"', 
         '_artop_multiplicityConfigClass': '"ECUC-MULTIPLICITY-CONFIGURATION-CLASS"', 
         '_artop_valueConfigClass': '"ECUC-VALUE-CONFIGURATION-CLASS"'})

    @property
    def origin_(self):
        return self._artop_origin

    @property
    def postBuildVariantMultiplicity_(self):
        if self._artop_postBuildVariantMultiplicity:
            if self._artop_postBuildVariantMultiplicity == "true":
                return True
            return False
        else:
            return self._artop_postBuildVariantMultiplicity

    @property
    def postBuildVariantValue_(self):
        if self._artop_postBuildVariantValue:
            if self._artop_postBuildVariantValue == "true":
                return True
            return False
        else:
            return self._artop_postBuildVariantValue

    @property
    def requiresIndex_(self):
        if self._artop_requiresIndex:
            if self._artop_requiresIndex == "true":
                return True
            return False
        else:
            return self._artop_requiresIndex

    @property
    def ref_configurationClassAffection_(self):
        return self._artop_configurationClassAffection

    @property
    def configurationClassAffection_(self):
        if self._artop_configurationClassAffection is not None:
            if hasattr(self._artop_configurationClassAffection, "uuid"):
                return self._artop_configurationClassAffection.uuid
        return

    @property
    def implementationConfigClass_EcucImplementationConfigurationClass(self):
        return self._artop_implementationConfigClass

    @property
    def multiplicityConfigClass_EcucMultiplicityConfigurationClass(self):
        return self._artop_multiplicityConfigClass

    @property
    def valueConfigClass_EcucValueConfigurationClass(self):
        return self._artop_valueConfigClass
