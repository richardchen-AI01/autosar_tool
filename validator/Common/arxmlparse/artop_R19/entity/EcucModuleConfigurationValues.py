# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucModuleConfigurationValues.py
from .ARElement import ARElement

class EcucModuleConfigurationValues(ARElement):

    def __init__(self):
        super().__init__()
        from .EcucModuleDef import EcucModuleDef
        from .BswImplementation import BswImplementation
        from .EcucContainerValue import EcucContainerValue
        self._artop_ecucDefEdition = None
        self._artop_implementationConfigVariant = None
        self._artop_postBuildVariantUsed = None
        self._artop_definitionRef = None
        self._artop_moduleDescriptionRef = None
        self._artop_container = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_definitionRef':"ECUC-MODULE-DEF", 
         '_artop_moduleDescriptionRef':"BSW-IMPLEMENTATION", 
         '_artop_container':"ECUC-CONTAINER-VALUE"})

    @property
    def ecucDefEdition_(self):
        return self._artop_ecucDefEdition

    @property
    def implementationConfigVariant_(self):
        return self._artop_implementationConfigVariant

    @property
    def postBuildVariantUsed_(self):
        if self._artop_postBuildVariantUsed:
            if self._artop_postBuildVariantUsed == "true":
                return True
            return False
        else:
            return self._artop_postBuildVariantUsed

    @property
    def ref_definition_(self):
        return self._artop_definitionRef

    @property
    def definition_(self):
        if self._artop_definitionRef is not None:
            if hasattr(self._artop_definitionRef, "uuid"):
                return self._artop_definitionRef.uuid
        return

    @property
    def ref_moduleDescription_(self):
        return self._artop_moduleDescriptionRef

    @property
    def moduleDescription_(self):
        if self._artop_moduleDescriptionRef is not None:
            if hasattr(self._artop_moduleDescriptionRef, "uuid"):
                return self._artop_moduleDescriptionRef.uuid
        return

    @property
    def containers_EcucContainerValue(self):
        return self._artop_container
