# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PostBuildVariantCriterionValue.py
from .ARObject import ARObject

class PostBuildVariantCriterionValue(ARObject):

    def __init__(self):
        super().__init__()
        from .PostBuildVariantCriterionValueSet import PostBuildVariantCriterionValueSet
        from .PostBuildVariantCriterion import PostBuildVariantCriterion
        from .IntegerValueVariationPoint import IntegerValueVariationPoint
        from .Annotation import Annotation
        self._artop_postBuildVariantCriterionValueSet = None
        self._artop_variantCriterionRef = None
        self._artop_value = None
        self._artop_annotation = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_postBuildVariantCriterionValueSet': '"POST-BUILD-VARIANT-CRITERION-VALUE-SET"', 
         '_artop_variantCriterionRef': '"POST-BUILD-VARIANT-CRITERION"', 
         '_artop_value': '"INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_annotation': '"ANNOTATION"'})

    @property
    def ref_postBuildVariantCriterionValueSet_(self):
        return self._artop_postBuildVariantCriterionValueSet

    @property
    def postBuildVariantCriterionValueSet_(self):
        if self._artop_postBuildVariantCriterionValueSet is not None:
            if hasattr(self._artop_postBuildVariantCriterionValueSet, "uuid"):
                return self._artop_postBuildVariantCriterionValueSet.uuid
        return

    @property
    def ref_variantCriterion_(self):
        return self._artop_variantCriterionRef

    @property
    def variantCriterion_(self):
        if self._artop_variantCriterionRef is not None:
            if hasattr(self._artop_variantCriterionRef, "uuid"):
                return self._artop_variantCriterionRef.uuid
        return

    @property
    def ref_value_(self):
        return self._artop_value

    @property
    def value_(self):
        if self._artop_value is not None:
            if hasattr(self._artop_value, "uuid"):
                return self._artop_value.uuid
        return

    @property
    def annotations_Annotation(self):
        return self._artop_annotation
