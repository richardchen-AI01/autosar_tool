# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PredefinedVariant.py
from .ARElement import ARElement

class PredefinedVariant(ARElement):

    def __init__(self):
        super().__init__()
        from .PostBuildVariantCriterionValueSet import PostBuildVariantCriterionValueSet
        from .SwSystemconstantValueSet import SwSystemconstantValueSet
        self._artop_includedVariantRef = []
        self._artop_postBuildVariantCriterionValueSetRef = []
        self._artop_swSystemconstantValueSetRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_includedVariantRef':"PREDEFINED-VARIANT", 
         '_artop_postBuildVariantCriterionValueSetRef':"POST-BUILD-VARIANT-CRITERION-VALUE-SET", 
         '_artop_swSystemconstantValueSetRef':"SW-SYSTEMCONSTANT-VALUE-SET"})

    @property
    def ref_includedVariants_(self):
        return self._artop_includedVariantRef

    @property
    def includedVariants_(self):
        return self._artop_includedVariantRef

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
