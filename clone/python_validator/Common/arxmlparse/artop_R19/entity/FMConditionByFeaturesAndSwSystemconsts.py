# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMConditionByFeaturesAndSwSystemconsts.py
from .FMFormulaByFeaturesAndSwSystemconsts import FMFormulaByFeaturesAndSwSystemconsts

class FMConditionByFeaturesAndSwSystemconsts(FMFormulaByFeaturesAndSwSystemconsts):

    def __init__(self):
        super().__init__()
        from .FMFeatureMapAssertion import FMFeatureMapAssertion
        self._artop_fmFeatureMapAssertion = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_fmFeatureMapAssertion": "FM-FEATURE-MAP-ASSERTION"})

    @property
    def ref_fMFeatureMapAssertion_(self):
        return self._artop_fmFeatureMapAssertion

    @property
    def fMFeatureMapAssertion_(self):
        if self._artop_fmFeatureMapAssertion is not None:
            if hasattr(self._artop_fmFeatureMapAssertion, "uuid"):
                return self._artop_fmFeatureMapAssertion.uuid
        return
