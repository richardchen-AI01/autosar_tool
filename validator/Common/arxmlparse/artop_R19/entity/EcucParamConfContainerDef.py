# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucParamConfContainerDef.py
from .EcucContainerDef import EcucContainerDef

class EcucParamConfContainerDef(EcucContainerDef):

    def __init__(self):
        super().__init__()
        from .EcucChoiceContainerDef import EcucChoiceContainerDef
        from .EcucParameterDef import EcucParameterDef
        from .EcucAbstractReferenceDef import EcucAbstractReferenceDef
        from .EcucContainerDef import EcucContainerDef
        self._artop_multipleConfigurationContainer = None
        self._artop_ecucChoiceContainerDef = None
        self._artop_parameter = []
        self._artop_reference = []
        self._artop_subContainer = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ecucChoiceContainerDef': '"ECUC-CHOICE-CONTAINER-DEF"', 
         '_artop_parameter': '"ECUC-PARAMETER-DEF"', 
         '_artop_reference': '"ECUC-ABSTRACT-REFERENCE-DEF"', 
         '_artop_subContainer': '"ECUC-CONTAINER-DEF"'})

    @property
    def multipleConfigurationContainer_(self):
        if self._artop_multipleConfigurationContainer:
            if self._artop_multipleConfigurationContainer == "true":
                return True
            return False
        else:
            return self._artop_multipleConfigurationContainer

    @property
    def ref_ecucChoiceContainerDef_(self):
        return self._artop_ecucChoiceContainerDef

    @property
    def ecucChoiceContainerDef_(self):
        if self._artop_ecucChoiceContainerDef is not None:
            if hasattr(self._artop_ecucChoiceContainerDef, "uuid"):
                return self._artop_ecucChoiceContainerDef.uuid
        return

    @property
    def parameters_EcucParameterDef(self):
        return self._artop_parameter

    @property
    def references_EcucAbstractReferenceDef(self):
        return self._artop_reference

    @property
    def subContainers_EcucContainerDef(self):
        return self._artop_subContainer
