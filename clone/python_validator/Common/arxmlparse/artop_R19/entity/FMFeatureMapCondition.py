# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMFeatureMapCondition.py
from .Identifiable import Identifiable

class FMFeatureMapCondition(Identifiable):

    def __init__(self):
        super().__init__()
        from .FMFeatureMapElement import FMFeatureMapElement
        from .FMConditionByFeaturesAndAttributes import FMConditionByFeaturesAndAttributes
        self._artop_fmFeatureMapElement = None
        self._artop_fmCond = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_fmFeatureMapElement':"FM-FEATURE-MAP-ELEMENT", 
         '_artop_fmCond':"FM-CONDITION-BY-FEATURES-AND-ATTRIBUTES"})

    @property
    def ref_fMFeatureMapElement_(self):
        return self._artop_fmFeatureMapElement

    @property
    def fMFeatureMapElement_(self):
        if self._artop_fmFeatureMapElement is not None:
            if hasattr(self._artop_fmFeatureMapElement, "uuid"):
                return self._artop_fmFeatureMapElement.uuid
        return

    @property
    def ref_fmCond_(self):
        return self._artop_fmCond

    @property
    def fmCond_(self):
        if self._artop_fmCond is not None:
            if hasattr(self._artop_fmCond, "uuid"):
                return self._artop_fmCond.uuid
        return
