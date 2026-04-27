# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucContainerDef.py
from .EcucDefinitionElement import EcucDefinitionElement

class EcucContainerDef(EcucDefinitionElement):

    def __init__(self):
        super().__init__()
        from .EcucDestinationUriDef import EcucDestinationUriDef
        from .EcucMultiplicityConfigurationClass import EcucMultiplicityConfigurationClass
        self._artop_postBuildChangeable = None
        self._artop_postBuildVariantMultiplicity = None
        self._artop_requiresIndex = None
        self._artop_destinationUriRef = []
        self._artop_multiplicityConfigClass = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_destinationUriRef':"ECUC-DESTINATION-URI-DEF", 
         '_artop_multiplicityConfigClass':"ECUC-MULTIPLICITY-CONFIGURATION-CLASS"})

    @property
    def postBuildChangeable_(self):
        if self._artop_postBuildChangeable:
            if self._artop_postBuildChangeable == "true":
                return True
            return False
        else:
            return self._artop_postBuildChangeable

    @property
    def postBuildVariantMultiplicity_(self):
        if self._artop_postBuildVariantMultiplicity:
            if self._artop_postBuildVariantMultiplicity == "true":
                return True
            return False
        else:
            return self._artop_postBuildVariantMultiplicity

    @property
    def requiresIndex_(self):
        if self._artop_requiresIndex:
            if self._artop_requiresIndex == "true":
                return True
            return False
        else:
            return self._artop_requiresIndex

    @property
    def ref_destinationUris_(self):
        return self._artop_destinationUriRef

    @property
    def destinationUris_(self):
        return self._artop_destinationUriRef

    @property
    def multiplicityConfigClass_EcucMultiplicityConfigurationClass(self):
        return self._artop_multiplicityConfigClass
