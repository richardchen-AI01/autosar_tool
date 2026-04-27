# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucContainerValue.py
from .EcucIndexableValue import EcucIndexableValue
from .Identifiable import Identifiable

class EcucContainerValue(Identifiable, EcucIndexableValue):

    def __init__(self):
        super().__init__()
        from .EcucContainerDef import EcucContainerDef
        from .EcucParameterValue import EcucParameterValue
        from .EcucAbstractReferenceValue import EcucAbstractReferenceValue
        from .VariationPoint import VariationPoint
        self._artop_definitionRef = None
        self._artop_parameterValue = []
        self._artop_referenceValue = []
        self._artop_subContainer = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_definitionRef': '"ECUC-CONTAINER-DEF"', 
         '_artop_parameterValue': '"ECUC-PARAMETER-VALUE"', 
         '_artop_referenceValue': '"ECUC-ABSTRACT-REFERENCE-VALUE"', 
         '_artop_subContainer': '"ECUC-CONTAINER-VALUE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

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
    def parameterValues_EcucParameterValue(self):
        return self._artop_parameterValue

    @property
    def referenceValues_EcucAbstractReferenceValue(self):
        return self._artop_referenceValue

    @property
    def subContainers_EcucContainerValue(self):
        return self._artop_subContainer

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return

    def getAttrValue(self, enum_path, variant_value=None):
        from ..artop_util import get_attribute_value
        return get_attribute_value(self, enum_path, variant_value)

    def getSubContainer(self, enum_path=None, variant_value=None):
        from ..artop_util import get_subcontainer
        return get_subcontainer(self, enum_path, variant_value)

    def getParentContainer(self):
        from ..artop_util import get_parentContainer
        return get_parentContainer(self.fatherUuid)

    def getIndex(self, variant_value=None) -> int:
        subContainers = self.getParentContainer().subContainers_EcucContainerValue
        if variant_value is None:
            list_same_def = [container for container in subContainers if container.ref_definition_ == self.ref_definition_]
        else:
            list_same_def = [container for container in subContainers if container.ref_definition_ == self.ref_definition_ and (container.v_id == -1 or container.v_id == variant_value)]
        index = list_same_def.index(self)
        return index

    def getWholeIndex(self, variant_value=None) -> int:
        from ..artop_util import get_wholeIndex
        return get_wholeIndex(self, variant_value)
