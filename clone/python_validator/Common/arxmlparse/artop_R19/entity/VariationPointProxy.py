# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VariationPointProxy.py
from .Identifiable import Identifiable

class VariationPointProxy(Identifiable):

    def __init__(self):
        super().__init__()
        from .ConditionByFormula import ConditionByFormula
        from .ImplementationDataType import ImplementationDataType
        from .PostBuildVariantCriterion import PostBuildVariantCriterion
        from .PostBuildVariantCondition import PostBuildVariantCondition
        from .AttributeValueVariationPoint import AttributeValueVariationPoint
        self._artop_conditionAccess = None
        self._artop_implementationDataTypeRef = None
        self._artop_postBuildValueAccessRef = None
        self._artop_postBuildVariantCondition = []
        self._artop_valueAccess = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_conditionAccess': '"CONDITION-BY-FORMULA"', 
         '_artop_implementationDataTypeRef': '"IMPLEMENTATION-DATA-TYPE"', 
         '_artop_postBuildValueAccessRef': '"POST-BUILD-VARIANT-CRITERION"', 
         '_artop_postBuildVariantCondition': '"POST-BUILD-VARIANT-CONDITION"', 
         '_artop_valueAccess': '"ATTRIBUTE-VALUE-VARIATION-POINT"'})

    @property
    def ref_conditionAccess_(self):
        return self._artop_conditionAccess

    @property
    def conditionAccess_(self):
        if self._artop_conditionAccess is not None:
            if hasattr(self._artop_conditionAccess, "uuid"):
                return self._artop_conditionAccess.uuid
        return

    @property
    def ref_implementationDataType_(self):
        return self._artop_implementationDataTypeRef

    @property
    def implementationDataType_(self):
        if self._artop_implementationDataTypeRef is not None:
            if hasattr(self._artop_implementationDataTypeRef, "uuid"):
                return self._artop_implementationDataTypeRef.uuid
        return

    @property
    def ref_postBuildValueAccess_(self):
        return self._artop_postBuildValueAccessRef

    @property
    def postBuildValueAccess_(self):
        if self._artop_postBuildValueAccessRef is not None:
            if hasattr(self._artop_postBuildValueAccessRef, "uuid"):
                return self._artop_postBuildValueAccessRef.uuid
        return

    @property
    def postBuildVariantConditions_PostBuildVariantCondition(self):
        return self._artop_postBuildVariantCondition

    @property
    def ref_valueAccess_(self):
        return self._artop_valueAccess

    @property
    def valueAccess_(self):
        if self._artop_valueAccess is not None:
            if hasattr(self._artop_valueAccess, "uuid"):
                return self._artop_valueAccess.uuid
        return
