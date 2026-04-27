# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMFeatureMapElement.py
from .Identifiable import Identifiable

class FMFeatureMapElement(Identifiable):

    def __init__(self):
        super().__init__()
        from .FMFeatureMap import FMFeatureMap
        from .FMFeatureMapAssertion import FMFeatureMapAssertion
        from .FMFeatureMapCondition import FMFeatureMapCondition
        from .PostBuildVariantCriterionValueSet import PostBuildVariantCriterionValueSet
        from .SwSystemconstantValueSet import SwSystemconstantValueSet
        self._artop_fmFeatureMap = None
        self._artop_assertion = []
        self._artop_condition = []
        self._artop_postBuildVariantCriterionValueSetRef = []
        self._artop_swSystemconstantValueSetRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_fmFeatureMap': '"FM-FEATURE-MAP"', 
         '_artop_assertion': '"FM-FEATURE-MAP-ASSERTION"', 
         '_artop_condition': '"FM-FEATURE-MAP-CONDITION"', 
         '_artop_postBuildVariantCriterionValueSetRef': '"POST-BUILD-VARIANT-CRITERION-VALUE-SET"', 
         '_artop_swSystemconstantValueSetRef': '"SW-SYSTEMCONSTANT-VALUE-SET"'})

    @property
    def ref_fMFeatureMap_(self):
        return self._artop_fmFeatureMap

    @property
    def fMFeatureMap_(self):
        if self._artop_fmFeatureMap is not None:
            if hasattr(self._artop_fmFeatureMap, "uuid"):
                return self._artop_fmFeatureMap.uuid
        return

    @property
    def assertions_FMFeatureMapAssertion(self):
        return self._artop_assertion

    @property
    def conditions_FMFeatureMapCondition(self):
        return self._artop_condition

    @property
    def ref_postBuildVariantCriterionValueSets_(self):
        return self._artop_postBuildVariantCriterionValueSetRef

    @property
    def postBuildVariantCriterionValueSets_(self):
        return self._artop_postBuildVariantCriterionValueSetRef

    @property
    def ref_swSystemconstantValueSets_(self):
        return self._artop_swSystemconstantValueSetRef

    @property
    def swSystemconstantValueSets_(self):
        return self._artop_swSystemconstantValueSetRef
