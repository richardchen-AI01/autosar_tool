# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucParameterValue.py
from .EcucIndexableValue import EcucIndexableValue

class EcucParameterValue(EcucIndexableValue):

    def __init__(self):
        super().__init__()
        from .EcucContainerValue import EcucContainerValue
        from .EcucParameterDef import EcucParameterDef
        from .Annotation import Annotation
        from .VariationPoint import VariationPoint
        self._artop_isAutoValue = None
        self._artop_ecucContainerValue = None
        self._artop_definitionRef = None
        self._artop_annotation = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ecucContainerValue': '"ECUC-CONTAINER-VALUE"', 
         '_artop_definitionRef': '"ECUC-PARAMETER-DEF"', 
         '_artop_annotation': '"ANNOTATION"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def isAutoValue_(self):
        if self._artop_isAutoValue:
            if self._artop_isAutoValue == "true":
                return True
            return False
        else:
            return self._artop_isAutoValue

    @property
    def ref_ecucContainerValue_(self):
        return self._artop_ecucContainerValue

    @property
    def ecucContainerValue_(self):
        if self._artop_ecucContainerValue is not None:
            if hasattr(self._artop_ecucContainerValue, "uuid"):
                return self._artop_ecucContainerValue.uuid
        return

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
    def annotations_Annotation(self):
        return self._artop_annotation

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
