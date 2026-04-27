# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucModuleDef.py
from .EcucDefinitionElement import EcucDefinitionElement
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class EcucModuleDef(ARElement, AtpBlueprint, AtpBlueprintable, EcucDefinitionElement):

    def __init__(self):
        super().__init__()
        from .EcucContainerDef import EcucContainerDef
        self._artop_apiServicePrefix = None
        self._artop_postBuildVariantSupport = None
        self._artop_supportedConfigVariant = None
        self._artop_refinedModuleDefRef = None
        self._artop_container = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_refinedModuleDefRef':"ECUC-MODULE-DEF", 
         '_artop_container':"ECUC-CONTAINER-DEF"})

    @property
    def apiServicePrefix_(self):
        return self._artop_apiServicePrefix

    @property
    def postBuildVariantSupport_(self):
        if self._artop_postBuildVariantSupport:
            if self._artop_postBuildVariantSupport == "true":
                return True
            return False
        else:
            return self._artop_postBuildVariantSupport

    @property
    def supportedConfigVariant_(self):
        return self._artop_supportedConfigVariant

    @property
    def ref_refinedModuleDef_(self):
        return self._artop_refinedModuleDefRef

    @property
    def refinedModuleDef_(self):
        if self._artop_refinedModuleDefRef is not None:
            if hasattr(self._artop_refinedModuleDefRef, "uuid"):
                return self._artop_refinedModuleDefRef.uuid
        return

    @property
    def containers_EcucContainerDef(self):
        return self._artop_container
